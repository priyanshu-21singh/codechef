M = [[1,2,3,4],[5,6,7,8],[8,9,0,1],[2,3,4,5]]
N = 4

circle = 0
#start point0,0
i,j=0,0
while(circle<N/2):

    cycles = N-1-2*circle
    jumps = 0 # tojump in circle
    while(jumps<cycles):
        temp = M[i][j+jumps]
        M[i][j+jumps] = M[i+cycles][j+cycles-jumps]
        M[i+cycles][j+cycles-jumps] = 
