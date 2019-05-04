def calculate_total_ticket_cost(no_of_adults, no_of_children):
  
  total_ticket_cost=0
   
 rate_per_adult=37550.0
  
  rate_per_child=rate_per_adult/3
 
   ticket_amount=(rate_per_adult*no_of_adults)+(rate_per_child*no_of_children)
   
 service_tax=(7/100)*ticket_amount
  
  ticket_cost=ticket_amount+service_tax
 
   total_ticket_cost=ticket_cost-(10/100)*ticket_cost

 
   return total_ticket_cost



total_ticket_cost=calculate_total_ticket_cost(3,1)

print("Total Ticket Cost:",total_ticket_cost)
