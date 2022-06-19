import sys

sys.path.append(r"C:\Program Files\Autodesk\FBX\FBX Python SDK\2020.0.1\samples\ImportScene")
sys.path.append("C:/Program Files/Autodesk/FBX/FBX Python SDK/2020.0.1/lib/Python33_x64")

import FbxCommon
from fbx import *
import DisplayAnimation

manager,Scene= FbxCommon.InitializeSdkObjects()

FbxCommon.LoadScene(manager, Scene, 'FBXCube.fbx')
rootNode = Scene.GetRootNode()
DisplayAnimation.DisplayAnimation(Scene)