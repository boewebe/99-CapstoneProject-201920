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
    real_thing()


def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)


def prox_frequency_increase(speed, frequency, rate_of_freq_increase):
    robot = rosebot.RoseBot()
    robot.drive_system.go(speed, speed)
    initial_distance = robot.drive_system.ir_prox_sensor.get_distance_in_inches()
    starting_frequency = frequency
    while True:
        frequency = starting_frequency + rate_of_freq_increase * ((initial_distance - robot.drive_system.ir_prox_sensor.get_distance_in_inches())/intital_distance)
        robot.sound_system.tone_maker.play_tone(frequency, 50).wait()
        time.sleep(0.2)
        if robot.drive_system.ir_prox_sensor.get_distance_in_inches() == 2:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.raise_arm()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()