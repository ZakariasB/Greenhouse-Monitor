import ubinascii
import machine

# Wireless network
WIFI_SSID = "Your_WiFi_Name"
WIFI_PASS = "Your_WiFi_Password"

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "Your_Adafruit_User_Name"
AIO_KEY = "Your_Adafruit_Application_Key"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()  # Can be anything
AIO_FEED_TEMPERATURE = "Your_Adafruit_User_Name/feeds/temperature"
AIO_FEED_KNOCK = "Your_Adafruit_User_Name/feeds/knock"