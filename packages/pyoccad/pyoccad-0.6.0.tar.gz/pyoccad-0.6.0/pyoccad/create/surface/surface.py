from OCC.Core.Adaptor3d import Adaptor3d_Surface
from OCC.Core.BRepAdaptor import BRepAdaptor_Surface
from OCC.Core.Geom import Geom_CylindricalSurface, Geom_Surface
from OCC.Core.GeomAdaptor import GeomAdaptor_Surface
from OCC.Core.gp import gp_Ax3, gp_Cylinder
from OCC.Core.TopoDS import TopoDS_Face

from pyoccad.typing import Surface3D


class CreateSurface:
    """Factory to create surfaces."""

    @staticmethod
    def as_adaptor(surface: Surface3D) -> Adaptor3d_Surface:
        """Create a surface adaptor.

        Parameters
        ----------
        surface: Union[Geom_Surface, TopoDS_Face]
            The surface

        Returns
        -------
        adaptor: Adaptor3d_Surface
            The resulting adaptor
        """
        if isinstance(surface, Geom_Surface):
            return GeomAdaptor_Surface(surface)
        if isinstance(surface, TopoDS_Face):
            return BRepAdaptor_Surface(surface)
        if isinstance(surface, Adaptor3d_Surface):
            return surface

        raise TypeError('Unsupported type "{}".'.format(type(surface)))

    @staticmethod
    def cylindrical(coord_system: gp_Ax3, radius: float) -> Geom_CylindricalSurface:
        """Create a cylindrical surface from its definition.

        Parameters
        ----------
        coord_system: gp_Ax3
            The coordinate system
        radius: float
            The radius

        Returns
        -------
        surface: Geom_CylindricalSurface
            The resulting surface
        """
        return Geom_CylindricalSurface(coord_system, radius)

    @staticmethod
    def from_cylinder(cylinder: gp_Cylinder) -> Geom_CylindricalSurface:
        """Create a cylindrical surface from a cylinder.

        Parameters
        ----------
        cylinder: gp_Cylinder
            The cylinder geometry

        Returns
        -------
        surface: Geom_CylindricalSurface
            The resulting surface
        """
        return Geom_CylindricalSurface(cylinder)
