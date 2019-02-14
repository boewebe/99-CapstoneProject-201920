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