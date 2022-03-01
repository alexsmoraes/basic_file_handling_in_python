from pathlib import Path
import os

files = list(Path('gen_files').glob('*.gen'))

for file in files:
	xyz_file = os.path.basename(str(file)).replace('gen','xyz')
	dir = Path(xyz_file.replace('.xyz',''))
	
	if not dir.exists():
		os.mkdir(dir)		

	xyz_file = dir / xyz_file

	with open(file,'r') as f:
		natoms = int(f.readline())
		gen = f.readlines()

	with open(xyz_file,'w') as f:
		f.write('{}\n\n'.format(natoms))
		for line in gen[:natoms]:
			line = line.split()
			atom = line[1][0]
			x = float(line[2])
			y = float(line[3])
			z = float(line[4])
			f.write('{:2s}\t{:24.16f}\t{:24.16f}\t{:24.16f}\n'.format(atom,x,y,z))


