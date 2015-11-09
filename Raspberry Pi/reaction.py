import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red_led = 17 # LED is in GPIO 4
yellow_led = 27 # Yello LED is in GPIO 27
green_led = 22 # Green LED is in GPIO 22

red_button = 14 # Red Button is in GPIO 14
yellow_button = 15 # Yellow Button is in GPIO 15
green_button = 23 # Green Button is in GPIO 23

rgb_red = 10 # RGB LED red in GPIO 10
rgb_green = 9 # RGB LED green in GPIO 9
rgb_blue = 11 # RGB LED blue in GPIO 11

buzzer = 24 # Buzzer in GPIO 24

# Setup GPIO OUT for LEDs
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

# Setup GPIO IN & PUD_UP for Buttons

GPIO.setup(red_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(yellow_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(green_button, GPIO.IN, GPIO.PUD_UP)

# Setup GPIO for RGB LED

GPIO.setup(rgb_red, GPIO.OUT)
GPIO.setup(rgb_green, GPIO.OUT)
GPIO.setup(rgb_blue, GPIO.OUT)

# Setup PWM for RGB LED, Frequency is 200Hz

red_PWM = GPIO.PWM(rgb_red, 200) 
green_PWM = GPIO.PWM(rgb_green, 200)
blue_PWM = GPIO.PWM(rgb_blue, 200)

# Setup PWM for Buzzer

GPIO.setup(buzzer, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
buzz_PWM = GPIO.PWM(buzzer, 0.001) # Zero frequency for default

# Music tune define

# Tune list for playing

tune1 = [262,294,330,349,392,440,494,523, 587, 659,698,784,880,988,1047]

# Other param

current_mark = 3 # Default C-mark

duration = 0.1 # Sound duration


def led_on(led):
	GPIO.output(led, 1)

def led_off(led):
	GPIO.output(led, 0)

def led_reverse(led):
	if GPIO.input(led) == 1:
		GPIO.output(led, 0)
	else:
		GPIO.output(led, 1)

def red_reverse(channel):
	led_reverse(red_led)

def yellow_reverse(channel):
	led_reverse(yellow_led)

def green_reverse(channel):
	led_reverse(green_led)

# Detects rising edge on button. ignores multiple rising edges in 200ms
GPIO.add_event_detect(red_button, GPIO.RISING, callback=red_reverse, bouncetime=200)
GPIO.add_event_detect(yellow_button, GPIO.RISING, callback=yellow_reverse, bouncetime=200)
GPIO.add_event_detect(green_button, GPIO.RISING, callback=green_reverse, bouncetime=200)

def btn_click(btn):
	if GPIO.input(btn) == False:
		return True
	else:
		return False

def flash(r,y,g,n):
	for i in xrange(0,n):
		print "3"
		led_on(red_led)
		time.sleep(r) # Red time
		led_off(red_led)
		print "2"
		led_on(yellow_led)
		time.sleep(y) # Yellow time
		led_off(yellow_led)
		print "1"
		led_on(green_led)
		time.sleep(g) # Green time
		led_off(green_led)

def setRGB(r, g, b):
	r_v = r / 2.55
	g_v = g / 2.55
	b_v = b / 2.55
	red_PWM.ChangeDutyCycle(r_v)
	green_PWM.ChangeDutyCycle(g_v)
	blue_PWM.ChangeDutyCycle(b_v)

def gradient(t):
	for (x,y) in zip(xrange(1,255), xrange(255,1,-1)):
		setRGB(y, x, 0) # red -> green
		time.sleep(t)
	for (x,y) in zip(xrange(1,255), xrange(255,1,-1)):
		setRGB(0, y, x) # green -> blue
		time.sleep(t)
	for (x,y) in zip(xrange(1,255), xrange(255,1,-1)):
		setRGB(x, 0, y) # blue -> red
		time.sleep(t)

def buzz(pitch, duration):
	if(pitch==0):
		time.sleep(duration)
		return
	period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
	delay = period / 2     #calcuate the time for half of the wave  
	cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency
	for i in xrange(cycles):
		GPIO.output(buzzer, 1)
		time.sleep(delay)
		GPIO.output(buzzer, 0)
		time.sleep(delay)

def play(tune):
	for p in tune:
		buzz(p, duration)  #feed the pitch and duration to the function, "buzz"
		time.sleep(duration *0.5)
	for p in reversed(tune):
		buzz(p, duration)
		time.sleep(duration *0.5)

# Define the music note, with mark(A to 1,B to 2...) and pitch (1-7) 
def note(mark, pitch):
	if (mark > 0 & mark < 8 & pitch > 0 & pitch < 8):
		mark-=1
		pitch-=1
	else:
		return 0 # check for mark and pitch input

	return tuneList[mark, pitch]

def upTune():
	current_mark = current_mark > 6 ? 1 : current_mark + 1

def downTune():
	current_mark = current_mark < 2 ? 7 : current_mark - 1


def start():
	print "Let's begin! Count 3 seconds..."
	flash(1,1,1,1) # flash red-yellow-blue LED
	red_PWM.start(0)
	green_PWM.start(0)
	buzz_PWM.start(50)
	print "Start ! Click button and play"

def stop():
	red_PWM.stop()
	green_PWM.stop()
	blue_PWM.stop()
	print "Stop"
	GPIO.cleanup()

def main():
	try:
		start()
		while True:
			gradient(0.005)
			play(tune1)
	except KeyboardInterrupt:
		stop()

main()