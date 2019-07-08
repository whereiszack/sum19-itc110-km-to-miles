#input number of kilometers and convert the number to miles.

def main():
    print("This program converts Kilometers to Miles") 
    km = float(input("Type the number of kilometers: "))#get user input
    miles = km * 31/50 #31/50 is the fraction eqiuvalent of .62
    print(km, "km  = ", miles, "miles") #final output of converted km to miles

main()
