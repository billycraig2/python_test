def tuples_to_dict(tuples):
    return {key: value for key, value in tuples}

'''
EXERCISE 1 - BASIC OPERATIONS

my_book = {'title': 'harry potter', 'year': 1999, 'author': 'jk rowling', 'genre': 'fantasy'}
print(my_book)

my_book['rating'] = '5*'
print(my_book)

my_book['year'] = 1998
print(my_book)

del my_book['rating']
print(my_book)

title = my_book.get('title')
items = my_book.items()
print(title)
print(items)
'''

'''
EXERCISE 2 - NESTED DICTIONARY

student = {
    'name': 'billy',
    'age': 22,
    'courses': {
        'tech': 'A',
        'business': 'A',
        'it': 'A',
    }
}
print(student)

student['courses']['chem'] = 'A'
print(student)

student['courses']['chem'] = 'C'
print(student)
'''

squares = {x: x*2 for x in range(1, 4)}  # Creates a dictionary of squares
print(squares)

names = ['william', 'chloe', 'samuel']
name_length = {names: len(names) for names in names}
print(name_length)

tuples = [('william', 'cool'), ('chloe', 'cute'), ('eddy', 'twin')]

print(tuples_to_dict(tuples))


