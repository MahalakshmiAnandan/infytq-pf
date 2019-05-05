def find_new_salary(current_salary,job_level):
   
 if(job_level==3):
        hike=(15/100)*current_salary
        new_salary=current_salary+hike
   
 elif(job_level==4):
       hike=(7/100)*current_salary
       new_salary=current_salary+hike
  
 elif(job_level==5):
        hike=(5/100)*current_salary
        new_salary=current_salary+hike
    
 else:
        hike=0
       new_salary=current_salary+hike

 return new_salary

new_salary=find_new_salary(15000,3)

print(new_salary)
