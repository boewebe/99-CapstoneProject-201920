import time
import rosebot


def test_increasing_beeps_as_approach(initial_beep_rate, rate_of_beep_increase):
    robot = rosebot.RoseBot()
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(50, 50)
    initial_beep_rate = int(initial_beep_rate)
    rate_of_beep_increase = int(rate_of_beep_increase)
    print('this edit has worked')

    while True:
        percent_distance = (robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) / (initial_distance)
        pause_time = 3 * (percent_distance) / ((initial_beep_rate) + ((rate_of_beep_increase) * (1 - percent_distance)))
        robot.sound_system.beeper.beep().wait()
        # print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        print(pause_time)

        time.sleep(abs(pause_time))
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <=2:
            robot.drive_system.stop()
            break

    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.calibrate_arm() # this is to reset it for testing
