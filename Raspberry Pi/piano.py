import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Buttons channel dictonary define, key is channel, value is pitch

buttons = {
	11 : 1,
	12 : 2,
	13 : 3,
	14 : 4,
	15 : 5,
	16 : 6,
	17 : 7	
}

up_button = 24

# Setup buttons(Piano keys)

for x in buttons.keys():
	GPIO.setup(x, GPIO.IN, GPIO.PUD_UP)
	GPIO.add_event_detect(x, GPIO.RISING, callback=playOnce, bouncetime=200)

GPIO.setup(up_button, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(up_button, GPIO.RISING, callback=upTune, bouncetime=200)

# Buzzer channel define

buzzer = 22

# Setup PWM for Buzzer

GPIO.setup(buzzer, GPIO.OUT)
buzz_PWM = GPIO.PWM(buzzer, 0.001) # Zero frequency for default

# Music tune define

# Tune list from A-G mark to 1-7 pitch
tuneList = np.array([[
	441,495,556,589,661,742,833],
   [495,556,624,661,742,833,935],
   [262,294,330,350,393,441,495],
   [294,330,350,393,441,495,556],
   [330,350,393,441,495,556,624],
   [350,393,441,495,556,624,661],
   [393,441,495,556,624,661,742]])

tune1 = [262,294,330,349,392,440,494,523, 587, 659,698,784,880,988,1047]

# Other param

current_mark = 3 # Default C-mark
duration = 0.2 # Sound duration

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

def playOnce(channel):
	pitch = buttons[channel]
	tune = node(current_mark, pitch)
	buzz(tune, duration)
	time.sleep(duration *0.5)
	buzz(tune, duration)
	time.sleep(duration *0.5)

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
		return # check for mark and pitch input

	return tuneList[mark, pitch]

def upTune(channel):
	current_mark = current_mark > 6 ? 1 : current_mark + 1

def downTune(channel):
	current_mark = current_mark < 2 ? 7 : current_mark - 1

def main():
	try:
		while True:
			
	except KeyboardInterrupt:
		stop()

main()