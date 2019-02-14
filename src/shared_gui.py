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
import sys


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

    entry_label_1 = ttk.Label(frame, text="Enter Speed")
    entry_label_2 = ttk.Label(frame, text="Enter Seconds")
    entry_label_3 =  ttk.Label(frame, text="Enter Inches")
    entry_label_4 =  ttk.Label(frame, text="Enter Color")
    entry_label_5 =  ttk.Label(frame, text="Enter Intensity")

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    seconds_entry = ttk.Entry(frame, width=8)
    seconds_entry.insert(0, "5")
    inches_entry = ttk.Entry(frame, width=8)
    inches_entry.insert(0, "10")
    color_entry = ttk.Entry(frame, width=8)
    color_entry.insert(0, "Yellow")
    intensity_entry = ttk.Entry(frame, width=8)
    intensity_entry.insert(0, "50")

    # Buttons and Labels

    seconds_speed = ttk.Button(frame, text="Seconds/Speed")
    inches_time = ttk.Button(frame, text="Inches/Time")
    inches_encoder = ttk.Button(frame, text="Inches/Encoder")

    ##########################
    #Feature 8 Implementations
    ##########################

    color_system_label = ttk.Label(frame, text="Color System Buttons")

    intensity_less_than_button = ttk.Button(frame, text="Intensity Less")
    intensity_greater_than_button = ttk.Button(frame, text="Intensity Greater")
    color_is_button = ttk.Button(frame, text="Straight/Color is")
    color_is_not_button = ttk.Button(frame, text="Straight/Color is NOT")

    infrared_label = ttk.Label(frame, text="Infrared Proximity Sensor")

    delta_label = ttk.Label(frame, text="Delta")
    delta_entry = ttk.Entry(frame, width=8)
    delta_entry.insert(0, "1")

    forward_less_button = ttk.Button(frame, text="Forward Less")
    backward_greater_button = ttk.Button(frame, text="Backward Greater")
    until_distance_within = ttk.Button(frame, text="Until Within")






    blank_line_label = ttk.Label(frame, text="")
    blank_line_label_1 = ttk.Label(frame, text="")
    blank_line_label_2 = ttk.Label(frame, text="")
    blank_line_label_3 = ttk.Label(frame, text="")
    blank_line_label_4 = ttk.Label(frame, text="")
    blank_line_label_5 = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=2)

    entry_label_1.grid(row=1, column=0)
    entry_label_2.grid(row=1, column=1)
    entry_label_3.grid(row=1, column=2)
    entry_label_4.grid(row=1, column=3)
    entry_label_5.grid(row=1, column=4)

    speed_entry.grid(row=2, column=0)
    seconds_entry.grid(row=2, column=1)
    inches_entry.grid(row=2, column=2)
    color_entry.grid(row=2, column=3)
    intensity_entry.grid(row=2, column=4)

    blank_line_label.grid(row=3, column=0)

    # Buttons
    seconds_speed.grid(row=4, column=1)
    inches_time.grid(row=4, column=2)
    inches_encoder.grid(row=4, column=3)

    blank_line_label_1.grid(row=5, column=0)

    # Color System
    color_system_label.grid(row=6, column=2)
    blank_line_label_2.grid(row=7, column=0)

    intensity_less_than_button.grid(row=8, column=0)
    intensity_greater_than_button.grid(row=8, column=1)
    color_is_button.grid(row=8, column=2)
    color_is_not_button.grid(row=8, column=3)

    #Infrared Proximity
    blank_line_label_3.grid(row=9, column=2)
    infrared_label.grid(row=10, column=2)
    blank_line_label_4.grid(row=11, column=2)
    delta_label.grid(row=12, column=2)
    delta_entry.grid(row=13, column=2)
    blank_line_label_5.grid(row=14, column=2)
    forward_less_button.grid(row=15, column=1)
    backward_greater_button.grid(row=15, column=2)
    until_distance_within.grid(row=15, column=3)



    # Set the button callbacks:
    seconds_speed["command"] = lambda: handle_seconds_speed(mqtt_sender,
        seconds_entry, speed_entry)
    inches_time["command"] = lambda: handle_inches_speed_time(mqtt_sender,
        inches_entry, speed_entry)
    inches_encoder["command"] = lambda: handle_inches_speed_encoder(mqtt_sender,
        inches_entry, speed_entry)


    intensity_less_than_button["command"] = lambda: handle_intensity_less_than(mqtt_sender,
        intensity_entry, speed_entry)
    intensity_greater_than_button["command"] = lambda: handle_intensity_greater_than(mqtt_sender,
        intensity_entry, speed_entry)
    color_is_button["command"] = lambda: handle_until_color_is(mqtt_sender,
        color_entry, speed_entry)
    color_is_not_button["command"] = lambda: handle_until_color_is_not(mqtt_sender,
        color_entry, speed_entry)


    forward_less_button["command"] = lambda: handle_forward_less(mqtt_sender,
        inches_entry, speed_entry)
    backward_greater_button["command"] = lambda: handle_backward_greater(mqtt_sender,
        inches_entry, speed_entry)
    until_distance_within["command"] = lambda: handle_until_distance_within(mqtt_sender,
        delta_entry, inches_entry, speed_entry)



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
    position_entry.insert(0, "1000")

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
    beep_button = ttk.Button(frame, text="Beep")

    frame_label_2 = ttk.Label(frame,text="Play a tone at a given frequency for a given duration")
    frequency = ttk.Entry(frame, width=8)
    frequency.insert(0, "440")
    frequency_button = ttk.Button(frame, text="Frequency")
    duration = ttk.Entry(frame, width=8)
    duration.insert(0, "10")

    frame_label_3 = ttk.Label(frame, text="Speak a given phrase")
    phrase = ttk.Entry(frame, width=8)
    phrase_button = ttk.Button(frame, text="Phrase")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    frame_label_1.grid(row=1, column=1)
    beep_number_times.grid(row=2, column=1)
    beep_button.grid(row=3, column=1)
    frame_label_2.grid(row=4, column=1)
    frequency.grid(row=5, column=0)
    frequency_button.grid(row=6, column=0)
    duration.grid(row=5, column=2)
    frame_label_3.grid(row=7, column=1)
    phrase.grid(row=8, column=1)
    phrase_button.grid(row=9, column=1)

    # Set the Button callbacks:
    beep_button["command"] = lambda: handle_beep(beep_number_times, mqtt_sender)
    frequency_button["command"] = lambda: handle_frequency(frequency, duration, mqtt_sender)
    phrase_button["command"] = lambda: handle_phrase(phrase, mqtt_sender)

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
    mqtt_sender.send_message("move_arm_to_position", [arm_position_entry.get()])


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
    mqtt_sender.send_message("quit")
    sys.exit()


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################

