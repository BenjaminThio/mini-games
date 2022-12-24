# *************** Declare Variables ***************
#get text input
Text = input("Please type some texts here: ")
#Text waviness
Waviness = 20
#Wave direction
Reverse = False
#Generate negative waviness text
if Waviness < 0:
	Waviness = Waviness * -1
	Reverse = not Reverse
#Spawnpoint
Coord = [0, Waviness]
#Grid container generator
Generator = [[" "] * len(Text) for i in range(Waviness + Waviness + 1)]
#Spawn text depends on spawnpoint
Generator[Coord[1]][Coord[0]] = list(Text)[Coord[0]]

# *************** Realtime Calculation ***************
#Run as long as waviness is greater than 0
if Waviness > 0:
	#Calculate times of wave generation
	for i in range(round(len(Text)/Waviness/2)):
		#Generate wavy text from mid => top => bottom
		if not Reverse:
			while Coord[0] + 1 < len(Generator[Coord[1]]) and Coord[1] - 1 >= 0:
				Coord = [Coord[0] + 1, Coord[1] - 1]
				Generator[Coord[1]][Coord[0]] = list(Text)[Coord[0]]
			while Coord[0] + 1 < len(Generator[Coord[1]]) and Coord[1] + 1 < len(Generator):
				Coord = [Coord[0] + 1, Coord[1] + 1]
				Generator[Coord[1]][Coord[0]] = list(Text)[Coord[0]]
		#Generate wavy text from mid => bottom => top
		else:
			while Coord[0] + 1 < len(Generator[Coord[1]]) and Coord[1] + 1 < len(Generator):
				Coord = [Coord[0] + 1, Coord[1] + 1]
				Generator[Coord[1]][Coord[0]] = list(Text)[Coord[0]]
			while Coord[0] + 1 < len(Generator[Coord[1]]) and Coord[1] - 1 >= 0:
				Coord = [Coord[0] + 1, Coord[1] - 1]
				Generator[Coord[1]][Coord[0]] = list(Text)[Coord[0]]
	print("".join([f"{''.join(i)}\n" for i in Generator]))
#0 waviness text
else:
	print(Text)