#Sprint 3 Code - Brendan Boewe


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import sys


def draw_staff(mqtt_sender):
    root = tkinter.Tk()
    root.title("Sprint 3 GUI and Canvas - Brendan Boewe")

    main_frame = ttk.Frame(root, padding=20, height=300, width=600)
    main_frame.grid()  # only grid call that does NOT need a row and column

    canvas = tkinter.Canvas(root)
    canvas.create_line(0, 40, 500, 40, width=5)
    canvas.create_line(0, 70, 500, 70, width=5)
    canvas.create_line(0, 100, 500, 100, width=5)
    canvas.create_line(0, 130, 500, 130, width=5)
    canvas.create_line(0, 160, 500, 160, width=5)


    canvas.grid(row=0, column=0)

# Labels
    song_1_label = ttk.Label(root, text="Song # 1")
    song_1_label.grid(row=2, column=0)

    song_2_label = ttk.Label(root, text="Song # 2")
    song_2_label.grid(row=4, column=0)

    song_3_label = ttk.Label(root, text="Song # 3")
    song_3_label.grid(row=6, column=0)

    sensor_function_label = ttk.Label(root, text="Sensor Functions")
    sensor_function_label.grid(row= 1,column=1)

    find_object_function_label = ttk.Label(root, text="Find Object Function")
    find_object_function_label.grid(row=2, column= 1)

    play_note_by_color_label = ttk.Label(root, text="Play Note by Color")
    play_note_by_color_label.grid(row=4, column=1)

    time_to_stop_entry_label = ttk.Label(root, text="Enter time to stop")
    time_to_stop_entry_label.grid(row=6, column=1)

    play_tune_by_color_label = ttk.Label(root, text="Play Tune by Color")
    play_tune_by_color_label.grid(row=8, column=1)

# Buttons
    stop_button = ttk.Button(root, text="Stop")
    stop_button.grid(row=1, column=0)

    play_song1_button = ttk.Button(root, text="Play")
    play_song1_button.grid(row=3, column=0)

    play_song2_button = ttk.Button(root, text="Play")
    play_song2_button.grid(row=5, column=0)

    play_song3_button = ttk.Button(root, text="Play")
    play_song3_button.grid(row=7, column=0)

    find_object_button = ttk.Button(root, text="Run")
    find_object_button.grid(row=3, column=1)

    play_note_by_color_button = ttk.Button(root, text="Run")
    play_note_by_color_button.grid(row=5, column=1)

    time_to_stop_entry = ttk.Entry(root, width=8)
    time_to_stop_entry.insert(0, "5")
    time_to_stop_entry.grid(row=7, column=1)

    play_tune_by_color_button = ttk.Button(root, text="Run")
    play_tune_by_color_button.grid(row=9, column=1)

    calibrate_arm_button = ttk.Button(root, text="Calibrate Arm")
    calibrate_arm_button.grid(row=10, column=1)

    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    play_song1_button["command"] = lambda: handle_play_song_1(mqtt_sender, canvas)
    play_song2_button["command"] = lambda: handle_play_song_2(mqtt_sender, canvas)
    play_song3_button["command"] = lambda: handle_play_song_3(mqtt_sender, canvas)
    find_object_button["command"] = lambda: handle_find_object(mqtt_sender)
    play_note_by_color_button["command"] = lambda: handle_color_sensor_play_note(mqtt_sender, time_to_stop_entry)
    play_tune_by_color_button["command"] = lambda: handle_color_sensor_play_tune(mqtt_sender, time_to_stop_entry)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)

    root.mainloop()

    return root and canvas



### Lambda Handle functions

def handle_stop(mqtt_sender):
    print('stop')
    mqtt_sender.send_message('quit')
    sys.exit()




def handle_play_song_1(mqtt_sender, canvas):


    note_head_start = 15
    note_head_end = note_head_start + 45

    notes_top = [130, 115, 100, 85, 70]
    notes_bottom =[100, 85, 70, 55, 40]

    for k in range(5):
        canvas.create_oval(note_head_start, notes_bottom[k], note_head_end, notes_top[k], fill='Black')
        canvas.create_line(note_head_end, (notes_bottom[k] + 15), note_head_end, (30 - (15*k)), width=3)

        note_head_start = note_head_start + 60
        note_head_end = note_head_start + 45

    mqtt_sender.send_message('m1_sprint3_song_1')

def handle_play_song_2(mqtt_sender, canvas):
    note_head_start = 15
    note_head_end = note_head_start + 45

    notes_top = [130, 130, 70, 70, 55, 55, 70]
    notes_bottom = [100, 100, 40, 40, 25, 25, 40]

    for k in range(7):
        canvas.create_oval(note_head_start, notes_bottom[k], note_head_end, notes_top[k], fill='Black')
        canvas.create_line(note_head_end, (notes_bottom[k] + 15), note_head_end, (30 - (15 * k)), width=3)

        note_head_start = note_head_start + 50
        note_head_end = note_head_start + 45

    mqtt_sender.send_message('m1_sprint3_song_2')

def handle_play_song_3(mqtt_sender, canvas):
    note_head_start = 15
    note_head_end = note_head_start + 45

    notes_top = [145, 115, 85, 115, 145]
    notes_bottom = [115, 85, 55, 85, 115]

    for k in range(5):
        canvas.create_oval(note_head_start, notes_bottom[k], note_head_end, notes_top[k], fill='Black')
        canvas.create_line(note_head_end, (notes_bottom[k] + 15), note_head_end, (30 - (15 * k)), width=3)

        note_head_start = note_head_start + 60
        note_head_end = note_head_start + 45

    mqtt_sender.send_message('m1_sprint3_song_3')




def handle_find_object(mqtt_sender):
    print("find object")
    mqtt_sender.send_message('m1_find_object')


def handle_color_sensor_play_note(mqtt_sender, time_to_stop):
    print("color sensor - play note unless not found within", int(time_to_stop.get()), "seconds")
    mqtt_sender.send_message('m1_color_sensor_play_note',[int(time_to_stop.get())])

def handle_color_sensor_play_tune(mqtt_sender, time_to_stop):
    print("color sensor - play tune unless not found within", int(time_to_stop.get()), "seconds")
    mqtt_sender.send_message('m1_color_sensor_play_tune',[int(time_to_stop.get())])

def handle_calibrate_arm(mqtt_sender):
    print("Calibrate Arm")
    mqtt_sender.send_message('calibrate_arm')


def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    while True:
        draw_staff(mqtt_sender)

main()