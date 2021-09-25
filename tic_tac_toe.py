import pandas as pd
import numpy as np


def main():

    playing = True

    # in the future, this code can be updated, because we can create a dashboard
    # bigger than 3x3. Now it'l be set up as default as 3x3.
    array_quantity = get_quantity(3)

    while playing:

        player_x = True
        player_y = False

        while player_x:

            try:
            
                sorted_list = dataframe(array_quantity)
                mainframe = get_mainframe(sorted_list, 3)
                print()

                print(mainframe)
                
                print()
                new_input = int(input('Player ❌: please, choose a number between(1-9): '))
                modify_array(array_quantity, new_input, 'X')
                won = check_winner(array_quantity, 'X')

                if won:
                    print()
                    print(won)
                    print()

                    sorted_list = dataframe(array_quantity)
                    mainframe = get_mainframe(sorted_list, 3)

                    print(mainframe)
                    print()

                    playing = False
                    player_y = False
                    break

                player_x = False
                player_y = True
            
            except TypeError:
                print('That\'s not allowed, please choose a number between 1-9' )
                continue
            except IndexError:
                print('That\'s not allowed, please choose a number between 1-9' )
                continue
            except ValueError:
                print('That\'s not allowed, please choose a number between 1-9' )
                continue

        
        while player_y:

            try:

                sorted_list = dataframe(array_quantity)
                mainframe = get_mainframe(sorted_list, 3)
                print()

                print(mainframe)
                
                print()
                new_input = int(input('Player 🔵: please, choose a number between(1-9): '))
                modify_array(array_quantity, new_input, 'O')
                won = check_winner(array_quantity, 'O')
                
                if won:
                    print()
                    print(won)
                    print()
                    sorted_list = dataframe(array_quantity)
                    mainframe = get_mainframe(sorted_list, 3)

                    print(mainframe)
                    print()
                    playing = False

                player_y = False

            except TypeError:
                print('That\'s not allowed, please choose a number between 1-9' )
                continue
            except IndexError:
                print('That\'s not allowed, please choose a number between 1-9' )
                continue
            except ValueError:
                print('That\'s not allowed, please choose a number between 1-9' )
                continue
    
    print()
    continue_playing = input('Would you like to play it again 😁? y/n: ')

    if continue_playing.lower() == 'y':
        main()
    else:
        print()
        print('Thank you for playing with us! 🤗')

def check_winner(array, player):
    '''This function only checks the winner on all the possibles
    scenarios for a dashboard 3 x 3'''

    won = False

    for i in array:
        if i == array[0] and i == array[1] and i == array[2]:
            won = True
        elif i == array[3] and i == array[4] and i == array[5]:
            won = True
        elif i == array[6] and i == array[7] and i == array[8]:
            won = True
        elif i == array[0] and i == array[3] and i == array[6]:
            won = True
        elif i == array[1] and i == array[4] and i == array[7]:
            won = True
        elif i == array[2] and i == array[5] and i == array[8]:
            won = True
        elif i == array[0] and i == array[4] and i == array[8]:
            won = True
        elif i == array[2] and i == array[4] and i == array[6]:
            won = True
        elif array.count('X') == 5 and array.count('O') == 4:
            return '😅 This game was a DRAW 🤙'

    if won:
        return f'🙌🙌 YAAY❕❗ Player {player} won! 🎉🎉'

def modify_array(array, input, player):
    '''This function only modifies the given array, in order to
    recreate the dataframe and print it out later.'''

    real_input = input -1

    if player == 'X':
        for i in array:
            if real_input not in array:
                array[real_input] = 'X'
            elif i == real_input:
                array[i] = 'X'

    elif player == 'O':
        for i in array:
            if real_input not in array:
                array[real_input] = 'O'
            elif i == real_input:
                array[i] = 'O'
    

def get_quantity(input_rows_columns):
    '''This functions takes the quantity of numbers that the
    dashboard will have, then stores them one by one on the
    all_numbers array. Then returns that array.'''

    quantity = input_rows_columns * input_rows_columns
    all_numbers = []
    
    for i in range(quantity):
        all_numbers.append(i+1)

    return all_numbers


def dataframe(all_numbers, columns_rows = 3):
    '''This function takes all_numbers as array
    and the columns and rows the user will choose.'''

    # This was created and the logic is working for any value
    # that you wanna pass, but wasn't applied at the end.
    
    sorted_numbers = []

    count = 0

    while count != columns_rows:
        # it sorts the given array for the get_mainframe function,
        # the for loop iterates from columns_rows parameter.
        for i in range (count, len(all_numbers), columns_rows):
            number = all_numbers[i]
            sorted_numbers.append(number)
        count+=1   

    return sorted_numbers

    
def get_mainframe(sorted_list, columns_rows):
    '''This function takes the sorted list and the column rows
    given, then created a data frame and returns it as str.'''

    d = {}

    np.array(sorted_list)

    new_arr = np.array_split(sorted_list, columns_rows)
    
    for j in range(columns_rows):
        d[j] = new_arr[j]

    df = pd.DataFrame(data=d)

    new = df.to_string(index=False, header=False)

    return new

if __name__ == "__main__":
    main()