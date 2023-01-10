color=input('Please enter your favorite color: ')
print(color.capitalize(),'is a fantastic color!')
years=input('How many years have you liked this color? ')
print('That is great that you have liked', color, 'for', years, 'years!') 
age=input('How old are you? ')
total=int(years)/int(age)*100
print('You have liked', color, 'for', int(total),'percent of your life!')