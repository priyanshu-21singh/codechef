#def is_greater_than_50(T,test_cases):
   # for i in range(T):
       # x,y,z = test_cases[i]
        #total_students = x * y

    #if z > total_students//2:
       # print("yes")
    #else:
       # print("no")

   # t = int(input()) 
   # test_cases = []   
    #for _ in range (T):
       # x,y,z = map(int,input().split())
       # test_cases.append((x,y,z))


       # is_greater_than_50(T,test_cases)

def is_greater_than_50_percent(T, test_cases):
    for i in range(T):
        X, Y, Z = test_cases[i]
        total_students = X * Y
        if Z > total_students // 2:
            print("YES")
        else:
            print("NO")

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    X, Y, Z = map(int, input().split())
    test_cases.append((X, Y, Z))

# Check if the number of students who passed is greater than 50%
is_greater_than_50_percent(T, test_cases)
    
    