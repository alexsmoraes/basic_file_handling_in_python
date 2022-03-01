from pathlib import Path
import os
from shutil import copy2, rmtree

files = list(Path().rglob('*.xyz'))

for file in files:
	dir = Path('xyz_files')
	if not dir.exists():
		os.mkdir(dir)
	aux = os.path.basename(file)
	old_dir = str(file.parent)

	new_file = dir / aux

	copy2(file, new_file)
	rmtree(old_dir)