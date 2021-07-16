'''
- If a customer purchases 0 books, he or she earns 0 points
- If a customer purchases 2 books, he or she earns 5 points
- If a customer purchases 4 books, he or she earns 15 points
- If a customer purchases 6 books, he or she earns 30 points
- If a customer purchases 8 or more books, he or she earns 60 points
'''

def book():
    reader = int(input("Enter the number of books you get this month: "))

    if reader <= 1:
        print('You did not earn any points.')
    elif reader > 2 and reader < 4:
        print('You earn 5 points!')
    elif reader > 4 and reader < 7:
        print('You earn 15 points!')
    elif reader > 6 and reader < 9:
        print('You earn 30 points!')
    elif reader > 8:
        print('You earn 60 points!')
book()