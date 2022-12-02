import bpy
#This Script Renames the armature Bones for CC3 Exported GameBase Characters to work in motion Builder.


# -> Make sure your Characters Armature has the same name as the specified in this first line below
# -> Select your armature and run the script

bones_list = bpy.data.armatures['Armature'].bones

for item in bones_list:


    item.name=item.name.replace("pelvis","Hips")

    # Left Leg
    item.name = item.name.replace("thigh_l","LeftUpLeg")
    item.name = item.name.replace("thigh_twist_01_l","LeftUpLeg_Twist")
    item.name = item.name.replace("calf_l","LeftLeg")
    item.name = item.name.replace("calf_twist_01_l","LeftLeg_Twist")
    item.name = item.name.replace("foot_l","LeftFoot")
    item.name = item.name.replace("ball_l","LeftBall")
    # Right Leg
    item.name = item.name.replace("thigh_r","RightUpLeg")
    item.name = item.name.replace("thigh_twist_01_r","RightUpLeg_Twist")
    item.name = item.name.replace("calf_r","RightLeg")
    item.name = item.name.replace("calf_twist_01_r","RightLeg_Twist")
    item.name = item.name.replace("foot_r","RightFoot")
    item.name = item.name.replace("ball_r","RightBall")
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
