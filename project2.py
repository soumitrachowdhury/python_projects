# Tip calculator

print("Welcome to tip calculator!")

bill=float(input("Enter the amount of bill- $"))
tip=int(input("Enter how much tip you want to give in percentage (i.e.-12,15,20)- "))
people=int(input("Enter the amount of people willing to pay- "))

result=(bill+(bill*tip/100))/people

print(f"Every person has to pay ${round(result,2)}")


