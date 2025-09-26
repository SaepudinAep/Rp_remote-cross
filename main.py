def bluecontrol():
    if uartData == "A":
        SuperBit.motor_run(SuperBit.enMotors.M1, 255)
        SuperBit.motor_run(SuperBit.enMotors.M3, 255)
    elif uartData == "B":
        SuperBit.motor_run(SuperBit.enMotors.M1, -255)
        SuperBit.motor_run(SuperBit.enMotors.M3, -255)
    elif uartData == "C":
        SuperBit.motor_run(SuperBit.enMotors.M1, 75)
        SuperBit.motor_run(SuperBit.enMotors.M3, 255)
    elif uartData == "D":
        SuperBit.motor_run(SuperBit.enMotors.M1, 255)
        SuperBit.motor_run(SuperBit.enMotors.M3, 75)
    elif uartData == "E":
        SuperBit.motor_run(SuperBit.enMotors.M1, -75)
        SuperBit.motor_run(SuperBit.enMotors.M3, -250)
    elif uartData == "F":
        SuperBit.motor_run(SuperBit.enMotors.M1, -250)
        SuperBit.motor_run(SuperBit.enMotors.M3, -75)
    elif uartData == "0":
        SuperBit.motor_run(SuperBit.enMotors.M1, 0)
        SuperBit.motor_run(SuperBit.enMotors.M3, 0)
def BreathLED():
    SuperBit.RGB_Program().clear()
    for k in range(256):
        SuperBit.RGB_Program().set_brightness(k)
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.RED))
        SuperBit.RGB_Program().show()
    for l in range(256):
        SuperBit.RGB_Program().set_brightness(255 - l)
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.RED))
        SuperBit.RGB_Program().show()

def on_bluetooth_connected():
    global connected, uartData
    basic.show_icon(IconNames.HAPPY)
    connected = 1
    while connected == 1:
        uartData = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
        bluecontrol()
        SevenColorLED()
        music2()
        ModeSelect()
        SevenWaterLED()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_icon(IconNames.SAD)
    connected = 0
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def ModeSelect():
    global g_mode
    if uartData == "S":
        basic.show_icon(IconNames.HOUSE)
        g_mode = 1
    elif uartData == "T":
        basic.show_icon(IconNames.ANGRY)
        g_mode = 2
    elif uartData == "U":
        basic.show_icon(IconNames.EIGHTH_NOTE)
        g_mode = 3
    elif uartData == "V":
        basic.show_icon(IconNames.HAPPY)
        g_mode = 0
def HorseLED():
    SuperBit.RGB_Program().set_brightness(255)
    SuperBit.RGB_Program().set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    SuperBit.RGB_Program().set_pixel_color(1, neopixel.colors(NeoPixelColors.GREEN))
    SuperBit.RGB_Program().set_pixel_color(2, neopixel.colors(NeoPixelColors.BLUE))
    SuperBit.RGB_Program().set_pixel_color(3, neopixel.colors(NeoPixelColors.VIOLET))
    SuperBit.RGB_Program().show()
    basic.pause(100)
    SuperBit.RGB_Program().clear()
    SuperBit.RGB_Program().set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
    SuperBit.RGB_Program().set_pixel_color(1, neopixel.colors(NeoPixelColors.BLUE))
    SuperBit.RGB_Program().set_pixel_color(2, neopixel.colors(NeoPixelColors.VIOLET))
def WaterLED():
    SuperBit.RGB_Program().set_brightness(255)
    SuperBit.RGB_Program().set_pixel_color(0, neopixel.colors(NeoPixelColors.VIOLET))
    SuperBit.RGB_Program().show()
    basic.pause(100)
    SuperBit.RGB_Program().clear()
    SuperBit.RGB_Program().set_pixel_color(1, neopixel.colors(NeoPixelColors.VIOLET))
    SuperBit.RGB_Program().show()
    basic.pause(100)
    SuperBit.RGB_Program().clear()
    SuperBit.RGB_Program().set_pixel_color(2, neopixel.colors(NeoPixelColors.VIOLET))
    SuperBit.RGB_Program().show()
    basic.pause(100)
    SuperBit.RGB_Program().clear()
    SuperBit.RGB_Program().set_pixel_color(3, neopixel.colors(NeoPixelColors.VIOLET))
    SuperBit.RGB_Program().show()
    basic.pause(100)
    SuperBit.RGB_Program().clear()
    SuperBit.RGB_Program().show()
