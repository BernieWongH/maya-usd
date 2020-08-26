#!/usr/bin/env python


import unittest
import maya.OpenMaya as om
import maya.cmds as cmds
import tempfile
import os

BASIC_TEST_EXPECTED_OUTPUT ='
#usda 1.0
(
    defaultPrim = "pCube1"
    metersPerUnit = 0.01
    upAxis = "Y"
)

def Mesh "pCube1" (
    prepend apiSchemas = ["MaterialBindingAPI"]
    kind = "component"
)
{
    uniform bool doubleSided = 1
    rel material:binding = </pCube1/Looks/initialShadingGroup>

    def BlendShape "pCubeShape2"
    {
    }

    def Scope "Looks"
    {
        def Material "initialShadingGroup"
        {
        }
    }
}
'


def mayaCreateBlendShapeTestSetup():
    om.MFileIO.newFile(True)

    # NOTE: (yliangsiew) Basic case: 1 base : 1 target
    cubeBase = cmds.polyCube()
    cubeTgt = cmds.duplicate()
    cmds.blendShape(cubeTgt, cubeBase, automatic=True)

    # TODO: (yliangsiew) Add the other cases that are already set up in the Maya test scene.

    return cubeBase


class MayaUsdBlendShapesTestCase(unittest.TestCase):
    """
    Verify that exporting blend shapes from Maya works.
    """
    def __init__(self):
        self.tempDir = ''

    @classmethod
    def setUpClass(cls):
        cmds.loadPlugin('mayaUsdPlugin')
        self.tempDir = tempfile.mkdtemp()

    def testBlendShapesExport(self):
        om.MFileIO.newFile(True)
        cubeBase = mayaCreateBlendShapeTestSetup()
        cmds.select(cubeBase, replace=True)
        tempFile = os.path.join(self.tempDir, 'test.usda')
        cmds.mayaUsdExport(tempFile, v=True, sl=True, ebs=True, skl="auto")
        self.assertTrue(os.path.isfile(tempFile))

        with open(tempFile, 'r') as f:
            buf = f.read()

        self.assertEqual(buf, BASIC_TEST_EXPECTED_OUTPUT)
