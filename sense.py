import board, adafruit_dht, os, requests, time

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D18)
send_URL = 'https://api.thingspeak.com/update?'
send_key = os.environ['SENDKEY']

def sensor_data():
    data = [0, 0, 0]
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        data = [temperature_c, temperature_f, humidity]

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        return data

    except Exception as error:
        dhtDevice.exit()
        return data
        raise error
        

    return data

def genrate_url(key, data, url):
    final_url = url + 'api_key=' + key
    count = 1
    for field in data:
        final_url += '&field' + count + '=' + data
        count += 1
    return final_url


if __name__ == '__main__':
    try:
        while True:
            data = sensor_data()
            print(data)
            url = genrate_url(send_key, data, send_URL)
            print(url)
            connection = requests.get(url)
            print(connection.status_code)
            connection.close()
            time.sleep(2)
    except KeyboardInterrupt:
        print('Closed by User')
    except Exception as e:
        print(e)


    