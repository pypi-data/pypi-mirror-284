import math
import uuid
from typing import List, NoReturn, Union

import numpy as np
from OCC.Core.BRep import BRep_Tool
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.GCPnts import GCPnts_TangentialDeflection
from OCC.Core.Geom import Geom_Curve, Geom_Surface
from OCC.Core.gp import gp_Quaternion, gp_Vec
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Core.TopoDS import TopoDS_Shape
from scipy.spatial.transform import Rotation as R

try:
    from pythreejs import (
        AmbientLight,
        AxesHelper,
        BufferAttribute,
        BufferGeometry,
        Color,
        ConeGeometry,
        Controls,
        DirectionalLight,
        GridHelper,
        Group,
        LineBasicMaterial,
        LineSegments,
        Material,
        Mesh,
        MeshBasicMaterial,
        MeshPhongMaterial,
        OrbitControls,
        PerspectiveCamera,
        Renderer,
        Scene,
    )
    from traitlets import (
        Bool,
        ClassBasedTraitType,
        Float,
        HasTraits,
        Instance,
        Int,
        Tuple,
        Type,
        default,
        observe,
        validate,
    )
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Please install pythreejs before using JupyterThreeJSRenderer or "
        "JupyterThreeJSRenderer2d"
    )

from pyoccad.create import CreateFace, CreateTopology, CreateVector
from pyoccad.explore.subshapes import ExploreSubshapes
from pyoccad.typing import CurveT

x_vec = gp_Vec(1, 0, 0)
y_vec = gp_Vec(0, 1, 0)


class PyoccadGroup(Group):
    def __len__(self):
        return len(self.children)

    def hide(self):
        """Hide the group"""
        self.visible = False

    def show(self):
        """Show the group"""
        self.visible = True


class PyoccadGridHelper(GridHelper):
    def rotateX(self, angle: float = math.pi / 2):
        """
        Rotate the grid around X-axis.

        Parameters
        ----------
        angle : float
            the rotation angle, in radians
        """
        super().rotateX(angle)

    def rotateX_deg(self, angle: float = 90.0):
        """
        Rotate the grid around X-axis.

        Parameters
        ----------
        angle : float
            the rotation angle, in degrees
        """
        self.rotateX(np.radians(angle))

    def rotateY(self, angle: float = math.pi / 2):
        """
        Rotate the grid around Y-axis.

        Parameters
        ----------
        angle : float
            the rotation angle, in radians
        """
        super().rotateY(angle)

    def rotateY_deg(self, angle: float = 90.0):
        """
        Rotate the grid around Y-axis.

        Parameters
        ----------
        angle : float
            the rotation angle, in degrees
        """
        self.rotateY(np.radians(angle))

    def rotateZ(self, angle: float = math.pi / 2):
        """
        Rotate the grid around Z-axis.

        Parameters
        ----------
        angle : float
            the rotation angle, in radians
        """
        super().rotateZ(angle)

    def rotateZ_deg(self, angle: float = 90.0):
        """
        Rotate the grid around Z-axis.

        Parameters
        ----------
        angle : float
            the rotation angle, in degrees
        """
        self.rotateZ(np.radians(angle))

    def hide(self):
        """Hide the group"""
        self.visible = False

    def show(self):
        """Show the group"""
        self.visible = True


class ShapeInstance(ClassBasedTraitType):
    def __init__(self, **kwargs):
        super(ShapeInstance, self).__init__(**kwargs)

    def validate(self, obj, value):
        if isinstance(value, (TopoDS_Shape, Geom_Surface, Geom_Curve)):
            return value
        else:
            self.error(obj, value)

    def info(self):
        return "(TopoDS_Shape, Geom_Surface, Geom_Curve)"


