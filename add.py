from calc_func import do_addition , do_subtraction, do_multiplication , do_division


def main():
    print("Welcome to the Calculator App")
    func = input("""Please Select the function: 1) "Add" 
                                         2) "Subtract" 
                                         3) "Multiply" 
                                         4) "Divide"  """)
    a= int(input("Please Enter Fist Number: "))
    b = int(input("Please Enter Second Number: "))
    
    if func =="Add":
        results = do_addition(a, b)
    elif func == "Subtract":
        results = do_subtraction(a, b)
    elif func == "Multiply":
        results = do_multiplication(a, b)
    elif func == "Divide":
        results = do_division(a, b)


    print("Result: ", results )
    

if __name__ == "__main__":
    main()

