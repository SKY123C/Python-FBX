from logging import root
import sys
sys.path.append("C:/Program Files/Autodesk/FBX/FBX Python SDK/2020.0.1/lib/Python33_x64")

import FbxCommon
from fbx import *
KFCURVENODE_T_X = "X"
KFCURVENODE_T_Y = "Y"
KFCURVENODE_T_Z = "Z"

KFCURVENODE_R_X = "X"
KFCURVENODE_R_Y = "Y"
KFCURVENODE_R_Z = "Z"
KFCURVENODE_R_W = "W"

KFCURVENODE_S_X = "X"
KFCURVENODE_S_Y = "Y"
KFCURVENODE_S_Z = "Z"
manager,Scene= FbxCommon.InitializeSdkObjects()

FbxCommon.LoadScene(manager, Scene, 'FBXCube.fbx')

rootNode = Scene.GetRootNode().GetChild(0)

for i in range(Scene.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimStack.ClassId))):
    lAnimStack = Scene.GetSrcObject(FbxCriteria.ObjectType(FbxAnimStack.ClassId), i)
    #print(lAnimStack.GetName())
    nbAnimLayers = lAnimStack.GetSrcObjectCount(FbxCriteria.ObjectType(FbxAnimLayer.ClassId))
    #print(nbAnimLayers)
    for l in range(nbAnimLayers):
        lAnimLayer = lAnimStack.GetSrcObject(FbxCriteria.ObjectType(FbxAnimLayer.ClassId), l)

        lAnimCurve = rootNode.LclTranslation.GetCurve(lAnimLayer, KFCURVENODE_T_X)
        lKeyCount = lAnimCurve.KeyGetCount()
        #print(dir(lAnimCurve))
        print(dir(lAnimCurve.KeyGetTime(0)))
        print(lAnimCurve.KeyGetTime(0).GetFrameCount(FbxTime.eFrames30))
        #print(dir(lAnimCurve))

# rootNode = scene.GetRootNode()
# print(fbx.FbxCriteria.ObjectType(fbx.FbxAnimStack.ClassId))
# print(scene.GetSrcObjectCount(fbx.FbxCriteria.ObjectType(fbx.FbxAnimStack.ClassId)))
# print(fbx.FbxAnimLayer.ClassId)
# for i in range(rootNode.GetChildCount()):
#     a = rootNode.GetChild(i)
#     #print(dir(a.GetNodeAttribute()))



# #print(dir(rootNode))

# for i in range(0, scene.GetSrcObjectCount()):
    
#     pass
#     #stack = scene.GetSrcObject(i)
#     #print(stack.GetName())