class ShapeGroup(PyoccadGroup):
    """A group to build and store all the display information of an OpenCascade shape.

    It generates the following groups structure, some identified in their names by
    specific headers "@...@":
        ShapeGroup
            faces_group (@faces@)
                face1
                face2
                ...
            lattice_group (@lattices@)
                curve1
                curve2
                ...
            edges_group (@edges@)
                curve1
                curve2
                ...
    """

    def __init__(
        self, shape: Union[TopoDS_Shape, Geom_Surface, Geom_Curve] = None, uid: str = "", **kwargs
    ):
        super(PyoccadGroup, self).__init__(name=uid, **kwargs)
        self.add(self.faces_group)
        self.add(self.lattice_group)
        self.add(self.edges_group)

        self._mapping = {}
        self._uids = []
        self.shape = shape

    shape = ShapeInstance(allow_none=True, default_value=None)

    faces_group = Instance(PyoccadGroup, kw=dict(name="@faces@" + uuid.uuid4().hex))
    lattice_group = Instance(PyoccadGroup, kw=dict(name="@lattices@" + uuid.uuid4().hex))
    edges_group = Instance(PyoccadGroup, kw=dict(name="@edges@" + uuid.uuid4().hex))

    plot_edges = Bool(True)
    wireframe = Bool(False)
    lattice = Tuple(Int(), Int(), default_value=(0, 0))

    face_color = Color("aliceblue")
    line_color = Color("#000000")
    lattice_color = Color("#222222")
    line_width = Float(
        1.0
    )  # TODO: linewidth not working https://github.com/mrdoob/three.js/issues/10357
    opacity = Float(1.0)

    linear_deflection = Float(0.01)
    angular_deflection = Float(0.05)
    curvature_deflection = Float(0.01)
    min_discretization = Int(2)

    face_material = Instance(Material)
    line_material = Instance(Material)
    lattice_material = Instance(Material)

    @default("line_material")
    def _default_line_material(self):
        return LineBasicMaterial(linewidth=self.line_width, color=self.line_color)

    @default("lattice_material")
    def _default_lattice_material(self):
        return LineBasicMaterial(linewidth=self.line_width, color=self.lattice_color)

    @default("face_material")
    def _default_face_material(self):
        transparent = self.opacity < 1.0
        return MeshPhongMaterial(
            color=self.face_color,
            side="DoubleSide",
            polygonOffset=False,
            polygonOffsetFactor=0,
            depthTest=True,
            depthWrite=not transparent,
            wireframe=self.wireframe,
            transparent=transparent,
            opacity=self.opacity,
        )

    @validate("shape")
    def _validate_shape(self, proposal):
        if isinstance(proposal["value"], Geom_Surface):
            return CreateFace.from_contour(proposal["value"])
        if isinstance(proposal["value"], Geom_Curve):
            return CreateTopology.make_edge(proposal["value"])
        else:
            return proposal["value"]

    @observe("line_color")
    def _observe_line_color(self, change):
        self.line_material.color = change["new"]

    @observe("line_width")
    def _observe_line_width(self, change):
        self.line_material.linewidth = change["new"]
        self.lattice_material.linewidth = change["new"]

    @observe("lattice_color")
    def _observe_lattice_color(self, change):
        self.lattice_material.color = change["new"]

    @observe("face_color")
    def _observe_face_color(self, change):
        self.face_material.color = change["new"]

    @observe("wireframe")
    def _observe_wireframe(self, change):
        self.face_material.wireframe = change["new"]

    def __register(self, shape, uid):
        self._mapping[uid] = shape
        self._uids.append(uid)

    def mesh_curve(self, curve):
        """
        Mesh a curve.

        Parameters
        ----------
        curve : a curve
            the curve to mesh
        """
        from pyoccad.create import CreateCurve

        curve_adaptor = CreateCurve.as_adaptor(curve)
        tesselation = GCPnts_TangentialDeflection(
            curve_adaptor,
            self.angular_deflection,
            self.curvature_deflection,
            self.min_discretization,
        )

        points = [tesselation.Value(i + 1).Coord() for i in range(tesselation.NbPoints())]
        vertices = np.array(points, dtype=np.float32)
        indices = np.repeat(np.arange(vertices.shape[0], dtype=np.uint32), 2)[1:-1]

        return indices, vertices

    def _build_curve(self, indices, vertices, group: Group, material: Material) -> NoReturn:
        """
        Add a curve to a group.

        Parameters
        ----------
        curve : CurveT
            the curve to add
        group : Group
            the group in which the curve will be added
        material : Material
            the curve material
        """
        uid = uuid.uuid4().hex

        geom = BufferGeometry(
            attributes=dict(
                position=BufferAttribute(vertices),
                index=BufferAttribute(indices, normalized=False),
            )
        )

        three_curve = LineSegments(name=uid, geometry=geom, material=material)

        group.add(three_curve)
        self.__register(three_curve, uid)

    def add_curve(self, indices, vertices) -> NoReturn:
        """
        Add a curve to the edges group.

        Parameters
        ----------
        curve : CurveT
            the curve to add
        """
        self._build_curve(indices, vertices, self.edges_group, self.line_material)

    def _mesh_shape(self):
        BRepMesh_IncrementalMesh(
            self.shape, self.linear_deflection, True, self.angular_deflection, True
        )

    @staticmethod
    def _loc_to_pos_quat(loc):
        trf = loc.Transformation()
        pos = np.r_[
            trf.TranslationPart().X(),
            trf.TranslationPart().Y(),
            trf.TranslationPart().Z(),
        ]
        quat = [
            trf.GetRotation().X(),
            trf.GetRotation().Y(),
            trf.GetRotation().Z(),
            trf.GetRotation().W(),
        ]

        return pos, quat

    @staticmethod
    def _get_face_loc(face):
        loc = TopLoc_Location()
        BRep_Tool().Triangulation(face, loc)
        return loc

    @staticmethod
    def _get_face_mesh(face):
        loc = TopLoc_Location()
        T = BRep_Tool().Triangulation(face, loc)

        if T is None:
            return

        nTri = T.NbTriangles()
        nVtx = T.NbNodes()
        vtx = []
        idx = []
        tri = T.Triangles()

        for pt_idx in range(1, nVtx + 1):
            pt = T.Node(pt_idx)
            for d in range(1, 4):
                vtx.append(pt.Coord(d))

        for t in tri:
            for i in range(1, 4):
                idx.append(t.Value(i) - 1)

        trf = loc.Transformation()
        vertices = np.reshape(np.array(vtx, "float32"), (nVtx, 3))
        faces = np.array(idx, "uint32").reshape(nTri, 3).ravel()
        pos = np.r_[
            trf.TranslationPart().X(),
            trf.TranslationPart().Y(),
            trf.TranslationPart().Z(),
        ]
        quat = [
            trf.GetRotation().X(),
            trf.GetRotation().Y(),
            trf.GetRotation().Z(),
            trf.GetRotation().W(),
        ]

        return vertices, faces, pos, quat

    def _build_face(self, vertices, faces, pos, quat, mesh_idx=None):

        geometry = BufferGeometry(
            attributes=dict(
                position=BufferAttribute(vertices, normalized=False),
                index=BufferAttribute(faces, normalized=False),
            )
        )
        geometry.exec_three_obj_method("computeVertexNormals")

        return self._create_mesh(geometry, pos, quat, mesh_idx)

    def _create_mesh(self, buffer, pos, quat, mesh_idx=None):
        def add_mesh(mat, mesh_idx, **kwargs):
            if mesh_idx is not None and mesh_idx < len(self._uids):
                mesh = self._mapping[self._uids[mesh_idx]]

                mesh.geometry = buffer
                # f.geometry.attributes['position'].array = vertices
                # f.geometry.attributes['index'].array = indices
                mesh.geometry.exec_three_obj_method("computeVertexNormals")

                mesh.position = pos
                mesh.quaternion = quat
                mesh.material = mat
            else:
                uid = "@face@" + uuid.uuid4().hex
                mesh = Mesh(
                    geometry=buffer, material=mat, position=pos, quaternion=quat, name=uid, **kwargs
                )
                self.faces_group.add(mesh)
                self.__register(mesh, uid)

        if self.opacity < 1.0:
            material_class = self.face_material.__class__
            mat1 = material_class(
                color=self.face_material.color,
                side="FrontSide",
                polygonOffset=False,
                polygonOffsetFactor=0,
                depthTest=True,
                depthWrite=self.face_material.depthWrite,
                wireframe=self.wireframe,
                transparent=self.face_material.transparent,
                opacity=self.opacity,
            )
            mat2 = material_class(
                color=self.face_material.color,
                side="BackSide",
                polygonOffset=False,
                polygonOffsetFactor=0,
                depthTest=True,
                depthWrite=self.face_material.depthWrite,
                wireframe=self.wireframe,
                transparent=self.face_material.transparent,
                opacity=self.opacity,
            )

            add_mesh(mat1, mesh_idx, renderOrder=2)
            mesh_idx += 1
            add_mesh(mat2, mesh_idx)
            return 2
        else:
            add_mesh(self.face_material, mesh_idx)
            return 1

    def _build_shape_faces(self):

        self._mesh_shape()  # Mesh all faces at once

        group_current_size = len(self.faces_group)
        shape_faces = [f for f in ExploreSubshapes.get_faces(self.shape)]

        vertices, faces, pos, quat = (
            np.empty((0, 3), dtype=np.float32),
            np.empty((0, 3), dtype=np.uint32),
            (0.0, 0.0, 0.0),
            R.identity().as_quat().tolist(),
        )

        faces_index = [
            min([i for i, fp in enumerate(shape_faces) if f.IsPartner(fp)]) for f in shape_faces
        ]
        faces_index_to_triangulate = set(faces_index)

        meshes = []
        for i, f in enumerate(shape_faces):
            if i in faces_index_to_triangulate:
                t = ShapeGroup._get_face_mesh(f)
                if t:
                    meshes.append(t)
            else:
                loc = self._get_face_loc(f)
                p, q = self._loc_to_pos_quat(loc)
                v, f, _, _ = meshes[faces_index[i]]
                meshes.append((v, f, p, q))

        for v, f, p, q in meshes:
            r = R.from_quat(q)

            faces = np.append(faces, f + np.size(vertices, axis=0))  # shift references to vertex
            # apply rotation and translation to store all faces in the same buffer
            vertices = np.append(vertices, np.array(r.apply(v) + p, dtype=np.float32), axis=0)

        if len(shape_faces) > 0:
            if isinstance(pos, np.ndarray):
                pos = pos.tolist()

            n = self._build_face(vertices, faces, tuple(pos), tuple(quat), 0)
            if group_current_size > 1:
                self.faces_group.remove(
                    [self.faces_group.children[i] for i in range(n, group_current_size)]
                )

    def _build_edges(self):

        self.edges_group.visible = self.plot_edges
        if self.shape is not None:

            group_current_size = len(self.edges_group)
            if self.plot_edges:
                shape_edges = [*ExploreSubshapes.get_edges(self.shape)]
            else:
                shape_edges = []

            indices, vertices = np.empty((0,), dtype=np.uint32), np.empty((0, 3), dtype=np.float32)
            for i, edge in enumerate(shape_edges):
                i, v = self.mesh_curve(edge)
                indices = np.append(indices, i + np.size(vertices, axis=0), axis=0)
                vertices = np.append(vertices, v, axis=0)

            if group_current_size == 1:
                e = self.edges_group.children[0]
                e.geometry.attributes["position"].array = vertices
                e.geometry.attributes["index"].array = indices
            else:
                self.add_curve(indices, vertices)

            self.edges_group.remove(
                [self.edges_group.children[i] for i in range(len(shape_edges), group_current_size)]
            )

    def clear(self):
        self._mapping.clear()
        self._uids.clear()
        self.lattice_group.remove([child for child in self.lattice_group.children])
        self.faces_group.remove([child for child in self.faces_group.children])
        self.edges_group.remove([child for child in self.edges_group.children])

    @observe("plot_edges")
    def _update_edges(self, changes):
        self.edges_group.visible = changes["new"]

    @staticmethod
    def _create_surface_lattice(surface, n_u: int, n_v: int) -> List[CurveT]:
        """
        Create a surface lattice.

        Parameters
        ----------
        surface : a surface
            the surface to consider for the lattice
        n_u : int
            number of subdivisions in the u direction
        n_v : int
            number of subdivisions in the v direction

        Returns
        -------
        curves : List[CurveT]
            a group of curves representing the surface lattice
        """
        u1, u2, v1, v2 = surface.Bounds()

        curves = []
        for u in np.linspace(u1, u2, n_u):
            curves.append(surface.UIso(u))

        for v in np.linspace(v1, v2, n_v):
            curves.append(surface.VIso(v))

        return curves

    def _build_shape_lattice(self):

        if self.shape is None:
            return

        n_u, n_v = self.lattice
        group_current_size = len(self.lattice_group)

        lattice_curves = []
        for face in ExploreSubshapes.get_faces(self.shape):
            surf = BRep_Tool.Surface(face)
            lattice_curves += ShapeGroup._create_surface_lattice(surf, n_u, n_v)

        self.lattice_group.visible = len(lattice_curves) > 0

        indices, vertices = np.empty((0,), dtype=np.uint32), np.empty((0, 3), dtype=np.float32)
        for i, curve in enumerate(lattice_curves):
            i, v = self.mesh_curve(curve)
            indices = np.append(indices, i + np.size(vertices, axis=0), axis=0)
            vertices = np.append(vertices, v, axis=0)

        if group_current_size == 1:
            e = self.lattice_group.children[0]
            e.geometry.attributes["position"].array = vertices
            e.geometry.attributes["index"].array = indices
        else:
            self._build_curve(indices, vertices, self.lattice_group, self.lattice_material)

        self.lattice_group.remove(
            [self.lattice_group.children[i] for i in range(len(lattice_curves), group_current_size)]
        )

    @observe("lattice")
    def _update_lattice(self, changes):
        self._build_shape_lattice()

    def _update_curve(self, curve, uid: str):
        """
        Update a curve already present in the scene.

        Parameters
        ----------
        curve : a curve
            the curve to update
        uid : str
            the unique id of the shape
        """
        if uid not in self._mapping:
            raise ValueError('Not able to update curve with uid "{}"'.format(uid))

        current_mesh = self._mapping[uid]
        indices, vertices = self.mesh_curve(curve)

        # Save time re-using the current Widgets instead of creating new ones
        # TODO: replacing BufferAttribute array raises DeprecationWarnings.
        #  See https://github.com/jupyter-widgets/pythreejs/issues/332
        #  For the moment, create 2 new BufferAttribute.
        #  Refactor when pydatawidgets will be fixed
        current_mesh.geometry.attributes["position"].array = vertices
        current_mesh.geometry.attributes["index"].array = indices

        # three_curve.geometry.attributes = dict(position=BufferAttribute(vertices),
        #                                        index=BufferAttribute(indices, normalized=False))

    def _build(self):

        if self.shape is not None:
            self._build_shape_faces()
            self._build_shape_lattice()
            self._build_edges()

    @observe("shape")
    def _update_shape(self, changes):
        self._build()


