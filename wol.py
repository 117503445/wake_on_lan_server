from wakeonlan import send_magic_packet
import file_util
import json


def wake_on_lan():
    js = json.loads(file_util.read_all_text('config.json'))
    mac = js['mac']
    broadcast = js['broadcast']
    # print(mac,broadcast)
    send_magic_packet(mac, ip_address=broadcast)



if __name__ == "__main__":
    wake_on_lan()
