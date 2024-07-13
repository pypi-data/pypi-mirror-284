from OCC.Core.gp import gp_Pnt
from OCC.Core.TopoDS import TopoDS_Vertex

from pyoccad.create import CreatePoint, CreateVertex
from pyoccad.tests.testcase import TestCase


class CreatVertexTest(TestCase):
    def test_from_point(self):
        vertex = CreateVertex.from_point((10.0, 20.0, 30.0))
        self.assertIsInstance(vertex, TopoDS_Vertex)

        point = CreatePoint.from_vertex(vertex)
        self.assertIsInstance(point, gp_Pnt)
        self.assertAlmostSameCoord(point, (10.0, 20.0, 30.0))
