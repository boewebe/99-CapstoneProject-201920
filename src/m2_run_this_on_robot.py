"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Parker Jordan.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    connect_to_robot()
    #prox_frequency_increase()


def connect_to_robot():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)


def run_test_pick_up_with_tones(initial_frequency, rate):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    speed = 50
    robot.drive_system.go(speed, speed)
    max_freq = (initial_frequency + 19 * rate) * 2
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.tone(100, max_freq - 2 * d * rate)
        print(max_freq - d * rate)
        time.sleep(0.2)
        if d <= 2:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()