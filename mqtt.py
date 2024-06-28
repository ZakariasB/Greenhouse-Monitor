from mqtt_client import MQTTClient
import keys

client = None

def connect():
    global client
    client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, port=keys.AIO_PORT, user=keys.AIO_USER, password=keys.AIO_KEY)
    client.connect()
    print('Connected to Adafruit IO!')

def publish(feed, message):
    global client
    client.publish(feed, message)
    print(f'Sent {message} to {feed}')


def disconnect():
    global client
    if client is not None:
        client.disconnect()
        client = None
        print("Disconnected from Adafruit IO.")