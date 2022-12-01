import bpy
# This Script allows you to Change the names of all selected objects at onec or add pre/suffixes to them

#set your custom prefix and suffix here or disable them
addPrefix = True;
addSuffix = True;
prefix = "pre_"
suffix = "_suff"

#Set this true if you want to change the current name
changeName = True
newName = "defaultCube"

# Set "addVersioning" True if you want to add versioning at the end with this syntax -> "defaultCube_0" , "defaultCube_1" .. "defaultCube_42"
#Change "startVersion" if you don't want the versioning to start from 0
# Keep in mind that blender will automatically add versioning if 2 objects have the same name
addVersioning = False
startVersion = 0



selection_list = bpy.context.selected_objects
for obj in selection_list:
    _name = obj.name

    if changeName:
        _name = newName
    if addPrefix:
        _name = prefix + _name
    if addSuffix:
        _name = _name + suffix

    if addVersioning:
        _name = _name + "_" + str(startVersion)


    obj.name = _name

    startVersion = startVersion + 1
