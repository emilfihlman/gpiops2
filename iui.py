# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO, sys, signal, time, uinput

clkp=38
dtap=40
bits=[0,0,0,0,0,0,0,0,0,0,0]
i=0
d={162:'0', 104:'1', 120:'2', 100:'3', 164:'4', 116:'5', 108:'6', 188:'7', 124:'8', 98:'9', 56:'a', 76:'b', 132:'c', 196:'d', 36:'e', 212:'f', 44:'g', 204:'h', 194:'i', 220:'j', 66:'k', 210:'l', 92:'m', 140:'n', 34:'o', 178:'p', 168:'q', 180:'r', 216:'s', 52:'t', 60:'u', 84:'v', 184:'w', 68:'x', 172:'y', 88:'z', 112:'`', 50:';', 74:'´', 42:'[', 218:']', 130:',', 146:'.', 186:'\\', 82:'/', 114:'-', 170:'=', 90:'\n', 148:' ', 176:'\t', 174:'\033[1A', 78:'\033[1B', 46:'\033[1C', 214:'\033[1D', 102:'\b \b'}

def signal_handler(signal, frame):
	print ""
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clkp, GPIO.IN)
GPIO.setup(dtap, GPIO.IN)
clk = lambda: GPIO.input(clkp)
dta = lambda: GPIO.input(dtap)

def printer():
	global bits
	if sum(bits[1:9])%2==1 and bits[9]==1 or sum(bits[1:9])%2==0 and bits[9]==0:
		print "Parity error"
	elif bits[1:9]!=[0,0,1,1,1,0,0,0]:
		print "Not a"
	else:
		print ''.join(map(str, bits[1:9]))
	

def sampler(clkp):
	global bits, i
	bits[i]=dta()
	i+=1
	if i>10:
		i=0
		printer()

#def sampler(clkp):
#	o=dta()
#	global timeout
#	global i
#	global c
#	if time.time()>timeout and i>0:
#		sys.stdout.write("Timed out\n")
#		c=0
#		i=0
#	else:
#		timeout = time.time()+0.01
#		c<<=1
#		c+=o
#		i+=1
#		if i>10:
#			#sys.stdout.write(bin((c>>2)&255)+"\n")
#			sys.stdout.write(format((c>>2)&255, '08b')+"\n")
#			sys.stdout.flush()
#			c=0
#			i=0
#			#if l!=15 and c in d:
#			#	sys.stdout.write(d[c])
#			#	sys.stdout.flush()
#			#l=c

GPIO.add_event_detect(clkp, GPIO.RISING, callback=sampler)

print "ps2keyboard test by Emil"

while True:
	time.sleep(0.5)
