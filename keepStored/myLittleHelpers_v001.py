bl_info = {
    # required
    'name': 'myLittleHelpers',
    'blender': (3, 0, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 2),
    'author': 'Janis Civan',
    'description': 'useful workflow functions',
}

import bpy

# == PROPERTIES:
PROPS = [
    ('sourceRig', bpy.props.StringProperty(name='CopyToRig', default='Armature')),
    ('targetRig', bpy.props.StringProperty(name='CopyFromRig', default='Armature.001')),
    ('removeConstraints', bpy.props.BoolProperty(name='Remove all constraints first', default=True)),
    ('applyConstraints', bpy.props.BoolProperty(name='Apply Constraints', default=True)),
    ('addLocationConstraint', bpy.props.BoolProperty(name='Location Constraint', default=True)),
    ('addRotationConstraint', bpy.props.BoolProperty(name='Rotation Constraint', default=True)),
    ('addScaleConstraint', bpy.props.BoolProperty(name='Scale Constraint', default=False)),

    # transfer shape key tool
    ('copyFrom', bpy.props.StringProperty(name='CopyFromMesh', default='CopyFrom')),
    ('copyTo', bpy.props.StringProperty(name='CopyToMesh', default='CopyTo')),

    # rename Selection tool
    ('rs_prefix', bpy.props.StringProperty(name='prefix', default='pre_')),
    ('rs_suffix', bpy.props.StringProperty(name='suffix', default='_suff')),
    ('rs_addPrefix', bpy.props.BoolProperty(name='Add Prefix', default=False)),
    ('rs_addSuffix', bpy.props.BoolProperty(name='Add Suffix', default=False)),
    ('rs_changeName', bpy.props.BoolProperty(name='Change Name', default=False)),
    ('rs_newName', bpy.props.StringProperty(name='New Name', default='DefaultCube')),
    ('rs_addVersioning', bpy.props.BoolProperty(name='Custom Versioning', default=False)),
    ('rs_startVersion', bpy.props.IntProperty(name='Start Version', default=0)),

    # rename Character creator rig tool
    ('rcc_ArmatureName', bpy.props.StringProperty(name='Armature Name', default='Armature')),

    # Create LightmapUVs tool
    ('cl_uvName', bpy.props.StringProperty(name='Layer Name', default='UV_Lightmap')),
]


# == PANELS
# copy transforms tool
class AutoCopyTransformsPanel(bpy.types.Panel):

    bl_idname = 'VIEW3D_PT_RS_panel'
    bl_label = 'Auto Copy Transforms'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


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

# Transfer shape keys tool
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

# Rename Selection tool
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
# Rename CC3 Rig tool
class RenameCCRigPanel(bpy.types.Panel):

    bl_idname = 'RenameCCRigPanel'
    bl_label = 'Rename CC3 Rig'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'rcc_ArmatureName')
        col.operator('opr.rename_cc_gamebaserig_bones', text='Rename')
# Create Lightmap uvs tool
class LightmapUVsPanel(bpy.types.Panel):

    bl_idname = 'LightmapUVsPanel'
    bl_label = 'Lightmap UVs'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'cl_uvName')
        col.operator('opr.create_lightmaps_for_selection', text='Create lightmap_pack')

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

# rename selection tool
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

# rename character creator game base rig
class RenameCCGameBaseRigOperator(bpy.types.Operator):
    """Rename CC Rig bones """      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rename_cc_gamebaserig_bones"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rename CC3 GameBaseRig bones"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.rcc_ArmatureName,
        )
        #This Script Renames the armature Bones for CC3 Exported GameBase Characters for our workflow
        # -> Make sure your Characters Armature has the same name as the specified in this first line below
        # -> Select your armature and run the script
        armatureName = context.scene.rcc_ArmatureName
        bones_list = bpy.data.armatures['armatureName'].bones

        for item in bones_list:
            item.name=item.name.replace("pelvis","Hips")

            # Left Leg
            item.name = item.name.replace("thigh_l","LeftUpLeg")
            item.name = item.name.replace("thigh_twist_01_l","LeftUpLeg_Twist")
            item.name = item.name.replace("calf_l","LeftLeg")
            item.name = item.name.replace("calf_twist_01_l","LeftLeg_Twist")
            item.name = item.name.replace("foot_l","LeftFoot")
            item.name = item.name.replace("ball_l","LeftToeBase")  # old one was LeftBall
            # Right Leg
            item.name = item.name.replace("thigh_r","RightUpLeg")
            item.name = item.name.replace("thigh_twist_01_r","RightUpLeg_Twist")
            item.name = item.name.replace("calf_r","RightLeg")
            item.name = item.name.replace("calf_twist_01_r","RightLeg_Twist")
            item.name = item.name.replace("foot_r","RightFoot")
            item.name = item.name.replace("ball_r","RightToeBase") # old one was RightBall
            # Spine
            item.name = item.name.replace("spine_01","Spine1")
            item.name = item.name.replace("spine_02","Spine2")
            item.name = item.name.replace("spine_03","Spine3")
            item.name = item.name.replace("neck_01","Neck")
            item.name = item.name.replace("head","Head")

            # Left Arm
            item.name=item.name.replace("clavicle_l","LeftShoulder")
            item.name=item.name.replace("upperarm_l","LeftArm")
            item.name=item.name.replace("upperarm_twist_01_l","LeftArm_Twist")
            item.name=item.name.replace("lowerarm_l","LeftForeArm")
            item.name=item.name.replace("lowerarm_twist_01_l","LeftForeArm_Twist")
            item.name=item.name.replace("hand_l","LeftHand")
            # Right Arm
            item.name=item.name.replace("clavicle_r","RightShoulder")
            item.name=item.name.replace("upperarm_r","RightArm")
            item.name=item.name.replace("upperarm_twist_01_r","RightArm_Twist")
            item.name=item.name.replace("lowerarm_r","RightForeArm")
            item.name=item.name.replace("lowerarm_twist_01_r","RightForeArm_Twist")
            item.name=item.name.replace("hand_r","RightHand")

            item.name=item.name.replace("CC_Base_R_RibsTwist","Right_RibsTwist")
            item.name=item.name.replace("CC_Base_L_RibsTwist","Left_RibsTwist")


        return {'FINISHED'}

# Lightmap UVs tool
class CreateLightmapUVsOperator(bpy.types.Operator):
    """Create LightmapUVs for all selected objects"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.create_lightmaps_for_selection"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Create Lightmaps"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.cl_uvName,
        )
        # creates lightmapUVs using build in lightmap pack unwrap option
        # for each selected object

        selection_list = bpy.context.selected_objects

        UVName = context.scene.cl_uvName

        bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:

            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.uv_texture_add()
            obj.data.uv_layers.active.name = UVName
            bpy.ops.uv.lightmap_pack()
            obj.select_set(False)

        return {'FINISHED'}





CLASSES = [
AutoCopyTransformsPanel,
AutoTransformsConstraintsOperator,
ApplyExistingConstraintsOperator,

TransferShapeKeysPanel,
TransferShapeKeysOperator,

RenameSelectionPanel,
RenameSelectionOperator,

RenameCCRigPanel,
RenameCCGameBaseRigOperator,

LightmapUVsPanel,
CreateLightmapUVsOperator,
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