def SevenColorLED():
    if uartData == "G":
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.RED))
        SuperBit.RGB_Program().show()
    elif uartData == "H":
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.GREEN))
        SuperBit.RGB_Program().show()
    elif uartData == "I":
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.BLUE))
        SuperBit.RGB_Program().show()
    elif uartData == "J":
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.YELLOW))
        SuperBit.RGB_Program().show()
    elif uartData == "K":
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.INDIGO))
        SuperBit.RGB_Program().show()
    elif uartData == "L":
        SuperBit.RGB_Program().show_color(neopixel.colors(NeoPixelColors.VIOLET))
        SuperBit.RGB_Program().show()
    elif uartData == "M":
        SuperBit.RGB_Program().clear()
        SuperBit.RGB_Program().show()
def SevenWaterLED():
    global g_RGBMode
    if uartData == "N":
        g_RGBMode = 1
    elif uartData == "P":
        g_RGBMode = 2
    elif uartData == "Q":
        g_RGBMode = 3
    elif uartData == "R":
        g_RGBMode = 4
    elif uartData == "W":
        g_RGBMode = 5
def music2():
    music.set_volume(255)
    if uartData == "1":
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        SuperBit.servo(SuperBit.enServo.S1, 130)
    elif uartData == "2":
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        SuperBit.servo(SuperBit.enServo.S1, 60)
    elif uartData == "3":
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        SuperBit.motor_run(SuperBit.enMotors.M2, 255)
        SuperBit.motor_run(SuperBit.enMotors.M4, 255)
    elif uartData == "4":
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        SuperBit.motor_run(SuperBit.enMotors.M2, 0)
        SuperBit.motor_run(SuperBit.enMotors.M4, 0)
    elif uartData == "5":
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
    elif uartData == "6":
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
    elif uartData == "7":
        music.play_tone(494, music.beat(BeatFraction.WHOLE))
    elif uartData == "8":
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
    elif uartData == "B1":
        music.play_tone(554, music.beat(BeatFraction.WHOLE))
    elif uartData == "B2":
        music.play_tone(622, music.beat(BeatFraction.WHOLE))
    elif uartData == "B3":
        music.play_tone(740, music.beat(BeatFraction.WHOLE))
    elif uartData == "B4":
        music.play_tone(831, music.beat(BeatFraction.WHOLE))
    elif uartData == "B5":
        music.play_tone(932, music.beat(BeatFraction.WHOLE))
    elif uartData == "O":
        music.set_volume(0)
gBlue = 0
g_Green = 0
g_Red = 0
g_mode = 0
uartData = ""
connected = 0
g_RGBMode = 0
m = 0
i = 0
g_RGBMode = 0
connected = 0
SuperBit.servo2(SuperBit.enServo.S1, 105)
bluetooth.start_uart_service()
basic.show_string("S")
music.set_built_in_speaker_enabled(False)

def on_forever():
    global g_Red, g_Green, gBlue, g_RGBMode
    if g_RGBMode == 1:
        SuperBit.RGB_Program().clear()
        WaterLED()
    elif g_RGBMode == 2:
        SuperBit.RGB_Program().clear()
        HorseLED()
    elif g_RGBMode == 3:
        SuperBit.RGB_Program().clear()
        BreathLED()
    elif g_RGBMode == 4:
        SuperBit.RGB_Program().clear()
        SuperBit.RGB_Program().set_brightness(200)
        g_Red = randint(0, 256)
        g_Green = randint(0, 256)
        gBlue = randint(0, 256)
        SuperBit.RGB_Program().show_color(neopixel.rgb(g_Red, g_Green, gBlue))
        SuperBit.RGB_Program().show()
        g_RGBMode = 0
    elif g_RGBMode == 5:
        SuperBit.RGB_Program().clear()
        SuperBit.RGB_Program().show()
    basic.pause(10)
basic.forever(on_forever)

def on_forever2():
    if input.button_is_pressed(Button.A):
        SuperBit.motor_run(SuperBit.enMotors.M2, 255)
    elif input.button_is_pressed(Button.B):
        SuperBit.motor_stop_all()
        pass
basic.forever(on_forever2)
