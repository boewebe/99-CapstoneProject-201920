# Gui for Parker Jordan's sprint 3
# Shell Game

import tkinter
from tkinter import ttk
import sys

def get_game_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Widigets
    game_label = ttk.Label(frame, text='Shell Game', font=20)
    cup_1_lable = ttk.Label(frame, text='Cup 1')
    cup_2_lable = ttk.Label(frame, text='Cup 2')
    cup_3_lable = ttk.Label(frame, text='Cup 3')

    cup_1_entry = ttk.Entry(frame, width=8)
    cup_2_entry = ttk.Entry(frame, width=8)
    cup_3_entry = ttk.Entry(frame, width=8)

    scramble_button = ttk.Button(frame, text="Scramble!")
    check_button = ttk.Button(frame, text="See if you're right!")

    cup_1_entry.grid(row=1, column=0)
    cup_2_entry.grid(row=1, column=1)
    cup_3_entry.grid(row=1, column=2)
    cup_1_lable.grid(row=2, column=0)
    cup_2_lable.grid(row=2, column=1)
    cup_3_lable.grid(row=2, column=2)

    scramble_button.grid(row=0, column=1)
    check_button.grid(row=3, column=1)

    scramble_button["command"] = lambda: handle_scramble(mqtt_sender)
    check_button["command"] = lambda: handle_check(mqtt_sender)

    return frame

def handle_scramble(mqtt_sender):

def handle_check(mqtt_sender):
    