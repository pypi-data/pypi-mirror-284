from math import pi

from OCC.Core.Geom import Geom_SphericalSurface
from OCC.Core.TopoDS import TopoDS_Shape

from pyoccad.create import CreateCircle, CreateSphere
from pyoccad.measure import solid as ms
from pyoccad.tests.testcase import TestCase


class CreateSphereTest(TestCase):
    def test_from_circle(self):
        circle = CreateCircle.from_radius_and_center(1.0, (1.0, 1.0, 2.0), (0.0, 0.0, 1.0))
        s1 = CreateSphere.from_circle(circle)
        self.assertAlmostSameCoord(s1.Location(), (1.0, 1.0, 2.0))
        self.assertAlmostEqual(s1.Radius(), 1.0)
        self.assertIsInstance(s1, Geom_SphericalSurface)

    def test_solid_from_radius_and_center(self):
        s1 = CreateSphere.solid_from_radius_and_center(1.0, [1.0, 1.0, 2.0])
        self.assertAlmostEqualValues(ms.volume(s1), 4 * pi / 3)
        cg = ms.center(s1)
        self.assertAlmostSameCoord(cg, (1.0, 1.0, 2.0))
        self.assertIsInstance(s1, TopoDS_Shape)

    def test_solid_from_circle(self):
        circle = CreateCircle.from_radius_and_center(1.0, (1.0, 1.0, 2.0), (0.0, 0.0, 1.0))
        s1 = CreateSphere.solid_from_circle(circle)
        self.assertAlmostEqualValues(ms.volume(s1), 4 * pi / 3)
        cg = ms.center(s1)
        self.assertAlmostSameCoord(cg, (1.0, 1.0, 2.0))
        self.assertIsInstance(s1, TopoDS_Shape)
