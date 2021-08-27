# Python Code for String Calculator using TDD Kata
# Submitted By : Rushi Patel (18BCE201)
# Institute of Technology, Nirma University


# test function which test for various test cases of String Calculator
def test():
    
    # test case for empty string
    assert (addStrings("")) == 0, "Empty String didn't return 0"
    
    # test case for single number
    assert (addStrings("1")) == 1, "Single number String \"1\" didn't return 1"
    assert (addStrings("2")) == 2, "Single number String \"2\" didn't return 2"
    assert (addStrings("42")) == 42, "Single number String \"42\" didn't return 42"
    
    # test case for two numbers - comma separated
    assert (addStrings("1,2")) == 3, "Given string \"1,2\" didn't return 3"
    assert (addStrings("4,5")) == 9, "Given string \"4,5\" didn't return 9"
    
    # test case for n numbers - comma separated
    assert (addStrings("1,2,3,4,5")) == 15, "Given string \"1,2,3,4,5\" didn't return 15"
    assert (addStrings("1,4,5")) == 10, "Given string \"1,4,5\" didn't return 10"
    
    print("\n===> All Test Cases Passed.\n")


# addStrings function to add number string
def addStrings(numString):
    
    if numString == "":
        return 0
    elif numString.isdigit():
        return(int(numString))
    else:
        sum = 0
        numbers = numString.split(",")
        for num in numbers:
            sum += int(num)
        return sum 
    

# call test function
test()

