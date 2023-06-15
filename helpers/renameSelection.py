import bpy

# == PROPERTIES:
Properties = [
    ('rs_prefix', bpy.props.StringProperty(name='prefix', default='pre_')),
    ('rs_suffix', bpy.props.StringProperty(name='suffix', default='_suff')),
    ('rs_addPrefix', bpy.props.BoolProperty(name='Add Prefix', default=False)),
    ('rs_addSuffix', bpy.props.BoolProperty(name='Add Suffix', default=False)),
    ('rs_changeName', bpy.props.BoolProperty(name='Change Name', default=False)),
    ('rs_newName', bpy.props.StringProperty(name='New Name', default='DefaultCube')),
    ('rs_addVersioning', bpy.props.BoolProperty(name='Custom Versioning', default=False)),
    ('rs_startVersion', bpy.props.IntProperty(name='Start Version', default=0)),
]


# == PANEL
class RenameSelectionPanel(bpy.types.Panel):

    bl_idname = 'RenameSelectionPanel'
    bl_label = 'Rename Selection'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'rs_addPrefix')
        col.prop(context.scene, 'rs_prefix')
        col.prop(context.scene, 'rs_addSuffix')
        col.prop(context.scene, 'rs_suffix')
        col.prop(context.scene, 'rs_changeName')
        col.prop(context.scene, 'rs_newName')
        col.prop(context.scene, 'rs_addVersioning')
        col.prop(context.scene, 'rs_startVersion')

        col.operator('opr.rename_all_selected_objects', text='Rename')
# == Operators
class RenameSelectionOperator(bpy.types.Operator):
    """Rename All Selected Objects"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rename_all_selected_objects"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rename Selection"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.rs_prefix,
            context.scene.rs_suffix,
            context.scene.rs_addPrefix,
            context.scene.rs_addSuffix,
            context.scene.rs_changeName,
            context.scene.rs_newName,
            context.scene.rs_addVersioning,
            context.scene.rs_startVersion,
        )

        # This Script allows you to Change the names of all selected objects at once and/or add pre/suffixes to them

        #set your custom prefix and suffix here or disable them
        addPrefix = context.scene.rs_addPrefix
        addSuffix = context.scene.rs_addSuffix
        prefix = context.scene.rs_prefix
        suffix = context.scene.rs_suffix

        #Set this true if you want to change the current name
        changeName = context.scene.rs_changeName
        newName = context.scene.rs_newName

        # Set "addVersioning" True if you want to add versioning at the end with this syntax -> "defaultCube_0" , "defaultCube_1" .. "defaultCube_42"
        # instead of blender default "defaultCube.001" , "defaultCube.002" .. "defaultCube.042"
        # Change "startVersion" if you don't want the versioning to start from 0
        # Keep in mind that blender will automatically add versioning if objects have the same name
        addVersioning = context.scene.rs_addVersioning
        startVersion = context.scene.rs_startVersion

        selection_list = bpy.context.selected_objects
        for obj in selection_list:
            _name = obj.name
            if changeName:
                _name = newName
            if addPrefix:
                _name = prefix + _name
            if addSuffix:
                _name = _name + suffix
            if addVersioning:
                _name = _name + "_" + str(startVersion)

            obj.name = _name
            startVersion = startVersion + 1

        return {'FINISHED'}


Classes = [
RenameSelectionPanel,
RenameSelectionOperator,
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
