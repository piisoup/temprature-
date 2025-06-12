'''
This a program which uses tkinter to make a celcious to farranheit and vice verse calculator.

V1: working
'''

from tkinter import *
from tkinter import ttk

class Converter:
    def __init__(self):
        """
        Initializes the main application window and sets up the frames.
        """
        # Main window setup
        self.root = Tk()
        self.root.title("temprtarure converter")
        self.root.geometry("350x200")

        # Container for all frames
        self.container = Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)

        # Dictionary to hold the frames
        self.frames = {}

        # add each frame to dictionarye
        for F in (MainFrame, celciusframe, farrenheightframe):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame("MainFrame")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

    def run(self):
        # start the main loops
        self.root.mainloop()

class MainFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main Menu", font=("Arial", 16, "bold"))
        label.pack(pady=20, padx=10)

        # Button to switch to the Fahrenheit to Celsius converter
        to_c_button = Button(self, text="Convert to Celsius", bg="lightyellow",
                            command=lambda: controller.show_frame("celciusframe"))
        to_c_button.pack(pady=5)
        
        # Button to switch to the Celsius to Fahrenheit converter
        to_f_button = Button(self, text="Convert to Fahrenheit", bg="lightpink",
                            command=lambda: controller.show_frame("farrenheightframe"))
        to_f_button.pack(pady=5)

class celciusframe(Frame):
    """
    The frame for converting Fahrenheit to Celsius.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        self.fahrenheit_var = StringVar()
        self.result_var = StringVar()
        self.result_var.set("Result...")

        label = ttk.Label(self, text="FAHRENHEIT TO CELCUIUS", font=("Arial", 14))
        label.pack(pady=10, padx=10)
        
        entry_frame = Frame(self)
        entry_frame.pack(pady=5, padx=10)

        entry_label = ttk.Label(entry_frame, text="Fahrenheit:")
        entry_label.pack(side="left", padx=5)

        entry = ttk.Entry(entry_frame, textvariable=self.fahrenheit_var)
        entry.pack(side="left")

        result_label = ttk.Label(self, textvariable=self.result_var, font=("Arial", 12,))
        result_label.pack(pady=10)

        convert_button = ttk.Button(self, text="CONVERSIONM", command=self.convert)
        convert_button.pack(pady=5)
        
        back_button = ttk.Button(self, text="TO HOMES",
                                 command=lambda: controller.show_frame("MainFrame"))
        back_button.pack(pady=10)

    def convert(self):
        """
        Performs the F to C conversion and updates the result label.
        """
        fahrenheit = float(self.fahrenheit_var.get())
        celsius = (fahrenheit - 32) * 5/9
        self.result_var.set(f"{celsius:.2f} C")

class farrenheightframe(Frame):
    """
    The frame for converting Celsius to Fahrenheit.
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.celsius_var = StringVar()
        self.result_var = StringVar()
        self.result_var.set("Result...")

        label = ttk.Label(self, text="Celsius to Fahrenheit", font=("Arial", 14))
        label.pack(pady=10, padx=10)

        entry_frame = Frame(self)
        entry_frame.pack(pady=5, padx=10)

        entry_label = ttk.Label(entry_frame, text="Celcius:")
        entry_label.pack(side="left", padx=5)

        entry = ttk.Entry(entry_frame, textvariable=self.celsius_var)
        entry.pack(side="left")

        result_label = ttk.Label(self, textvariable=self.result_var, font=("Arial", 12,))
        result_label.pack(pady=10)

        convert_button = ttk.Button(self, text="Convert", command=self.convert)
        convert_button.pack(pady=5)
        
        back_button = ttk.Button(self, text="Back to home !! 🏠",
                                 command=lambda: controller.show_frame("MainFrame"))
        back_button.pack(pady=10)

    def convert(self):
        """
        Performs the C to F conversion and updates the result label.
        """
        celsius = float(self.celsius_var.get())
        fahrenheit = (celsius * 9/5) + 32
        self.result_var.set(f"{fahrenheit:.2f} F")



#  execute !!
if __name__ == "__main__":
    app = Converter()
    app.run()