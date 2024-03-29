
import bpy
from bpy.types import Operator

# == PROPERTIES:
Properties = [

]


def make_active(name):
    uvs = bpy.context.view_layer.objects.active.data.uv_layers
    for uv in uvs:
        if uv.name == name:
            uvs.active = uv
            return
    print("Could not find:", name, "\n(this should never happen)")


def move_to_bottom(index):
    uvs = bpy.context.view_layer.objects.active.data.uv_layers
    uvs.active_index = index
    new_name = uvs.active.name

    bpy.ops.mesh.uv_texture_add()

    # delete the "old" one
    make_active(new_name)
    bpy.ops.mesh.uv_texture_remove()

    # set the name of the last one
    uvs.active_index = len(uvs) - 1
    uvs.active.name = new_name



# == Operators
class Move_uv_down(Operator):
    bl_idname = "mesh.uv_down"
    bl_label = "Move Down"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        uvs = context.view_layer.objects.active.data.uv_layers

        # get the selected UV map
        orig_ind = uvs.active_index
        orig_name = uvs.active.name

        if orig_ind == len(uvs) - 1:
            return {'FINISHED'}

        # use "trick" on the one after it
        move_to_bottom(orig_ind + 1)

        # use the "trick" on the UV map
        move_to_bottom(orig_ind)

        # use the "trick" on the rest that are after where it was
        for i in range(orig_ind, len(uvs) - 2):
            move_to_bottom(orig_ind)

        make_active(orig_name)

        return {'FINISHED'}


class Move_uv_up(Operator):
    bl_idname = "mesh.uv_up"
    bl_label = "Move Up"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        uvs = bpy.context.view_layer.objects.active.data.uv_layers

        if uvs.active_index == 0:
            return {'FINISHED'}

        original = uvs.active.name
        uvs.active_index -= 1
        bpy.ops.mesh.uv_texture_down()
        make_active(original)

        return {'FINISHED'}


class Sort_uvs_a_to_z (Operator):
    bl_idname = 'mesh.uvs_a_to_z'
    bl_label = 'Sort A to Z'
    bl_description = "Sorting UVs by name (A to Z)"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        uvs = context.view_layer.objects.active.data.uv_layers
        orig_name = uvs.active.name

        for j in range (len(uvs)):
            for i in range (len(uvs)-1):
                uvs.active_index = i
                temp_name = uvs.active.name
                uvs.active_index = i+1
                if uvs.active.name < temp_name:
                    bpy.ops.mesh.uv_texture_up()

        make_active(orig_name)

        return {"FINISHED"}


class Sort_uvs_z_to_a (Operator):
    bl_idname = 'mesh.uvs_z_to_a'
    bl_label = 'Sort Z to A'
    bl_description = "Sorting UVs by name (Z to A)"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        uvs = context.view_layer.objects.active.data.uv_layers
        orig_name = uvs.active.name

        for j in range (len(uvs)):
            for i in range (len(uvs)-1):
                uvs.active_index = i+1
                temp_name = uvs.active.name
                uvs.active_index = i
                if uvs.active.name < temp_name:
                    bpy.ops.mesh.uv_texture_down()

        make_active(orig_name)

        return {"FINISHED"}


def uv_tools_addition(self, context):
    layout = self.layout
    layout.label(text="Active object UV Tools:")
    row = layout.row()

    col1 = row.column(align=True)
    col1.operator("mesh.uv_up", icon='TRIA_UP')
    col1.operator("mesh.uv_down", icon='TRIA_DOWN')

    layout.separator()

    col2 = row.column(align=True)
    col2.operator("mesh.uvs_a_to_z", icon='TRIA_UP_BAR')
    col2.operator("mesh.uvs_z_to_a", icon='TRIA_DOWN_BAR')


Classes = [
Move_uv_down,
Move_uv_up,
Sort_uvs_a_to_z,
Sort_uvs_z_to_a,
]

def register():
    for (prop_name, prop_value) in Properties:
        setattr(bpy.types.Scene, prop_name, prop_value)

    for cls in Classes:
        bpy.utils.register_class(cls)

    bpy.types.DATA_PT_uv_texture.append(uv_tools_addition)


def unregister():
    for (prop_name, prop_value) in Properties:
        delattr(bpy.types.Scene, prop_name)

    for cls in Classes:
        bpy.utils.unregister_class(cls)

    bpy.types.DATA_PT_uv_texture.remove(uv_tools_addition)


if __name__ == "__main__":
    register()
