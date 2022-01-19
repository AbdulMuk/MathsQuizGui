import random
import math

replaceCarr = lambda userAns: userAns.replace("^2", "²")

def remove0(num, a, b):
    while num == 0:
        num = random.randint(a, b)
    return num

# argument is a list, removes all zero terms
# removes number if number is 1 or -1, leaving just the sign and the variable
# if number term (no var) then 1 and -1 are not removed
def checkTerm(term):
    if term[0] == 0:
        return ""

    elif term[0] == 1:
        if term[1] == "":
            return f"+ 1 "
        else:
            return f"+ {term[1]} "

    elif term[0] == -1:
        if term[1] == "":
            return f"- 1 "
        else:
            return f"- {term[1]} "

    else:
        if term[0] > 0:
            return f"+ {term[0]}{term[1]} "
        else:
            return f"- {term[0] * -1}{term[1]} " # space between - sign and number

# takes a 3 tier list and outputs a list
def makeListCT(qList):
    newList = []

    for inner1 in qList: # list of terms
        newStr = ""

        for inner2 in inner1: # list of coeffficient and term
            # use checkTerm to make a string from inner-most list
            # concat all terms to make 1 string
            newStr += checkTerm(inner2)
        
        # strip the leading + sign and any whitespace
        # make a new q and a list
        newStr = newStr.lstrip("+")
        newStr = newStr.strip()
        newList.append(newStr)

    return newList

# not for 1st term, + - before num
checkNum = lambda num: f"+ {num}" if num > 0 else f"- {num * -1}"

# for coefficients, removes num if 1 leaving + -
def check1(num):
    if num == 1:
        return f""
    elif num == -1:
        return f"-"
    else:
        return num

# not for 1st term, does both the above
def checkBoth(num):
    if num > 0:
        if num == 1:
            return f"+ "
        else:
            return f"+ {num}"
    else:
        if num == -1:
            return f"- "
        else:
            return f"- {num * -1}"

def multiples(num, b):
    multiplesList = []
    for i in range(1, b):
        multiplesList.append(num * i)

    return multiplesList

def factors(num):
    factorsList = []

    for i in range(1, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            factorsList.append(i)
            if num / i != i:
                factorsList.append(int(num / i))

    factorsList.sort()
    return factorsList

def checkAns(ans, userAns, msg, correct):
    ans = ans.replace(" ", "")
    ans = ans.replace(",", "")
    userAns = userAns.replace(" ", "")
    userAns = userAns.replace(",", "")

    if ans == userAns.lower():
        msg = "Correct, well done!"
        correct += 1
    
    return [msg, correct]