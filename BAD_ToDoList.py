from tkinter import *
from tkinter import font
from tkinter import simpledialog
from tkinter import messagebox


class SetupEvents:
    def __init__(self):
        self.typed_task: str = None
        self.typed_month: str = None
        self.typed_day: str = None
        self.typed_hour: str = None
        self.typed_minute: str = None
        self.current_task_we_are_on: int = 0
        self.task_return_label: list = ["", "", "", "", "", "", "", "", "", ""]
        self.date_return_label: list = ["", "", "", "", "", "", "", "", "", ""]
        self.time_return_label: list = ["", "", "", "", "", "", "", "", "", ""]

    def validate_task_entry(self, text):
        if len(text) <= 20:
            return True
        else:
            return False

    def validate_month_entry(self, text):
        if len(text) <= 2:
            return True
        else:
            return False

    def validate_day_entry(self, text):
        if len(text) <= 2:
            return True
        else:
            return False

    def validate_hour_entry(self, text):
        if len(text) <= 2:
            return True
        else:
            return False

    def validate_minute_entry(self, text):
        if len(text) <= 2:
            return True
        else:
            return False

    def task_on_entry_change(self, *args):
        self.typed_task = task_entry_var.get()

    def month_on_entry_change(self, *args):
        self.typed_month = month_entry_var.get()

    def day_on_entry_change(self, *args):
        self.typed_day = day_entry_var.get()

    def hour_on_entry_change(self, *args):
        self.typed_hour = hour_entry_var.get()

    def minute_on_entry_change(self, *args):
        self.typed_minute = minute_entry_var.get()

    def add_button_on_press_event(self):
        # Turn the task1_label into self.typed_task
        self.task_return_label[self.current_task_we_are_on] = self.typed_task

        # Turn the date1_label into input
        self.date_return_label[self.current_task_we_are_on] = f"{self.typed_month}/{self.typed_day}"

        # Turn the time1_label into input
        self.time_return_label[self.current_task_we_are_on] = f"{self.typed_hour}:{self.typed_minute}"

        if self.current_task_we_are_on == 0:
            task0_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date0_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time0_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 1:
            task1_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date1_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time1_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 2:
            task2_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date2_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time2_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 3:
            task3_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date3_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time3_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 4:
            task4_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date4_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time4_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 5:
            task5_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date5_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time5_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 6:
            task6_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date6_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time6_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 7:
            task7_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date7_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time7_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 8:
            task8_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date8_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time8_label.config(text=self.time_return_label[self.current_task_we_are_on])
        elif self.current_task_we_are_on == 9:
            task9_label.config(text=self.task_return_label[self.current_task_we_are_on])
            date9_label.config(text=self.date_return_label[self.current_task_we_are_on])
            time9_label.config(text=self.time_return_label[self.current_task_we_are_on])

        self.current_task_we_are_on += 1

    def edit_button_on_press_event(self, task_number):
        # opens window and lets you input information
        task_user_input = simpledialog.askstring("Input", "Enter your new task name:")
        date_user_input = simpledialog.askstring("Input", "Enter your new date (e.g. 04/12):")
        time_user_input = simpledialog.askstring("Input", "Enter your new tune (e.g. 11:11):")
        if task_user_input or date_user_input or time_user_input:
            messagebox.showinfo("User Input", f"Your input: {task_user_input}")
        else:
            messagebox.showerror("Error", "Please enter some text.")
        # once submit button gets pressed, information of task will update
        return

    def delete_button_on_press_event(self, task_number):
        # deletes task after getting prompted by pop-up window
        # if there are tasks below, the tasks below will shift up once
        return


root = Tk()
root.title("To-Do-List")
root.geometry("500x500+1400+250")
root.resizable(True, True)
root.configure(bg="#313338")

to_do_list = SetupEvents()

# root.grid_rowconfigure(0, weight=1, uniform="row_height")
universal_font = font.Font(family="Roboto Condensed", size=12)
button_font = font.Font(family="Roboto Condensed", size=15)
label_font = font.Font(family="Roboto Condensed", size=12)
emoji_font = font.Font(family="Segoe UI Emoji", size=12)
section_two_font = font.Font(family="Roboto Condensed", size=12)


add_task_button = Button(text="+", font=button_font, relief="flat", bg="#313338", fg="#B5BAC1",
                         command=to_do_list.add_button_on_press_event)

