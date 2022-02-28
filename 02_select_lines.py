file = 'gen_files/c4mim.gen'

with open(file,'r') as f:
	natoms = int(f.readline())
	gen = f.readlines()

for line in gen[:natoms]:
	print(line)
