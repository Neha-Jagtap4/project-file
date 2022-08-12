import array

def main():
	print("Demostartion of array in python ")
	arr = array.array('i',[10,20,30,40])

	print(arr)
	print("Length of array : ",len(arr))
	print("Type is: ",type(arr))
	
if __name__ == "__main__":
	main()