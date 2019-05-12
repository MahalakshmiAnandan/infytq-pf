def calculate(distance,no_of_passengers):
    pass
    price=70
    ticket_cost=80
    mileage=10
    route_cost=(distance/mileage)*price
    total_ticket_cost=(no_of_passengers*ticket_cost)
    if(total_ticket_cost>route_cost):
        profit=total_ticket_cost-route_cost
        return profit
    else:
        return (-1)
  
  
distance=30
no_of_passengers=2
print(calculate(distance,no_of_passengers))
