def function(varA, varB):
    if type(varA) == str or type(varB) == str:
        print("string involved")
    else:
        if varA > varB:
            print("bigger")
        elif varA == varB:
            print("equal")
        elif varA < varB:
            print("smaller")

function("hello", 2)
function(2, 3)
function(3, 1)
