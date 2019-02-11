"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Brendan Boewe, Parker Jordan, and Colin Browne.
  Winter term, 2018-2019.
"""

import rosebot

class ResponderToGUIMessages(object):
    def __init__(self, robot):
        """

        :type robot: rosebot.RoseBot
        """
        self.robot = robot

    def go(self, left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        right = int(right_wheel_speed)
        self.robot.drive_system.go(left, right)

    def stop(self):
        self.robot.drive_system.stop()

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, position):
        self.robot.arm_and_claw.move_arm_to_position(position)

    #def quit(self):

    #def exit(self):

    def seconds_speed(self, num_seconds, desired_speed):
        self.robot.drive_system.go_straight_for_seconds(num_seconds, desired_speed)

    def inches_time(self, num_inches, desired_speed):
        self.robot.drive_system.go_straight_for_inches_using_time(num_inches, desired_speed)

    def inches_encoder(self, num_inches, desired_speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(num_inches, desired_speed)

    #def beep_n_times(self, n):

    #def play_tone(self, frequency, duration_time):

    #def speak_phrase(self, phrase):