#SMpixel - control LED RGB cu Terminal BT
# 
# PICO UART1 : Tx=pin6, RX=pin 7
# Testul se face cu un telefon mobil cu aplicatie
# tip Terminal.
# 
# cu 1 -LED aprins
# cu 0 -LED stins
from machine import UART, Pin
import time

red = Pin(18, Pin.OUT)        # LED rosu
green = Pin(19, Pin.OUT)      # LED verde
blue = Pin(20, Pin.OUT)       # LED blue

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
uart.init(bits=8, parity=None, stop=2)

ser = UART(1, 9600)           # tx=6   rx=7 GND=8
red.low()                     # stare initiala
green.low()
blue.low()

while 1:
    c=ser.read(1)         # lectura din UART 1
    data = uart.read() 
        
    if(str(c) != 'None'):
        ser.write(str(c))         # ecou
        print(data)

    if c == b'1' or data==b'Rosu':
        red.high()    # rosu aprins
        green.low()
        blue.low()
        #time.sleep(0.3)
    if c == b'2' or data==b'Verde':
        green.high()  # verde aprins
        red.low()
        blue.low()
        #time.sleep(0.3)
    if c == b'3' or data==b'Albastru':
        blue.high()   # albastru aprins
        red.low()
        green.low()
    if c == b'0' or data==b'Stins':         # sting
        red.low()
        green.low()
        blue.low()

