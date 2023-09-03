import socket

port_list = []
banner_list = []
formatted_banners = []

ip_list = ["***.***.*.***"]
for ip in ip_list:
    for port in range(1, 26):  # Iterate through ports 1 to 26
        try:
            soket = socket.socket()
            soket.connect((ip, port))
            print("[+]Port:", port)
            print("[+]IP:", ip)
            banner = soket.recv(1024)
            banner_list.append(banner)
            port_list.append(port)
            soket.close()
            print("=" * 10)
            if "SSH" in str(banner):
                print("Sistem Linux veya network cihazı olabilir")
                log = str(ip)
                file = open("linux.txt", "w")
                file.write(log)
                file.close()
            banner_file = (
                str(banner).replace(" ", "_").replace("\n", "").replace("b'", "")
                + ".txt"
            )

            log = str(ip) + "\n"
            file = open(banner_file, "w")
            file.write(log)
            file.close()
        except:
            pass
for banner in banner_list:
    try:
        decoded_banner = banner.decode("utf-8")
    except UnicodeDecodeError:
        pass
    formatted_banner = decoded_banner.strip()
    formatted_banners.append(formatted_banner)
for banner in formatted_banners:
    print(banner)
print(port_list)
