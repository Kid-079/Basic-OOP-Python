import tkinter

main_window = tkinter

label1 = tkinter.Label(main_window, text = "Life Is Like Riding A Bicycle. To Keep Your Balance, You Must Keep Moving")
label1 = tkinter.Label(main_window, text = "What Ever You Are, Be A Good One")

button1 = tkinter.Button(main_window, text = "Press Button 1")
button2 = tkinter.Button(main_window, text = "Press Button 2")

# Method Positioning
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# Method Show GUI
main_window.mainloop()