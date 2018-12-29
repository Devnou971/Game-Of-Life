#coding:utf-8
"""

Python  2.X / 3.X

Damien DASSEUX

Game Of Life

"""

import os # Bientot besoin pour le saves
import json # besoins pour es préférences

try: # Ce morceau de script permet de 
	from Tkinter import *
	#from tkFileDialog import askopenfilename
except ImportError:
	try:
		from tkinter import *
		#from tkinter import filedialog
	except ImportError:
		print("Tkinter n'est pas intallé sur votre machine.")

fen = Tk()
fen.title("Game of Life")
fen.minsize(600,500)

#menubar = Menu(fen)

fichierpreference = open("preference.json", "r") 
preference = json.load(fichierpreference)
fichierpreference.close()

couleurs_dispo = preference["couleurs_dispo"]
couleur = preference["couleur"]

algo = "algo/" + preference["algo_de_base"]

exec(open(algo, "r").read())

pas_x = 15
pas_y = 15
width = 800 
height = 500
resolution = [int(width/pas_x), int(height/pas_y)]
play = False
gen = 0
gen_IntVar = IntVar()
gen_IntVar.set(0)

old_grid = []
new_grid = []

can = Canvas(fen, width =width, height=height, bg="white", scrollregion=(0,0,height*2,width*2))


for x in range(resolution[0]+1):
	can.create_line(pas_x*x,0,pas_x*x,height*2)
for y in range(resolution[1]+1):
	can.create_line(0,pas_y*y,width*2,pas_y*y)

def reload():
	global pas_x, pas_y, new_grid, resolution, height, width

	can.delete(ALL)

	for x in range(resolution[0]+1):
		can.create_line(pas_x*x,0,pas_x*x,height)
	for y in range(resolution[1]+1):
		can.create_line(0,pas_y*y,width,pas_y*y)
	

	for i in range(len(new_grid)):
		x0 = new_grid[i][0] * pas_x
		y0 = new_grid[i][1] * pas_y
		x1 = x0 + pas_x
		y1 = y0 + pas_y

		can.create_rectangle(x0 , y0 , x1 , y1 , fill=couleur[1])


def click_case(event):
	global resolution, pas_y,pas_x,new_grid, gen, gen_IntVar

	x , y = event.x, event.y
	print("x : ", x, " y : ", y)
	#pos_case_clicke = [0,0]
	i = 0
	j = 0
	while pas_x * i <= x:
		i = i + 1
	while pas_y * j <= y:
		j = j + 1

	pos_case_clicke = [i-1, j-1]

	#print("i : ", i ," j : ", j)
	
	if pos_case_clicke in new_grid:
		new_grid.remove(pos_case_clicke)
	else:
		new_grid.append(pos_case_clicke)
	gen = 0
	gen_IntVar.set(0)
	reload()


def jouer():
	global play, gen_IntVar, gen
	play = True
	while play:
		algorithme()
		gen = gen + 1
		gen_IntVar.set(gen)
		can.update_idletasks() # on update toutes les précédentes fonctions
		can.update() # on update la fenetre

def stopper(): # ici on arretele jeu en cours
	global play
	play = False

def reset():
	global play, old_grid, new_grid, gen, gen_IntVar
	play = False
	old_grid = []
	new_grid = []
	gen = 0
	gen_IntVar.set(0)
	reload()

def zoomM():
	global pas_x, pas_y
	pas_x = pas_x - 1
	pas_y = pas_y - 1
	resolution = [int(width/pas_x), int(height/pas_y)]
	print(resolution)
	reload()

def zoomP():
	global pas_x, pas_y
	pas_x = pas_x + 1
	pas_y = pas_y + 1
	resolution = [int(width/pas_x), int(height/pas_y)]
	print(resolution)
	reload()

taillecase = IntVar()
taillecase.set(pas_x)


zoomMinus = Button(fen, text="Zoom Minus", command=zoomM)
zoomMinus.grid(row=3 , column = 0)

zoomPlus = Button(fen, text="Zoom Plus", command = zoomP)
zoomPlus.grid(row=3, column = 1)

affichageGeneration = Label(fen, textvariable=gen_IntVar)
affichageGeneration.grid(row=2, column=2)

boutonReset = Button(fen, text="Reset", command=reset)
boutonReset.grid(row = 2, column= 1)

boutonNext = Button(fen, text="Next", command=algorithme)
boutonNext.grid(row = 1, column = 1)

boutonJouer = Button(fen, text="Play", command=jouer)
boutonJouer.grid(row = 1, column = 0)

boutonStop = Button(fen, text="Stop", command=stopper)
boutonStop.grid(row = 1, column = 2)

can.bind("<Button-1>", click_case)
can.grid(row=0, column=1)

fen.mainloop()