from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk

############################################################################################################################################
root = Tk()
root.title('SEAMLESS CONVERTER')
root.geometry("450x400+100+200")
bg = PhotoImage(file = "bcd.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

#############################################################################################################################################
#WEIGHT CONVERTER

def WeightConverter():
# factors to multiply to a value to convert from the following units to gram(g)

    factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
    ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "gram" : 'g', "centigram" : 'cg', "milligram" : 'mg'}

    def convert(amt, frm, to):
# function to convert from a given unit to another
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

# initiate window
    root = Toplevel()
    root.title("Weight Converter")
# initiate frame
    mainframe = ttk.Frame(root, padding="3 30 12 12")
    mainframe.pack(fill=BOTH,expand=1)
    titleLabel = Label (mainframe, text = "Weight Converter", font = ("Arial", 12, "bold"), justify = CENTER,fg="orange").grid(column=1,row=1)
    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()
    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

# Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2)

# Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram") .grid(column=3, row=1)

# Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3)
    in_select = OptionMenu(mainframe, out_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram").grid(column=3, row=3,)
    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2,)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    in_field.focus()

###############################################################################################################################################
#AREA CONVERTER

def AreaConverter():
    root = Toplevel()
    root.title("Area Converter")

    mainframe = ttk.Frame(root, padding="3 30 12 12") #inc left | inc top | inc right | inc bottom
    mainframe.pack(fill=BOTH,expand=1)

    meterFactor = {'square meter': 1, 'square km': 1000000, 'square cm': 0.0001, 'square foot': 0.09290304,
                   'square inch': 0.00064516, 'square mile': 2589988.110336, 'milimeter': 0.000001,
                   'square acre': 4046.8564224}

    def convert(x, fromUnit, toUnit):
        if fromVar.get() in meterFactor.keys() and toVar.get() in meterFactor.keys():
            resultxt.delete(0, END)
            result = (float(str(x)) * meterFactor[fromUnit]) / (meterFactor[toUnit])
            resultxt.insert(0, str(result))

    titleLabel = Label(mainframe, text="Area Converter", font=("Arial", 12, "bold",), justify=CENTER, fg="orange").grid(column=1, row=1)

    e = Entry(mainframe)
    e.grid(row=1, column=2)
    values = list(meterFactor.keys())

    fromVar = StringVar(mainframe)
    toVar = StringVar(mainframe)

    fromVar.set("Select Unit")
    toVar.set("Select Unit")

    fromOption = OptionMenu(mainframe, fromVar, *values, command=lambda y: convert(e.get(), fromVar.get(), toVar.get()))
    fromOption.grid(row=1, column=3)

    toLabel = Label(mainframe, text="To: ", font="Arial").grid(row=2, column=2)

    toOption = OptionMenu(mainframe, toVar, *values, command=lambda x: convert(e.get(), fromVar.get(), toVar.get()))
    toOption.grid(row=3, column=3)

    resultxt = Entry(mainframe)
    resultxt.grid(row=3, column=2)

#############################################################################################################################################################
#LENGTH CONVERTER

def LengthConverter():

# factors to multiply to a value to convert from the following units to meters(m)
    factors = {'nmi' : 1852, 'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
    ids = {"Nautical Miles" : 'nmi', "Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "meters" : 'm', "centimeters" : 'cm', "millileters" : 'mm'}

# function to convert from a given unit to another
    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

# initiate window
    root = Toplevel()
    root.title("Length Converter")

# initiate frame
    mainframe = ttk.Frame(root, padding="3 30 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Length Converter", font = ("Arial", 12, "bold",), justify = CENTER, fg="orange").grid(column=1,row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

# Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2)

# Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=1)

# Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=3)
    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    in_field.focus()

###################################################################################################################################################################
#TEMPERATURE CONVERTER

def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()

        if celTempVar.get() != 0.0:
            celToFah = (celTemp * 9/5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5/9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=100, pady=100)
        top.grid()
        message = Label(top, text = "Reset Complete")
        button = Button(top, text="OK", command=top.destroy)
        message.grid(row = 0, padx = 55, pady = 8)
        button.grid(row = 1, ipadx = 15, ipady = 1, padx = 5, pady = 5)
        fahTempVar.set(int(0))
        celTempVar.set(int(0))

    top = Toplevel()
    top.title("Temperature Converter")
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))

    celLabel = Label (top, text = "Celcius: ", font = ("Arial", 20,"bold"), fg = "green")
    celLabel.grid(row = 2, column = 1, pady = 50, sticky = NW,padx = 100)

    fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 20,"bold"), fg = "blue")
    fahLabel.grid(row = 2, column = 1, pady = 100, sticky = NW,padx = 100)

    celEntry = Entry (top, width = 10, bd = 3, textvariable = celTempVar)
    celEntry.grid(row = 2, column = 1, pady = 50, sticky = NW, padx = 215 )

    fahEntry = Entry (top, width = 10, bd = 3, textvariable = fahTempVar)
    fahEntry.grid(row = 2, column = 1, pady = 100, sticky = NW, padx = 215 )

    convertButton =Button (top, text = "Convert", font = ("Arial", 12, "bold"), relief = RAISED, bd=3, justify = CENTER, overrelief = GROOVE, activeforeground="blue", command = convert)
    convertButton.grid(row = 3, column = 1, ipady = 2, ipadx = 12, pady = 1, sticky = NW, padx = 125)

    resetButton = Button (top, text = "Reset", font = ("Arial", 12, "bold"), relief = RAISED, bd=3, justify = CENTER, overrelief = GROOVE, activeforeground="blue", command = reset)
    resetButton.grid(row = 3, column = 1,ipady = 2, ipadx = 12, pady = 1, sticky = NW, padx = 240)

widget = Button(root, text="Temperature converter", bg="white" , fg="orange",font = ("Arial", 20, "bold"), relief = RAISED, overrelief = GROOVE, bd=2, justify = CENTER, command=TemperatureConverter).place(x=100,y=100,)
widget = Button(root, text="Length Converter", bg="white" , fg="orange",font = ("Arial", 20, "bold"), relief = RAISED, overrelief = GROOVE, bd=2, justify = CENTER, command=LengthConverter).place(x=100,y=160)
widget = Button(root, text="Area Converter", bg="white" , fg="orange",font = ("Arial", 20, "bold"), relief = RAISED, overrelief = GROOVE, bd=2, justify = CENTER, command=AreaConverter).place(x=100,y=220)
widget = Button(root, text="Weight Converter", bg="white" , fg="orange",font = ("Arial", 20, "bold"), relief = RAISED, overrelief = GROOVE, bd=2, justify = CENTER, command=WeightConverter).place(x=100,y=280)
widget = Button(root, text="QUIT", bg="white", fg="grey",font = ("arial", 15,"bold"),relief = RAISED, overrelief = GROOVE, bd=2, justify = CENTER, command=root.destroy).place(x=350,y=350)
root.mainloop()
