#Calculate change using fewest number of coins

##User Input
user_input = int(input("Enter purchase price of an item (less than 100 cents): "))

##assuming customer paid $1 which is 100 cents, calculate change due to the customer
change_due = 100 - user_input

##Define variables for quarters, dime and pennies
q = 25
d = 10
p = 1

##counter number of quarters
counter_q = change_due // q
print(counter_q, " quarters")
change_due = change_due % q

##if quarters are not sufficient for change then go to dimes
if change_due != 0:        
    counter_d = change_due // d
    change_due = change_due % d
    print(counter_d, " dimes")
##if quarters and dime are not sufficient then anything remaining is the number of pennies    
    print (change_due, "pennies")

#End

