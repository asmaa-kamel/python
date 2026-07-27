name=input("Enter your name :")


if name.isalpha():
  e_mail=input("Enter your mail :")
  if e_mail.find('@')!=-1:
   print("Name :"+name +"and Email :"+e_mail)
  else:
      print("Name :"+name+ " and Email is not valid!!" )
      
else:
   print("Name not valid!!")       
  

 

 
 