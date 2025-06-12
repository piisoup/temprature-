'''
This a program which uses tkinter to make a celsius to fahrenheit and vice versa calculator.

V1: working
V2: i add picture and added tyhingys an make it work better
'''

from tkinter import *
from tkinter import ttk

class Converter:
    """
    main applications.
    """
    def __init__(self):
        # setup for main window! 
        self.root = Tk()
        self.root.title("Temperature Converter")
        self.root.geometry("350x250")

        # Container for all frames
        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to hold the frames
        self.frames = {}

        # Add each frame to the dictionary
        for F in (MainFrame, CelsiusFrame, FahrenheitFrame, CatFrame):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show initial frame
        self.show_frame("MainFrame")

    def show_frame(self, frame_name):
        # shows requested frame
        frame = self.frames[frame_name]
        frame.tkraise()

    def run(self):
        # tkinter loop
        self.root.mainloop()

class MainFrame(Frame):
    # main menue with navigation
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="HOMES 🏠🫃", font=("Verdana", 16, "bold"))
        label.pack(pady=20, padx=10)

        # Button to switch to the Fahrenheit to Celsius converter
        to_c_button = Button(self, text="Convert Fahrenheit to Celsius", bg="pink",
                            command=lambda: controller.show_frame("CelsiusFrame"))
        to_c_button.pack(pady=5, fill='x', padx=20)
        
        # Button to switch to the Celsius to Fahrenheit converter
        to_f_button = Button(self, text="Convert Celsius to Fahrenheit", bg="lightyellow",
                            command=lambda: controller.show_frame("FahrenheitFrame"))
        to_f_button.pack(pady=5, fill='x', padx=20)

        # Button to show a picture
        to_cat_button = Button(self, text="Show a Picture", bg="#C4A484",
                            command=lambda: controller.show_frame("CatFrame"))
        to_cat_button.pack(pady=5, fill='x', padx=20)

class CelsiusFrame(Frame):
    #faranheit to celcuoius
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.fahrenheit_var = StringVar()
        self.result_var = StringVar()
        self.result_var.set("Result...")

        label = ttk.Label(self, text="Fahrenheit to Celsius", font=("Verdana", 14, "bold"))
        label.pack(pady=10, padx=10)
        
        entry_frame = Frame(self)
        entry_frame.pack(pady=5, padx=10)

        entry_label = ttk.Label(entry_frame, text="Fahrenheit:")
        entry_label.pack(side="left", padx=5)

        entry = ttk.Entry(entry_frame, textvariable=self.fahrenheit_var)
        entry.pack(side="left")

        result_label = ttk.Label(self, textvariable=self.result_var, font=("Verdana", 12, "italic"))
        result_label.pack(pady=10)

        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        convert_button.pack(pady=5)
        
        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        back_button.pack(pady=10)

    def convert(self):
        # fareagnheight tio celsuius
        try:
            fahrenheit = float(self.fahrenheit_var.get())
            celsius = (fahrenheit - 32) * 5/9
            self.result_var.set(f"{celsius:.2f} °C")
        except (ValueError, TclError):
            self.result_var.set("Invalid Input")

class FahrenheitFrame(Frame):
    # c to f
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.celsius_var = StringVar()
        self.result_var = StringVar()
        self.result_var.set("Result...")

        label = ttk.Label(self, text="Celsius to Fahrenheit", font=("Verdana", 14, "bold"))
        label.pack(pady=10, padx=10)

        entry_frame = Frame(self)
        entry_frame.pack(pady=5, padx=10)

        entry_label = ttk.Label(entry_frame, text="Celsius:")
        entry_label.pack(side="left", padx=5)

        entry = ttk.Entry(entry_frame, textvariable=self.celsius_var)
        entry.pack(side="left")

        result_label = ttk.Label(self, textvariable=self.result_var, font=("Verdana", 12, "italic"))
        result_label.pack(pady=10)

        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        convert_button.pack(pady=5)
        
        back_button = ttk.Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        back_button.pack(pady=10)

    def convert(self):
        # c to f conversion
        try:
            celsius = float(self.celsius_var.get())
            fahrenheit = (celsius * 9/5) + 32
            self.result_var.set(f"{fahrenheit:.2f} °F")
        except (ValueError, TclError):
            self.result_var.set("Invalid Input")

class CatFrame(Frame):
    # idk a picyure
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = ttk.Label(self, text="Meow! ₍^. .^₎⟆", font=("Verdana", 16, "bold"))
        label.pack(pady=10, padx=10)
        # loadf the file into the thingy
        self.cat_image = PhotoImage(file="Sitting Cat PNG.png")

        # downsize to 0.25
        self.cat_image = self.cat_image.subsample(4)

        # label
        image_label = Label(self, image=self.cat_image)
        image_label.pack(pady=10)
        back_button = Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame("MainFrame"))
        back_button.pack(pady=10)

# run
if __name__ == "__main__":
    app = Converter()
    app.run()
