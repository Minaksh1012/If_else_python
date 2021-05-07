day=input("enter the name of day")
time=input("enter the time period")

if day=="monday":
    if time=="breakfast":
        print("poha")
    elif time=="lunch":
        print("dal rice and pumkin curry")
    else:
        print("chiken")    
elif day=="tuesday":
    if time=="breakfast":
        print(" halwaa")
    elif time=="lunch":
        print("gobi curry")
    else:
         print("anda rice")
elif day=="wednesday":
    if time=="breakfast":
        print("pasta")
    elif time=="lunch":
        print("khichdi besn")
    else:
        print("biryani")
elif day=="thursday":
    if time=="breakfast":
        print("chana masala")
    elif time=="lunch":
        print("chole bhatore")
    else:
        print("andaa curry")
elif day=="friday":
    if time=="breakfast":
        print("chilaa")
    elif time=="lunch":
        print("muttor punneer")
    else :
        print("chiken lolipop")
elif day=="saturday":
    if time=="breakfast":
        print("allu paratha")
    elif time=="lunch":
        print("dam allu curry and roti")
    else:
        print("chiken fry")                               
else:
    print("today is holiday u can go hotels")
