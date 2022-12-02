
import bpy
# This Script will add a copy location and copy rotation constraint for each bone of the SourceRig and have it refrence location and rotation from the target rig.
# For this to work properly it is essentatil that the rigs are identical especially the names have to be the exact same.
# It is intended to be used if you have two identical rigs and want to copy a pose from one to the other or just reference the animation.

SourceRigName = 'Armature'
TargetRigName = 'Armature.001'

removeAllConstraintsFirst = True # removes all constraints first before adding new ones
applyAllConstraintsAfter = True # applys all constraints

addCopyLocationConstraint = False
addCopyRotationConstraint = True
addCopyScaleConstraint = False


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
