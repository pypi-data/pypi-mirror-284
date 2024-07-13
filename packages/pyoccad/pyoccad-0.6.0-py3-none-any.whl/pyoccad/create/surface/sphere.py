from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere
from OCC.Core.Geom import Geom_SphericalSurface
from OCC.Core.gp import gp_Circ, gp_Sphere
from OCC.Core.TopoDS import TopoDS_Solid

from pyoccad.create import CreatePoint, CreateUnsignedCoordSystem
from pyoccad.typing import PointT


class CreateSphere:
    """Factory to build a sphere."""

    @staticmethod
    def from_circle(circle: gp_Circ) -> Geom_SphericalSurface:
        """Build a sphere from a circle.

        Parameters
        ----------
        - circle: gp_Circ
            The base circle

        Returns
        -------
        - sphere: Geom_SphericalSurface
            The resulting sphere
        """
        return Geom_SphericalSurface(
            gp_Sphere(
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
    def solid_from_radius_and_center(radius: float, center: PointT = (0, 0, 0)) -> TopoDS_Solid:
        """Build a solid sphere.

        Parameters
        ----------
        - radius [float]:
            The radius
        - center : container of coordinates, optional
            The center {Default=(0, 0, 0)}

        Returns
        -------
        - sphere [TopoDS_Solid]:
            The resulting sphere
        """
        return BRepPrimAPI_MakeSphere(CreatePoint.as_point(center), radius).Solid()

    @staticmethod
    def solid_from_circle(circle: gp_Circ) -> TopoDS_Solid:
        """Build a sphere from a circle.

        Parameters
        ----------
        - circle: gp_Circ
            The base circle

        Returns
        -------
        - sphere [TopoDS_Solid]:
            The resulting sphere
        """
        return BRepPrimAPI_MakeSphere(circle.Location(), circle.Radius()).Solid()
