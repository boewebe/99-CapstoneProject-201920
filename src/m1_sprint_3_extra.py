
import rosebot
import time



## Sprint 3 Functions

def G4_note():
    robot = rosebot.RoseBot()
    print("G4")
    robot.sound_system.tone_maker.play_tone(392, 250).wait()

def A4_note():
    robot = rosebot.RoseBot()
    print("A4")
    robot.sound_system.tone_maker.play_tone(440, 250).wait()

def B4_note():
    robot = rosebot.RoseBot()
    print("B4")
    robot.sound_system.tone_maker.play_tone(493.88, 250).wait()

def C5_note():
    robot = rosebot.RoseBot()
    print("C5")
    robot.sound_system.tone_maker.play_tone(523.25, 250).wait()

def C5_sharp_note():
    robot = rosebot.RoseBot()
    print("C#5")
    robot.sound_system.tone_maker.play_tone(554.37, 250).wait()

def D5_note():
    robot = rosebot.RoseBot()
    print("D5")
    robot.sound_system.tone_maker.play_tone(587.33, 250).wait()

def E5_note():
    robot = rosebot.RoseBot()
    print("E5")
    robot.sound_system.tone_maker.play_tone(659.25, 250).wait()

def F5_sharp_note():
    robot = rosebot.RoseBot()
    print("F#5")
    robot.sound_system.tone_maker.play_tone(739.99, 250).wait()

def G5_note():
    robot = rosebot.RoseBot()
    print("G5")
    robot.sound_system.tone_maker.play_tone(783.99, 250).wait()

def A5_note():
    robot = rosebot.RoseBot()
    print("A5")
    robot.sound_system.tone_maker.play_tone(880, 250).wait()



def find_object():
    robot = rosebot.RoseBot()
    print("Find and Pick Up Object")
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 4:
            break
        robot.sound_system.tone_maker.play_tone(220, 500).wait()
        time.sleep(1)

    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    A4_note()
    C5_sharp_note()
    E5_note()
    A5_note()

def color_sensor_play_note(time_to_stop):
    robot = rosebot.RoseBot()
    print("Hello")
    print("Play Note Based on Color")
    initial_time = time.time()
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Red':
            print("Red")
            robot.drive_system.stop()
            A4_note()
            break
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Green':
            print("Green")
            robot.drive_system.stop()
            B4_note()
            break
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Yellow':
            print("Yellow")
            robot.drive_system.stop()
            C5_note()
            break
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Black':
            print("Black")
            robot.drive_system.stop()
            C5_sharp_note()
            break
        if time.time() - initial_time >= time_to_stop:
            print("I did not find any color")
            robot.drive_system.stop()
            robot.sound_system.speech_maker.speak("I did not find any color")
            break


def color_sensor_play_tune(time_to_stop):
    robot = rosebot.RoseBot()
    print("Play Tune Based on Color")
    initial_time = time.time()
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Red':
            print("Red")
            robot.drive_system.stop()
            A4_note()
            B4_note()
            C5_sharp_note()
            D5_note()
            E5_note()
            break
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Green':
            print("Green")
            robot.drive_system.stop()
            A4_note()
            A4_note()
            E5_note()
            E5_note()
            F5_sharp_note()
            F5_sharp_note()
            E5_note()
            break
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Yellow':
            print("Yellow")
            robot.drive_system.stop()
            G4_note()
            B4_note()
            D5_note()
            B4_note()
            G4_note()
            break
        if robot.sensor_system.color_sensor.get_color_as_name() == 'Black':
            print("Black")
            robot.drive_system.stop()
            G4_note()
            B4_note()
            D5_note()
            G5_note()
            G5_note()
            D5_note()
            B4_note()
            G4_note()
            break
        if time.time() - initial_time >= time_to_stop:
            print("I did not find any color")
            robot.drive_system.stop()
            robot.sound_system.speech_maker.speak("I did not find any color")
            break
