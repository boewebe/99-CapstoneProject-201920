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


mqtt_sender = com.MqttClient()
# mqtt_sender.connect_to_ev3()





class SampleApp(tk.Tk):

    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Main Menu')
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

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
        label = tk.Label(self, text="This is the Main Menu", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One(Robo-keyboard)",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two(Simple Teleoperations)",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Go to Page Three(Maze Solver)",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        #key1 = tk.Button(self, text='C4', command=lambda: note_sender_to_robot)

        #def note_sender_to_robot(mqtt_sender, frequency, duration):
          #  pass


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

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
        self.controller = controller
        label = tk.Label(self, text="This is page 3(Maze Solver)", font=controller.title_font)
        label.grid(row=0, column=0)
        button = tk.Button(self, text="Return to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=0, column=1)



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


