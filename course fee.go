package main
import ("fmt")

func main(){
 
   var finalFee int

   var course_fee int

   var mark int
    
   var mark1 int
   
   var scholarship int
   
   var extra_fee int
  
   var fee int
    
   course_fee=25000
    
   mark=70
    
   mark1=mark/2
    
   scholarship=(mark1/100)*course_fee
    
   extra_fee=1500
    
   fee=course_fee - scholarship
  
   finalFee= fee+ extra_fee
println(finalFee)
