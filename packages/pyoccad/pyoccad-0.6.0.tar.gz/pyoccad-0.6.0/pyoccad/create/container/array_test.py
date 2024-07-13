import numpy as np
from OCC.Core.gp import gp_Pnt, gp_Pnt2d, gp_Vec, gp_Vec2d
from OCC.Core.TColStd import (
    TColStd_Array1OfBoolean,
    TColStd_Array1OfInteger,
    TColStd_Array1OfReal,
    TColStd_Array2OfBoolean,
    TColStd_Array2OfInteger,
    TColStd_Array2OfReal,
)

from pyoccad.create.container.array import CreateArray1, CreateArray2
from pyoccad.tests.testcase import TestCase


class CreateArray1Test(TestCase):
    def test_has_strict_positive_length(self):
        self.assertEqual(3, CreateArray1.has_strict_positive_length((0.0, 3, 5)))
        self.assertEqual(1, CreateArray1.has_strict_positive_length([0]))

        with self.assertRaises(ValueError):
            CreateArray1.has_strict_positive_length([])
        with self.assertRaises(ValueError):
            CreateArray1.has_strict_positive_length(())
        with self.assertRaises(TypeError):
            CreateArray1.has_strict_positive_length(True)

    def test_of_points(self):
        result = CreateArray1.of_points([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result.Length(), 2)
        self.assertIsInstance(result.Value(1), gp_Pnt)

        result = CreateArray1.of_points([[1, 2], [3, 4]])
        self.assertEqual(result.Length(), 2)
        self.assertIsInstance(result.Value(1), gp_Pnt2d)

        with self.assertRaises(TypeError):
            CreateArray1.of_points([[1, 2, 3], [4, 5]])
        with self.assertRaises(ValueError):
            CreateArray1.of_points([])
        with self.assertRaises(TypeError):
            CreateArray1.of_points([(1,)])
        with self.assertRaises(TypeError):
            CreateArray1.of_points(["abc"])

    def test_of_vectors(self):
        result = CreateArray1.of_vectors([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result.Length(), 2)
        self.assertIsInstance(result.Value(1), gp_Vec)

        result = CreateArray1.of_vectors([[1, 2], [3, 4]])
        self.assertEqual(result.Length(), 2)
        self.assertIsInstance(result.Value(1), gp_Vec2d)

        with self.assertRaises(TypeError):
            CreateArray1.of_vectors([[1, 2, 3], [4, 5]])
        with self.assertRaises(ValueError):
            CreateArray1.of_vectors([])
        with self.assertRaises(TypeError):
            CreateArray1.of_vectors([(1,)])
        with self.assertRaises(TypeError):
            CreateArray1.of_vectors(["abc"])

    def test_of_integers(self):
        int_list = [1, 2, 3, 4, 5]
        arr1 = CreateArray1.of_integers(int_list)
        self.assertEqual(arr1.Length(), len(int_list))
        self.assertIsInstance(arr1, TColStd_Array1OfInteger)
        for i, val in enumerate(int_list):
            self.assertEqual(arr1.Value(i + 1), val)

        with self.assertRaises(ValueError):
            CreateArray1.of_integers([])
        with self.assertRaises(TypeError):
            CreateArray1.of_integers([1, 2, 3, 4.0])

    def test_of_floats(self):
        float_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        arr1 = CreateArray1.of_floats(float_list)
        self.assertEqual(arr1.Length(), len(float_list))
        self.assertIsInstance(arr1, TColStd_Array1OfReal)
        for i, val in enumerate(float_list):
            self.assertEqual(arr1.Value(i + 1), val)

        with self.assertRaises(ValueError):
            CreateArray1.of_floats([])

    def test_of_booleans(self):
        bool_list = [True, True, False, True, True]
        arr1 = CreateArray1.of_booleans(bool_list)
        self.assertEqual(arr1.Length(), len(bool_list))
        self.assertIsInstance(arr1, TColStd_Array1OfBoolean)
        for i, val in enumerate(bool_list):
            self.assertEqual(arr1.Value(i + 1), val)

        with self.assertRaises(TypeError):
            CreateArray1.of_booleans([[1, 2, 3], True, False, True, True])
        with self.assertRaises(ValueError):
            CreateArray1.of_booleans([])
        with self.assertRaises(TypeError):
            CreateArray1.of_booleans([0, 1])


class CreateArray2Test(TestCase):
    def test_of_points(self):
        result = CreateArray2.of_points([[[1, 2, 3]], [[4, 5, 6]]])
        self.assertEqual(result.Length(), 2)
        self.assertIsInstance(result.Value(1, 1), gp_Pnt)

        result = CreateArray2.of_points([[[1, 2]], [[3, 4]]])
        self.assertEqual(result.Length(), 2)
        self.assertIsInstance(result.Value(1, 1), gp_Pnt2d)

        with self.assertRaises(TypeError):
            CreateArray2.of_points([[[1, 2, 3]], [[4, 5]]])
        with self.assertRaises(ValueError):
            CreateArray2.of_points([])
        with self.assertRaises(TypeError):
            CreateArray2.of_points([[(1,)]])
        with self.assertRaises(TypeError):
            CreateArray2.of_points([["abc"]])

    def test_of_integers(self):
        int_list = [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]]
        arr = CreateArray2.of_integers(int_list)
        self.assertEqual(arr.Length(), np.size(int_list))
        self.assertIsInstance(arr, TColStd_Array2OfInteger)
        for i, row in enumerate(int_list):
            for j, val in enumerate(row):
                self.assertEqual(arr.Value(i + 1, j + 1), val)

        with self.assertRaises(ValueError):
            CreateArray2.of_integers([[]])
        with self.assertRaises(TypeError):
            CreateArray2.of_integers([[1, 2, 3, 4.0]])

    def test_of_floats(self):
        float_list = [[1.0, 2.0, 3.0, 4.0, 5.0], [11.0, 12.0, 13.0, 14.0, 15.0]]
        arr = CreateArray2.of_floats(float_list)
        self.assertEqual(arr.Length(), np.size(float_list))
        self.assertIsInstance(arr, TColStd_Array2OfReal)
        for i, row in enumerate(float_list):
            for j, val in enumerate(row):
                self.assertEqual(arr.Value(i + 1, j + 1), val)

        with self.assertRaises(ValueError):
            CreateArray2.of_floats([[]])

    def test_of_booleans(self):
        bool_list = [[True, True, False, True, True]]
        arr = CreateArray2.of_booleans(bool_list)
        self.assertEqual(arr.Length(), np.size(bool_list))
        self.assertIsInstance(arr, TColStd_Array2OfBoolean)
        for i, row in enumerate(bool_list):
            for j, val in enumerate(row):
                self.assertEqual(arr.Value(i + 1, j + 1), val)

        with self.assertRaises(TypeError):
            CreateArray2.of_booleans([[[1, 2, 3], True, False, True, True]])
        with self.assertRaises(ValueError):
            CreateArray2.of_booleans([[]])
        with self.assertRaises(TypeError):
            CreateArray2.of_booleans([[0, 1]])
