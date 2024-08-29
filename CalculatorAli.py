import CaclUi


def main():

    num1=int(input("Enter Num1: "))
    num2=int(input("Enter Num2: "))

    operation = 0
    answer=0

    operation=input("Choose operation to use Enter 1:Addition 2:Subtraction 3:Devide 4:Multiply: ")

    CaclUi.CaclUi(operation,num1,num2)

    print("Thank you ")



if __name__ == "__main__":
    main()
