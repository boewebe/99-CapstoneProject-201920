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


def prox_frequency_increase(speed, frequency, rate_of_freq_increase):
    robot = rosebot.RoseBot()
    robot.drive_system.go(int(speed), int(speed))
    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    starting_frequency = int(frequency)
    while True:
        frequency = starting_frequency + int(rate_of_freq_increase) * ((initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())/robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        robot.sound_system.tone_maker.play_tone(int(frequency), 50).wait()
        time.sleep(0.2)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() == 2:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.raise_arm()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()