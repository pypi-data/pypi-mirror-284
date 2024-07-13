from math import pi, sqrt

from OCC.Core.Geom import Geom_Ellipse
from OCC.Core.gp import gp_Pnt

from pyoccad.create.curve.ellipse import CreateEllipse
from pyoccad.create.direction import CreateDirection
from pyoccad.create.point import CreatePoint
from pyoccad.tests.testcase import TestCase


class CreateEllipseTest(TestCase):
    @staticmethod
    def build_ellipse():
        center = CreatePoint.as_point((1.0, 2.0, 3.0))
        normal_direction = CreateDirection.as_direction((0.0, 0.0, 1.0))
        major_axis_direction = CreateDirection.as_direction((0.0, 1.0, 0.0))

        ellipse = CreateEllipse.from_center_directions_radii(
            center, (normal_direction, major_axis_direction), (5.0, 10.0)
        )
        return ellipse

    def test_from_center_directions_radii(self):
        ellipse = CreateEllipseTest.build_ellipse()

        self.assertIsInstance(ellipse, Geom_Ellipse)
        self.assertEqual(10.0, ellipse.MajorRadius())
        self.assertEqual(5.0, ellipse.MinorRadius())
        self.assertAlmostEqual(sqrt(1 - 0.5**2), ellipse.Eccentricity())
        self.assertTrue(ellipse.IsClosed())

        point_ = gp_Pnt()
        ellipse.D0(0.0, point_)
        self.assertAlmostSameCoord(gp_Pnt(1.0, 12.0, 3.0), point_)
        ellipse.D0(pi / 2.0, point_)
        self.assertAlmostSameCoord(gp_Pnt(-4.0, 2.0, 3.0), point_)
        ellipse.D0(pi, point_)
        self.assertAlmostSameCoord(gp_Pnt(1.0, -8.0, 3.0), point_)
        ellipse.D0(3 * pi / 2.0, point_)
        self.assertAlmostSameCoord(gp_Pnt(6.0, 2.0, 3.0), point_)
