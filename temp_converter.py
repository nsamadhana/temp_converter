import tkinter as tk
from functools import partial
root = tk.Tk()

def store_temp_type(user_temp):
    temp_type = user_temp
    print(temp_type)

def call_back():
        temp_val = input_entry.get()
        print(temp_val)


number_entry = tk.StringVar()
dropdown_variable = tk.StringVar()
'''
frame1 = tk.Frame(root, width = 300, height = 200, background="bisque")
frame1.pack()
'''
root.configure(background = "bisque")


temp_input_label = tk.Label(root, text="Enter a temperature")
#temp_input_label.configure(background = "grey")
temp_input_label.grid(row=0)
input_entry = tk.Entry(root, textvariable=number_entry) #User number input

input_entry.grid(row=0, column=1) #Positions entry box

#After converting, the result is the two different temperature types
result_label_1 = tk.Label(root, text = "result1")
result_label_2 = tk.Label(root, text = "result2")
result_label_1.grid(row=2, column = 1)
result_label_2.grid(row=3, column = 1)


convert_button = tk.Button(root, text = "CONVERT", command = call_back)
convert_button.grid(row=1, column =1)

option_list = ["farenheight","celcius", "kelvin "]
dropdown= tk.OptionMenu(root,dropdown_variable,*option_list, command=store_temp_type)
dropdown_variable.set(option_list[1]) #Sets the initial temp option to be in farenheight
dropdown.grid(row=0, column=2)

root.mainloop()
