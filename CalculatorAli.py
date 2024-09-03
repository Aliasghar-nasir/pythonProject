import sys
import CaclUi

def main():
    if len(sys.argv) == 1:
        # Interactive mode
        num1 = int(input("Enter Num1: "))
        num2 = int(input("Enter Num2: "))

        operation = input("Choose operation to use Enter 1:Addition 2:Subtraction 3:Divide 4:Multiply: ")
    elif len(sys.argv) == 4:
        # Command-line arguments mode
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        operation = sys.argv[3]
    else:
        print("Usage: python CalculatorAli.py [<num1> <num2> <operation>]")
        sys.exit(1)

    CaclUi.CaclUi(operation, num1, num2)

    print("Thank you Ali Asghar Bin Muhammad Nasir ")

if __name__ == "__main__":
    main()
