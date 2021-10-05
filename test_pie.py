import unittest
import pie


class TestIsDateCalc(unittest.TestCase):

    def setUp(self):
        self.case1 = (0, 55, 55)
        self.case2 = (12, 55, 55)
        self.case3 = (13, 55, 55)
        self.case4 = (99, 99, 99)
        self.case5 = (87, 20, 40)

        self.otherSide1 = (100, 45, 45)
        self.otherSide2 = (62, 45, 45)
        self.otherSide3 = (63, 45, 45)
        self.otherSide4 = (99, 26, 75,)
        self.otherSide5 = (75, 26, 75,)

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

    def test_otherSide(self):
        self.assertEqual(
            pie.checkPoint(self.otherSide1[0], self.otherSide1[1], self.otherSide1[2]), "black")

        self.assertEqual(
            pie.checkPoint(self.otherSide2[0], self.otherSide2[1], self.otherSide2[2]), "white")

        self.assertEqual(
            pie.checkPoint(self.otherSide3[0], self.otherSide3[1], self.otherSide3[2]), "black")

        self.assertEqual(
            pie.checkPoint(self.otherSide4[0], self.otherSide4[1], self.otherSide4[2]), "black")

        self.assertEqual(
            pie.checkPoint(self.otherSide5[0], self.otherSide5[1], self.otherSide5[2]), "white")


if __name__ == '__main__':
    unittest.main()
