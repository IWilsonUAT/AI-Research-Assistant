
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
    #imports for parser_config
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizers
    text_format = entry.get('1.0',tk.END)
    # We can use this parse format format for all three when we use raw strings
    parser_config = PlaintextParser.from_string(text_format, Tokenizer("english"))
    summerTime = SummerTime()
    summer_all = summerTime.lex_rank_analysis(parse_config, 2)
    # summer_all = print(), summer_all
    summer_all = summer_all + summerTime.luhn_analysis(parser_config, 2)
     # summer_all = print(), summer_all
    summer_all = summer_all + summerTime.lsa_analysis(parser_config, 2)
    scrubbed = []
    for sentance in summer_all:
         concat = str(sentance) + "\n\n\n"
         concat.replace("","{")
         concat.replace("","}")
         scrubbed.append(concat)
    output_display.insert(tk.END, scrubbed)
    print("\nAbout to print summer all results\n")
    print(summer_all)

# Build Main Home Tab
label_text_to_summarize = Label(tab_main, text = 'Enter Text to Summarize', padx = 5, pady = 5)
label_text_to_summarize.grid(row = 1, colum = 0)
entry = ScrolledText(tab_main, height = 30)
entryt.grid(row = 2, colum = 0, columspan = 5, padx = 5, pady = 5)

# User Action Controls and Events
button_run = Button(tab_mian, text = "Invoke Tex-A-Tron", command = summer_time, width = 22, bg = '#25d366', fg = '#fff' )





output_display = ScrollText(tab_main)
output_display.grid(row = 9, colum = 0, columspan = 5, padx = 5, pady = 5)



window.mainloop()