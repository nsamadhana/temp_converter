import tkinter as tk
root = tk.Tk()

number_entry = tk.StringVar()
dropdown_variable = tk.StringVar()

temp_input_label = tk.Label(root, text="Enter a temperature")
input_entry = tk.Entry(root, textvariable=number_entry)
result_label_1 = tk.Label(root, text = "result1")
result_label_2 = tk.Label(root, text = "result2")
input_entry.grid(row=0, column=1) #Positions entry box
temp_input_label.grid(row=0)
result_label_1.grid(row=2, column = 1)
result_label_2.grid(row=3, column = 1)

option_list = ["celcius", "farenheight", "kelvin "]
dropdown= tk.OptionMenu(root,dropdown_variable,*option_list)
dropdown_variable.set(option_list[1])
dropdown.grid(row=0, column=2)

result_button = tk.Button(root, text = "CONVERT")
result_button.grid(row=1, column =1)




root.mainloop()
