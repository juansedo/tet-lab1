#Code based on https://github.com/ST0263/st0263-20212/blob/main/LabSocketsMultiThread/ServerLab.py

#!/usr/bin/env python3
import socket
import threading

IP_SERVER = '127.0.0.1'
PORT = 10000
RECV_BUFFER_SIZE = 1024
ENCODING_FORMAT = 'utf-8'

# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = IP_SERVER

def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:", server_address)
    print("Port:", PORT)
    server_execution()

#Function to start server process...
def server_execution():
    tuple_connection = (server_address, PORT)
    server_socket.bind(tuple_connection)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...')
    server_socket.listen(5)
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
        client_thread.start()
    print('Socket is closed...')
    server_socket.close()

# Handler for manage incomming clients conections...
def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        data_received = client_connection.recv(RECV_BUFFER_SIZE)
        remote_string = str(data_received.decode(ENCODING_FORMAT))
        remote_command = remote_string.split()
        if (len(remote_command) == 0):
            continue
        command = remote_command[0]
        print (f'Data received from: {client_address[0]}:{client_address[1]}')
        
        
        # Command with arguments
        if (len(remote_command) > 1):
            if (command == 'gen-table'):
                if (len(remote_command) < 4):
                    response = f'400 MARG\n\rMissing arguments: gen-table <init-value> <ir-%> <total-months>\n\r'
                    client_connection.sendall(response.encode(ENCODING_FORMAT))    
                value, ir, total_months = verify_arguments(remote_command[1], remote_command[2], remote_command[3])
                table_in_string = generate_table(value, ir, total_months)
                client_connection.sendall(table_in_string.encode(ENCODING_FORMAT))
            else:
                response = f'400 BCMD\n\rCommand-Description: Unknown command "{command}"\n\r'
                client_connection.sendall(response.encode(ENCODING_FORMAT))
        
        #Command without arguments
        else:
            if (command == 'exit'):
                response = '200 BYE\n'
                client_connection.sendall(response.encode(ENCODING_FORMAT))
                is_connected = False
            else:
                response = f'400 BCMD\n\rCommand-Description: Unknown command "{command}"\n\r'
                client_connection.sendall(response.encode(ENCODING_FORMAT))

    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

def verify_arguments(val, ir, m):
    return val, ir, m

def generate_table(value, ir, total_months):
    return f'-------------\n- Value: {value}\n- Interest Rate: {ir}\n- Total months: {total_months}\n-------------\n'

if __name__ == "__main__":
    main()