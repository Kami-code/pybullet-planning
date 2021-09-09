from ..utils import IKFastInfo
from ..ikfast import * # For legacy purposes

# TODO: deprecate this file
#FRANKA_URDF = "models/franka_description/robots/panda_arm.urdf"
#FRANKA_URDF = "models/franka_description/robots/hand.urdf"
UR5_URDF = "models/ur5_description/urdf/ur5_robotiq_85.urdf"

UR5_INFO = IKFastInfo(module_name='ur5.ikfast_ur5_arm', base_link='base_link',
                        ee_link='ee_link', free_joints=['ee_fixed_joint'])
