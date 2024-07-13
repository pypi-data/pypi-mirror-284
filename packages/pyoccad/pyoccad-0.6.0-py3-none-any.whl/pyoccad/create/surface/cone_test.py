from math import pi

from pyoccad.create import CreateCircle, CreateCone
from pyoccad.measure import solid as ms
from pyoccad.tests.testcase import TestCase


class CreateConeTest(TestCase):
    def test_solid_from_base_and_height(self):
        circle = CreateCircle.from_radius_and_center(1.0, [0, 0, 0], [1, 0, 0])
        c1 = CreateCone.solid_from_base_and_height(circle, 1.0)
        self.assertAlmostEqualValues(ms.volume(c1), pi / 3)