# Limits task_entry characters to 20
validate_task_entry_cmd = root.register(to_do_list.validate_task_entry)
task_entry_var = StringVar()
task_entry_var.trace("w", to_do_list.task_on_entry_change)
type_task_name_entry_box = Entry(font=universal_font, bg="#383A40", fg="#B5BAC1", textvariable=task_entry_var,
                                 validate="key", validatecommand=(validate_task_entry_cmd, '%P'))

due_date_label = Label(text="  Due:", font=label_font, bg="#313338", fg="#B5BAC1")

# Limits month_entry characters to 2
validate_month_entry_cmd = root.register(to_do_list.validate_month_entry)
month_entry_var = StringVar()
month_entry_var.trace("w", to_do_list.month_on_entry_change)
month_entry_box = Entry(font=universal_font, width=2, bg="#383A40", fg="#B5BAC1", textvariable=month_entry_var,
                        validate="key", validatecommand=(validate_month_entry_cmd, '%P'))

slash_label = Label(text="/", font=label_font, bg="#313338", fg="#B5BAC1")

# Limits day_entry characters to 2
validate_day_entry_cmd = root.register(to_do_list.validate_day_entry)
day_entry_var = StringVar()
day_entry_var.trace("w", to_do_list.day_on_entry_change)
day_entry_box = Entry(font=universal_font, width=2, bg="#383A40", fg="#B5BAC1", textvariable=day_entry_var,
                      validate="key", validatecommand=(validate_day_entry_cmd, '%P'))

at_label = Label(text="  @", font=label_font, bg="#313338", fg="#B5BAC1")

# Limits hour_entry characters to 2
validate_hour_entry_cmd = root.register(to_do_list.validate_hour_entry)
hour_entry_var = StringVar()
hour_entry_var.trace("w", to_do_list.hour_on_entry_change)
hour_entry_box = Entry(font=universal_font, width=2, bg="#383A40", fg="#B5BAC1", textvariable=hour_entry_var,
                       validate="key", validatecommand=(validate_hour_entry_cmd, '%P'))

colon_label = Label(text=":", font=label_font, bg="#313338", fg="#B5BAC1")

# Limits minute_entry characters to 2
validate_minute_entry_cmd = root.register(to_do_list.validate_minute_entry)
minute_entry_var = StringVar()
minute_entry_var.trace("w", to_do_list.minute_on_entry_change)
minute_entry_box = Entry(font=universal_font, width=2, bg="#383A40", fg="#B5BAC1", textvariable=minute_entry_var,
                         validate="key", validatecommand=(validate_minute_entry_cmd, '%P'))

# Top UI for Adding New Tasks with details of (1) Task Name, (2) Month/Day, (3) Hour/Minute
add_task_button.grid(row=0, column=0)
type_task_name_entry_box.grid(row=0, column=1)
due_date_label.grid(row=0, column=2)
month_entry_box.grid(row=0, column=3)
slash_label.grid(row=0, column=4)
day_entry_box.grid(row=0, column=5)
at_label.grid(row=0, column=6)
hour_entry_box.grid(row=0, column=7)
colon_label.grid(row=0, column=8)
minute_entry_box.grid(row=0, column=9)

# Invisible Divider
divider_label = Label(text="", bg="#313338")
divider_label.grid(row=1, column=2, rowspan=2, columnspan=9)

# Headers
done_header_label = Label(text="Done", font=label_font, bg="#313338", fg="#B5BAC1")
task_name_header_label = Label(text="Things to Do", font=label_font, bg="#313338", fg="#B5BAC1")
date_header_label = Label(text="Date", font=label_font, bg="#313338", fg="#B5BAC1")
time_header_label = Label(text="Time", font=label_font, bg="#313338", fg="#B5BAC1")
edit_header_label = Label(text="Edit", font=label_font, bg="#313338", fg="#B5BAC1")
delete_header_label = Label(text="Delete", font=label_font, bg="#313338", fg="#B5BAC1")

done_header_label.grid(row=3, column=0)
task_name_header_label.grid(row=3, column=1, columnspan=3)
date_header_label.grid(row=3, column=4, columnspan=3)
time_header_label.grid(row=3, column=7, columnspan=3)
edit_header_label.grid(row=3, column=10, columnspan=3)
delete_header_label.grid(row=3, column=13, columnspan=3)

