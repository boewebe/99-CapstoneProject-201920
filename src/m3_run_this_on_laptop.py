"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Colin Browne.
  Winter term, 2018-2019.
"""

import tkinter as tk
from tkinter import font as tkfont
import mqtt_remote_method_calls as com
from tkinter import ttk
import mqtt_remote_method_calls
import shared_gui


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    drive_system_2_frame = shared_gui.get_drive_system_2_frame(main_frame, mqtt_sender)

    return teleop_frame, drive_system_frame, drive_system_2_frame, arm_frame, control_frame, sound_system_frame

def grid_frames(teleop_frame, drive_system_frame, drive_system_2_frame, arm_frame, control_frame, sound_system_frame):
    teleop_frame.grid(row=2, column=2)
    drive_system_frame.grid(row=1, column=0)
    drive_system_2_frame.grid(row=1, column=2)
    arm_frame.grid(row=2, column=0)
    control_frame.grid(row=2, column=1)
    sound_system_frame.grid(row=1, column=1)


def handle_note_sender_to_robot(mqtt_sender, frequency):
    print('sending note, ', frequency, 'hertz')
    mqtt_sender.send_message('play_tone', [frequency, 0.5])

mqtt_sender = com.MqttClient()
# mqtt_sender.connect_to_ev3()





class SampleApp(tk.Tk):

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()



    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Main Menu')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

      #  self.publish_topic_name = mqtt_sender.publish_topic_name

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()




class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Robo-Piano",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Simple Teleoperations",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Go to Maze Solver",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.publish_topic_name = mqtt_sender.connect_to_ev3()

        self.controller = controller
        label = tk.Label(self, text="This is Robo-Piano", font=controller.title_font)
        label.grid(row=0, column=0)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=1, column=0)
        C4 = tk.Button(self, text='C4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 261.6))
        C4.grid(row=3, column=1)
        Csharp4 = tk.Button(self, text='C#4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 277.18))
        Csharp4.grid(row=2, column=2)
        D4 = tk.Button(self, text='D4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 293.66))
        D4.grid(row=3, column=3)
        Dsharp4 = tk.Button(self, text='D#4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 311.12))
        Dsharp4.grid(row=2, column=4)
        E4 = tk.Button(self, text='E4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 329.62))
        E4.grid(row=3, column=5)
        F4 = tk.Button(self, text='F4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 349.22))
        F4.grid(row=3, column=6)
        Fsharp4 = tk.Button(self, text='F#4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 369.99))
        Fsharp4.grid(row=2, column=7)
        G4 = tk.Button(self, text='G4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 391.99))
        G4.grid(row=3, column=8)
        Gsharp4 = tk.Button(self, text='G#4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 415.30))
        Gsharp4.grid(row=2, column=9)
        A4 = tk.Button(self, text='A4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 440))
        A4.grid(row=3, column=10)
        Asharp4 = tk.Button(self, text='A#4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 466.16))
        Asharp4.grid(row=2, column=11)
        B4 = tk.Button(self, text='B4', command=lambda: handle_note_sender_to_robot(mqtt_sender, 493.88))
        B4.grid(row=3, column=12)
        C5 = tk.Button(self, text='C5', command=lambda: handle_note_sender_to_robot(mqtt_sender, 523.25))
        C5.grid(row=3, column=13)



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.publish_topic_name = mqtt_sender.connect_to_ev3()

        teleop_frame, drive_system_frame, drive_system_2_frame, arm_frame, control_frame, sound_system_frame = get_shared_frames(
            self, mqtt_sender)
        grid_frames(teleop_frame, drive_system_frame, drive_system_2_frame, arm_frame, control_frame,
                    sound_system_frame)

        self.controller = controller
        label = tk.Label(self, text="Simple Teleoperations", font=controller.title_font)
        label.grid(row=0, column=0)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=1)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.publish_topic_name = mqtt_sender.connect_to_ev3()

        self.controller = controller
        label = tk.Label(self, text="This is page 3(Maze Solver)", font=controller.title_font)
        label.grid(row=0, column=0)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=1, column=0)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


