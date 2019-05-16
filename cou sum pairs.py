def find_pairs_of_numbers(num_list,n):
    count=0
    s=len(num_list)
    for i in range(0,s):
        for j in range(i+1,s):
            if(num_list[i]+num_list[j]==n):
                count+=1
            
    return(count)
            

num_list=[10,30,40,50,60]
n=90
print(find_pairs_of_numbers(num_list,n))
