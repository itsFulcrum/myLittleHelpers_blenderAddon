import bpy

# == PROPERTIES:
Properties = [
    # rename Character creator rig tool
    ('rcc_ArmatureName', bpy.props.StringProperty(name='Armature Name', default='Armature')),

]


# == PANEL
class RenameCCRigPanel(bpy.types.Panel):

    bl_idname = 'RenameCCRigPanel'
    bl_label = 'Rename CC3 Rig'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        col.prop(context.scene, 'rcc_ArmatureName')
        col.operator('opr.rename_cc_gamebaserig_bones', text='Rename GameBase')
        col.operator('opr.rename_cc_base_rig_bones', text='Rename Base')
# == Operators
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
        bones_list = bpy.data.armatures[armatureName].bones

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

class RenameCCBaseRigOperator(bpy.types.Operator):
    """Rename CC Rig bones """      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rename_cc_base_rig_bones"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rename CC3 Base Rig bones"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.rcc_ArmatureName,
        )
        #This Script Renames the armature Bones for CC3 Exported GameBase Characters for our workflow
        # -> Make sure your Characters Armature has the same name as the specified in this first line below
        # -> Select your armature and run the script
        armatureName = context.scene.rcc_ArmatureName
        bones_list = bpy.data.armatures[armatureName].bones

        for item in bones_list:

            item.name=item.name.replace("CC_Base_BoneRoot","root")

            item.name=item.name.replace("CC_Base_Hip","Hips")
            item.name=item.name.replace("CC_Base_Pelvis","Pelvis")

            # Left Leg
            item.name = item.name.replace("CC_Base_L_Thigh","LeftUpLeg")
            item.name = item.name.replace("CC_Base_L_ThighTwist01","LeftUpLeg_Twist")
            item.name = item.name.replace("CC_Base_L_Calf","LeftLeg")
            item.name = item.name.replace("CC_Base_L_CalfTwist01","LeftLeg_Twist")
            item.name = item.name.replace("CC_Base_L_Foot","LeftFoot")
            item.name = item.name.replace("CC_Base_L_ToeBase","LeftToeBase")  # old one was LeftBall
            # Right Leg
            item.name = item.name.replace("CC_Base_R_Thigh","RightUpLeg")
            item.name = item.name.replace("CC_Base_R_ThighTwist01","RightUpLeg_Twist")
            item.name = item.name.replace("CC_Base_R_Calf","RightLeg")
            item.name = item.name.replace("CC_Base_R_CalfTwist01","RightLeg_Twist")
            item.name = item.name.replace("CC_Base_R_Foot","RightFoot")
            item.name = item.name.replace("CC_Base_R_ToeBase","RightToeBase") # old one was RightBall
            # Spine
            item.name = item.name.replace("CC_Base_Waist","Spine1")
            item.name = item.name.replace("CC_Base_Spine01","Spine2")
            item.name = item.name.replace("CC_Base_Spine02","Spine3")
            item.name=item.name.replace("CC_Base_R_RibsTwist","Right_RibsTwist")
            item.name=item.name.replace("CC_Base_L_RibsTwist","Left_RibsTwist")
            # Head
            item.name = item.name.replace("CC_Base_NeckTwist01","Neck")
            item.name = item.name.replace("CC_Base_NeckTwist02","Neck_Twist")
            item.name = item.name.replace("CC_Base_Headr","Head")

            # Left Arm
            item.name=item.name.replace("CC_Base_L_Clavicle","LeftShoulder")
            item.name=item.name.replace("CC_Base_L_Upperarm","LeftArm")
            item.name=item.name.replace("CC_Base_L_UpperarmTwist01","LeftArm_Twist")
            item.name=item.name.replace("CC_Base_L_Forearm","LeftForeArm")
            item.name=item.name.replace("CC_Base_L_ForearmTwist01","LeftForeArm_Twist")
            item.name=item.name.replace("CC_Base_L_Hand","LeftHand")
            # Right Arm
            item.name=item.name.replace("CC_Base_R_Clavicle","RightShoulder")
            item.name=item.name.replace("CC_Base_R_Upperarm","RightArm")
            item.name=item.name.replace("CC_Base_R_UpperarmTwist01","RightArm_Twist")
            item.name=item.name.replace("CC_Base_R_Forearm","RightForeArm")
            item.name=item.name.replace("CC_Base_R_ForearmTwist01","RightForeArm_Twist")
            item.name=item.name.replace("CC_Base_R_Hand","RightHand")



        return {'FINISHED'}



Classes = [
RenameCCRigPanel,
RenameCCGameBaseRigOperator,
RenameCCBaseRigOperator,
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
