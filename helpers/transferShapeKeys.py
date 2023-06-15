import bpy

# == PROPERTIES:
Properties = [
('copyFrom', bpy.props.StringProperty(name='CopyFromMesh', default='CopyFrom')),
('copyTo', bpy.props.StringProperty(name='CopyToMesh', default='CopyTo')),
]


# == PANEL
class TransferShapeKeysPanel(bpy.types.Panel):

    bl_idname = 'TransferShapeKeysPanel'
    bl_label = 'Transfer Shape Keys'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'copyFrom')
        col.prop(context.scene, 'copyTo')
        col.operator('opr.transfer_all_shape_keys', text='Transfer Shapekeys')


# == Operators
class TransferShapeKeysOperator(bpy.types.Operator):
    """transfer all shape keys at once to a target"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.transfer_all_shape_keys"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Transfer Shapekeys"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.copyFrom,
            context.scene.copyTo,
        )

        # Copy objects name
        copyFromName = context.scene.copyFrom
        copyToName = context.scene.copyTo

        copyFrom = bpy.data.objects[copyFromName]
        copyTo = bpy.data.objects[copyToName]

        bpy.ops.object.mode_set(mode='OBJECT')   # force object mode
        # clear selection
        bpy.ops.object.select_all(action='DESELECT')
        # select copyFrom
        copyFrom.select_set(True)
        # select copyTo
        copyTo.select_set(True)
        # make copyTo active object
        bpy.context.view_layer.objects.active = copyTo

        for shapeKeyIndex in range(1, len(copyFrom.data.shape_keys.key_blocks)):
            # select next shape key
            copyFrom.active_shape_key_index = shapeKeyIndex
            # transfer shapekey
            bpy.ops.object.shape_key_transfer()

        # for loop end

        copyTo.show_only_shape_key = False
        bpy.ops.object.select_all(action='DESELECT')
        copyTo.select_set(True)
        bpy.context.view_layer.objects.active = copyTo



        return {'FINISHED'}


Classes = [
TransferShapeKeysPanel,
TransferShapeKeysOperator,
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
