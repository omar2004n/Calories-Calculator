from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from os import system

system("cls")


class wind:
    def __init__(self, root: Tk):
        bgcol = "#74b9ff"
        self.root = root
        self.root.geometry("630x620")
        self.root.resizable(FALSE, FALSE)
        self.root.config(bg=bgcol)
        self.root.grid_propagate(0)
        self.root.pack_propagate(0)
        style = ttk.Style()

        """ Entries for height ,weight and age"""
        ent = [Entry(self.root, width=5,) for i in range(3)]
        ent.append(ttk.Combobox(self.root, values=[
                   'Male', 'Female'], state='readonly', width=10))
        s = ['height', 'weight', 'age', 'gender']
        i = 1
        Label(self.root, text="Calories   Calculator", font=("TROUPERS", 30),
              bg=bgcol).pack(side='top', pady=30, padx=30)
        Label(self.root, bg=bgcol).grid(row=0, column=0, pady=50, )
        Label(self.root, bg=bgcol).grid(row=1, column=0, padx=90, )
        act = [
            "Sedentary (little or no exercise)",
            "Lightly active (light exercise or sports 1-3 days a week)",
            "Moderately active (moderate exercise or sports 3-5 days a week)",
            "Very active (hard exercise or sports 6-7 days a week)",
            "Super active (extreme exercise and a physical job twice a day)"]

        def calc(act):
            if ent[3].get() == 'Male':
                i = 88.362 + (13.397 * float(ent[1].get())) + (
                    4.799 * float(ent[0].get())) - (5.677 * float(ent[2].get()))
            elif ent[3].get() == 'Female':
                i = 447.593 + (9.247 * float(ent[1].get())) + (
                    3.098 * float(ent[0].get())) - (4.330 * float(ent[2].get()))
            match act.index(freq.get()):
                case 0:
                    i *= 1.2
                case 1:
                    i *= 1.375
                case 2:
                    i *= 1.55
                case 3:
                    i *= 1.725
                case 4:
                    i *= 1.9
            msg.showinfo('result', message='Needed calories : ' +
                         str(round(i, 2)),)

        for x in ent:
            x.grid(row=i, column=2, pady=20,)
            Label(self.root, text=s[i-1], bg=bgcol, font=('EVOGRIA')).grid(row=i,
                                                                           column=1, pady=10, padx=50)
            i += 1

        ent[3].current(0)
        freq = ttk.Combobox(self.root, values=act, width=60, state='readonly')

        freq.current(0)
        done = Button(self.root, text='Show results',
                      font=("verdana", 10, 'bold'), bg='#0984e3', command=lambda: calc(act))
        done.pack(side=BOTTOM, pady=60,)
        freq.pack(side="bottom", pady=0)
        self.root.mainloop()


w = wind(Tk())
