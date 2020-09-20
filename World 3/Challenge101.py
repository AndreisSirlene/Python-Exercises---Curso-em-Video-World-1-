def vote(dob):
	from datetime import date
	actual = date.today().year
	age = actual - dob
	if 18 < age < 65:
		return f'With {age} years: Right to Vote!'
	elif age < 16:
		return f'With {age} years: Can not vote! '
	else:
		return f'With {age} years: Vote is optional'

#Main Program
birth = int(input('What is your year of birth? '))
print(vote(birth))

