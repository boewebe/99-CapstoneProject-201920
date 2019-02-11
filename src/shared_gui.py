"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Brendan Boewe, Parker Jordan, Colin Browne.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_drive_system_frame(window, mqtt_sender):

    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive System")
    frame_lable_1 = ttk.Label(frame, text="Go straight for __ SECONDS at __ SPEED")
    left_speed_label = ttk.Label(frame, text="Enter Desired Speed")
    right_seconds_label = ttk.Label(frame, text="Enter Number of Seconds")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_seconds_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_seconds_entry.insert(0, "10")

    go_1 = ttk.Button(frame, text="Seconds/Speed")

    frame_lable_2 = ttk.Label(frame, text="Go straight for __ INCHES at __ speed using TIME")
    left_speed_label_1 = ttk.Label(frame, text="Enter Desired Speed")
    right_inches_label_1 = ttk.Label(frame, text="Enter Number of Inches")

    left_speed_entry_1 = ttk.Entry(frame, width=8)
    left_speed_entry_1.insert(0, "100")
    right_inches_entry_1 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_inches_entry_1.insert(0, "8")

    go_2 = ttk.Button(frame, text = "Inches/Time")

    frame_lable_3 = ttk.Label(frame, text="Go straight for __ INCHES at __ speed using ENCODER")
    left_speed_label_2 = ttk.Label(frame, text="Enter Desired Speed")
    right_inches_label_2 = ttk.Label(frame, text="Enter Number of Inches")

    left_speed_entry_2 = ttk.Entry(frame, width=8)
    left_speed_entry_2.insert(0, "100")
    right_inches_entry_2 = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_inches_entry_2.insert(0, "8")

    go_3 = ttk.Button(frame, text="Inches/Encoder")



    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    frame_lable_1.grid(row=1, column = 1)
    left_speed_label.grid(row=2, column=0)
    right_seconds_label.grid(row=2, column=2)
    left_speed_entry.grid(row=3, column=0)
    right_seconds_entry.grid(row=3, column=2)

    go_1.grid(row=4, column=1)

    frame_lable_2.grid(row=5, column=1)
    left_speed_label_1.grid(row=6, column=0)
    right_inches_label_1.grid(row=6, column=2)
    left_speed_entry_1.grid(row=7, column=0)
    right_inches_entry_1.grid(row=7, column=2)

    go_2.grid(row=8, column=1)

    frame_lable_3.grid(row=9, column=1)
    left_speed_label_2.grid(row=10, column=0)
    right_inches_label_2.grid(row=10, column=2)
    left_speed_entry_2.grid(row=11, column=0)
    right_inches_entry_2.grid(row=11, column=2)

    go_3.grid(row=12, column=1)

    # Set the button callbacks:
    go_1["command"] = lambda: handle_seconds_speed(mqtt_sender,
        right_seconds_entry, left_speed_entry)
    go_2["command"] = lambda: handle_inches_speed_time(mqtt_sender,
        right_inches_entry_1, left_speed_entry)
    go_3["command"] = lambda: handle_inches_speed_encoder(mqtt_sender,
        right_inches_entry_2, left_speed_entry)



    return frame



def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_sound_system_frame(window, mqtt_sender):

    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sound System")
    frame_label_1 = ttk.Label(frame,text="Beep for a given number of times")
    beep_number_times = ttk.Entry(frame, width=8)
    beep_number_times.insert(0, "5")
    Beep = ttk.Button(frame, text="Beep")

    frame_label_2 = ttk.Label(frame,text="Play a tone at a given frequency for a given duration")
    frequency = ttk.Entry(frame, width=8)
    frequency.insert(0, "440")
    frequency_button = ttk.Button(frame, text="Frequency")

    frame_label_3 = ttk.Label(frame, text="Speak a given phrase")
    phrase = ttk.Entry(frame, width=8)
    phrase_button = ttk.Button(frame, text="Phrase")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    frame_label_1.grid(row=1, column=1)
    beep_number_times.grid(row=2, column=1)
    Beep.grid(row=3, column=1)
    frame_label_2.grid(row=4, column=1)
    frequency.grid(row=5, column=1)
    frequency_button.grid(row=6, column=1)
    frame_label_3.grid(row=7, column=1)
    phrase.grid(row=8, column=1)
    phrase_button.grid(row=9, column=1)

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("go", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward", -int(left_entry_box.get()), -int(right_entry_box.get()))
    left = -int(left_entry_box.get())
    right = -int(right_entry_box.get())
    mqtt_sender.send_message("go", [str(left), str(right)])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("left", -int(left_entry_box.get()), right_entry_box.get())
    left = -int(left_entry_box.get())
    mqtt_sender.send_message("go", [str(left), right_entry_box.get()])



def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("right", left_entry_box.get(), - int(right_entry_box.get()))
    right = -int(right_entry_box.get())
    mqtt_sender.send_message("go", [left_entry_box.get(), str(right)])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("stop")
    mqtt_sender.send_message("stop")


###############################################################################
# Handlers for Buttons in the DriveSystem frame.
###############################################################################
def handle_seconds_speed(mqtt_sender, num_seconds, desired_speed):
    print("Seconds/Speed", num_seconds.get(), desired_speed.get())
    mqtt_sender.send_message("seconds_speed", [num_seconds.get(), desired_speed.get()])


def handle_inches_speed_time(mqtt_sender, num_inches, desired_speed):
    print("Inches/Time", num_inches.get(), desired_speed.get())
    mqtt_sender.send_message("inches_time", [num_inches.get(), desired_speed.get()])

def handle_inches_speed_encoder(mqtt_sender, num_inches, desired_speed):
    print("Inches/Encoder", num_inches.get(), desired_speed.get())
    mqtt_sender.send_message("inches_encoder", [num_inches.get(), desired_speed.get()])

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("raise_arm")
    mqtt_sender.send_message("raise_arm")

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("lower_arm")
    mqtt_sender.send_message("lower_arm")

def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("calibrate_arm")
    mqtt_sender.send_message("calibrate_arm")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("move_arm_to_position", arm_position_entry.get())
    mqtt_sender.send_message("move_arm_to_position", arm_position_entry.get())


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print("Quit")
    mqtt_sender.send_message("quit")


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print("Exit")
    mqtt_sender.send_message("exit")