# Checkboxes
checkbox0 = Checkbutton(bg="#313338")
checkbox1 = Checkbutton(bg="#313338")
checkbox2 = Checkbutton(bg="#313338")
checkbox3 = Checkbutton(bg="#313338")
checkbox4 = Checkbutton(bg="#313338")
checkbox5 = Checkbutton(bg="#313338")
checkbox6 = Checkbutton(bg="#313338")
checkbox7 = Checkbutton(bg="#313338")
checkbox8 = Checkbutton(bg="#313338")
checkbox9 = Checkbutton(bg="#313338")
checkbox0.grid(row=4, column=0)
checkbox1.grid(row=5, column=0)
checkbox2.grid(row=6, column=0)
checkbox3.grid(row=7, column=0)
checkbox4.grid(row=8, column=0)
checkbox5.grid(row=9, column=0)
checkbox6.grid(row=10, column=0)
checkbox7.grid(row=11, column=0)
checkbox8.grid(row=12, column=0)
checkbox9.grid(row=13, column=0)

# Task Labels
task0_label = Label(text=to_do_list.task_return_label[0], bg="#313338", fg="#B5BAC1", font=section_two_font)
task1_label = Label(text=to_do_list.task_return_label[1], bg="#313338", fg="#B5BAC1", font=section_two_font)
task2_label = Label(text=to_do_list.task_return_label[2], bg="#313338", fg="#B5BAC1", font=section_two_font)
task3_label = Label(text=to_do_list.task_return_label[3], bg="#313338", fg="#B5BAC1", font=section_two_font)
task4_label = Label(text=to_do_list.task_return_label[4], bg="#313338", fg="#B5BAC1", font=section_two_font)
task5_label = Label(text=to_do_list.task_return_label[5], bg="#313338", fg="#B5BAC1", font=section_two_font)
task6_label = Label(text=to_do_list.task_return_label[6], bg="#313338", fg="#B5BAC1", font=section_two_font)
task7_label = Label(text=to_do_list.task_return_label[7], bg="#313338", fg="#B5BAC1", font=section_two_font)
task8_label = Label(text=to_do_list.task_return_label[8], bg="#313338", fg="#B5BAC1", font=section_two_font)
task9_label = Label(text=to_do_list.task_return_label[9], bg="#313338", fg="#B5BAC1", font=section_two_font)
task0_label.grid(row=4, column=1, columnspan=3)
task1_label.grid(row=5, column=1, columnspan=3)
task2_label.grid(row=6, column=1, columnspan=3)
task3_label.grid(row=7, column=1, columnspan=3)
task4_label.grid(row=8, column=1, columnspan=3)
task5_label.grid(row=9, column=1, columnspan=3)
task6_label.grid(row=10, column=1, columnspan=3)
task7_label.grid(row=11, column=1, columnspan=3)
task8_label.grid(row=12, column=1, columnspan=3)
task9_label.grid(row=13, column=1, columnspan=3)

# Date Labels (Months and Days Combined)
date0_label = Label(text=to_do_list.date_return_label[0], bg="#313338", fg="#B5BAC1", font=section_two_font)
date1_label = Label(text=to_do_list.date_return_label[1], bg="#313338", fg="#B5BAC1", font=section_two_font)
date2_label = Label(text=to_do_list.date_return_label[2], bg="#313338", fg="#B5BAC1", font=section_two_font)
date3_label = Label(text=to_do_list.date_return_label[3], bg="#313338", fg="#B5BAC1", font=section_two_font)
date4_label = Label(text=to_do_list.date_return_label[4], bg="#313338", fg="#B5BAC1", font=section_two_font)
date5_label = Label(text=to_do_list.date_return_label[5], bg="#313338", fg="#B5BAC1", font=section_two_font)
date6_label = Label(text=to_do_list.date_return_label[6], bg="#313338", fg="#B5BAC1", font=section_two_font)
date7_label = Label(text=to_do_list.date_return_label[7], bg="#313338", fg="#B5BAC1", font=section_two_font)
date8_label = Label(text=to_do_list.date_return_label[8], bg="#313338", fg="#B5BAC1", font=section_two_font)
date9_label = Label(text=to_do_list.date_return_label[9], bg="#313338", fg="#B5BAC1", font=section_two_font)
date0_label.grid(row=4, column=4, columnspan=3)
date1_label.grid(row=5, column=4, columnspan=3)
date2_label.grid(row=6, column=4, columnspan=3)
date3_label.grid(row=7, column=4, columnspan=3)
date4_label.grid(row=8, column=4, columnspan=3)
date5_label.grid(row=9, column=4, columnspan=3)
date6_label.grid(row=10, column=4, columnspan=3)
date7_label.grid(row=11, column=4, columnspan=3)
date8_label.grid(row=12, column=4, columnspan=3)
date9_label.grid(row=13, column=4, columnspan=3)

