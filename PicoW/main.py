import socket
import network
import urequests
from machine import Pin, UART

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
uart.init(bits=8, parity=None, stop=2)

page = open("index.html", "r")
html = page.read()
page.close()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('lab-pm','microweb')
sta_if = network.WLAN(network.STA_IF)
print(sta_if.ifconfig()[0])
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
while True:
    cl, addr = s.accept()
    cl_file = cl.makefile('rwb', 0)
    response = html
    res = None
    while True:
        res = str(cl.recv(1024))
        if res:
            #print(res)
            break
    command = res.split(" ")[1]
    if command != '/':
        if command[1] == '?':
            command = command[2:]
            command = command.split("=")[1]
            print(command)
            uart.write(command)
   
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()
