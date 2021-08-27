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
    
    
    print("\n===> All Test Cases Passed.\n")


# addStrings function to add number string
def addStrings(numString):
    
    if numString == "":
        return 0
    return(int(numString))
    

# call test function
test()
