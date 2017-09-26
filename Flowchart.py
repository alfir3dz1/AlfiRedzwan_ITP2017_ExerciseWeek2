available = ['Math', 'Science', 'English']
borrowed = ['Social Studies', 'Computer', 'Bahasa Indonesia']

program_run = True

while program_run:
    print('1. Borrow')
    print('2. Return')

    action = int(input("What do you want to do?"))
    if action == 1:
        for i in range(len(available)):
            print(str(i + 1) + ". " + available[i])

        choice_invalid = True
        while choice_invalid:
            choice = int(input("Choose which book you want to borrow"))
            if choice < 1 or choice > len(available):
                print("Book doesn't exist")
            else:
                # choice is valid
                choice_invalid = False
                book = available[choice - 1]
                del available[choice - 1]

                borrowed.append(book)
                print("Book has been borrowed")

    elif action == 2:
        for j in range(len(borrowed)):
            print(str(j + 1) + ". " + borrowed[j])
        choice_invalid = True
        while choice_invalid:
            choice = int(input("Choose which book you want to return"))
            if choice < 1 or choice > len(borrowed):
                print("Book doesn't exist")
            else:
                # choice is valid
                choice_invalid = False
                book = borrowed[choice - 1]
                del borrowed[choice - 1]

                available.append(book)
                print("Book has been returned")

    prompt = (input('Do you want to borrow another book?'))
    if prompt == 'No':
        print('Thank you!')
        break

