
This Repository is an addon for blender that contains a collection of useful blender scripts I wrote to speedup my workflow.
There is no overarching theme in this addon it really is just a bunch of random scripts i use day to day.


== INSTALL ==
compatible with blender 3.0 and upwards. highest version tested is 3.6.1
Download Repository as zip and install like any other blender addon.

If you are just interested in just one function once. all script are modular meaning that you can just copy the specifc scripts contents
into blenders text editor, run it and the panel for this specific script will appear in the side panel. without you having to download and install the whole addon.

==== DOCUMENTATION ====

== Copy Bone Tranforms ==
This script is meant to be used when you have two identical rigs and want to copy the current pose of one to the other.
you may use this also for transfering existing animations to a different rig.
For this to work the rigs need to have the exact same bones and those bone need to have the same names.
size or position of the bones is not essential but will likely give better results depending on your usecase.

The script will go through all bones of your rig and create copy transform constraints for all of them and automatically assign the correct bones from the rig you want to sample the transforms from.

In first two field enter the names of your armatures that you want to copy the transforms from / to.
you can specify witch transforms constrains should be created (copy location, copy rotation, copy scale).
Apply constraints checkbox will apply your constrains directly without you pressing the apply constrains button, which you may do afterwards if you first want to inspect your result.
to get rid of all existing constrains of your rig. you can uncheck everything except "Remove all constraints first" and then press Copy transforms button. Now it will get rid of any existing constrains and not create new once.


== Transfer shape key ==
blender already offers a way of transfering shape keys between identical meshes. However as of yet it is not possible to transfer multiple shape key at once it has to be done one by one.
This Script will do just that and go through every shape key and transfer it over.
Specify your meshes by putting their names into the textboxes of Copy From and Copy to mesh and press the button.
This procces may take a bit of time if you have a lot of shape keys so don't get confused if blender frezes for a little while.

== Rename Selection ==
With blender 3.6 it is now finally possible to rename multiple objects at once but this script still allows you to add pre or suffixes to multiple objects at once.
Fore example you can add _lowpoly to all your selected object with one button click and it offers a cusom versioning that uses this convetion
someName_0,someName_1,someName_2 instead of blenders default someName.001,someName.002,someName.003
Note that if you disable custom versioning blender will automatically add its default versioning if to objects would otherwise have the same name.

the "Match Data Block" button will simply copy the current object name and past it as the name for its data block (thats the one with the green triangle in the properties panel).
Somehow blender uses different names there and usually nobody cares what name it has since its just blender internal but if you do want it extra tidy it there.

== UV Tools ==
this is a bunch of uv operations you can perform on multiple objects at once.
Set a name for newly created or renamed uv layers
Create lighmap pack will create a new uv layer and perform blenders build in lightmap_pack() uv unwrap methon on all your objects.
Lightmap from active will dublicate the currently active uv layer and will then perfrom the average_scale command to even the scale of all uv islands and that perform the build in pack algorithm usign the specified Pack margin.
Use the "Layer Index" value to specify which uv layer to rename, set as active or set as the current rendered.

== UV Transform Tools ==
these are only visible in the side panel of the Image Editor / UV editor view  and Not in the 3D view
There are just some buttons to rotate your selected islands by 45,90 or 180 degrees.  
I know it's a trivial thing but when you need to deal with a lot of uv islands that you need to manually rotate to make an optimal uv pack it can actually be a good time saver,
especially if you put these in your quick favorites menu.

== Attribute Tools ==
For now I only implemented vertex color.
You can specify a color and name and add a vertex color attribute to all your selected object.


== Rename CC3 Rig ==
you will most likely never use this but for the sake of completion I'll explain it.
if you export a character from character creator 3 using the game base version you can press this button and it will rename the bone names
You may not find this useful because it is simply the nameing convetion that we need at work for our worklflow to copy mocap data onto any character that we create using CC3.
If you are interest in something similar but need a different naming convention you may want to look at the code for this.
As all the others its in the helpers folder and all it does is litterally just look for a specific bone name that comes from character creator and replace it with the one we decided on for our workflow.
you can simply enter your own namings there for example one that works with mixamo rigs. you shouldn't have a hard time figuring out where to specify the new names.
Originally it was setup so that Maya's motion builder would automatically recognise the bones but now we use maya itself and don't need to use this specific one but we saw no reason to change and just kept it.
