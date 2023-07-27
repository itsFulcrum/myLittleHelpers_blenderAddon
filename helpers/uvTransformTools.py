import bpy

# == PROPERTIES:
Properties = [
# Create LightmapUVs tool

#we currently dont need anything here

]


# == PANEL
class UVTransformToolsPanel(bpy.types.Panel):

    bl_idname = 'UVTransformToolsPanel'
    bl_label = 'UV Transform Tools'
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        # lightmap pack

        # rename uv layers
        col.operator('opr.rotate_uv_island_45_degrees', text='Rotate +45')
        col.operator('opr.rotate_uv_island_minus_45_degrees', text='Rotate -45')
        col.operator('opr.rotate_uv_island_90_degrees', text='Rotate +90')
        col.operator('opr.rotate_uv_island_minus_90_degrees', text='Rotate -90')
        col.operator('opr.rotate_uv_island_180_degrees', text='Rotate +180')





# == Operators
class RotateIslands45Operator(bpy.types.Operator):
    """rotate selected uv islands by 45 degrees"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rotate_uv_island_45_degrees"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rotate UV Island by 45"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
        )
        # rotates all selected uv islands by 45 degrees
        context = bpy.context
        last_area = bpy.context.area.type
        bpy.context.area.type = 'IMAGE_EDITOR'

        # check if in edit mode
        if(context.object.mode == 'EDIT'):
            bpy.ops.transform.rotate(value=0.785398)
        else:
            self.report({'INFO'}, 'MyLittleHelpersAddon: -> you are not in edit mode')

        bpy.context.area.type = last_area
        return {'FINISHED'}

# == Operators
class RotateIslandsMinus45Operator(bpy.types.Operator):
    """rotate selected uv islands by -45 degrees"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rotate_uv_island_minus_45_degrees"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rotate UV Island by -45"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
        )
        # rotates all selected uv islands by -45 degrees
        context = bpy.context
        last_area = bpy.context.area.type
        bpy.context.area.type = 'IMAGE_EDITOR'

        # check if in edit mode
        if(context.object.mode == 'EDIT'):
            bpy.ops.transform.rotate(value=-0.785398)
        else:
            self.report({'INFO'}, 'MyLittleHelpersAddon: -> you are not in edit mode')

        bpy.context.area.type = last_area
        return {'FINISHED'}


# == Operators
class RotateIslands90Operator(bpy.types.Operator):
    """rotate selected uv islands by 90 degrees"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rotate_uv_island_90_degrees"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rotate UV Island by 90"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
        )
        # rotates all selected uv islands by 90 degrees
        context = bpy.context
        last_area = bpy.context.area.type
        bpy.context.area.type = 'IMAGE_EDITOR'

        # check if in edit mode
        if(context.object.mode == 'EDIT'):
            bpy.ops.transform.rotate(value=1.5708)
        else:
            self.report({'INFO'}, 'MyLittleHelpersAddon: -> you are not in edit mode')

        bpy.context.area.type = last_area
        return {'FINISHED'}

# == Operators
class RotateIslandsMinus90Operator(bpy.types.Operator):
    """rotate selected uv islands by -90 degrees"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rotate_uv_island_minus_90_degrees"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rotate UV Island by -90"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
        )
        # rotates all selected uv islands by 90 degrees
        context = bpy.context
        last_area = bpy.context.area.type
        bpy.context.area.type = 'IMAGE_EDITOR'

        # check if in edit mode
        if(context.object.mode == 'EDIT'):
            bpy.ops.transform.rotate(value=-1.5708)
        else:
            self.report({'INFO'}, 'MyLittleHelpersAddon: -> you are not in edit mode')

        bpy.context.area.type = last_area
        return {'FINISHED'}

# == Operators
class RotateIslands180Operator(bpy.types.Operator):
    """rotate selected uv islands by 180 degrees"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rotate_uv_island_180_degrees"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rotate UV Island by 180"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
        )
        # rotates all selected uv islands by 90 degrees
        context = bpy.context
        last_area = bpy.context.area.type
        bpy.context.area.type = 'IMAGE_EDITOR'

        # check if in edit mode
        if(context.object.mode == 'EDIT'):
            bpy.ops.transform.rotate(value=3.14159)
        else:
            self.report({'INFO'}, 'MyLittleHelpersAddon: -> you are not in edit mode')

        bpy.context.area.type = last_area
        return {'FINISHED'}




Classes = [
UVTransformToolsPanel,
RotateIslands45Operator,
RotateIslandsMinus45Operator,
RotateIslands90Operator,
RotateIslandsMinus90Operator,
RotateIslands180Operator,
]

def register():
    for (prop_name, prop_value) in Properties:
        setattr(bpy.types.Scene, prop_name, prop_value)

    for cls in Classes:
        bpy.utils.register_class(cls)

def unregister():
    for (prop_name, prop_value) in Properties:
        delattr(bpy.types.Scene, prop_name)

    for cls in Classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
