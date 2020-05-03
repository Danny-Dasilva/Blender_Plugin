import bpy


class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "Test+_PT_Panel"
    bl_label = "Test panel"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        # layout = self.layout
        # row = layout.row
        #
        layout = self.layout
        layout.operator('view3d.cursor_center', text="Center 3D cursor")
        box = layout.box()
        box.label(text="Selection Tools")
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")