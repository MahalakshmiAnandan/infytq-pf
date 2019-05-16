def find_winner_of_the_day(*match_tuple):
    count=0
    count1=0
    n=len(match_tuple)
    for i in range(0,n):
        if match_tuple[i]=="Team1":
            count+=1
        if match_tuple[i]=="Team2":
            count1+=1
    if(count>count1):
        return(match_tuple[i])
    elif(count1>count):
        return(match_tuple[i])
    else:
        return("Tie")
            
        
            
     


#print(find_winner_of_the_day("Team1","Team2","Team1"))
print(find_winner_of_the_day("Team1","Team2","Team1","Team2","Team2"))
