import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculator(first_number, second_number, operation):
    '''Use this 4 function calculator to compute simple mathematical operations.'''
    if operation == '*':
        return first_number * second_number
    if operation == '/':
        return first_number / second_number
    if operation == '+':
        return first_number + second_number
    if operation == '-':
        return first_number - second_number

memory = []
loops = 0
should_stop = False
continue_calc = 'no'
while should_stop == False:
    if continue_calc == 'yes':
        first_number = memory[loops - 1]
    else:
        os.system('cls||clear')
        print(logo)
        print('Welcome to the Pythonista Calculator!')
        first_number = float(input('What is the first number? '))
    operation = input('''
+
-
*
/
Pick an operation. ''')
    second_number = float(input('What is the second number? '))
    result = calculator(first_number, second_number, operation)
    print(f'The result is {result}.')
    continue_calc = input(f'Type "yes" if you want to continue calculating with {result} or "no" to start over. Type "stop" to stop using the calculator. ').lower()
    if continue_calc == 'yes':
        memory.append(result)
        loops += 1
    elif continue_calc == 'stop':
        should_stop = True
        print('Thanks for using the Pythonista Calculator!')