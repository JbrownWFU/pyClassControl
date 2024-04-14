import tkinter as tk
from tkinter import ttk

# testing
class Windows(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # set window title
        self.window_title =("Test Application")
        # set window size
        self.geometry("350x600")

        # create frame
        main_frame = tk.Frame(self,highlightbackground="black", highlightthickness=1)
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

# first test page
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label page
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # button for switching frames
        switch_window_button = tk.Button(
            self, text = "Go to side page", command=lambda: controller.ShowFrame(SidePage)
        )
        switch_window_button.pack(side="bottom", pady=10)

# second test page
class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label page
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        # button for switching frames
        switch_window_button = tk.Button(
            self, text = "Go to Final Page", command=lambda: controller.ShowFrame(FinalPage)
        )
        switch_window_button.pack(side="bottom", pady=10)

# second test page
class FinalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label page
        label = tk.Label(self, text="This is the END OF THE LINE!")
        label.pack(padx=10, pady=10)

        # button for switching frames
        switch_window_button = tk.Button(
            self, text = "Go to Main Page", command=lambda: controller.ShowFrame(MainPage)
        )
        switch_window_button.pack(side="bottom", pady=10)