
#Create a Python file named lab_2-8.py
#A team needs to score 15 points to win a gold medal, 
#between 12-14 points to win a silver medal, 
#and between 9-11 point to win a bronze medal. 
#A team does not earn a medal if they earn 8 or fewer points.
#Write a program using nested if else statements where a user can input the number of points a team scored and the medal that they earned is displayed.

print("please give us your")
score = int(input("score:"))
if score <= 8:
    print("you earned nothing :D")
else:
    if score <= 11:
        print("you earned a bronze metal")
        
    else:
        if score <= 14:
            print("you earned a silver metal")
            
        else:
            print("you earned a gold metal")   
            

#now copy lab 2-8 and rename it to lab 2-9 and do the same with nested conditions            
print("please give us your")             
score = int(input("score:"))
if score <= 8:
    print("you earned nothing :D")
elif score <= 11:
    print("you earned a bronze metal")
elif score <= 14:
    print("you earned a silver metal")
else:
    print("you earned a gold metal")   
                    
