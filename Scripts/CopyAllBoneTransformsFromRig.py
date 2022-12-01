import bpy
# This Script will add a copy location and copy rotation constraint for each bone of the SourceRig and have it refrence location and rotation from the target rig.
# For this to work properly it is essentatil that the rigs are identical especially the names have to be the exact same.
# It is intended to be used if you have two identical rigs and want to copy a pose from one to the other or just reference the animation.

# If you want to apply all of the constraints. well.
# As of now blender doesn't offer a way to apply all bone constraints on all bones of a rig either through code nor is there a way to apply them through a build in command / shortcut.
# At least to my knowlage

# The only workaround I know of is to export your rig as a fbx and import it back. The export will apply all constraints automatically. then you can keyframe it.


SourceRigName = 'Armature'
TargetRigName = 'Armature.001'
# Set "removeAllConstraintsFirst" True if you want all existing Constraints to be removed (Not applyed, Remove) first, before adding new one. Good if you changed something and just want to update it.
removeAllConstraintsFirst = False

addCopyLocationConstraint = True
addCopyRotationConstraint = True
addCopyScaleConstraint = False

source = bpy.data.objects[SourceRigName]
target = bpy.data.objects[TargetRigName]


for bone in source.pose.bones:

    if removeAllConstraintsFirst:
        currentConstraints = bone.constraints
        for constraint in currentConstraints:
            bone.constraints.remove(constraint)


    if addCopyLocationConstraint:
        bone.constraints.new('COPY_ROTATION')
        CopyLocationConstraint = bone.constraints[-1]
        CopyLocationConstraint.target = target
        CopyLocationConstraint.subtarget = bone.name

    if addCopyRotationConstraint:
        bone.constraints.new('COPY_LOCATION')
        CopyRotationConstraint = bone.constraints[-1]
        CopyRotationConstraint.target = target
        CopyRotationConstraint.subtarget = bone.name

    if addCopyScaleConstraint:
        bone.constraints.new('COPY_SCALE')
        CopyScaleConstraint = bone.constraints[-1]
        CopyScaleConstraint.target = target
        CopyScaleConstraint.subtarget = bone.name
