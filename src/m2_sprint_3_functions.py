import rosebot
import time

def test_scramble():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.spin_clockwise_until_sees_object(50, 15)
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
    robot.drive_system.go_straight_until_color_is('Blue', -50)
    robot.drive_system.spin_clockwise_until_sees_object(50, 10)
    robot.drive_system.go_straight_until_color_is('Black', 50)
    robot.drive_system.spin_clockwise_until_sees_object(50, 15)
    robot.drive_system.go_straight_for_inches_using_encoder(12, 50) #could make this a color sensor thing
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_until_color_is('Black', -50)
    robot.arm_and_claw.calibrate_arm()

    robot.drive_system.spin_counterclockwise_until_sees_object(50, 15)
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
    robot.drive_system.go_straight_until_color_is('Black', -50)
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 15)
    robot.drive_system.go_straight_until_color_is('Green', 50)
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 15)
    robot.drive_system.go_straight_for_inches_using_encoder(12, 50)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_until_color_is('Green', -50)
    robot.arm_and_claw.calibrate_arm()

    robot.drive_system.spin_counterclockwise_until_sees_object(50, 15)
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
    robot.drive_system.go_straight_until_color_is('Green', -50)
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 15)
    robot.drive_system.go_straight_until_color_is('Blue', 50)
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 15)
    robot.drive_system.go_straight_for_inches_using_encoder(12, 50)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_until_color_is('Blue', -50)

    robot.sound_system.beeper.beep().wait()
    robot.sound_system.beeper.beep().wait()


def check(cup_2_entry):
    robot = rosebot.RoseBot()
    if cup_2_entry == 'x':
        robot.sound_system.tone_maker.play_tone(440, 1).wait()
        robot.sound_system.tone_maker.play_tone(880, 1).wait()
        print('YOU DID IT!')
