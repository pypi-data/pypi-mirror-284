from typing import Iterable, Tuple, Union

from OCC.Core.Adaptor3d import Adaptor3d_Curve
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeFace, BRepBuilderAPI_MakeSolid
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeHalfSpace
from OCC.Core.Geom import Geom_Curve, Geom_Surface
from OCC.Core.gp import gp_Circ, gp_Pln, gp_Pnt
from OCC.Core.TopoDS import TopoDS_Face, TopoDS_Shape, TopoDS_Shell, TopoDS_Solid

from pyoccad.create import CreateCone, CreateCylinder, CreatePoint, CreateSphere, CreateVector
from pyoccad.typing import PointT, VectorT


class CreateBox:
    @staticmethod
    def from_dimensions(dimensions: Tuple[float, float, float]) -> TopoDS_Solid:
        """Build a box with its first corner at (0., 0., 0.).

        Parameters
        ----------
        - dimensions, Tuple[float, float, float]:
            Dimension on x, y and z axis

        Returns
        -------
        - box [TopoDS_Solid]:
            The resulting box
        """
        return BRepPrimAPI_MakeBox(*dimensions).Solid()

    @staticmethod
    def from_dimensions_and_center(
        dimensions: Tuple[float, float, float], center: PointT = (0, 0, 0)
    ) -> TopoDS_Solid:
        """Build a box centered at a given point.

        Parameters
        ----------
        - dimensions, Tuple[float, float, float]:
            Dimension on x, y and z axis
        - center [PointT]: container of coordinates, optional
            Center of the box {default=(0., 0., 0.)}

        Returns
        -------
        - box [TopoDS_Solid]:
            The resulting box
        """
        from pyoccad.measure import solid
        from pyoccad.transform import Translate

        box = BRepPrimAPI_MakeBox(*dimensions).Solid()
        cg = solid.center(box)
        vg = CreateVector.from_point(cg)
        vc = CreateVector.from_point(center)
        Translate.from_vector(box, vc - vg)

        return box

    Shape = Union[Adaptor3d_Curve, Geom_Curve, Geom_Surface, TopoDS_Shape]

    @staticmethod
    def bounding_box(shape: Union[Shape, Iterable[Shape]]) -> TopoDS_Solid:
        """Create a box containing a shape.

        Parameters
        ----------
        - shape, Union[Shape, Iterable[Shape]]:
            The shape

        Returns
        -------
        - box [TopoDS_Solid]:
            The resulting box
        """
        from pyoccad.create import CreateTopology

        box = Bnd_Box()
        if not isinstance(shape, Iterable):
            shape = [shape]

        for sh in shape:
            brepbndlib.Add(CreateTopology.as_shape(sh), box)
        xmin, ymin, zmin, xmax, ymax, zmax = box.Get()

        return BRepPrimAPI_MakeBox(
            gp_Pnt(xmin, ymin, zmin), xmax - xmin, ymax - ymin, zmax - zmin
        ).Solid()


class CreateSolid:
    @staticmethod
    def from_shell(shell: TopoDS_Shell) -> TopoDS_Solid:
        """Build a solid from a shell.

        Parameters
        ----------
        - shell [TopoDS_Shell]:
            The shell

        Returns
        -------
        - solid [TopoDS_Solid]:
            The resulting solid
        """
        return BRepBuilderAPI_MakeSolid(shell).Solid()

    @staticmethod
    def half_space(plane: gp_Pln) -> TopoDS_Solid:
        """Build a half space solid, the outside part of the solid is toward plane's direction.

        Parameters
        ----------
        - plane [gp_Pln]:
            The plane dividing space in 2 regions

        Returns
        -------
        - solid [TopoDS_Solid]:
            The resulting half space
        """

        f = BRepBuilderAPI_MakeFace(plane).Face()
        p_in = plane.Location().Translated(CreateVector.from_point(plane.Axis().Direction()))
        return BRepPrimAPI_MakeHalfSpace(f, p_in).Solid()

    @staticmethod
    def half_space_from_face(face: TopoDS_Face, point: PointT) -> TopoDS_Solid:
        """Build half space from a face.

        Parameters
        ----------
        - face [TopoDS_Face]:
            The face dividing space in 2 regions
        - point [PointT]:
            A point to define which region is the half space

        Returns
        -------
        - solid [TopoDS_Solid]:
            The resulting half space
        """
        return BRepPrimAPI_MakeHalfSpace(face, CreatePoint.as_point(point)).Solid()

    @staticmethod
    def half_space_from_surface(surface: Geom_Surface, point: PointT) -> TopoDS_Solid:
        """Build half space from a face.

        Parameters
        ----------
        - surface [Geom_Surface]:
            The surface dividing space in 2 regions
        - point [PointT]:
            A point to define which region is the half space

        Returns
        -------
        - solid [TopoDS_Solid]:
            The resulting half space
        """
        face = BRepBuilderAPI_MakeFace(surface, 1e-6).Face()
        return CreateSolid.half_space_from_face(face, point)

    @staticmethod
    def cylindrical_from_base_and_dir(
        base_center: PointT,
        vector: VectorT,
        radius: float,
    ) -> TopoDS_Solid:
        """Build a solid cylinder.

        Parameters
        ----------
        - base_center [PointT]:
            The cylinder's base centre
        - vector [VectorT]:
            The vector representing direction and length
        - radius [float]:
            Cylinder radius

        Returns
        -------
        - cylinder [TopoDS_Solid]:
            The resulting cylindrical solid
        """
        return CreateCylinder.solid_from_base_and_dir(base_center, vector, radius)

    @staticmethod
    def conical_from_base_and_height(
        circle: gp_Circ, height: float, top_radius: float = 0.0
    ) -> TopoDS_Solid:
        """Build a solid cone.

        Parameters
        ----------
        - circle: gp_Circ
            The base circle
        - height: float
            The height
        - top_radius: float, optional
            The top radius {0 by default}

        Returns
        -------
        - cone [TopoDS_Solid]:
            The resulting solid cone
        """
        return CreateCone.solid_from_base_and_height(circle, height, top_radius)

    @staticmethod
    def spherical_from_circle(base: gp_Circ) -> TopoDS_Solid:
        """Build a solid sphere.

        Parameters
        ----------
        - base: gp_Circ
            The base circle

        Returns
        -------
        - sphere [TopoDS_Solid]:
            The resulting solid sphere
        """
        return CreateSphere.solid_from_circle(base)
