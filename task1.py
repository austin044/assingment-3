invest = float(input("How much do you want to invest: "))
monthly = float(input("How much money are you paying per month: "))
intrest = float(input("What is your intrest rate: "))
years = float(input("How many years are you going to pay this: "))

monthlyrate = intrest / 12 / 100
months = years * 12

futurevalue = invest * ((1 + monthlyrate) ** months)
futurevalue2 = futurevalue + monthly * (((1 + monthlyrate) ** months) - 1) / monthlyrate * (1 + monthlyrate)

futurevalue3 = round(futurevalue2, 2)
print("Your future value is: " +str(futurevalue3))