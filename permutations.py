def permute(config, perm): #config = [], perm = [] (arrays)
	k = len(perm)
	new_config = config.copy()
	for i in range(1, k): #range is exclusive
		new_config[perm[i]-1] = config[perm[i-1]-1]
	new_config[perm[0]-1] = config[perm[-1]-1]

	return new_config
	
if __name__ == '__main__':
	die = [1, 2, 3, 5, 4, 6]
	
	right = [1, 2, 6, 4]
	up = [1, 3, 6, 5]
	left = [1, 4, 6, 2]
	down = [1, 5, 6, 3]
	
	print(die, '\n')
	print(permute(die, right))
	print(permute(die, up))
	print(permute(die, left))
	print(permute(die, down))
	
	print(permute([6, 5, 3, 2, 4, 1], left))
	
		
	