def convert_currency(amount_needed_inr,current_currency_name):
   
 current_currency_amount=0
   
 if(current_currency_name=="Euro"):
       current_currency_amount=0.01417*amount_needed_inr
       print(current_currency_amount)
    
elif(current_currency_name=="British pound"):
        current_currency_amount=0.100*amount_needed_inr
        print(current_currency_amount)
    
elif(current_currency_name=="Australian dollar"):
        current_currency_amount=0.02140*amount_needed_inr
        print(current_currency_amount)
    
elif(current_currency_name=="Canadian dollar"):
        current_currency_amount=0.02027*amount_needed_inr
       print(current_currency_amount)
else:
       print(-1)
    
return current_currency_amount




currency_needed=convert_currency(3500,"British pound")



