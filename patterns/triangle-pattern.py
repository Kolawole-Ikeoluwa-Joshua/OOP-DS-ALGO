def printTriangle(N):
    if N > 20:
        return "Please input a valid integer between 1 to 20"
    
    for i in range(0, N):
        j = i+1

        for k in range(j):            
            print("* ", end="")
        print()

    return "Pattern Printed Successfully"



result = printTriangle(3)
print(result)