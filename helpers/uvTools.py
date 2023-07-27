import bpy

# == PROPERTIES:
Properties = [
# Create LightmapUVs tool

('uvt_uvName', bpy.props.StringProperty(name='New UV Name', default='UV_Main')),
('uvt_uvIndex', bpy.props.IntProperty(name='Layer Index', default=0)),
('uvt_uvPackMargin', bpy.props.FloatProperty(name='Pack Margin', default=0.004)),

]


# == PANEL
class UVToolsPanel(bpy.types.Panel):

    bl_idname = 'UVToolsPanel'
    bl_label = 'UV Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()
        # lightmap pack

        # rename uv layers
        col.prop(context.scene,'uvt_uvName')
        col.operator('opr.create_lightmaps_for_selection', text='Create lightmap_pack')
        col.prop(context.scene,'uvt_uvPackMargin')
        col.operator('opr.make_lightmap_from_active_uv_for_selection', text='Lightmap from active')
        col.prop(context.scene,'uvt_uvIndex')
        col.operator('opr.rename_uv_layers_for_selected', text='Rename UV Layer')
        col.operator('opr.make_uv_layer_active', text='Set Active UV Layer')
        col.operator('opr.make_uv_layer_active_render', text='Set Active Render UV Layer')



# == Operators
class CreateLightmapUVsOperator(bpy.types.Operator):
    """Create and add LightmapUV layer using blenders Lightmap_pack unwrap method, for all selected objects"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.create_lightmaps_for_selection"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Create Lightmaps"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.uvt_uvName,
        )
        # creates lightmapUVs using build in lightmap pack unwrap option
        # for each selected object

        selection_list = bpy.context.selected_objects

        UVName = context.scene.uvt_uvName

        bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:

            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.uv_texture_add()
            obj.data.uv_layers.active.name = UVName
            bpy.ops.uv.lightmap_pack()
            obj.select_set(False)

        return {'FINISHED'}

# == Operators
class MakeLightmapFromActiveOperator(bpy.types.Operator):
    """creates Lightmap from active uv layer by dublicating active layer, then average scale islands, and pack operator"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.make_lightmap_from_active_uv_for_selection"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Create Lightmap From Active"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.uvt_uvName,
            context.scene.uvt_uvPackMargin,
        )
        # creates Lightmap from active uv layer by dublicating active layer, then average scale islands, and pack operator
        # for each selected object



        selection_list = bpy.context.selected_objects

        UVName = context.scene.uvt_uvName
        packMargin =context.scene.uvt_uvPackMargin

        bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:

            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            bpy.ops.mesh.uv_texture_add()
            obj.data.uv_layers.active.name = UVName

            # go to edit mode
            bpy.ops.object.mode_set(mode='EDIT')
            # change context area to image editor
            last_area = bpy.context.area.type
            bpy.context.area.type = 'IMAGE_EDITOR'
            bpy.context.area.ui_type = 'UV'

            # select all uv islands
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.uv.average_islands_scale()
            bpy.ops.uv.pack_islands(margin=packMargin)


            # restor previous context area
            bpy.context.area.type = last_area
            # return to object mode
            bpy.ops.object.mode_set(mode='OBJECT')
            obj.select_set(False)


        # Restore selection
        for obj in selection_list:
            obj.select_set(True)

        return {'FINISHED'}



class RenameUVLayers(bpy.types.Operator):
    """Renames specified UV layer (if existing) for all selected object at once"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.rename_uv_layers_for_selected"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Rename UV Layer"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.uvt_uvName,
            context.scene.uvt_uvIndex,

        )
        # Renames uv layer specified by index for each selected object

        selection_list = bpy.context.selected_objects

        UVName = context.scene.uvt_uvName
        uvIndex = context.scene.uvt_uvIndex

        #bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:
            if len(obj.data.uv_layers) > uvIndex:
                obj.data.uv_layers[uvIndex].name = UVName

        return {'FINISHED'}


class MakeActiveRenderUVLayer(bpy.types.Operator):
    """Makes specified UV layer index the active uv layer for rendering"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.make_uv_layer_active_render"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Make UV Layer Active Render"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.uvt_uvIndex,

        )
        # Makes specified UV layer index the active uv layer for rendering

        selection_list = bpy.context.selected_objects

        uvIndex = context.scene.uvt_uvIndex

        #bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:
            if len(obj.data.uv_layers) > uvIndex:
                obj.data.uv_layers[uvIndex].active_render = True

        return {'FINISHED'}

class MakeActiveUVLayer(bpy.types.Operator):
    """Makes specified UV layer index the active uv layer for rendering"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.make_uv_layer_active"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Make UV Layer Active"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.uvt_uvIndex,

        )
        # Makes specified UV layer index the active uv layer

        selection_list = bpy.context.selected_objects

        uvIndex = context.scene.uvt_uvIndex

        #bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:
            if len(obj.data.uv_layers) > uvIndex:
                obj.data.uv_layers[uvIndex].active = True

        return {'FINISHED'}





Classes = [
UVToolsPanel,
CreateLightmapUVsOperator,
MakeLightmapFromActiveOperator,
RenameUVLayers,
MakeActiveUVLayer,
MakeActiveRenderUVLayer,
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
