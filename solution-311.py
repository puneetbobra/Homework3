#Miles per gallon - exercise 3.11
##Initialize variables for gallons used = gallons, miles driven = miles, miles per gallon = mpg, 
##total miles driven = total_miles, total gallons used = total_gallons, total miles per gallon = tmpg

gallons = 0
miles = 0
mpg = 0
total_miles = 0
total_gallons = 0
tmpg = 0

##sentinel controlled repition script to accept user input for miles driven and gallons used
while gallons != -1:
    gallons =  float (input("Enter the gallons used (-1 to end): "))
    if gallons == -1: break
    miles = float (input("Enter the miles driven: "))
    mpg = miles / gallons
    print ("The miles/gallon for this tank was ", f"{round(mpg, 6):}")
    total_gallons += gallons
    total_miles += miles

#evaluate total miles per gallon
tmpg = total_miles / total_gallons
print("The overall average miles/gallon was", f"{round(tmpg, 6):}")

##End
