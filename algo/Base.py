def voisinage(x, y):# permet de connaitre le nombre de voisins qu'à une cellule
	global old_grid# On appelle old_grid
	voisins = 0

	#On vérifie 1 à 1 les 8 cases 
	if [x-1,y-1] in old_grid: 
		voisins = voisins + 1
	if [x-1,y] in old_grid:
		voisins = voisins +1
	if [x-1,y+1] in old_grid:
		voisins = voisins +1
	if [x,y+1] in old_grid:
		voisins = voisins +1
	if [x,y-1] in old_grid:
		voisins = voisins +1
	if [x+1,y-1] in old_grid:
		voisins = voisins +1
	if [x+1,y+1] in old_grid:
		voisins = voisins +1
	if [x+1,y] in old_grid:
		voisins = voisins +1
	return voisins


def algorithme(): # Le coeur du programme
	global new_grid, old_grid

	old_grid = []
	a_supprimer = [] # On ne peut pas faire des actions de suppression comme ça : sinon
	for i in range(len(new_grid)): # On copie new_grid dans old_grid
		old_grid.append(new_grid[i])

	#old_grid.sort() 
	#new_grid.sort()

	for i in range(len(old_grid)-1, -1, -1):
		nbvoisins = voisinage(old_grid[i][0], old_grid[i][1])
		if nbvoisins > 3:
			del new_grid[i]
		if nbvoisins < 2:
			del new_grid[i]
		x = old_grid[i][0]
		y = old_grid[i][1]
		if nbvoisins >= 2 and nbvoisins <= 7 :
			if not [x-1,y-1] in new_grid:
				voisins = voisinage(x-1, y-1)
				if voisins == 3 :
					new_grid.append([x-1,y-1])

			if not [x,y-1] in new_grid:
				voisins = voisinage(x, y-1)
				if voisins == 3 :
					new_grid.append([x,y-1])

			if not [x+1,y-1] in new_grid:
				voisins = voisinage(x+1, y-1)
				if voisins == 3 :
					new_grid.append([x+1,y-1])

			if not [x-1,y] in new_grid:
				voisins = voisinage(x-1, y)
				if voisins == 3 :
					new_grid.append([x-1,y])

			if not [x+1,y] in new_grid:
				voisins = voisinage(x+1, y)
				if voisins == 3 :
					new_grid.append([x+1,y])

			if not [x-1,y+1] in new_grid:
				voisins = voisinage(x-1, y+1)
				if voisins == 3 :
					new_grid.append([x-1,y+1])

			if not [x,y+1] in new_grid:
				voisins = voisinage(x, y+1)
				if voisins == 3 :
					new_grid.append([x,y+1])

			if not [x+1,y+1] in new_grid:
				voisins = voisinage(x+1, y+1)
				if voisins == 3:
					new_grid.append([x+1,y+1])


	reload()


