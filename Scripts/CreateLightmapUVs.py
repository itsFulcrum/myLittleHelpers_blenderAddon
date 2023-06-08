import bpy


# creates lightmapUVs using build in lightmap pack unwrap option
# for each selected object

selection_list = bpy.context.selected_objects

UVName = 'UV_Lightmap'

bpy.ops.object.select_all(action='DESELECT')

for obj in selection_list:
    
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    bpy.ops.mesh.uv_texture_add()
    obj.data.uv_layers.active.name = UVName
    bpy.ops.uv.lightmap_pack()
    obj.select_set(False)