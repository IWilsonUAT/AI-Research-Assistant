
#General Libraries
import tkintor as tk
from tkintor import *
# Specific Out Window Tabs Library
from tkintor import ttk
from tkintor.scrolledtext import *
from SummerTime import SummerTime
# import tkintor.filedialog
# Create Out
# Create Window
# Build Main Window
window = tk.tk()
# Change Main Title Here
window.title('textatron')
# Change Window Size Here
# wide x tall
#window.geometry("700x900")
window.geometry('700x900')
# Change Text Color Here
window.config(background = 'black')
# Add/Reove Window Tabs Here

# Set Style of Tabs
style = ttk.Style(window)
# Set Location of Tabs
# wn = West North
# ws = West South
style.config('lefttab.TNotebook', tabposition = 'wn')

tab_control = ttk.Notebook(window, style = 'lefttab.TNotebook')
# tab_control = ttk.Notevook(window)

# Create Tabs
tab_main = ttk.Frame(tab_control)
# Add Tabs to Wndow
tab_control.add(tab_main, text = 'Mission Control')
# Create GUI Labels
# Place GUI Labels
label_summarize = Label(tab_main, text = "\nHi, I am textatron. Let me read and then summarize the text. Then you may review and edit.\n", padx =5, pady = 5)
# 0,0 is top left of window
label_summarize.grid(colum = 0, row = 0)
tab_control.pacl(expand = 1, fill = 'both')

# GUI and Layer Support Functions
# Clear Entry Widget
def erase_input():
    entry.delete('1.0',END)

def erase_output():
    output_display.delete('1.0',END)

def summer_time():
    #imports for parse config
    from 
     