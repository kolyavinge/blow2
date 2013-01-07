# -*- coding: utf-8 -*-

import unittest
from blow.model.Geometry import *

class GeometryTest(unittest.TestCase): 

    def testGetMoveVectorPoint_Left(self):
        expectedVector = (1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0))
        actualVector = getMoveVectorPoint(-1.0, -1.0)
        self.assertVectors(expectedVector, actualVector)
    
    def testGetMoveVectorPoint_Center(self):
        expectedVector = (0.0, 1.0)
        actualVector = getMoveVectorPoint(0.0, -1.0)
        self.assertVectors(expectedVector, actualVector)
    
    def testGetMoveVectorPoint_Right(self):
        expectedVector = (-1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0))
        actualVector = getMoveVectorPoint(1.0, -1.0)
        self.assertVectors(expectedVector, actualVector)

    def assertVectors(self, expectedVector, actualVector):
        self.assertAlmostEqual(expectedVector[0], actualVector[0], 0.001)
        self.assertAlmostEqual(expectedVector[1], actualVector[1], 0.001)

    def assertAlmostEqual(self, expected, actual, epsilon):
        self.assertTrue(math.fabs(expected - actual) <= epsilon, "{0} != {1}".format(expected, actual))

