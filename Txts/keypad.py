import digitalio
import usb_hid
import board
import time

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

LED = digitalio.DigitalInOut(board.LED)
LED.direction = digitalio.Direction.OUTPUT
LED.value = False

Button1 = digitalio.DigitalInOut(board.GP15)
Button1.switch_to_input(pull=digitalio.Pull.UP)

Button2 = digitalio.DigitalInOut(board.GP13)
Button2.switch_to_input(pull=digitalio.Pull.UP)

Keypad = Keyboard(usb_hid.devices)
Layout = KeyboardLayoutUS(Keypad)

Pressed1 = False
Pressed2 = False

while True:
    LED.value = not Button1.value
    # Button 1
    if Button1.value == False and not Pressed1:
        Pressed1 = True
        Keypad.press(Keycode.S)
    elif Button1.value == True and Pressed1:
        Pressed1 = False
        Keypad.release(Keycode.S)

    # Button 2
    if Button2.value == False and not Pressed2:
        Pressed2 = True
        Keypad.press(Keycode.D)
    elif Button2.value == True and Pressed2:
        Pressed2 = False
        Keypad.release(Keycode.D)
