import board, adafruit_dht, os, requests, time
from http.client import responses


dhtDevice = adafruit_dht.DHT22(board.D18)
send_URL = 'https://api.thingspeak.com/update?'
send_key = os.environ['SENDKEY']

def sensor_data():
    data = [None, None, None]
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        data = [temperature_c, temperature_f, humidity]

    except RuntimeError as error:
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
        final_url += '&field' + str(count) + '=' + str(field)
        count += 1
    return final_url


if __name__ == '__main__':
    try:
        while True:
            data = sensor_data()
            print(f'Data from Sensor: temp_c = {data[0]}, temp_f = {data[1]}, humidity = {data[2]}')
            url = genrate_url(send_key, data, send_URL)
            connection = requests.get(url)
            print('Attempting to send Data')
            status_code = connection.status_code
            print(f'Response Code : {status_code} {responses[status_code]}')
            connection.close()
            time.sleep(5)
    except KeyboardInterrupt:
        print('Closed by User')
    except Exception as e:
        print(e)