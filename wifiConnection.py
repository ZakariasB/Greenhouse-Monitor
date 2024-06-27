import network
from time import sleep
import keys

def connect():
    wlan = network.WLAN(network.STA_IF)  # Put modem on Station mode
    if not wlan.isconnected():  # Check if already connected
        print('Connecting to network...')
        wlan.active(True)  # Activate network interface
        wlan.config(pm=0xa11140)  # Optional: disable power-saving mode
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Connect to the WiFi network
        print('Waiting for connection...', end='')
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'\nConnected on {ip}')
    return ip

def disconnect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    wlan.disconnect()
    wlan = None