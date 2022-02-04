def checkDriverAge(age):
 message = ''
 if int(age) < 18:
	 message = "Sorry, you are too young to drive this car. Powering off"
 elif int(age) > 18:
	 message = "Powering On. Enjoy the ride!"
 elif int(age) == 18:
	 message = "Congratulations on your first year of driving. Enjoy the ride!"
 return message

age = input("What is your age?: ")
print(checkDriverAge(92))


