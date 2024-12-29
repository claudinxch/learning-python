# january, february, march, april, may
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(f'extra: {expenses[1] - expenses[0]}')
# 2. Find out your total expense in first quarter (first three months) of the year.
total = sum(expenses[:3])
print(f'total expense first quarter: {total}')

# 3. Find out if you spent exactly 2000 dollars in any month
# def find_expense():
#     for expense in expenses:
#         if(expense == 2000):
#             return expense

# print(find_expense())

print(f'Did i spent 2000$ in a month? {2000 in expenses}')

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] -= 200
print(expenses)

print('---------------------------')

heroes = ['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(f'Length of the list: {len(heroes)}')
# 2. Add 'black panther' at the end of this list
heroes.append('black panther')
print(f'List after adding black panther', heroes)
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heroes.remove('black panther')
print(heroes)
heroes.insert(3, 'black panther')
print(heroes)
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# heroes[1] = heroes[2] = 'doctor strange'
heroes[1:3] = ['doctor strange']
print(heroes)
# 5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(f'Sorted heroes list {heroes}')

max_number = int(input('Type the maximum number you want: '))
odd_number = [x for x in range(1, max_number) if x / 2 != 1]
print(odd_number)

# List has to be sorted so binary_search works
def binary_search(arr, item):
    lower = 0
    highest = len(arr) - 1

    while lower <= highest:
        middle = (lower + highest) // 2
        guess = arr[middle]
        
        if guess == item:
            return middle
        elif guess < item:
            lower = middle + 1
        else:
            highest = middle + 1

    return None


hero_name = input('hero name from list to get index: ')
searched = binary_search(heroes, hero_name)
print(f'Index of hero {hero_name} is {searched}')
