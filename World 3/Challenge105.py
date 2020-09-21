def notes(*n, sit=False):
    """
    -> Function to analyse notes and student situation
    :parameter n: note of students(accept many notes)
    :parameter sit: optional value , indicate if want to see the student situation or not
    :return: the dictionary that show the student situation 
    """
    di = dict()
    di['total'] = len(n)
    di ['higher'] = max(n)
    di ['lower'] = min(n)
    di['average'] = round(sum(n)/len(n),3)
    if sit:
        if di ['average'] >= 7:
            di['situation:'] =  'GOOD!'
        elif di ['average'] >= 5:
            di['situation:'] = 'REGULAR'
        else:
            di['situation:'] = 'BAD'
    return di
# Main Program
answer = notes(6.0, 5.5, 8.5, 8.9, 7.5, sit=True)
print(answer)
#help(notes)
