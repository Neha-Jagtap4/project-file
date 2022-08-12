import array as M

def main():
	print("Demostartion of array in python ")
	Data = M.array('i',[10,20,30,40,50])

	print(Data)
	print("Length of array : ",len(Data))
	print("Type is: ",type(Data))
	print("Type is: ",type(Data[4]))

	print(Data[0])
	print(type(Data))
	print(Data[1])

	i = 0
	#for i in range(0,3):  #len(Data)
	#	print(Data[i])

	for no in Data:
		print(no,end =" ")

	print(".......")
	while(i<len(Data)): 
		print(Data[i])
		i = i+1
	
if __name__ == "__main__":
	main()