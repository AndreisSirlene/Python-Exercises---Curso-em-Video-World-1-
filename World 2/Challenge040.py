import emoji
grade1 = float(input('What is your first grade in Maths? '))
grade2 = float(input('Now tell me yor second grade in Maths: '))
average = (grade1 + grade2) / 2
print('Lets check how you did this semester!')
if average <= 5.0:
    print(emoji.emojize('FAILLED :-1:! You need to repeat this subject next year.',use_aliases=True))
elif average >= 5.0 and average < 7.0:
    print(emoji.emojize('You almost get :pray:, need REPEAT the subject!',use_aliases=True))
elif average >= 7.0:
    print(emoji.emojize('Congratulations :gift::mortar_board:, you have been APPROVED!!!', use_aliases=True))
