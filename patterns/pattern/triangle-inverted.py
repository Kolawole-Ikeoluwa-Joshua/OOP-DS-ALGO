def printTriangle(N):
        
    for i in range(1, 2*N):
        stars = i
        if (i > N): 
            stars = 2*N-i
            
        for j in range(0, stars):
            print("* ", end="")
 
        print()

    return "Pattern Printed Successfully"



result = printTriangle(5)
print(result)