# Time Labels (Hours and Minutes Combined)
time0_label = Label(text=to_do_list.time_return_label[0], bg="#313338", fg="#B5BAC1", font=section_two_font)
time1_label = Label(text=to_do_list.time_return_label[1], bg="#313338", fg="#B5BAC1", font=section_two_font)
time2_label = Label(text=to_do_list.time_return_label[2], bg="#313338", fg="#B5BAC1", font=section_two_font)
time3_label = Label(text=to_do_list.time_return_label[3], bg="#313338", fg="#B5BAC1", font=section_two_font)
time4_label = Label(text=to_do_list.time_return_label[4], bg="#313338", fg="#B5BAC1", font=section_two_font)
time5_label = Label(text=to_do_list.time_return_label[5], bg="#313338", fg="#B5BAC1", font=section_two_font)
time6_label = Label(text=to_do_list.time_return_label[6], bg="#313338", fg="#B5BAC1", font=section_two_font)
time7_label = Label(text=to_do_list.time_return_label[7], bg="#313338", fg="#B5BAC1", font=section_two_font)
time8_label = Label(text=to_do_list.time_return_label[8], bg="#313338", fg="#B5BAC1", font=section_two_font)
time9_label = Label(text=to_do_list.time_return_label[9], bg="#313338", fg="#B5BAC1", font=section_two_font)
time0_label.grid(row=4, column=7, columnspan=3)
time1_label.grid(row=5, column=7, columnspan=3)
time2_label.grid(row=6, column=7, columnspan=3)
time3_label.grid(row=7, column=7, columnspan=3)
time4_label.grid(row=8, column=7, columnspan=3)
time5_label.grid(row=9, column=7, columnspan=3)
time6_label.grid(row=10, column=7, columnspan=3)
time7_label.grid(row=11, column=7, columnspan=3)
time8_label.grid(row=12, column=7, columnspan=3)
time9_label.grid(row=13, column=7, columnspan=3)

# Edit Buttons
edit_button0 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(1))
edit_button1 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(2))
edit_button2 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(3))
edit_button3 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(4))
edit_button4 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(5))
edit_button5 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(6))
edit_button6 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(7))
edit_button7 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(8))
edit_button8 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                      command=lambda: to_do_list.edit_button_on_press_event(9))
edit_button9 = Button(text="📝", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                       command=lambda: to_do_list.edit_button_on_press_event(10))
edit_button0.grid(row=4, column=10, columnspan=3)
edit_button1.grid(row=5, column=10, columnspan=3)
edit_button2.grid(row=6, column=10, columnspan=3)
edit_button3.grid(row=7, column=10, columnspan=3)
edit_button4.grid(row=8, column=10, columnspan=3)
edit_button5.grid(row=9, column=10, columnspan=3)
edit_button6.grid(row=10, column=10, columnspan=3)
edit_button7.grid(row=11, column=10, columnspan=3)
edit_button8.grid(row=12, column=10, columnspan=3)
edit_button9.grid(row=13, column=10, columnspan=3)

# Delete Buttons
delete_button0 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(1))
delete_button1 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(2))
delete_button2 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(3))
delete_button3 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(4))
delete_button4 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(5))
delete_button5 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(6))
delete_button6 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(7))
delete_button7 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(8))
delete_button8 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                        command=lambda: to_do_list.delete_button_on_press_event(9))
delete_button9 = Button(text="🗑️", font=emoji_font, bg="#383A40", fg="#B5BAC1",
                         command=lambda: to_do_list.delete_button_on_press_event(10))
delete_button0.grid(row=4, column=13, columnspan=3)
delete_button1.grid(row=5, column=13, columnspan=3)
delete_button2.grid(row=6, column=13, columnspan=3)
delete_button3.grid(row=7, column=13, columnspan=3)
delete_button4.grid(row=8, column=13, columnspan=3)
delete_button5.grid(row=9, column=13, columnspan=3)
delete_button6.grid(row=10, column=13, columnspan=3)
delete_button7.grid(row=11, column=13, columnspan=3)
delete_button8.grid(row=12, column=13, columnspan=3)
delete_button9.grid(row=13, column=13, columnspan=3)

root.mainloop()
