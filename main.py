import tkinter

# Create the root window
root = tkinter.Tk()

# Set title of the window
root.title('GUI Window')

# Create a label
label = tkinter.Label(root, text='Welcome to GUI Window', font=("Times New Roman", 20))

# Position the label on the center of the window
label.pack(fill="both", expand=1)

# Execute the main loop
root.mainloop()