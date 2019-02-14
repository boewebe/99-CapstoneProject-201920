import rosebot
import time


# Feature 9: Prox Sensor with increasing frequency

def run_test_object_pick_up_with_frequency(initial_frequency, rate):

    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    speed = 50
    robot.drive_system.go(speed, speed)
    max_freq = (initial_frequency + 19 * rate) * 2
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.tone_maker.play_tone(max_freq - 2 * d * rate, 10)
        print(max_freq - d * rate)
        time.sleep(0.2)
        if d <= 2:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()