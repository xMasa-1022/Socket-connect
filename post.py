#coding=utf-8
import socket, json, time, subprocess, sys, requests

# サーバーのIPアドレスとポート番号を設定
HOST = '192.168.11.100' # Ubuntu ServerのIPアドレスに変更
PORT = 3000
version = "v0.1.1-alpha"

def logo():
    print(f"""
    _____         _       _                               _   
    |   __|___ ___| |_ ___| |_ ___ ___ ___ ___ ___ ___ ___| |_ 
    |__   | . |  _| '_| -_|  _|___|  _| . |   |   | -_|  _|  _|
    |_____|___|___|_,_|___|_|     |___|___|_|_|_|_|___|___|_|  

    {version} | xMasa-1022
""")

def fetch_release():
    print("[?] -> 最新のバージョンを確認しています…")

    try:
        url = "https://api.github.com/repos/xMasa-1022/Socket-connect/releases/latest"
        response = requests.get(url)
        latest_release = response.json()["tag_name"]
        if version != latest_release:
            print(f"[!]   -> {latest_release}が見つかりました！ 更新を行います…")
            assets = response.json()["assets"]
            for item in range(0, len(assets)):
                if assets[item]["name"] != "post.py":
                    pass
                else:
                    try:
                        update_link = assets[item]["browser_download_url"]
                        res = requests.get(update_link)
                        with open(f"post.py", "w", encoding = "utf-8") as f:
                            f.write(res.text)
                            f.close()
                        subprocess.Popen([sys.executable, "post.py"])
                        print("[!]   -> 更新しました。")
                    except:
                        print("[!]   -> 更新できませんでした…")
        else:
            print("[!]   -> 現在最新のバージョンです！")
    except:
        print("[!]   -> 最新バージョンの取得に失敗しました…")

def main():
    print("[!] -> Socket通信を開始します…")
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

        print("[!]   -> 通信に成功しました。 60秒後に再試行します…")

        time.sleep(60)

if __name__ == "__main__":
    logo()
    fetch_release()
    main()
