import bpy

#on the source rig it will add a copy location and copy rotation constraint for each bone which will reference that bone from the target rig.
# for this to work it is essentatil that the rigs are identical especially the names have to be the exact same.
# to apply the constraints as of now there is no other way then to export the rig as fbx and import it back or do it manually for each bone.
SourceRigName = 'Armature'
TargetRigName = 'Armature.001'



source = bpy.data.objects[SourceRigName]
target = bpy.data.objects[TargetRigName]

for bone in source.pose.bones:
    bone.constraints.new('COPY_ROTATION')
    CopyLocationConstraint = bone.constraints[-1]
    CopyLocationConstraint.target = target
    CopyLocationConstraint.subtarget = bone.name
    bone.constraints.new('COPY_LOCATION')
    CopyRotationConstraint = bone.constraints[-1]
    CopyRotationConstraint.target = target
    CopyRotationConstraint.subtarget = bone.name
