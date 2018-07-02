
import tkinter as tk
root = tk.Tk()
number_entry = tk.StringVar()
dropdown_variable = tk.StringVar()
temp_type = "farenheight"
def store_temp_type(user_temp):
    temp_type = user_temp
    print(temp_type)

def convert(): #Perfroms conversions
        temp_val = float(input_entry.get())
        if dropdown_variable.get() == "farenheight":#Convert from farenheight
            f2c = ((temp_val-32)*5)/9
            f2k = (temp_val+459.67)*(5/9)
            result_label_1.config(text = f2c)
            result_label_2.config(text = f2k)
            temp_desc1.config(text = "celcius:")
            temp_desc2.config(text = "kelvin:")
        elif dropdown_variable.get() == "celcius": #Convert from celcius
            c2f = temp_val*(9/5)+32
            c2k = temp_val+273.15
            result_label_1.config(text = c2f)
            result_label_2.config(text = c2k)
            temp_desc1.config(text = "farenheight:")
            temp_desc2.config(text = "kelvin:")
        else:                                      #Convert from kelvin
            k2f = temp_val*(9/5)-459.67
            k2c = temp_val-273.15
            result_label_1.config(text = k2f)
            result_label_2.config(text = k2c)
            temp_desc1.config(text = "farenheight:")
            temp_desc2.config(text = "celcius:")

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

convert_button = tk.Button(root, text = "CONVERT", command = convert)
convert_button.grid(row=1, column =1)

option_list = ["farenheight","celcius", "kelvin "]
dropdown= tk.OptionMenu(root,dropdown_variable,*option_list, command=store_temp_type)
dropdown_variable.set(option_list[0]) #Sets the initial temp option to be in farenheight
dropdown.grid(row=0, column=2)

temp_desc1 = tk.Label(root, text = "celcius:")
temp_desc2 = tk.Label(root, text = "kelvin:")
temp_desc1.grid(row=2, column=0)
temp_desc2.grid(row=3,column=0)

root.mainloop()
