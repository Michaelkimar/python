weight=eval(input("Weight: "))
unit=input("(K)g or (L)bs: ")
if unit== "k" or "K": 
    converted=weight/0.45
    print("weight in Lbs : " +str(converted))
elif unit=="l" or "L":
    converted=weight * 0.45
    print("weight in Kg: " +str(converted))