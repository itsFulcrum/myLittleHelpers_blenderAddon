import bpy

prefix = "pre_"
suffix = "_suff"

#Set this true if you want to change the current name
changeName = True
newName = "defaultCube"

# Set this true if you want to add versioning at the end like this _0._1
# Keep in mind that blender will automatically add versioning if 2 objects have the same name
addVersioning = False
startVersion = 0

selection_list = bpy.context.selected_objects

for obj in selection_list:

    if changeName:
        if addVersioning:
            obj.name = prefix + newName + suffix + "_" + str(startVersion)
        else:
            obj.name = prefix + newName + suffix
    else:
        currentName = obj.name

        if addVersioning:
            obj.name=prefix + currentName + suffix + "_" + str(sartVersion)
        else:
            obj.name = prefix + currentName + suffix

    startVersion = startVersion+1
