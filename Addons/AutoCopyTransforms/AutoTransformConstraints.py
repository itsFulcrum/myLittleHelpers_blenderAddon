bl_info = {
    # required
    'name': 'Auto Transform Constraints',
    'blender': (3, 0, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 1),
    'author': 'Janis Civan',
    'description': 'Copy Transform from one rig to another',
}

import bpy

# == PROPERTIES:
PROPS = [
    ('sourceRig', bpy.props.StringProperty(name='CopyToRig', default='Armature')),
    ('targetRig', bpy.props.StringProperty(name='CopyFromRig', default='Armature.001')),
    ('removeConstraints', bpy.props.BoolProperty(name='Remove all constraints first', default=True)),
    ('applyConstraints', bpy.props.BoolProperty(name='Apply Constraints', default=True)),
    ('addLocationConstraint', bpy.props.BoolProperty(name='Location Constraint', default=False)),
    ('addRotationConstraint', bpy.props.BoolProperty(name='Rotation Constraint', default=True)),
    ('addScaleConstraint', bpy.props.BoolProperty(name='Scale Constraint', default=False)),
    # transfer shape key tool
    ('copyFrom', bpy.props.StringProperty(name='CopyFromMesh', default='CopyFrom')),
    ('copyTo', bpy.props.StringProperty(name='CopyToMesh', default='CopyTo')),
]


# == PANELS
class AutoCopyTransformsPanel(bpy.types.Panel):

    bl_idname = 'VIEW3D_PT_RS_panel'
    bl_label = 'AutoCopyTransforms'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Auto Copy Transforms'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'sourceRig')
        col.prop(context.scene, 'targetRig')
        col.prop(context.scene, 'removeConstraints')
        col.prop(context.scene, 'applyConstraints')
        col.prop(context.scene, 'addLocationConstraint')
        col.prop(context.scene, 'addRotationConstraint')
        col.prop(context.scene, 'addScaleConstraint')


        col.operator('opr.auto_copy_transforms', text='Copy Transforms')
        col.operator('opr.apply_existing_transforms', text='Apply Constraints')

# == PANELS
class TransferShapeKeysPanel(bpy.types.Panel):

    bl_idname = 'TransferShapeKeysPanel'
    bl_label = 'TransferShapeKeys'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Auto Copy Transforms'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'copyFrom')
        col.prop(context.scene, 'copyTo')
        col.operator('opr.transfer_all_shape_keys', text='Transfer Shapekeys')



# == Operators
# copy transforms tool

class AutoTransformsConstraintsOperator(bpy.types.Operator):
    """Copy transforms form an identical rig"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.auto_copy_transforms"        # Unique identifier for buttons and menu items to reference.
    bl_label = "copy Transforms from rig"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.sourceRig,
            context.scene.targetRig,
            context.scene.removeConstraints,
            context.scene.applyConstraints,
            context.scene.addLocationConstraint,
            context.scene.addRotationConstraint,
            context.scene.addScaleConstraint,
        )

        # The original script
        SourceRigName = context.scene.sourceRig
        TargetRigName = context.scene.targetRig

        removeAllConstraintsFirst = context.scene.removeConstraints# removes all constraints first before adding new ones
        applyAllConstraintsAfter = context.scene.applyConstraints # applys all constraints

        addCopyLocationConstraint = context.scene.addLocationConstraint
        addCopyRotationConstraint = context.scene.addRotationConstraint
        addCopyScaleConstraint = context.scene.addScaleConstraint


        # -------------------------------------------------
        source = bpy.data.objects[SourceRigName]
        target = bpy.data.objects[TargetRigName]

        userMode = bpy.context.object.mode      #store current mode
        bpy.ops.object.mode_set(mode='POSE')    #set mode to pose mode. Neccesary because we can only use apply operator in pose mode

        for bone in source.pose.bones:

            if removeAllConstraintsFirst:
                currentConstraints = bone.constraints
                for constraint in currentConstraints:
                    bone.constraints.remove(constraint)

            # set active bone to current bone in loop, to use apply operator on it
            bpy.context.object.data.bones.active = bone.bone

            if addCopyLocationConstraint:
                bone.constraints.new('COPY_LOCATION')
                CopyLocationConstraint = bone.constraints[-1]
                CopyLocationConstraint.target = target
                CopyLocationConstraint.subtarget = bone.name
                if applyAllConstraintsAfter:
                    bpy.ops.constraint.apply(constraint=CopyLocationConstraint.name, owner='BONE')

            if addCopyRotationConstraint:
                bone.constraints.new('COPY_ROTATION')
                CopyRotationConstraint = bone.constraints[-1]
                CopyRotationConstraint.target = target
                CopyRotationConstraint.subtarget = bone.name
                if applyAllConstraintsAfter:
                    bpy.ops.constraint.apply(constraint=CopyRotationConstraint.name, owner='BONE')

            if addCopyScaleConstraint:
                bone.constraints.new('COPY_SCALE')
                CopyScaleConstraint = bone.constraints[-1]
                CopyScaleConstraint.target = target
                CopyScaleConstraint.subtarget = bone.name
                if applyAllConstraintsAfter:
                    bpy.ops.constraint.apply(constraint=CopyScaleConstraint.name, owner='BONE')

        #set the mode back to what the user had before
        bpy.ops.object.mode_set(mode=userMode)


        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

class ApplyExistingConstraintsOperator(bpy.types.Operator):
    """Apply all Existing constraints on a rig"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.apply_existing_transforms"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Apply all constraints"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.sourceRig,
        )

        # The original script
        SourceRigName = context.scene.sourceRig

        # -------------------------------------------------
        source = bpy.data.objects[SourceRigName]

        userMode = bpy.context.object.mode      #store current mode
        bpy.ops.object.mode_set(mode='POSE')    #set mode to pose mode. Neccesary because we can only use apply operator in pose mode

        for bone in source.pose.bones:
            # set active bone to current bone in loop, to use apply operator on it
            bpy.context.object.data.bones.active = bone.bone

            _constraints = bone.constraints
            for const in _constraints:
                bpy.ops.constraint.apply(constraint=const.name, owner='BONE')


        #set the mode back to what the user had before
        bpy.ops.object.mode_set(mode=userMode)

        return {'FINISHED'}


# transfershape keys tool
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








CLASSES = [
AutoCopyTransformsPanel,
AutoTransformsConstraintsOperator,
ApplyExistingConstraintsOperator,
TransferShapeKeysPanel,
TransferShapeKeysOperator,
]

def register():
    for (prop_name, prop_value) in PROPS:
        setattr(bpy.types.Scene, prop_name, prop_value)

    for klass in CLASSES:
        bpy.utils.register_class(klass)

def unregister():
    for (prop_name, prop_value) in PROPS:
        delattr(bpy.types.Scene, prop_name)

    for klass in CLASSES:
        bpy.utils.unregister_class(klass)

if __name__ == '__main__':
    register()
