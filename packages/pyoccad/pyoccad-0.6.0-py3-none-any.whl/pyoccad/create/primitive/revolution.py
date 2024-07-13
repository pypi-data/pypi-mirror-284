from math import pi
from typing import Union

from OCC.Core.Adaptor2d import Adaptor2d_Curve2d
from OCC.Core.Adaptor3d import Adaptor3d_Curve
from OCC.Core.BRepAdaptor import BRepAdaptor_CompCurve, BRepAdaptor_Curve
from OCC.Core.BRepBuilderAPI import (
    BRepBuilderAPI_MakeEdge,
    BRepBuilderAPI_MakeFace,
    BRepBuilderAPI_MakeWire,
)
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeRevol
from OCC.Core.Geom import Geom_Curve, Geom_RectangularTrimmedSurface, Geom_SurfaceOfRevolution
from OCC.Core.Geom2d import Geom2d_Curve
from OCC.Core.GeomAPI import geomapi
from OCC.Core.gp import gp_Ax1, gp_Ax2, gp_Pln
from OCC.Core.TopoDS import (
    TopoDS_Edge,
    TopoDS_Face,
    TopoDS_Shape,
    TopoDS_Shell,
    TopoDS_Solid,
    TopoDS_Wire,
)

from pyoccad.create import CreateAxis, CreateCurve
from pyoccad.typing import Axis3T, CurveT


class CreateRevolution:
    @staticmethod
    def surface_from_curve(
        curve: CurveT, axis: Axis3T, angle: float = 2 * pi
    ) -> Union[Geom_SurfaceOfRevolution, TopoDS_Shape]:
        """Create a revolution surface from a curve around an axis.

        Parameters
        ----------
        curve: CurveT
            The linear element to revolve
        axis: Axis3T
            The axis of revolution

        Returns
        -------
        revolution: Union[Geom_SurfaceOfRevolution, TopoDS_Shape]
            The revolution surface
        """
        axis = CreateAxis.as_axis(axis)
        if not isinstance(axis, gp_Ax1):
            raise TypeError('AxisT should be 3D and have type gp_Ax1, got "{}".'.format(type(axis)))

        if isinstance(curve, Geom_Curve):
            return Geom_SurfaceOfRevolution(curve, axis)

        if isinstance(curve, Geom2d_Curve):
            coord_system = gp_Ax2(axis.Location(), axis.Direction())
            plane = gp_Pln(axis.Location(), coord_system.XDirection())
            curve_3d = Geom_Curve.DownCast(geomapi.To3d(curve, plane))
            return Geom_SurfaceOfRevolution(curve_3d, axis)

        if isinstance(curve, (TopoDS_Edge, TopoDS_Wire)):
            return BRepPrimAPI_MakeRevol(curve, axis, angle).Shape()

        if isinstance(
            curve,
            (
                Adaptor3d_Curve,
                Adaptor2d_Curve2d,
                BRepAdaptor_Curve,
                BRepAdaptor_CompCurve,
            ),
        ):
            return CreateRevolution.surface_from_curve(CreateCurve.from_adaptor(curve), axis)

        raise TypeError('CurveT type "{}" not supported yet.'.format(type(curve)))

    @staticmethod
    def trimmed_surface_from_curve(
        curve: CurveT, axis: Axis3T, start_angle: float, end_angle: float
    ) -> Geom_RectangularTrimmedSurface:
        """Create a trimmed revolution surface from a curve around an axis.

        Parameters
        ----------
        curve: CurveT
            The linear element to revolve
        axis: Axis3T
            The axis of revolution
        start_angle: float
            [rad] Start angle of the trim
        end_angle: float
            [rad] End angle of the trim

        Returns
        -------
        revolution: Geom_RectangularTrimmedSurface
            The revolution surface
        """

        surface = CreateRevolution.surface_from_curve(curve, axis)
        if isinstance(surface, TopoDS_Shape):
            raise TypeError("Topological geometries can not be trimmed.")

        _, _, v1, v2 = surface.Bounds()
        return Geom_RectangularTrimmedSurface(surface, start_angle, end_angle, v1, v2)

    @staticmethod
    def solid_from_curve(curve: CurveT, axis: Axis3T) -> TopoDS_Solid:
        """Create a solid of revolution from a closed curve.

        Parameters
        ----------
        curve: CurveT
            The element to revolve
        axis: Axis3T
            The axis of revolution

        Returns
        -------
        s : TopoDS_Solid
            The revolution solid

        """
        axis = CreateAxis.as_axis(axis)
        if not isinstance(axis, gp_Ax1):
            raise TypeError("AxisT should be 3D, got dimension 2.")

        if isinstance(curve, (TopoDS_Edge, TopoDS_Wire)):
            if isinstance(curve, TopoDS_Edge):
                curve = BRepBuilderAPI_MakeWire(curve).Wire()
            face = BRepBuilderAPI_MakeFace(curve).Face()
            return CreateRevolution.solid_from_face(face, axis)

        if isinstance(curve, Geom_Curve):
            return CreateRevolution.solid_from_curve(BRepBuilderAPI_MakeEdge(curve).Edge(), axis)
        if isinstance(curve, Geom2d_Curve):
            coord_system = gp_Ax2(axis.Location(), axis.Direction())
            plane = gp_Pln(axis.Location(), coord_system.XDirection())
            curve_3d = Geom_Curve.DownCast(geomapi.To3d(curve, plane))
            return CreateRevolution.solid_from_curve(curve_3d, axis)

        if isinstance(
            curve,
            (
                Adaptor2d_Curve2d,
                Adaptor3d_Curve,
                BRepAdaptor_Curve,
                BRepAdaptor_CompCurve,
            ),
        ):
            return CreateRevolution.solid_from_curve(CreateCurve.from_adaptor(curve), axis)

        raise TypeError('CurveT type "{}" not supported yet.'.format(type(curve)))

    @staticmethod
    def solid_from_face(face: TopoDS_Face, axis: Axis3T, angle: float = 2 * pi) -> TopoDS_Solid:
        """Create a solid of revolution from a face.

        Parameters
        ----------
        face: TopoDS_Face
            The element to revolve
        axis: Axis3T
            The axis of revolution

        Returns
        -------
        s : TopoDS_Solid
            The revolution solid
        """
        axis = CreateAxis.as_axis(axis)
        if not isinstance(axis, gp_Ax1):
            raise TypeError("AxisT should be 3D, got dimension 2.")

        if isinstance(face, (TopoDS_Face, TopoDS_Shell)):
            return BRepPrimAPI_MakeRevol(face, axis, angle).Shape()

        raise TypeError('Face type "{}" not supported yet.'.format(type(face)))