class JupyterThreeJSRenderer(HasTraits):
    """3D renderer using pythreeJS"""

    background_color = Color("aliceblue")

    camera_position = Tuple(Float(), Float(), Float(), default_value=(3.0, 3.0, 3.0))
    camera_target = Tuple(Float(), Float(), Float(), default_value=(0.0, 0.0, 0.0))
    camera_aspect_ratio = Float(4.0 / 3.0)
    camera_fov = Float(75.0)
    camera_near = Float(0.1)
    camera_far = Float(1000.0)
    camera_quaternion = Tuple(
        Float(), Float(), Float(), Float(), default_value=(0.0, 0.0, 0.0, 1.0)
    )

    show_axes = Bool(True)

    grid_normal = Tuple(Float(), Float(), Float(), default_value=(0.0, 1.0, 0.0))

    view_size = Tuple(Int(), Int(), default_value=(800, 500))

    camera_control_type = Type(OrbitControls, klass=Controls)

    def __init__(self, **kwargs):
        """3D renderer using pythreeJS."""
        self._mapping = {}

        self._scene = Scene()
        self._scene.background = self.background_color

        self._ax = PyoccadGroup(name="@axes@" + uuid.uuid4().hex)
        self._scene.add(self._ax)
        self.add_axes(1.0)

        self._grid = None
        self.add_grid()

        self._displayed = PyoccadGroup()
        self._scene.add(self._displayed)

        self._cam = None
        self.add_camera(
            self.camera_position,
            fov=self.camera_fov,
            near=self.camera_near,
            far=self.camera_far,
            aspect=self.view_size[0] / self.view_size[1],
        )

        self._cc = self.camera_control_type(controlling=self._cam)

        self._renderer = Renderer(
            camera=self._cam,
            background="pink",
            background_opacity=1,
            antialias=True,
            scene=self._scene,
            controls=[self._cc],
            width=self.view_size[0] + 2,
            height=self.view_size[1] + 2,
            layout={
                "height": "{}px".format(self.view_size[1] + 2),
                "width": "{}px".format(self.view_size[0] + 2),
                "border": "1px solid black",
                "margin": "5px",
            },
        )

        super(JupyterThreeJSRenderer, self).__init__(**kwargs)

    @validate("camera_aspect_ratio")
    def _validate_camera_aspect_ratio(self, proposal):
        val = proposal["value"]
        if val <= 0.1:
            val = 0.1
        return val

    @observe("camera_position")
    def _observe_camera_position(self, change):
        self._cam.position = change["new"]
        self._observe_camera_target({"new": self.camera_target})

    @observe("camera_near")
    def _observe_camera_near(self, change):
        self._cam.near = change["new"]

    @observe("camera_far")
    def _observe_camera_far(self, change):
        self._cam.far = change["new"]

    @observe("camera_fov")
    def _observe_camera_fov(self, change):
        self._cam.fov = change["new"]

    @observe("view_size")
    def _observe_view_size(self, change):
        width, height = change["new"]
        self.camera_aspect_ratio = self._cam.aspect = width / height
        self._update_view()

    @observe("camera_aspect_ratio")
    def _observe_camera_aspect_ratio(self, change):
        self.view_size = (int(self.view_size[1] * change["new"]), self.view_size[1])
        self._cam.aspect = change["new"]
        self._update_view()

    @observe("camera_target")
    def _observe_camera_target(self, change):
        self._cam.lookAt(change["new"])
        self.camera_quaternion = self._cam.quaternion
        self._cc.target = change["new"]

    @observe("camera_control_type")
    def _observe_camera_control_type(self, change):
        self._cc = change["new"](controlling=self._cam)
        self._renderer.controls = [self._cc]

    @observe("show_axes")
    def _observe_show_axes(self, change):
        self._ax.visible = change["new"]

    @observe("grid_normal")
    def _observe_grid_normal(self, change):
        occ_quaternion = gp_Quaternion(
            CreateVector.as_vector((0.0, 1.0, 0.0)),
            CreateVector.as_vector(change["new"]),
        )
        self._grid.quaternion = (
            occ_quaternion.X(),
            occ_quaternion.Y(),
            occ_quaternion.Z(),
            occ_quaternion.W(),
        )

    def _update_view(self):
        self._renderer.width = self.view_size[0] - 1
        self._renderer.height = self.view_size[1] - 1
        self._renderer.layout = {
            "height": "{}px".format(self.view_size[1]),
            "width": "{}px".format(self.view_size[0]),
            "border": "1px solid black",
            "padding": "1px",
            "margin": "1px",
        }

    @observe("background_color")
    def _observe_background_color(self, change):
        self._scene.background = change["new"]

    def show(self):
        return self._renderer

    def add_axes(self, size: float) -> None:
        """Add reference cartesian axes to the scene.

        Parameters
        ----------
        size : float
            The norm of the axes (size = ||x|| = ||y|| = ||z||)
        """
        self._ax.visible = self.show_axes
        self._ax.add(AxesHelper(size))

        base_radius = 0.05 * size
        height = 0.1 * size

        for direction, color in [
            ((1.0, 0.0, 0.0), "red"),
            ((0.0, 1.0, 0.0), "chartreuse"),
            ((0.0, 0.0, 1.0), "blue"),
        ]:

            geometry = ConeGeometry(base_radius, height, 20)
            material = MeshBasicMaterial(
                color=color,
                side="DoubleSide",
                polygonOffset=True,
                polygonOffsetFactor=1,
            )
            position = tuple(np.array(direction) * size + height / 2 * np.array(direction))
            occ_quaternion = gp_Quaternion(
                CreateVector.as_vector((0.0, 1.0, 0.0)),
                CreateVector.as_vector(direction),
            )
            quaternion = (
                occ_quaternion.X(),
                occ_quaternion.Y(),
                occ_quaternion.Z(),
                occ_quaternion.W(),
            )

            mesh = Mesh(
                geometry=geometry,
                material=material,
                position=position,
                quaternion=quaternion,
            )

            self._ax.add(mesh)

    def add_camera(self, position, fov: float, near: float, far: float, aspect: float = 1) -> None:
        """Add a camera to the scene.

        Parameters
        ----------
        position : {coordinates container}
            The camera position
        fov : float, optional
            The camera field of view
        near : float, optional
            The minimum distance visible to the camera
        far : float, optional
            The maximum distance visible to the camera
        aspect : float, optional
            The camera aspect ratio
        """
        cam = PerspectiveCamera(
            position=position,
            fov=fov,
            aspect=aspect,
            near=near,
            far=far,
            children=[
                DirectionalLight(color="#ffffff", position=position, intensity=0.3),
                AmbientLight(color="#ffffff", position=position, intensity=0.8),
            ],
        )
        self._cam = cam
        self._scene.add(cam)

    def add_ambient_light(self, color: str = "#dddddd", intensity: float = 0.9) -> NoReturn:
        """Add an ambient light to the scene.

        Parameters
        ----------
        color : str, HTML valid, optional
            The light color {Default='#dddddd'}
        intensity : float, optional
            The light intensity {Default=0.9}
        """
        self._scene.add(AmbientLight(color=color, intensity=intensity))

    def add_directional_light(
        self, position: tuple, color: str = "#dddddd", intensity: float = 0.9
    ) -> NoReturn:
        """Add a directional light to the scene.

        Parameters
        ----------
        position : tuple
            the light position in 3D space
        color : str, HTML valid, optional
            the light color {Default='#dddddd'}
        intensity : float, optional
            the light intensity {Default=0.9}
        """
        light = DirectionalLight(color=color, intensity=intensity)
        light.position = position
        self._scene.add(light)

    def add_grid(
        self,
        size: float = 20,
        divisions: int = 20,
        centerline_color: str = "#444444",
        grid_color: str = "#444444",
    ) -> None:
        """Add a square grid to the current scene.

        Parameters
        ----------
        size : float
            The grid size
        divisions : int
            The number of subdivisions of the grid
        centerline_color : str, html valid color
            The grid center line color {Default='#444444'}
        grid_color : str, html valid color
            The grid other lines color {Default='#444444'}
        """
        g = PyoccadGridHelper(
            size=size,
            divisions=divisions,
            colorCenterLine=centerline_color,
            colorGrid=grid_color,
        )

        self._grid = g
        self._scene.add(self._grid)

    def register(self, shape: ShapeGroup, uid: str) -> None:
        """Register a shape in the mapping of shapes displayed.

        Parameters
        ----------
        shape : ShapeGroup
            The shape to register

        uid : str
            The unique id of the shape
        """
        self._displayed.add(shape)
        self._mapping[uid] = shape

    def add_shape(self, shape, uid: str = None, force: bool = False, **kwargs) -> ShapeGroup:
        """
        Add a shape to the scene.

        Parameters
        ----------
        shape : a shape
            The shape to add to the scene
        uid : str, optional
            The unique id to identify the shape. If not provided, it will be automatically generated
        force : bool, optional
            Whether to force the shape to be added if the uid already exists
        """
        if uid in self._mapping:
            if force:
                self.remove_shape(uid)
            else:
                raise AttributeError(
                    'There already is a "{}" object displayed! Please choose another name or use '
                    "the update_shape method.".format(uid)
                )

        if uid is None:
            uid = uuid.uuid4().hex

        self.register(ShapeGroup(shape, uid, **kwargs), uid)
        return self.get_shape(uid)

    def update_shape(
        self, new_shape: Union[TopoDS_Shape, Geom_Surface, Geom_Curve], uid: str
    ) -> ShapeGroup:
        """Update a shape already added to the scene.

        Parameters
        ----------
        new_shape : Union[TopoDS_Shape, Geom_Surface, Geom_Curve]
            The shape to use for update
        uid : str
            The unique id of the shape to update
        """
        try:
            self._mapping[uid].shape = new_shape
        except KeyError:
            raise KeyError('The uid "{}" was not found in shapes currently displayed.'.format(uid))

        return self.get_shape(uid)

    def get_shape(self, uid: str) -> ShapeGroup:
        """Get a shape already added to the scene.

        Parameters
        ----------
        uid : str
            The unique id of the shape to remove
        """
        try:
            return self._mapping[uid]
        except KeyError:
            raise KeyError('The uid "{}" was not found in shapes currently displayed.'.format(uid))

    def remove_shape(self, uid: str) -> NoReturn:
        """Remove a shape from the scene.

        Parameters
        ----------
        uid : str
            The unique id of the shape to remove
        """
        try:
            self._displayed.remove(self._mapping.pop(uid))
        except KeyError:
            raise KeyError('The uid "{}" was not found in shapes currently displayed.'.format(uid))

    def clear_shapes(self) -> NoReturn:
        """Remove all shapes from the scene."""
        self._displayed.remove([leaf for leaf in self._displayed.children])
        self._mapping.clear()
