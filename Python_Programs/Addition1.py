#list,loop,input function,starter,function defination
def Addition(Value):
	sum = 0
	for i in range(len(Value)):
		sum = sum + Value[i]
	
	return sum


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

	ret = Addition(data)
	print("Addition is: ",ret)


if __name__ == "__main__":
	main()