import tkinter as tk
r=tk.Tk()
r.title('ICON COMPUTER')

# Create Button
button= tk.Button(r,text='Exit',width=25,command=r.destroy)
button.pack()

r.mainloop()
