#import Marvellous2
from Marvellous2 import *

def main():
	size =0

	print("How many elements you want")
	size = int(input())

	data = []

	print("Enter the elements")
	for i in range(size):
		no = int(input())
		data.append(no)
		#ORRRRRRRRRRR
		#data.append(int(input()))
	print("Your entered data is: ",data)

	#ret = Marvellous2.Addition(data)
	ret = Addition(data)
	print("Addition is: ",ret)


if __name__ == "__main__":
	main()