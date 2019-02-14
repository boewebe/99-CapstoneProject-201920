"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Colin Browne.
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
    #run_test_of_functions()
    connect_to_robot()


#def increasing_beeps_as_approach(speed, initial_beep_rate, rate_of_beep_increase):
#    robot = rosebot.RoseBot()
#    beeps_per_second_max = 1/initial_beep_rate
#    initial_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
#    robot.drive_system.go(speed, speed)

#    while True:
#        delay_between_beeps = (1/(int(rate_of_beep_increase))) * ((initial_distance - robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())/(initial_distance))/(beeps_per_second_max)
#        robot.sound_system.beeper.beep().wait()
#        time.sleep(delay_between_beeps)
#        if int(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) <= 2:
#            break





def run_test_of_functions():
    robot = rosebot.RoseBot()
    robot.drive_system.go(100,100)
    time.sleep(4)
    robot.drive_system.stop()
    time.sleep(3)
    print('should calibrate arm next')
    robot.arm_and_claw.calibrate_arm()
    print('made it this far')
    time.sleep(1)

    print('you are done')

def connect_to_robot():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.ResponderToGUIMessages(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()