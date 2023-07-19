import bpy

# == PROPERTIES:
Properties = [
# Create LightmapUVs tool

('atr_name', bpy.props.StringProperty(name='New Attribute Name', default='Color')),
('atr_deleteExisting', bpy.props.BoolProperty(name='Delete Existing', default=True)),
('atr_color', bpy.props.FloatVectorProperty(name='Color', subtype='COLOR', default=(0,0,0), min=0.0, max=1.0, description="color picker")),

]


# == PANEL
class AttributeToolsPanel(bpy.types.Panel):

    bl_idname = 'AttributeToolsPanel'
    bl_label = 'Attribute Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'myLittleHelpers'


    def draw(self, context):
        col = self.layout.column()

        # rename uv layers
        col.prop(context.scene,'atr_name')
        col.prop(context.scene,'atr_color')
        col.prop(context.scene,'atr_deleteExisting')
        col.operator('opr.add_color_attribute', text='Add Color Attribute')


# == Operators
class AddColorAttributeOperator(bpy.types.Operator):
    """Adds a new Color Attribute to all selected objects"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "opr.add_color_attribute"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Add Color Attribute"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):
        params = (
            context.scene.atr_name,
            context.scene.atr_deleteExisting,
            context.scene.atr_color,
        )
        # Creates a new color attribute for all selected objects with specified parameters
        # for each selected object

        selection_list = bpy.context.selected_objects



        attributeName = context.scene.atr_name
        deleteExistingColorAttributes = context.scene.atr_deleteExisting
        specifiedColor = context.scene.atr_color


        newColor = (specifiedColor.r,specifiedColor.g,specifiedColor.b,1)


        bpy.ops.object.select_all(action='DESELECT')

        for obj in selection_list:

            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj

            # delete existing color attributes
            if(deleteExistingColorAttributes):
                if(obj.data.color_attributes): # does it have any color attributes
                    all_Color_Attributes = obj.data.color_attributes
                    for r in range(len(obj.data.color_attributes)-1, -1, -1):
                        all_Color_Attributes.remove(all_Color_Attributes[r])
                    #End
                #End
            #End


            bpy.ops.geometry.color_attribute_add(
            name=attributeName,
            domain='POINT',
            data_type='FLOAT_COLOR',
            color=newColor
            )

            obj.select_set(False)
        # For loop End

        # Restore selection
        for obj in selection_list:
            obj.select_set(True)



        return {'FINISHED'}




Classes = [
AttributeToolsPanel,
AddColorAttributeOperator,
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
