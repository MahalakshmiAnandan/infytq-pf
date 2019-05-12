def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    start=101
    temp=start

    for i in range(101,101+no_of_passengers):
        a=source[0:3]
        b=destination[0:3]
        ticket_number=airline+":"+a+":"+b+":"+str(temp)
        ticket_number_list.append(ticket_number)
        temp=temp+1
            
    
    return ticket_number_list[-5:]
print(generate_ticket("AI","Bangalore","London",4))
