import bpy

source = bpy.data.objects['Armature']
target = bpy.data.objects['Armature.001']

for bone in source.pose.bones:
    bone.constraints.new('COPY_LOCATION')
    CopyLocationConstraint = bone.constraints[-1]
    CopyLocationConstraint.target = target
    CopyLocationConstraint.subtarget = bone.name
    CopyLocationConstraint.apply
