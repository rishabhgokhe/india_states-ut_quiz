import turtle
import pandas
from tkinter import messagebox

FONT = ("Courier", 12, "normal")

screen = turtle.Screen()
screen.setup(700, 800)
screen.title("INDIA State Game")
image = "india_state.gif"
turtle.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv("states_coordinate.csv")
states_list = data_states["state"].to_list()
states_guessed_list = []

ut_states = pandas.read_csv("union_territory_coordinates.csv")
ut_list = ut_states["ut"].to_list()
ut_guessed_list = []

while len(states_guessed_list) < 36:
    answer = screen.textinput(
        title=f"Guessed {len(states_guessed_list)}/28-{len(ut_guessed_list)}/8 states,UT correctly",
        prompt="Enter the state name").title()
    if answer == "Exit":
        missing_list = []
        for state in states_list:
            if state not in states_guessed_list:
                missing_list.append(state)
        for ut_state in ut_list:
            if ut_state not in ut_guessed_list:
                missing_list.append(ut_state)

        # ------------------ tried generating popup by tkinter Toplevel Window ------------------ #
        # window = tkinter.Tk()
        # popup = tkinter.Toplevel(window)
        # popup.config(pady=40, padx=40)
        # popup.title("You missed all of this.")
        # title_label = tkinter.Label(text=str(missing_list))
        # title_label.pack()
        # ok_button = tkinter.Button(text="okay", command=popup.destroy)
        # popup.mainloop()

        messagebox.showinfo(title="You missed out this.", message=f"Missing States/UT: \n{str(missing_list)}")
        print(missing_list)
        break
    if answer in states_list:
        states_guessed_list.append(answer)
        t = turtle.Turtle()
        t.penup()
        state_data = data_states[data_states["state"] == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, font=FONT)
    elif answer in ut_list:
        ut_guessed_list.append(answer)
        t = turtle.Turtle()
        t.penup()
        ut_data = ut_states[ut_states["ut"] == answer]
        t.goto(int(ut_data.x), int(ut_data.y))
        t.write(answer, font=FONT)

# --------------------------------- Code for getting coordinates in turtle grid --------------------------------- #
# def get_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_coordinates)
# screen.mainloop()
