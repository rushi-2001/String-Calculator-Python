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
    
     # test case for two numbers - newline separated
    assert (addStrings("1\n2")) == 3, "Given string \"1\n2\" didn't return 3"
    assert (addStrings("4\n5")) == 9, "Given string \"4\n5\" didn't return 9"
    
    
    # test case for n numbers - newline separated
    assert (addStrings("1\n2\n3\n4\n5")) == 15, "Given string \"1\n2\n3\n4\n5\" didn't return 15"
    assert (addStrings("1\n4\n5")) == 10, "Given string \"1\n4\n5\" didn't return 10"
    
    
    # test case for n numbers - comma and newline separated
    assert (addStrings("1\n2\n3,4,5")) == 15, "Given string \"1\n2\n3,4,5\" didn't return 15"
    assert (addStrings("2,3\n5")) == 10, "Given string \"2,3\n5\" didn't return 10"
    
    # test case for n numbers - custom delimiter of 1 char
    assert (addStrings("//;\n1;2;3")) == 6, "Given string \"//;\n1;2;3\" didn't return 6"
    assert (addStrings("//%\n3%4%5%6")) == 18, "Given string \"//%\n3%4%5%6\" didn't return 18"
    
    # test case for n numbers - custom delimiter of n char
    assert (addStrings("//***\n1***2***3")) == 6, "Given string \"//***\n1***2***3\" didn't return 6"
    assert (addStrings("//@$@$\n3@$@$4@$@$5@$@$6")) == 18, "Given string \"//@$@$\n3@$@$4@$@$5@$@$6\" didn't return 18"
    
    # test case for n numbers - multiple custom delimiters
    assert (addStrings("//[**][!!]\n1**2!!3")) == 6, "Given string \"//[**][!!]\n1**2!!3\" didn't return 6"
    assert (addStrings("//[+][||]\n3+4||5||6")) == 18, "Given string \"//[+][||]\n3+4||5||6\" didn't return 18"
    
    
    
    print("\n===> All Test Cases Passed.\n")


# addStrings function to add number string
def addStrings(numString):
    
    if numString == "":
        return 0
    elif numString.isdigit():
        return(int(numString))
    elif numString[0] == '/' and numString[2] == "[":
        list1 = numString.split('\n')
        list2 = list1[0].split('[')
        list2 = list2[1:]
        
        # store all delimeters in list
        delimiters = []
        for s in list2:
            x = s[0:len(s)-1]
            delimiters.append(x)
        
        str1 = list1[1]
        
        # replace all delimiters with comma
        for delim in delimiters:
            if delim in str1:
                str1 = str1.replace(delim, ',')
        
        numbers = str1.split(",")
        return addNumbers(numbers)          
          
        
    elif numString[0] == '/':
        list1 = numString.split('\n')
        delimiter = list1[0][2:]
        numbers = list1[1].split(delimiter)
        return addNumbers(numbers)
    
        
    else:
        sum = 0
        delimiter = ","        
        if numString.find('\n') != -1 and numString.find(',') != -1:
            numList = []
            str1 = numString.split('\n')
            for s in str1:
                if "," in s:
                    x = s.split(',')
                    for i in x:
                        numList.append(int(i))
                else:
                    numList.append(int(s))
            
            return addNumbers(numList)
        elif numString.find('\n') != -1:
            delimiter = '\n'    
        
        numbers = numString.split(delimiter)
        return addNumbers(numbers)

def addNumbers(numbers):
    sum = 0
    for num in numbers:
        sum += int(num)
    return sum
    

# call test function
test()

