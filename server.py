import socket, json
from datetime import datetime

# ソケットの作成
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバーのIPアドレスとポート番号を指定
host = '0.0.0.0'
port = 3000

# ソケットを指定したIPアドレスとポート番号にバインド
server_socket.bind((host, port))

# クライアントからの接続を待ち続ける
while True:
    # クライアントからの接続を受け付ける
    server_socket.listen(1)
    client_socket, client_address = server_socket.accept()

    if client_address[0] == "192.168.11.100":
        break

    # クライアントからのデータを受信して表示
    datas = client_socket.recv(1024)
    with open(f"/home/user/latest.json", "r") as f:
        data = json.load(f)
        f.close()
    
    json_data = datas.decode()
    dict_data = json.loads(json_data)
    data[client_address[0]] = {
        "data": dict_data,
        "timestamp": datetime.now().timestamp()
    }

    with open(f"/home/user/latest.json", "w") as f:
        json.dump(data, f, indent = 4)
        f.close()
#    print(f'Received from {client_address}: {data.decode()}')

    # ソケットをクローズ
    client_socket.close()
