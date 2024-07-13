from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeCone
from OCC.Core.Geom import Geom_ConicalSurface
from OCC.Core.gp import gp_Circ, gp_Cone
from OCC.Core.TopoDS import TopoDS_Solid

from pyoccad.create import CreateUnsignedCoordSystem


class CreateCone:
    """Factory to build a cone."""

    @staticmethod
    def from_base_and_height(base: gp_Circ, angle: float) -> Geom_ConicalSurface:
        """Build a cone from its base and angle.

        Parameters
        ----------
        - base: gp_Circ
            The base

        Returns
        -------
        - cone: Geom_ConicalSurface
            The resulting cone
        """
        return Geom_ConicalSurface(
            gp_Cone(
                CreateUnsignedCoordSystem.as_coord_system(
                    (base.Location(), base.XAxis(), base.Axis())
                ),
                angle,
                base.Radius(),
            )
        )

    @staticmethod
    def solid_from_base_and_height(
        base: gp_Circ, height: float, top_radius: float = 0.0
    ) -> TopoDS_Solid:
        """Build a cone solid.

        Parameters
        ----------
        - base: gp_Circ
            The base circle
        - height: float
            The height
        - top_radius: float, optional
            The top radius {0 by default}

        Returns
        -------
        - cone [TopoDS_Solid]:
            The resulting cone
        """
        return BRepPrimAPI_MakeCone(base.Position(), base.Radius(), top_radius, height).Solid()
