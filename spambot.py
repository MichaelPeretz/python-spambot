from tkinter import *
import pyautogui as pag


window = Tk()
window.geometry("300x120")


window.resizable(False, False)


window.title("Michael Spam Bot")
spam_input = StringVar()
number_input = StringVar()


spam_input_box = Entry(window, textvariable=spam_input, font=("Hervetica", "16"))
spam_input_box.grid(row=2, column=1, pady=6)


number_input_box = Entry(window, textvariable=number_input, font=("Hervetica", "16"))
number_input_box.grid(row=3, column=1, pady=6)


def buttonClick():
    for i in range(int(number_input.get())):
        pyautogui.typewrite(spam_input.get())
        pyautogui.press("enter")


start_btn = Button(window, text="Start", bg="#34495e", fg="#fff", font=("Helventica", "12"), command=buttonClick)
start_btn.grid(row=4, column=1, pady=6)


exit_button = Button(window, text="Exit", bg="#34495e", fg="#fff", font=("Helventica", "12"), command=window.destroy)
exit_button.grid(row=4, column=2, pady=6)


window.mainloop()