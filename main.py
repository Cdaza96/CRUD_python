

def create_client(client_name):
    global clients
    clients += client_name
    _add_comma()

def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print('WELCOME VENTAS')
    print('*'*50)
    print('what would you like to do today')
    print('[C]reate clients')
    print('[D]elete clients')

if __name__ == '__main__':
    _print_welcome()
    
    command = input()

    if command == 'C':
        list_clients()
        client_name = input('What is the client name: ')
        create_client(client_name)
        list_clients()

    elif commando == 'D':
        pass
    else:
        print('invalid command')
