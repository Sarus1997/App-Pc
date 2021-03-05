import tkinter as tk

def show():
    number = int(number_input.get())
    if number == 0:
        output_label.configure(text='ผิด')
        return

    output = ' '
    for i in range(1,31):
        output += str(number) + ' x ' + str(i)
        output += '=' + str(number*i) + '\n'

        output_label.configure(text = output)

window = tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=500,height=400)

title_label = tk.Label(master=window, text='สูตรคูณ')
title_label.pack(pady=10)

number_input = tk.Entry(master=window)
number_input.pack()

ok_button = tk.Button(master=window, text='ผลลัพธ์', command=show)
ok_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()