# Complete project details at https://RandomNerdTutorials.com
import json


def web_page():
    #     # if led.value() == 1:
    #     #     gpio_state = "ON"
    #     # else:
    #     #     gpio_state = "OFF"
    plant01_value = plant01.read()
    plant01_value_string = str(plant01_value)

    #
    # #     file = open('body.html', 'r')
    # #     newhtml = file.read()
    # #     file.close()
    #
    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}.button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1><p>Plant01 Level: <strong>""" + plant01_value_string + """</strong></p><p></body></html>"""
    return html


def soil_json():
    plant01_value = plant01.read()
    plant01_value_string = str(plant01_value)
    the_data = {"plant01":plant01_value}
    the_json = json.dumps(the_data)
    #the_json_string = str(the_json)
    return the_json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    # led_on = request.find('/?led=on')
    # led_off = request.find('/?led=off')
    # if led_on == 6:
    #     print('LED ON')
    #     led.value(1)
    # if led_off == 6:
    #     print('LED OFF')
    #     led.value(0)

    response = soil_json()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
