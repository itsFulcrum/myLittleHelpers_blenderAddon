import bpy

# Copy objects name
copyFromName = 'CopyFrom'
copyToName = 'CopyTo'


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
