import socket

def send_image(image_path, server_address, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_address, server_port))

        with open(image_path, "rb") as file:
            image_data = file.read()
            client_socket.sendall(image_data)

    print("Image sent successfully!")

def main():
    image_path = "ENCRYPT/rub_enc_img.jpeg"
    server_address = "11.12.111.15"
    server_port = 5555

    send_image(image_path, server_address, server_port)

if __name__ == "__main__":
    main()
