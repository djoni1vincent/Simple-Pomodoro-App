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
is_running = False
current_count = 0

# ---------------------------- TIMER RESET ------------------------------- #]
def reset():
    global reps, is_running, current_count
    reps = 0
    is_running = False
    current_count = 0
    window.after_cancel(timer_l)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Pomodoro", fg=GREEN)
    start.config(text="Start")
    checkmark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps, is_running, current_count
    short_break_s = SHORT_BREAK_MIN * 60
    long_break_s = LONG_BREAK_MIN * 60
    work_s = WORK_MIN * 60

    if is_running:
        is_running = False
        start.config(text="Start")
        window.after_cancel(timer_l)
        return

    is_running = True
    start.config(text="Stop")

    if current_count > 0:
        count_down(current_count)
        return

    reps += 1

    if reps % 8 == 0:
        current_count = LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=GREEN)
    elif reps % 2 == 0:
        current_count = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", fg=PINK)
        checkmark['text'] += "✔"
    else:
        current_count = WORK_MIN * 60
        timer_label.config(text="Work", fg=RED)

    count_down(current_count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer_l, current_count

    current_count = count

    min = count // 60
    sec = count % 60
    canvas.itemconfig(timer_text, text=f"{min:02}:{sec:02}")

    if count > 0 and is_running:
        timer_l = window.after(1000, count_down, count - 1)
    elif count == 0:
        current_count = 0
        timer_start()


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
