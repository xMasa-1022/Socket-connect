import socket, json, time, subprocess

# サーバーのIPアドレスとポート番号を設定
HOST = '192.168.11.100' # Ubuntu ServerのIPアドレスに変更
PORT = 3000

while True:
    # ソケットを作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 辞書型のデータを作成する
        data = {'power': 'ON'}

        # JSON形式に変換する
        json_data = json.dumps(data)

        # ソケット通信でデータを送信する
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.sendall(json_data.encode())

    time.sleep(60)
