bl_info = {
    # required
    'name': 'myLittleHelpers',
    'blender': (3, 0, 0),
    'category': 'Object',
    # optional
    'version': (1, 0, 6),
    'author': 'Fulcrum',
    'description': 'useful workflow operations',
}



from . import panel_Init

from .helpers import copyBoneTransforms
from .helpers import transferShapeKeys
from .helpers import renameSelection
from .helpers import uvTools
from .helpers import attributeTools
from .helpers import renameCCRigBones

from .helpers import uvTransformTools
from .helpers import uvReorder

import bpy




modules = [panel_Init,copyBoneTransforms,transferShapeKeys,renameSelection,uvTools,attributeTools,renameCCRigBones,uvTransformTools,uvReorder]

# register scripts

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
