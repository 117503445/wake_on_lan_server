from wakeonlan import send_magic_packet
import file_util
import json


def wake_on_lan():
    js = file_util.read_all_text('config.json')
    js = json.loads(js)
    mac = js['mac']
    broadcast = js['broadcast']
    print(mac, broadcast)
    send_magic_packet(mac, ip_address=broadcast)
    send_magic_packet('2c:f0:5D:21:54:1e', ip_address='192.168.31.255')



if __name__ == "__main__":
    wake_on_lan()
