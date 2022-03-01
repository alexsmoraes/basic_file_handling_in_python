file = 'gen_files/c4mim.gen'

with open(file,'r') as f:
	natoms = int(f.readline())
	gen = f.readlines()

print(natoms)
print('')
for line in gen[:natoms]:
	line = line.split()
	atom = line[1][0]
	x = float(line[2])
	y = float(line[3])
	z = float(line[4])
	print('{:2s}\t{:20.16f}\t{:20.16f}\t{:20.16f}'.format(atom,x,y,z))


