#def Addition(value1,value2):
#	result = 0
#	result = value1+value2
#	return result
import Marvellous

def main():
	print("Inside module :",__name__)
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter seconf number: "))

	ret = Marvellous.Addition(no1,no2)
	print("Addition is :",ret)

if __name__ == "__main__":   #starter
	main()