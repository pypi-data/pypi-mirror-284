from math import pi

from OCC.Core.Geom import Geom_CylindricalSurface
from OCC.Core.TopoDS import TopoDS_Shape

from pyoccad.create import CreateCircle, CreateCylinder
from pyoccad.measure import solid as ms
from pyoccad.tests.testcase import TestCase


class CreateCylinderTest(TestCase):
    def test_from_circle(self):
        circle = CreateCircle.from_radius_and_center(1.0, (1.0, 1.0, 2.0), (0.0, 0.0, 1.0))
        c1 = CreateCylinder.from_circle(circle)
        self.assertAlmostSameCoord(c1.Location(), (1.0, 1.0, 2.0))
        self.assertAlmostEqual(c1.Radius(), 1.0)
        self.assertIsInstance(c1, Geom_CylindricalSurface)

    def test_solid_from_base_and_height(self):
        circle = CreateCircle.from_radius_and_center(1.0, (1.0, 1.0, 2.0), (0.0, 0.0, 1.0))
        c1 = CreateCylinder.solid_from_base_and_height(circle, 1.0)
        self.assertAlmostEqualValues(ms.volume(c1), pi)
        cg = ms.center(c1)
        self.assertAlmostSameCoord(cg, (1.0, 1.0, 2.5))
        self.assertIsInstance(c1, TopoDS_Shape)
