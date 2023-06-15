import bpy
#This Script Renames the armature Bones for CC3 Exported GameBase Characters to work in motion Builder.

# ----- >>> IMPORTANT
#Enter Custom Rig Name with Armature
bones_list = bpy.data.armatures['Armature_Name'].bones #armature name

for item in bones_list:
    item.name=item.name.replace("CC_Base_Pelvis","Hips")

    item.name=item.name.replace("CC_Base_L_Thigh","LeftUpLeg")
    item.name=item.name.replace("CC_Base_L_ThighTwist01","LeftUpLeg_Twist")
    item.name=item.name.replace("CC_Base_L_Calf","LeftLeg")
    item.name=item.name.replace("CC_Base_L_CalfTwist01","LeftLeg_Twist")
    item.name=item.name.replace("CC_Base_L_Foot","LeftFoot")
    item.name=item.name.replace("CC_Base_L_ToeBase","LeftToeBase")

    item.name=item.name.replace("CC_Base_R_Thigh","RightUpLeg")
    item.name=item.name.replace("CC_Base_R_ThighTwist01","RightUpLeg_Twist")
    item.name=item.name.replace("CC_Base_R_Calf","RightLeg")
    item.name=item.name.replace("CC_Base_R_CalfTwist01","RightLeg_Twist")
    item.name=item.name.replace("CC_Base_R_Foot","RightFoot")
    item.name=item.name.replace("CC_Base_R_ToeBase","RightToeBase")

    item.name=item.name.replace("CC_Base_L_Clavicle","LeftShoulder")
    item.name=item.name.replace("CC_Base_L_Upperarm","LeftArm")
    item.name=item.name.replace("CC_Base_L_UpperarmTwist01","LeftArm_Twist")
    item.name=item.name.replace("CC_Base_L_Forearm","LeftForeArm")
    item.name=item.name.replace("CC_Base_L_ForearmTwist01","LeftForeArm_Twist")
    item.name=item.name.replace("CC_Base_L_Hand","LeftHand")

    item.name=item.name.replace("CC_Base_R_Clavicle","RightShoulder")
    item.name=item.name.replace("CC_Base_R_Upperarm","RightArm")
    item.name=item.name.replace("CC_Base_R_UpperarmTwist01","RightArm_Twist")
    item.name=item.name.replace("CC_Base_R_Forearm","RightForeArm")
    item.name=item.name.replace("CC_Base_R_ForearmTwist01","RightForeArm_Twist")
    item.name=item.name.replace("CC_Base_R_Hand","RightHand")
