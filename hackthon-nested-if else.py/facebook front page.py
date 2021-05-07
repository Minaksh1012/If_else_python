print("FACEBOOK FRONT PAGE")
language=input("enter the language")
ch=input("enter the anyone name ")
email_id=(input("enter the email id"))
password=input("enter the password")
gender=input("enter the gender")

if language=="english"or"hindi"or"marathi":
    if ch>="a" and ch<="z":
        if email_id=="ch@gmail.com":
            if password=="doma":
                if gender=="male"and"female":
                    print("valid")
                else:
                    print("invalid")        
            else: 
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
    prinr("invalid")                           

    