def solve(heads,legs):
   error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    c=0
    flag=1
    for r in range(heads,-1,-1):
        if(2*chicken_count+4*rabbit_count==legs):
            
           chicken_count=c
            rabbit_count=r
            break
        c=c+1
    if(flag==0):
       print(chicken_count,rabbit_count)
    else:
        print(error_msg)
solve(38,131)
