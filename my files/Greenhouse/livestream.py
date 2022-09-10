import camera
import network
import socket
import machine

uart1 = UART(1, baudrate=9600, tx=33, rx=32)
ssid = 'iotdevlab+virus'
password = 'm,./@1234'

print("ssid: ", ssid)

camera.init(0, format=camera.JPEG)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)
print(sta_if.ifconfig())

def take_photo():
    print("Taking Picture")
    camera.framesize(camera.FRAME_240X240)
    buf=camera.capture()
    f = open('image.jpg','w')
    f.write(buf)
    f.close()
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80))


while True:
    take_photo()
    
    s.listen(80)
    conn, addr = s.accept()
    print("got connection from %s" % str(addr))
    
    request = conn.recv(1024)
    request = str(request)
    string_list = request.split(' ')
    method = string_list[0]
    requesting_file = string_list[1]
    
    print("client request ", requesting_file)
    
    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')
    
    if (myfile == ''):
        myfile == 'index.html'
    try:
        file = open(myfile, 'rb')
        response = file.read()
        file.close()
        
        header = 'HTTP/1.1 200 OK\n'
        if (myfile.endswith(".jpg")):
            mimetype = 'image/jpg'
        elif (myfile.endswith(".css")):
            mimetype = 'text/css'
        else:
            mimetype = 'text/html'
        header += "Content-Type: " + str(mimetype) + '\n\n'
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: file not found</h3></center></body></html>'
        
    final_response = header.encode('utf-8')
    final_response += response
    try:
        conn.send(final_response)
    except:
        print("there was an error, Resetting")
    conn.close()