import math

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_l = None

# ---------------------------- TIMER RESET ------------------------------- #]
def reset():
    global reps
    reps = 0
    window.after_cancel(timer_l)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Pomodoro", fg=GREEN)



# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    reps += 1

    short_break_s = SHORT_BREAK_MIN * 60
    long_break_s = LONG_BREAK_MIN * 60
    work_s = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_s)
        timer_label.config(text="Break", fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_s)
        timer_label.config(text="Break", fg=PINK)
        if len(checkmark["text"]) == 4:
              checkmark['text'] = ""
        checkmark['text'] += "✔"

    else:
        count_down(work_s)
        timer_label.config(text="Work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_l
        timer_l = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        # if reps % 2 == 0:

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.maxsize(425,380)
window.minsize(425,380)
window.title("Pomodoro App")
window.config(padx=40, pady=40, bg=YELLOW)

timer_label = Label(text="Pomodoro", font=(FONT_NAME, 34, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# img
canvas = Canvas(width=200, height=228, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png", )
canvas.create_image(100, 105, image=tomato)
timer_text = canvas.create_text(100,125, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=1, column=1)

# buttons
start = Button(text="Start", command=timer_start, highlightthickness=0, bg=RED, fg=YELLOW, font=(FONT_NAME, 10, "bold"))
start.grid(row=2, column=0)

checkmark = Label(text="✔", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset, highlightthickness=0, bg=RED, fg=YELLOW, font=(FONT_NAME, 10, "bold"))
reset_button.grid(row=2, column=2)


window.mainloop()
