from sklearn import tree

def MarvellousMl(weight,surface):
	BallFeatures = [[35,1],[47,1],[90,0],[56,1],[67,0],[34,0],[78,1],[53,1]]

	Names = [1,1,0,1,0,0,1,1]

	clf = tree.DecisionTreeClassifier()

	clf = clf.fit(BallFeatures,Names)

	result = clf.predict([[weight,surface]])

	if result == 1:
		print("Your objects looks like Tennis ball")

	elif result == 0:
		print("Your objects looks like Cricket ball")

def main():
	print("Enter the weight of object")
	weight = input()

	print("What is the surface type of your object Rough or Smooth")
	surface = input()

	if surface.lower() =="rough":
		surface =1
	elif surface.lower() == "smooth":
		surface =0
	else:
		print("Error : Wrong input")
		exit()

	MarvellousMl(weight,surface)

if __name__ == "__main__":
	main()