import rosebot


def test_scramble():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.spin_clockwise_until_sees_object(50, 50)
    robot.drive_system.go(50, 50)
    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() == 2:
        robot.drive_system.stop()
        robot.arm_and_claw.raise_arm()
    robot.drive_system.go_straight_for_inches_using_time(10, -50)


def check(cup_2_entry):
    robot = rosebot.RoseBot()
    if cup_2_entry == 'x':
        robot.sound_system.tone_maker.play_tone(440, 1).wait()
        robot.sound_system.tone_maker.play_tone(880, 1).wait()
        print('YOU DID IT!')
