file = 'gen_files/c4mim.gen'

with open(file,'r') as f:
	natoms = int(f.readline())
	gen = f.readlines()

print(natoms)
print('')
for line in gen[:natoms]:
	line = line.split()
	atom = line[1][0]
	x = line[2]
	y = line[3]
	z = line[4]
	print(atom,x,y,z)


