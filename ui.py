import tkinter as tk
from tkinter import ttk

from processes import *


# TODO windows testing
class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set window title
        self.window_title = ("Test Application")
        # set window size
        self.geometry("240x360")

        # create frame
        main_frame = tk.Frame(self, highlightbackground="black", highlightthickness=1)
        # pack frame
        main_frame.pack(side="top", padx=0)

        # configure location of frame (container) with grid
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        # frames dictionary to switch between
        self.frames = {}
        # three test frames for now
        for f in (MainPage, SidePage, FinalPage):
            frame = f(main_frame, self)

            # root window for other frames
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.ShowFrame(MainPage)

    def ShowFrame(self, content):
        frame = self.frames[content]
        # raise current frame
        frame.tkraise()

    # TODO Process stuff

    # update stringvar for label
    # def UpdateStringVar(self, content):


# first test page
# pull in initial state data and display

    def LaunchButton(self, process_obj):
        output = process_obj.LaunchProcess()
        return output

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label page
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # button for switching frames
        switch_window_button = tk.Button(
            self, text="Go to side page", command=lambda: controller.ShowFrame(SidePage)
        )
        switch_window_button.pack(side="top", padx=10, pady=5)

        # create test object
        process_obj = DeejProcess("deej.exe", 0, False)
        # string testing
        test_string = tk.StringVar()
        # assign test string
        test_string.set(process_obj.GetPid())
        # test button
        test_button = tk.Button(
            self, text="Refresh", command=lambda: process_obj.GetPid()
        )
        # pack
        test_button.pack(side="left", padx=10, pady=5)

        pid_label = tk.Label(
            self, textvariable=test_string
        )

        pid_label.pack(side="left", padx=20, pady=5)

    # refresh pid and return string
    def MainRefresh(self, process_obj):
        test_string = process_obj.GetPid()
        return test_string

    def LaunchButton(self, process_obj):
        output = process_obj.LaunchProcess()
        return output


# second test page
class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label page
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        # button for switching frames
        switch_window_button = tk.Button(
            self, text="Go to Final Page", command=lambda: controller.ShowFrame(FinalPage)
        )
        switch_window_button.pack(side="bottom", pady=10)


# final test page
class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label page
        label = tk.Label(self, text="This is the END OF THE LINE!")
        label.pack(padx=10, pady=10)

        # button for switching frames
        switch_window_button = tk.Button(
            self, text="Go to Main Page", command=lambda: controller.ShowFrame(MainPage)
        )
        switch_window_button.pack(side="bottom", pady=10)
