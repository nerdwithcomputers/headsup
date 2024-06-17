from PIL import ImageGrab, Image
import LCD_1inch69
import time
from pynput.mouse import Controller

disp = LCD_1inch69.LCD_1inch69()
mouse = Controller()
mouseim = Image.open('cursor.png')

disp.begin()
disp.bl_DutyCycle(50)
try:
	while True:
		#disp.clear()
		screenimg = ImageGrab.grab()
		screenimg.paste(mouseim, mouse.position, mask=mouseim)
		screenimg = screenimg.resize((280,240))
		disp.ShowImage(screenimg)
		time.sleep(0.01)
except KeyboardInterrupt:
	disp.clear()
