# Gui for Parker Jordan's sprint 3
# Shell Game

import tkinter
from tkinter import ttk
import sys


def get_game_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Widigets
    picture = cup_image(window)

    game_label = ttk.Label(frame, text='Shell Game!', font='TimesNewRoman 40 bold')
    cup_1_lable = ttk.Label(frame, text='Cup 1')
    cup_2_lable = ttk.Label(frame, text='Cup 2')
    cup_3_lable = ttk.Label(frame, text='Cup 3')

    cup_select_text = ttk.Label(frame, text="When you select a cup, put a 'x' in the entry box of your choice and press the 'See if you're right button!'")

    cup_1_entry = ttk.Entry(frame, width=8)
    cup_2_entry = ttk.Entry(frame, width=8)
    cup_3_entry = ttk.Entry(frame, width=8)

    scramble_button = ttk.Button(frame, image=picture)
    scramble_button.image = picture
    check_button = ttk.Button(frame, text="See if you're right!")

    cup_1_entry.grid(row=3, column=0)
    cup_2_entry.grid(row=3, column=1)
    cup_3_entry.grid(row=3, column=2)
    cup_1_lable.grid(row=4, column=0)
    cup_2_lable.grid(row=4, column=1)
    cup_3_lable.grid(row=4, column=2)

    game_label.grid(row=0, column=1)
    cup_select_text.grid(row=2, column=1)

    scramble_button.grid(row=1, column=1)
    check_button.grid(row=5, column=1)

    scramble_button["command"] = lambda: handle_scramble(mqtt_sender)
    check_button["command"] = lambda: handle_check(mqtt_sender, cup_2_entry)

    return frame

def cup_image(window):
    path = 'ezgif.com-crop.gif'
    img = tkinter.PhotoImage(file=path)
    panel = ttk.Label(window, image=img)
    panel.image = img

    return img

def handle_scramble(mqtt_sender):
    mqtt_sender.send_message("scramble_function")
    print('Scrambling')

def handle_check(mqtt_sender, cup_2_entry):
    print('Check')
    mqtt_sender.send_message("check", [cup_2_entry.get()])
