# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.

import tkinter
from tkinter import ttk



def main():
    root = tkinter.Tk()
    root.title("Tkinter Canvas")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    canvas = tkinter.Canvas(root)
    canvas.create_line(0,0, 400, 400)

    canvas.grid(row=0, column=0)

    root.mainloop()


main()