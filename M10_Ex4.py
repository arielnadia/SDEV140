# Celsius/Fahrenheit Converter Program!

import tkinter

class TempConverterGUI:
    def __init__(self):
        # Define the layout
        self.Main_Window = tkinter.Tk()
        self.Top_Frame = tkinter.Frame()
        self.Upper_Mid_Frame = tkinter.Frame()
        self.Mid_Frame = tkinter.Frame()
        self.Lower_Mid_Frame = tkinter.Frame()
        self.Bottom_Frame = tkinter.Frame()

        self.Prompt_Label = tkinter.Label(self.Top_Frame,\
                                          text='Enter a temperature:')
        self.Temp_Entry = tkinter.Entry(self.Upper_Mid_Frame, width=5)
        self.Prompt_Label.pack()
        self.Temp_Entry.pack()

        self.Descr_Label = tkinter.Label(self.Mid_Frame,\
                                         text='Conversion:')
        self.Value = tkinter.StringVar()
        self.Temp_Label = tkinter.Label(self.Mid_Frame,\
                                        textvariable=self.Value)
        self.Descr_Label.pack()
        self.Temp_Label.pack()

        # Create the buttons
        self.Fahrenheit_Button = tkinter.Button(self.Lower_Mid_Frame,\
                                                text='Convert Celsius \n'\
                                                'to Fahrenheit', command=self.fahrenheit)
        self.Celsius_Button = tkinter.Button(self.Lower_Mid_Frame,\
                                             text='Convert Fahrenheit \n'\
                                             'to Celsius', command=self.celsius)
        self.Quit_Button = tkinter.Button(self.Bottom_Frame,\
                                          text='Quit', command=self.Main_Window.destroy)

        self.Fahrenheit_Button.pack(side='left')
        self.Celsius_Button.pack(side='left')
        self.Quit_Button.pack(side='left')

        self.Top_Frame.pack()
        self.Upper_Mid_Frame.pack()
        self.Mid_Frame.pack()
        self.Lower_Mid_Frame.pack()
        self.Bottom_Frame.pack()

        tkinter.mainloop()

    # Define the fahrenheit conversion
    def fahrenheit(self):
        Temp = float(self.Temp_Entry.get())
        Fahrenheit = format(((9/5)*Temp) + 32, '.1f')
        self.Value.set(Fahrenheit)
        
    # Define the celsius conversion
    def celsius(self):
        Temp = float(self.Temp_Entry.get())
        Celsius = format((Temp - 32) * (5/9), '.1f')
        self.Value.set(Celsius)

# Run the program!
temp_copy = TempConverterGUI()

        
