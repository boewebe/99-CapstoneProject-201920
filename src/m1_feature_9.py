import rosebot
import time

def test_led_pickup(initial_led_rate, rate_of_led_increase):
    robot = rosebot.RoseBot()
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    robot.drive_system.go(50, 50)
    initial_led_rate = int(initial_led_rate)
    rate_of_led_increase = int(rate_of_led_increase)

    while True:
        percent_distance = (initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        pause_time = (percent_distance) / (
                    (initial_led_rate) + ((rate_of_led_increase) * (1 / 10) * (100 - percent_distance)))
        led_sequecne()
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        time.sleep(pause_time)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            robot.drive_system.stop()
            break

    robot.arm_and_claw.raise_arm()


def led_sequecne():
    robot = rosebot.RoseBot()
    robot.led_system.left_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_off()



def spin_until_sees_object(clock_or_counter, speed, area):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

    if clock_or_counter == '1':
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))
        test_increasing_beeps_as_approach(100,50)
    if clock_or_counter == '2':
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))
        test_increasing_beeps_as_approach(100,50)


def test_increasing_beeps_as_approach(initial_beep_rate, rate_of_beep_increase):
    robot = rosebot.RoseBot()
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(50, 50)
    initial_beep_rate = int(initial_beep_rate)
    rate_of_beep_increase = int(rate_of_beep_increase)

    while True:
        percent_distance = (initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        pause_time = (percent_distance) / ((initial_beep_rate) + ((rate_of_beep_increase) * (1/10)*(100 - percent_distance)))
        robot.sound_system.beeper.beep().wait()
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        time.sleep(abs(pause_time))
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <=2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

