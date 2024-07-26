# OLED message generator code:-
records_char=[]
import machine
import time
from machine import Pin, I2C
import ssd1306
led = machine.Pin(2,machine.Pin.OUT)
led.off()
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# ************************
# Configure the ESP32 wifi
# as STAtion mode.

import network
#import wifi_credentials

sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    sta.connect('Dd13', '1234abcd')
    #sta.connect(wifi_credentials.ssid, wifi_credentials.password)
    while not sta.isconnected():
        pass
print('network config:', sta.ifconfig())

# ************************
# Configure the socket connection
# over TCP/IP
import socket

# AF_INET - use Internet Protocol v4 addresses
# SOCK_STREAM means that it is a TCP socket.
# SOCK_DGRAM means that it is a UDP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80)) # specifies that the socket is reachable 
#                 by any address the machine happens to have
s.listen(5)     # max of 5 socket connections

# ************************
# Function for creating the
# web page to be displayed

def prc(char,x,y,clr=1):
    oled.text(char,x,y,clr)
    oled.show()


def web_page():
    '''if led.value()==1:
        led_state = 'ON'
        oled.fill(0)
        oled.show()
        oled.text('XYZ',0,0)
        oled.show()
        #print('led is ON')
    elif led.value()==0:
        led_state = 'OFF'
        oled.fill(0)
        oled.show()
        oled.text('A',0,0)
        oled.show()
        #print('led is OFF')
        '''

    html_page = """
<!DOCTYPE html>
<html>   
      <head>   
       <meta content="width=device-width, initial-scale=1" name="viewport"></meta>   
      </head>   
      <body>   
        <center><h2>ESP32 Message Generator using Wifi Module in Micropython</h2></center>   
        <center>
        <form>
         <div class="num">
          <button name="LED" type="submit" value="0">0</button>
          <button name="LED" type="submit" value="1">1</button>
          <button name="LED" type="submit" value="2">2</button>
          <button name="LED" type="submit" value="3">3</button>
          <button name="LED" type="submit" value="4">4</button>
          <button name="LED" type="submit" value="5">5</button>
          <button name="LED" type="submit" value="6">6</button>
          <button name="LED" type="submit" value="7">7</button>
          <button name="LED" type="submit" value="8">8</button>
          <button name="LED" type="submit" value="9">9</button>
          <button name="LED" type="submit" value=".">.</button>
         </div>
         <div class="line1">  
          <button name="LED" type="submit" value="Q">Q</button>
          <button name="LED" type="submit" value="W">W</button>
          <button name="LED" type="submit" value="E">E</button>
          <button name="LED" type="submit" value="R">R</button>
          <button name="LED" type="submit" value="T">T</button>
          <button name="LED" type="submit" value="Y">Y</button>
          <button name="LED" type="submit" value="U">U</button>
          <button name="LED" type="submit" value="I">I</button>
          <button name="LED" type="submit" value="O">O</button>
          <button name="LED" type="submit" value="P">P</button>
          <button name="LED" type="submit" value="-">CLR</button>
         </div> 
         <div class="line2">  
          <button name="LED" type="submit" value="A">A</button>
          <button name="LED" type="submit" value="S">S</button>
          <button name="LED" type="submit" value="D">D</button>
          <button name="LED" type="submit" value="F">F</button>
          <button name="LED" type="submit" value="G">G</button>
          <button name="LED" type="submit" value="H">H</button>
          <button name="LED" type="submit" value="J">J</button>
          <button name="LED" type="submit" value="K">K</button>
          <button name="LED" type="submit" value="L">L</button>
          <button name="LED" type="submit" value="*">ENTER</button>
          <button name="LED" type="submit" value="/"> BKC</button>
         </div> 
         <div class="line3">  
          <button name="LED" type="submit" value="Z">Z</button>
          <button name="LED" type="submit" value="X">X</button>
          <button name="LED" type="submit" value="C">C</button>
          <button name="LED" type="submit" value="V">V</button>
          <button name="LED" type="submit" value="B">B</button>
          <button name="LED" type="submit" value="N">N</button>
          <button name="LED" type="submit" value="M">M</button>
          <button name="LED" type="submit" value="_">SPACE</button>
         </div>
         </form>
        </center>   
        <center><p>LED is now <strong>""" + "led_state" + """</strong>.</p></center>   
      </body>   
      </html>
"""
        
    return html_page   


x=0
y=0
prc('WELCOME USER',5,5)
# prc('WELCOME USER',5,5)
time.sleep(2)
oled.fill(0)
oled.show()


