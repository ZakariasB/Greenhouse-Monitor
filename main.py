import wifiConnection
import mqtt
import machine
import time
import keys

# MCP9700 setup
adc = machine.ADC(26)  # Analog pin for MCP9700
scale_factor = 3.3 / 65535  # Scale factor for 16-bit ADC

# Knock sensor setup
knock_sensor = machine.Pin(27, machine.Pin.IN)

def read_temperature():
    adc_value = adc.read_u16()
    voltage = adc_value * scale_factor
    temperature_c = (voltage - 0.5) * 100
    return temperature_c

def read_knock():
    return not knock_sensor.value()  # Inverted logic for pull-up

def main():
    wifiConnection.connect()
    mqtt.connect()

    while True:
        temperature = read_temperature()
        mqtt.publish(keys.AIO_FEED_TEMPERATURE, str(temperature))

        knock = read_knock()
        mqtt.publish(keys.AIO_FEED_KNOCK, '1' if knock else '0')

        time.sleep(60)  # Adjust the interval as needed

if __name__ == '__main__':
    main()
