from OCC.Core.Geom import Geom_CylindricalSurface

from pyoccad.create import CreateCircle, CreateCylinder, CreateSurface, CreateUnsignedCoordSystem
from pyoccad.tests.testcase import TestCase


class CreateSurfaceTest(TestCase):
    def test_as_cylindrical(self):
        surface = CreateSurface.cylindrical(CreateUnsignedCoordSystem.ox(), 1.0)
        self.assertIsInstance(surface, Geom_CylindricalSurface)

    def test_from_cylinder(self):
        cylinder = CreateCylinder.from_circle(
            CreateCircle.from_radius_and_center(1.0, (0.0, 0.0, 0.0), (1.0, 0.0, 0.0))
        )
        surface = CreateSurface.from_cylinder(cylinder.Cylinder())
        self.assertIsInstance(surface, Geom_CylindricalSurface)
