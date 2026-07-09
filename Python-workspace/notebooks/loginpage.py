

#login page
email=input("Enter your email:")
if '@' in email:
    password=input("Enter your password")
    if email=="tayyba06@gmail.com" and password == "123456":
        print("Welcome to the space")
    elif email =="tayyba06@gmail.com" and password!="123456":
         print("Password incorrect")
         password=input("Write your password again")
         if password=="123456":
                print("Finally correct")
         else:
          print("OOPS,password is incorrect again")
    else:
        print("incorrect credentials")
else:
  print("Email is incorrect,write the correct one")