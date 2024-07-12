

import apollo_file_py as a
from utils.robot_preprocessor_directories import RobotPreprocessorRobotsDirectory

p = a.PathBufPy.new_from_documents_dir().append('apollo-robots-dir/robots')
r = RobotPreprocessorRobotsDirectory(p)
s = r.get_robot_subdirectory('ur5')

urdf = s.to_urdf_module()
print(urdf)