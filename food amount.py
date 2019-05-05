def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
   
 bill_amount=0
    
if(food_type=="N"):
       if(distance_in_kms<=3):
           delivery_charge=0
        elif(3<distance_in_kms<7):
           delivery_charge=3
        else:
            delivery_charge=6
        bill_amount=(150*quantity_ordered)+delivery_charge
 elif(food_type=="V"):
       if(distance_in_kms<=3):
            delivery_charge=0
       elif(3<distance_in_kms<7):
            delivery_charge=3
        else:
            delivery_charge=6
       bill_amount=(120*quantity_ordered)+delivery_charge
 else:
        print(-1)
        
 return bill_amount

bill_amount=calculate_bill_amount("V",1,7)

print(bill_amount)
