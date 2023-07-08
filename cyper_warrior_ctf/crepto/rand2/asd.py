import re
import socket

# Server details
host = '44.206.255.170'
port = 1028
extracted_numbers = []
for i in range(10):
    for i in range(10):
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to the server
            client_socket.connect((host, port))
            # print("Connected to the server.")

            # Send multiple messages to the server
            messages = ["Hello, server!", "How are you?", "This is another message."]
            
            # Counter for extracted numbers
            extracted_count = 0
            
            for message in messages:
                client_socket.sendall(message.encode())
                # print("Sent message:", message)

                # Receive and process response from the server
                response = client_socket.recv(1024).decode()
                # print("Server response:", response)

                # Extract numbers from the response
                numbers = re.findall(r'Number is : (\d+)', response)
                if numbers:
                    for number in numbers:
                        # print("Extracted number:", number)
                        extracted_numbers.append(number)
                        extracted_count += 1
                        if extracted_count == 3:
                            # print(extracted_numbers)
                            break
                
                if extracted_count == 3:
                    # print(extracted_numbers)
                    break

        except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running.")

        finally:
            # Close the socket
            client_socket.close()
            print(extracted_numbers)
            # print(abs(int(extracted_numbers[0]) - int(extracted_numbers[1]) ), abs(int(extracted_numbers[1]) - int(extracted_numbers[2])))
            extracted_numbers.clear()
