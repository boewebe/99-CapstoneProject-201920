#Sprint 3 Code - Brendan Boewe


import tkinter
from tkinter import ttk
import rosebot
import mqtt_remote_method_calls as com
import sys



class Delegate_for_pc(object):

    def __init__(self):
        pass

    def draw_things(self, root, canvas, note_head_start):
        self.root = root
        self.canvas = canvas
        self.note_head_start = note_head_start
        return self.root, self.canvas, self.note_head_start


def draw_staff(mqtt_sender, a, note_head_start):
    root = tkinter.Tk()
    root.title("Tkinter Canvas")

    main_frame = ttk.Frame(root, padding=20, height=500, width=600)
    main_frame.grid()  # only grid call that does NOT need a row and column

    canvas = tkinter.Canvas(root)
    canvas.create_line(0, 40, 500, 40, width=5)
    canvas.create_line(0, 70, 500, 70, width=5)
    canvas.create_line(0, 100, 500, 100, width=5)
    canvas.create_line(0, 130, 500, 130, width=5)
    canvas.create_line(0, 160, 500, 160, width=5)


    canvas.grid(row=0, column=0)

    stop_button = ttk.Button(root, text="Stop")
    stop_button.grid(row=1, column=0)

    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    x = mqtt_sender.send_message('m1_sprint_3_Color', [mqtt_sender, root, canvas, note_head_start])

    print(x)


    root.mainloop()

    return root and canvas


def A4_note(mqtt_sender, root, canvas, note_head_start):

    print("A4")
    mqtt_sender.send_message("play_tone", [440, 0.75])

    note_head_end = note_head_start + 45

    canvas.create_oval(note_head_start, 100, note_head_end, 130, fill='Black')
    canvas.create_line(note_head_end, 115, note_head_end, 30, width = 3)

    root.mainloop()

    note_head_new_start = note_head_end + 30

    return note_head_new_start

def B4_note(mqtt_sender, root, canvas, note_head_start):

    print("B4")
    mqtt_sender.send_message("play_tone", [493.88, 0.75])

    note_head_end = note_head_start + 45

    canvas.create_oval(note_head_start, 85, note_head_end, 115, fill='Black')
    canvas.create_line(note_head_end, 100, note_head_end, 15, width=3)

    root.mainloop()

    note_head_new_start = note_head_end + 30

    return note_head_new_start

def C5_sharp_note(mqtt_sender, root, canvas):

    print("C#5")
    mqtt_sender.send_message("play_tone", [554.37, 0.75])

def D5_note(mqtt_sender, root, canvas):

    print("D5")
    mqtt_sender.send_message("play_tone", [587.33, 0.75])

def E5_note(mqtt_sender, root, canvas):

    print("E5")
    mqtt_sender.send_message("play_tone", [659.25, 0.75])

def F5_sharp_note(mqtt_sender, root, canvas):

    print("F#5")
    mqtt_sender.send_message("play_tone", [739.99, 0.75])




def handle_stop(mqtt_sender):
    print('stop')
    mqtt_sender.send_message('quit')
    sys.exit()




def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    a = 5

    note_head_start = 15
    while True:
        canvas = draw_staff(mqtt_sender, a, note_head_start)

    #A4_note(mqtt_sender, canvas[0], canvas[1])


main()