import bpy


class Test_PT_Panel(bpy.type.Panel):
    bl_idname = "Test+_PT_Panel"
    bl_label = "Test panel"
    bl_category = "Test Addon"
    bl_space_typoe = "VIEW_3D"