import os
import shutil
to_dir = 'C:/Users/HARJI/OneDrive/Documents'
from_dir = 'C:/Users/HARJI/OneDrive'
allfiles = os.listdir(from_dir)
for f in allfiles:
	src_path = os.path.join(from_dir, f)
	dst_path = os.path.join(to_dir, f)
	shutil.move(src_path, dst_path)

import os
source = 'C:/Users/HARJI/OneDrive/Documents'
destination = '/Users/HARJI/OneDrive'
allfiles = os.listdir(source)
for f in allfiles:
	src_path = os.path.join(source, f)
	dst_path = os.path.join(destination, f)
	os.rename(src_path, dst_path)











