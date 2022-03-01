files = ['gen_files/c4mim.gen', 'gen_files/beti.gen', 'gen_files/n1114.gen', 'gen_files/tf2n.gen']

for file in files:
	xyz_file = file.replace('gen','xyz')
	
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


