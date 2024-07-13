from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCylinder
from OCC.Core.Geom import Geom_CylindricalSurface
from OCC.Core.gp import gp_Circ, gp_Cylinder
from OCC.Core.TopoDS import TopoDS_Solid

from pyoccad.create import CreateUnsignedCoordSystem


class CreateCylinder:
    """Factory to build a cylinder."""

    @staticmethod
    def from_circle(circle: gp_Circ) -> Geom_CylindricalSurface:
        """Build a cylinder from its base and direction.

        Parameters
        ----------
        - circle: gp_Circ
            The base

        Returns
        -------
        - cylinder: Geom_CylindricalSurface
            The resulting cylinder
        """
        return Geom_CylindricalSurface(
            gp_Cylinder(
                CreateUnsignedCoordSystem.as_coord_system(
                    (
                        circle.Location(),
                        circle.XAxis().Direction(),
                        circle.Axis().Direction(),
                    )
                ),
                circle.Radius(),
            )
        )

    @staticmethod
    def solid_from_base_and_height(
        base: gp_Circ,
        height: float,
    ) -> TopoDS_Solid:
        """Build a solid cylinder.

        Parameters
        ----------
        - base: gp_Circ
            The base
        - height: float
            The height

        Returns
        -------
        - cylinder [TopoDS_Solid]:
            The resulting cylindrical solid
        """
        return BRepPrimAPI_MakeCylinder(base.Position(), base.Radius(), height).Solid()
