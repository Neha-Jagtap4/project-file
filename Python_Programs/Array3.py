import array as M

def main():
	print("Demostartion of array in python ")
	Data = M.array('f',[10.1,20.2,30.3,40.4,50.5])   #50.5 flaot is not use
					#' f' is float
	print(Data)
	print("Length of array : ",len(Data))
	print("Type is: ",type(Data))
	print("Type is: ",type(Data[4]))

	print(Data[0])
	print(type(Data))
	print(Data[1])
	print("TypeCode of aaray is: ",Data.typecode)

	i = 0
	#for i in range(0,3):  #len(Data)
	#	print(Data[i])

	for no in Data:
		print(no,end =" ")

	while(i<len(Data)): 
		print(Data[i])
		i = i+1
	
if __name__ == "__main__":
	main()