bl_info = {
    # required
    'name': 'Rename Selection',
    'blender': (3, 0, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 0),
    'author': 'Janis Civan',
    'description': 'Rename entire selection at once',
}

import bpy

# == PROPERTIES:
PROPS = [
    ('addPrefix', bpy.props.BoolProperty(name='Add Prefix', default=True)),
    ('prefix', bpy.props.StringProperty(name='Prefix', default='Pref_')),
    ('addSuffix', bpy.props.BoolProperty(name='Add Suffix', default=True)),
    ('suffix', bpy.props.StringProperty(name='Suffix', default='_Suff')),
    ('changeName', bpy.props.BoolProperty(name='Change Name', default=False)),
    ('newName', bpy.props.StringProperty(name='New Name', default='dafaultCube')),
    ('addVersion', bpy.props.BoolProperty(name='Add Version', default=False)),
    ('startVersion', bpy.props.IntProperty(name='startVersion', default=0)),
]

# == PANELS
class RenameSelectionPanel(bpy.types.Panel):

    bl_idname = 'VIEW3D_PT_RS_panel'
    bl_label = 'Rename Selection'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rename Selection'


    def draw(self, context):
        col = self.layout.column()
        for (prop_name, _) in PROPS:
            row = col.row()
            row.prop(context.scene, prop_name)
        col.operator('opr.object_rename_selection', text='Rename')

# == OPERATORS
class RenameSelectionOperator(bpy.types.Operator):
    bl_idname = 'opr.object_rename_selection'
    bl_label = 'rename selection'

    def execute(self, context):
        params = (
            context.scene.addPrefix,
            context.scene.addSuffix,
            context.scene.prefix,
            context.scene.suffix,
            context.scene.changeName,
            context.scene.newName,
            context.scene.addVersion,
            context.scene.addVersion,
        )

        # renameObjects()

        _addPrefix = context.scene.addPrefix
        _addSuffix = context.scene.addSuffix
        _prefix = context.scene.prefix
        _suffix = context.scene.suffix

        _changeName = context.scene.changeName
        _newName = context.scene.newName

        _addVersioning = context.scene.addVersion
        _startVersion = context.scene.startVersion

        selection_list = bpy.context.selected_objects

        for obj in selection_list:
            _name = obj.name

            if _changeName:
                _name = _newName
            if _addPrefix:
                _name = _prefix + _name
            if _addSuffix:
                _name = _name + _suffix

            if _addVersioning:
                _name = _name + "_" + str(_startVersion)

            obj.name = _name
            _startVersion = _startVersion + 1

        return {'FINISHED'}

CLASSES = [
RenameSelectionPanel,
RenameSelectionOperator,
]

def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

    for klass in CLASSES:
        bpy.utils.register_class(klass)

def unregister():
    for (prop_name, prop_value) in PROPS:
        delattr(bpy.types.Scene, prop_name, prop_value)

    for klass in CLASSES:
        bpy.utils.unregister_class(klass)

if __name__ == '__main__':
    register()
