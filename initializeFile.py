import sys
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

param1 = sys.argv[1]


def getCamersList():
    cmds.file(param1, o=True)
    cameras_list = cmds.listCameras()
    return cameras_list


def getRenderableCamera():
    cameras_list = getCamersList()
    for camera in cameras_list:
        if cmds.getAttr(camera + '.renderable'):
            return camera


print('*' + str(getCamersList()) + '*')
print('*' + getRenderableCamera() + '*')
