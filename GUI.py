import Tkinter



#create root window
root = Tkinter.Tk()


#create widgets
lbl_title = Tkinter.label(root, text= "Chat")
lbl_title.pack()

lbl_result = Tkinter.Label(root, text="Good Luck!")

btn_check = Tkinter.Button(root, text="Check", fg="green", command=root.quit)
btn_check.pack(side="left")

btn_reset = Tkinter.Button(root, text="Reset", fg="red", command=root.quit)
btn_check.pack(side="right")

txt_guess = Tkinter.Entry(root, width=3)
txt_guess.pack()


#start the main events
root.mainloop()
root.destroy()
