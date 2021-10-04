import unittest
import pie


class TestIsDateCalc(unittest.TestCase):

    def setUp(self):
        self.case1 = (0, 55, 55)
        self.case2 = (12, 55, 55)
        self.case3 = (13, 55, 55)
        self.case4 = (99, 99, 99)
        self.case5 = (87, 20, 40)

    def tearDown(self):
        pass

    def test_givenExamples(self):
        self.assertEqual(
            pie.checkPoint(self.case1[0], self.case1[1], self.case1[2]), "white")

        self.assertEqual(
            pie.checkPoint(self.case2[0], self.case2[1], self.case2[2]), "white")

        self.assertEqual(
            pie.checkPoint(self.case3[0], self.case3[1], self.case3[2]), "black")

        self.assertEqual(
            pie.checkPoint(self.case4[0], self.case4[1], self.case4[2]), "white")

        self.assertEqual(
            pie.checkPoint(self.case5[0], self.case5[1], self.case5[2]), "black")


if __name__ == '__main__':
    unittest.main()
