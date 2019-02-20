# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

import tkinter
from tkinter import ttk




def main():
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

    root.mainloop()

    #if color == 'Blue':
    #    C5_sharp_note(mqtt_sender, root, canvas)

    #if color == 'Green':
    #    D5_note(mqtt_sender, root, canvas)

    #if color == 'Yellow':
    #    E5_note(mqtt_sender, root, canvas)

    #if color == 'White':
    #    F5_sharp_note(mqtt_sender, root, canvas)
main()