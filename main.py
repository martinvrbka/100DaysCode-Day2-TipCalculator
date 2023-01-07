
#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What is the bill:\n"))

number_of_people = float(input("How many people are spliting the bill:\n"))

before_tax_per_person = bill / number_of_people

tax = float(input("What is the tax: \n"))

result = before_tax_per_person + ((before_tax_per_person / 100) * tax)

print(f"Each person will pay {round(result, 2)} dollars.")
