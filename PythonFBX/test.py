import unreal as ue
import fbx
import FbxCommon
import os
import cgtw2


def set_camera_property(fbx_file_path, component):
    lSdkManager, lScene = FbxCommon.InitializeSdkObjects()
    lResult = FbxCommon.LoadScene(lSdkManager, lScene, fbx_file_path)
    root_node = lScene.GetRootNode()
    if not os.path.exists(fbx_file_path):
        return
    if not isinstance(component, ue.CineCameraComponent):
        return 
    if not root_node:
        return
    for i in range(root_node.GetChildCount()):
        child_node = root_node.GetChild(i)
        node_type = child_node.GetNodeAttribute().GetAttributeType()
        if node_type == fbx.FbxNodeAttribute.eCamera:
            camera_attr_obj = child_node.GetNodeAttribute()
            if camera_attr_obj.GetApertureMode() == fbx.FbxCamera.eFocalLength:
                FocalLength = camera_attr_obj.FocalLength.Get()
                FieldOfView = camera_attr_obj.ComputeFieldOfView(FocalLength)
            else:
                FieldOfView = camera_attr_obj.FieldOfView.Get()
                FocalLength = camera_attr_obj.ComputeFocalLength(FieldOfView)
            ApertureWidth = camera_attr_obj.GetApertureWidth()
            ApertureHeight = camera_attr_obj.GetApertureHeight()
            component.set_projection_mode(ue.CameraProjectionMode.PERSPECTIVE if camera_attr_obj.ProjectionType.Get() == fbx.FbxCamera.ePerspective else ue.CameraProjectionMode.ORTHOGRAPHIC)
            component.set_aspect_ratio(camera_attr_obj.AspectWidth.Get() / camera_attr_obj.AspectHeight.Get())
            component.set_ortho_near_clip_plane(camera_attr_obj.NearPlane.Get())
            component.set_ortho_far_clip_plane(camera_attr_obj.FarPlane.Get())
            component.set_ortho_width(camera_attr_obj.OrthoZoom.Get())
            component.set_field_of_view(FieldOfView)
            if ue.SystemLibrary.get_engine_version().startswith("4.27"):
                component.filmback.sensor_width = 36.0
                component.filmback.sensor_height = 20.25
                component.focus_settings.focus_method = ue.CameraFocusMethod.DISABLE
            else:
                component.filmback_settings.sensor_width = ApertureWidth * 25.4
                component.filmback_settings.sensor_height = ApertureHeight * 25.4
            if FocalLength < component.lens_settings.min_focal_length:
        
                component.lens_settings.min_focal_length = FocalLength
        
            if FocalLength > component.lens_settings.max_focal_length:
        
                component.lens_settings.max_focal_length = FocalLength
        
            component.current_focal_length = FocalLength
