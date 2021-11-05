from ..utils import IKFastInfo
from ..ikfast import * # For legacy purposes

UR5_URDF = "models/ur5_description/urdf/ur5_robotiq_85.urdf"

UR5_INFO = IKFastInfo(module_name='ur5.ikfast_ur5', base_link='base_link',
                        ee_link='ee_link', free_joints=[])
