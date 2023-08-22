keys = ['phone_number', 'first_name', 'last_name', 'city', 'country']
values = ['first_name', 'last_name', 'city', 'country']

def print_commands():
    print('Available commands:',
          'print - Print all phone records',
          'new - Create new record',
          'sf - Search by first name',
          'sl - Search by last name',
          'sfl - Search by full name',
          'sp - Search by phone number',
          'sct - Search by city',
          'sc - Search by country',
          'up - Update record',
          'del - Delete record',
          'help - List commands',
          'exit - Exit the program',
          sep='\n')

def print_result(result_list):
    for phone, data in result_list.items():
        print('\n')
        print(f'Phone number: {phone}')
        for name, record in zip(values, data):
            print(f'{name.capitalize()}: {data[record]}')

def read_values():
    phone = input('Input phone number: ')
    new_data = {phone: {}}
    for key, value in zip(keys, values):
        new_data[phone][key] = input(f'Input {value}: ')
    return new_data