def handle_beep(number_of_beeps, mqtt_sender):
    print("Beep", number_of_beeps.get(), "times")
    mqtt_sender.send_message("beep_n_times", [number_of_beeps.get()])

def handle_frequency(frequency, duration, mqtt_sender):
    print("Sound Frequency", frequency.get(), "for", duration.get(), "seconds")
    mqtt_sender.send_message("play_tone", [frequency.get(), duration.get()])


def handle_phrase(phrase, mqtt_sender):
    print("Phrase", phrase.get())
    mqtt_sender.send_message("speak_phrase", phrase.get())



########### Color Sensor

def handle_intensity_less_than(mqtt_sender, intensity, speed):
    print("Less Intensity:", intensity.get())
    print("Speed:", speed.get())
    print()
    mqtt_sender.send_message("intensity_less_than", [intensity.get(), speed.get()])

def handle_intensity_greater_than(mqtt_sender, intensity, speed):
    print("Greater Intensity:", intensity.get())
    print("Speed:", speed.get())
    print()
    mqtt_sender.send_message("intensity_greater_than", [intensity.get(), speed.get()])

def handle_until_color_is(mqtt_sender, color, speed):
    print("Color (Is function):", color.get())
    print("Speed:", speed.get())
    print()
    mqtt_sender.send_message("until_color_is", [color.get(), speed.get()])

def handle_until_color_is_not(mqtt_sender, color, speed):
    print("Color (Is NOT function):", color.get())
    print("Speed:", speed.get())
    print()
    mqtt_sender.send_message("until_color_is", [color.get(), speed.get()])




def handle_forward_less(mqtt_sender, inches, speed):
    print("go forward until distance is less than", inches.get(), "at speed", speed.get())
    print()
    mqtt_sender.send_message("forward_less", [inches.get(), speed.get()])

def handle_backward_greater(mqtt_sender, inches, speed):
    print("go backwards until distance is greater than", inches.get(), "at speed", speed.get())
    print()
    mqtt_sender.send_message("backward_greater", [inches.get(), speed.get()])

def handle_until_distance_within(mqtt_sender, delta, inches, speed):
    print("go until distance is within delta", delta.get(), "of", inches.get(), "inches at speed", speed.get())
    print()
    mqtt_sender.send_message("until_within", [delta.get(), inches.get(), speed.get()])