from tkinter import *

root = Tk()
root.title("Color")
root.geometry("600x400")
root.configure(background='white')

main_frame = Frame(root, background='white')
main_frame.pack()


def update_color(frame, name, code):
    frame.entry_name.delete(0, END)
    frame.entry_name.insert(0, name)
    frame.entry_code.delete(0, END)
    frame.entry_code.insert(0, code)
    root.configure(background=code)


def create_color_frame(frame, name, code):
    frame.entry_name = Entry(frame, width=20, justify='left')
    frame.entry_name.pack(side=LEFT, padx=10)

    Button(frame, text=name, bg=code, fg="black", width=20, 
           command=lambda: update_color(frame, name, code)).pack(side=LEFT, padx=10, pady=5)

    frame.entry_code = Entry(frame, width=20, justify='right')
    frame.entry_code.pack(side=RIGHT, padx=10)


frame1 = Frame(main_frame, background='white')
frame1.pack()
create_color_frame(frame1, "Light Pink", "#FFB6C1")

frame2 = Frame(main_frame, background='white')
frame2.pack()
create_color_frame(frame2, "Hot Pink", "#FF69B4")

frame3 = Frame(main_frame, background='white')
frame3.pack()
create_color_frame(frame3, "Deep Pink", "#FF1493")

frame4 = Frame(main_frame, background='white')
frame4.pack()
create_color_frame(frame4, "Pale Violet Red", "#DB7093")

frame5 = Frame(main_frame, background='white')
frame5.pack()
create_color_frame(frame5, "Medium Violet Red", "#C71585")

frame6 = Frame(main_frame, background='white')
frame6.pack()
create_color_frame(frame6, "Pink", "#FFC0CB")

frame7 = Frame(main_frame, background='white')
frame7.pack()
create_color_frame(frame7, "Light Hot Pink", "#FF6EB4")

frame8 = Frame(main_frame, background='white')
frame8.pack()
create_color_frame(frame8, "Cherry Blossom Pink", "#FFB7C5")

frame9 = Frame(main_frame, background='white')
frame9.pack()
create_color_frame(frame9, "Blush Pink", "#FE6F5E")

frame10 = Frame(main_frame, background='white')
frame10.pack()
create_color_frame(frame10, "Orchid Pink", "#DA70D6")

root.mainloop()