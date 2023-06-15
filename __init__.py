bl_info = {
    # required
    'name': 'myLittleHelpers',
    'blender': (3, 0, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 3),
    'author': 'Fulcrum',
    'description': 'useful workflow automisation operations',
}



from . import panel_Init

from .helpers import copyBoneTransforms
from .helpers import transferShapeKeys
from .helpers import renameSelection
from .helpers import uvTools
from .helpers import renameCCRigBones

import bpy




modules = [panel_Init,copyBoneTransforms,transferShapeKeys,renameSelection,uvTools,renameCCRigBones]

# register scripts

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