while True:
        if x>=127:
            y+=11
            x=0
 # Socket accept() 
        conn, addr = s.accept()
        print("Got connection from %s" % str(addr))

        # Socket receive()
        request=conn.recv(1024)
        print("")
        print("")
        print("Content %s" % str(request))

        # Socket send()
        request = str(request)

        #char=input("Next character: ")
        # char=getch()
        #response = web_page()
        
        
        button_respA = request.find("/?LED=A")
        button_respB = request.find("/?LED=B")
        button_respC = request.find("/?LED=C")
        button_respD = request.find("/?LED=D")
        button_respE = request.find("/?LED=E")
        button_respF = request.find("/?LED=F")
        button_respG = request.find("/?LED=G")
        button_respH = request.find("/?LED=H")
        button_respI = request.find("/?LED=I")
        button_respJ = request.find("/?LED=J")
        button_respK = request.find("/?LED=K")
        button_respL = request.find("/?LED=L")
        button_respM = request.find("/?LED=M")
        button_respN = request.find("/?LED=N")
        button_respO = request.find("/?LED=O")
        button_respP = request.find("/?LED=P")
        button_respQ = request.find("/?LED=Q")
        button_respR = request.find("/?LED=R")
        button_respS = request.find("/?LED=S")
        button_respT = request.find("/?LED=T")
        button_respU = request.find("/?LED=U")
        button_respV = request.find("/?LED=V")
        button_respW = request.find("/?LED=W")
        button_respX = request.find("/?LED=X")
        button_respY = request.find("/?LED=Y")
        button_respZ = request.find("/?LED=Z")
        button_resp0 = request.find("/?LED=0")
        button_resp1 = request.find("/?LED=1")
        button_resp2 = request.find("/?LED=2")
        button_resp3 = request.find("/?LED=3")
        button_resp4 = request.find("/?LED=4")
        button_resp5 = request.find("/?LED=5")
        button_resp6 = request.find("/?LED=6")
        button_resp7 = request.find("/?LED=7")
        button_resp8 = request.find("/?LED=8")
        button_resp9 = request.find("/?LED=9")
        button_dot = request.find("/?LED=.")
        button_clr = request.find("/?LED=-")
        button_bkc = request.find("/?LED=/")
        button_ent = request.find("/?LED=*")
        button_spc = request.find("/?LED=_")

        if button_respA == 6:
                prc('A',x,y)
                x+=9
                records_char.append('A')

        elif button_respB == 6:
                prc('B',x,y)
                x+=9
                records_char.append('B')

        elif button_respC == 6:
                prc('C',x,y)
                x+=9
                records_char.append('C')

        elif button_respD == 6:
                prc('D',x,y)
                x+=9
                records_char.append('D')

        elif button_respE == 6:
                prc('E',x,y)
                x+=9
                records_char.append('E')

        elif button_respF == 6:
                prc('F',x,y)
                x+=9
                records_char.append('F')

        elif button_respG == 6:
                prc('G',x,y)
                x+=9
                records_char.append('G')

        elif button_respH == 6:
                prc('H',x,y)
                x+=9
                records_char.append('H')

        elif button_respI == 6:
                prc('I',x,y)
                x+=9
                records_char.append('I')

        elif button_respJ == 6:
                prc('J',x,y)
                x+=9
                records_char.append('J')

        elif button_respK == 6:
                prc('K',x,y)
                x+=9
                records_char.append('K')

        elif button_respL == 6:
                prc('L',x,y)
                x+=9
                records_char.append('L')

        elif button_respM == 6:
                prc('M',x,y)
                x+=9
                records_char.append('M')

        elif button_respN == 6:
                prc('N',x,y)
                x+=9
                records_char.append('N')

        elif button_respO == 6:
                prc('O',x,y)
                x+=9
                records_char.append('O')

        elif button_respP == 6:
                prc('P',x,y)
                x+=9
                records_char.append('P')

        elif button_respQ == 6:
                prc('Q',x,y)
                x+=9
                records_char.append('Q')

        elif button_respR == 6:
                prc('R',x,y)
                x+=9
                records_char.append('R')

        elif button_respS == 6:
                prc('S',x,y)
                x+=9
                records_char.append('S')

        elif button_respT == 6:
                prc('T',x,y)
                x+=9
                records_char.append('T')

        elif button_respU == 6:
                prc('U',x,y)
                x+=9
                records_char.append('U')

        elif button_respV == 6:
                prc('V',x,y)
                x+=9
                records_char.append('V')

        elif button_respW == 6:
                prc('W',x,y)
                x+=9
                records_char.append('W')

        elif button_respX == 6:
                prc('X',x,y)
                x+=9
                records_char.append('X')

        elif button_respY == 6:
                prc('Y',x,y)
                x+=9
                records_char.append('Y')

        elif button_respZ == 6:
                prc('Z',x,y)
                x+=9
                records_char.append('Z')

        elif button_resp0 == 6:
                prc('0',x,y)
                x+=9
                records_char.append('0')

        elif button_resp1 == 6:
                prc('1',x,y)
                x+=9
                records_char.append('1')

        elif button_resp2 == 6:
                prc('2',x,y)
                x+=9
                records_char.append('2')

        elif button_resp3 == 6:
                prc('3',x,y)
                x+=9
                records_char.append('3')

        elif button_resp4 == 6:
                prc('4',x,y)
                x+=9
                records_char.append('4')

        elif button_resp5 == 6:
                prc('5',x,y)
                x+=9
                records_char.append('5')

        elif button_resp6 == 6:
                prc('6',x,y)
                x+=9
                records_char.append('6')

        elif button_resp7 == 6:
                prc('7',x,y)
                x+=9
                records_char.append('7')

        elif button_resp8 == 6:
                prc('8',x,y)
                x+=9
                records_char.append('8')

        elif button_resp9 == 6:
                prc('9',x,y)
                x+=9
                records_char.append('9')

        elif button_dot == 6:
                prc('.',x,y)
                x+=9
                records_char.append('.')

        elif button_bkc == 6:
            x-=9
            prc(records_char[len(records_char)-1],x,y,0)
            e=records_char.pop()
            
        elif button_clr == 6:
            oled.fill(0)
            oled.show()
            x=0
            y=0
            
        elif button_ent == 6:
                #if char=='ent':
                # char='\n'
                y+=11
                x=0
                continue
            
        elif button_spc == 6:
                #prc('_',x,y)
                x+=7
                
            
        response=web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        
        # Socket close()
        conn.close()
