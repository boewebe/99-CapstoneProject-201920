"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Brendan Boewe, Parker Jordan, and Colin Browne.
  Winter term, 2018-2019.
"""

import rosebot
import m2_run_this_on_robot

class ResponderToGUIMessages(object):
    def __init__(self, robot):
        """

        :type robot: rosebot.RoseBot
        """
        self.robot = robot
        self.m2_run_this_on_robot = m2_run_this_on_robot
        self.stop_program = False

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

    def quit(self):
        self.stop_program = True

    def seconds_speed(self, num_seconds, desired_speed):
        self.robot.drive_system.go_straight_for_seconds(num_seconds, desired_speed)

    def inches_time(self, num_inches, desired_speed):
        self.robot.drive_system.go_straight_for_inches_using_time(num_inches, desired_speed)

    def inches_encoder(self, num_inches, desired_speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(num_inches, desired_speed)

    def beep_n_times(self, n):
        print("beeping", n, "times")
        for k in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def play_tone(self, frequency, duration_time):
        self.robot.sound_system.tone_maker.play_tone(int(frequency), (int(duration_time) * 1000)).wait()

    def speak_phrase(self, phrase):
        self.robot.sound_system.speech_maker.speak(phrase)

    def intensity_less_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity, speed)

    def intensity_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity, speed)

    def until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, speed)

    def until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, speed)

    def forward_less(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)

    def backward_greater(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)

    def until_within(self, delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(delta, inches, speed)

    def display_camera_data(self):
        self.robot.drive_system.display_camera_data()

    def spin_clockwise(self, area, speed):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)

    def spin_counterclockwise(self, area, speed):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)

    def m2_rate_of_freq(self, speed, freq, rate_of_freq):
        self.m2_run_this_on_robot.prox_frequency_increase(speed, freq, rate_of_freq)