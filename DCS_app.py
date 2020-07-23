# DCS App using Tkinter, Python3, and SMBus

from tkinter import *
from smbus import SMBus

#window setup
root = Tk()
root.wm_title("DCS Controller")
root.geometry("320x240")

# I2C init
addr = 0x8
bus = SMBus(1)            


#This is how we use the buttons to swtich between the different programs
prog = None

def PrgZero():
    global prog
    progLab.configure(text = "Program 0")
    prog = 0
    

def PrgOne():
    global prog
    progLab.configure(text = "Program 1")
    prog = 1
    
    
    
def PrgTwo():
    global prog
    progLab.configure(text = "Program 2")
    prog = 2

# This will call functions to program the DCS
def PrgDcs():
    # insert all of the DCS programming code here
    
    if prog == 0:
        #first program section
        DpmOnBoardBEOsprey()
        
        bus.write_byte(addr, 0x00);
       
    elif prog == 1:
        bus.write_byte(addr, 0x01)
        
    elif prog == 2:
        bus.write_byte(addr, 0x02)
        
    else:
        bus.write_byte(addr, 0x03)
        
# This function is just the Arduino code from DCS_REV02_DPM_OnBoard_BE_Osprey converted into python
def DpmOnBoardBEOsprey():
    DCS_I2C_MUX_ADR = 0x70
   
        
    
# When pressed it begins executing code to program the DCS
btnZero = Button(root, text = "0", command = PrgZero)
btnZero.place(x = 80, y = 100, height = 50, width = 50, anchor = CENTER)

btnOne = Button(root, text = "1", command = PrgOne)
btnOne.place(x = 160, y = 100, height = 50, width = 50, anchor = CENTER)

btnTwo = Button(root, text = "2", command = PrgTwo)
btnTwo.place(x = 240, y = 100, height = 50, width = 50, anchor = CENTER)

runProgBtn = Button(root, text = "Program DCS", command = PrgDcs)
runProgBtn.place(x = 160, y = 200, anchor = CENTER)

# This is the label to identify which program has been selected
progLab = Label(root, text = "None")
progLab.place(x = 160, y = 50, anchor = CENTER)



# start the main gui loop when everything is ready
root.mainloop() 