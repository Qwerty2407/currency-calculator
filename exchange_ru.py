from tkinter import *
from tkinter.ttk import Combobox
from pycbrf.toolbox import ExchangeRates
from datetime import *


window = Tk()
window.title("Калькулятор валют v.1")
window.geometry("800x800")


c = Canvas(width=800, height=300, bg="orange")
p = Canvas(width=800, height=300, bg="orange")
t = Canvas(width=800, height=200, bg="orange")


c.pack()
p.pack()
t.pack()


c.create_text(50, 50, text="Выберите первую валюту", anchor=NW, font='Arial 18', fill="black")
p.create_text(50, 50, text="Выберите вторую валюту", anchor=NW, font='Arial 18', fill="black")
c.create_text(50, 150, text="Укажите количество", anchor=NW, font='Arial 18', fill="black")


methods = ['USD', 'EUR', 'RUB', 'BYN', 'PLN']
combobox = Combobox(values=methods, width=30, state='readonly')
c.create_window(100, 100, anchor=CENTER, window=combobox, width=100, height=30)
combobox.set("USD")


ent = Entry()
c.create_window(100, 200, anchor=CENTER, window=ent, width=100, height=30)
ent.insert(0, "1")


combobox2 = Combobox(value=methods, width=30, state='readonly')
p.create_window(100, 100, anchor=CENTER, window=combobox2, width=100, height=30)
combobox2.set("USD")


btn = Button(text='Рассчитать', command=lambda: result_btn(combobox.get(), combobox2.get(), float(ent.get())))
p.create_window(600, 200, window=btn, width=100, height=50)


date = datetime.now().date()
rates = ExchangeRates(str(date))


def usd_eur(num):
    t.delete(ALL)
    result = rates["USD"].value
    result2 = rates["EUR"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def usd_rub(num):
    t.delete(ALL)
    result = float(rates["USD"].value)
    result2 = round(result * float(num), 2)
    t.create_text(400, 100, text=str(result2), font="Arial 16", fill="black")


def usd_byn(num):
    t.delete(ALL)
    result = rates["USD"].value
    result2 = rates["BYN"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def usd_pln(num):
    t.delete(ALL)
    result = rates["USD"].value
    result2 = rates["PLN"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def eur_usd(num):
    t.delete(ALL)
    result = rates["EUR"].value
    result2 = rates["USD"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def eur_rub(num):
    t.delete(ALL)
    result = float(rates["EUR"].value)
    result2 = round(result * float(num), 2)
    t.create_text(400, 100, text=str(result2), font="Arial 16", fill="black")


def eur_byn(num):
    t.delete(ALL)
    result = rates["EUR"].value
    result2 = rates["BYN"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def eur_pln(num):
    t.delete(ALL)
    result = rates["EUR"].value
    result2 = rates["PLN"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def rub_usd(num):
    t.delete(ALL)
    result = rates["USD"].value
    result2 = 1 / float(result)
    t.create_text(400, 100, text=str(round(result2 * float(num), 2)), font="Arial 16", fill="black")


def rub_eur(num):
    t.delete(ALL)
    result = rates["EUR"].value
    result2 = 1 / float(result)
    t.create_text(400, 100, text=str(round(result2 * float(num), 2)), font="Arial 16", fill="black")


def rub_byn(num):
    t.delete(ALL)
    result = rates["BYN"].value
    result2 = 1 / float(result)
    t.create_text(400, 100, text=str(round(result2 * float(num), 2)), font="Arial 16", fill="black")


def rub_pln(num):
    t.delete(ALL)
    result = rates["PLN"].value
    result2 = 1 / float(result)
    t.create_text(400, 100, text=str(round(result2 * float(num), 2)), font="Arial 16", fill="black")


def byn_usd(num):
    t.delete(ALL)
    result = rates["BYN"].value
    result2 = rates["USD"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def byn_eur(num):
    t.delete(ALL)
    result = rates["BYN"].value
    result2 = rates["EUR"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def byn_rub(num):
    t.delete(ALL)
    result = rates["BYN"].value
    result2 = round(float(result) * float(num), 2)
    t.create_text(400, 100, text=str(result2), font="Arial 16", fill="black")


def byn_pln(num):
    t.delete(ALL)
    result = rates["BYN"].value
    result2 = rates["PLN"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def pln_usd(num):
    t.delete(ALL)
    result = rates["PLN"].value
    result2 = rates["USD"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def pln_eur(num):
    t.delete(ALL)
    result = rates["PLN"].value
    result2 = rates["EUR"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def pln_rub(num):
    t.delete(ALL)
    result = rates["PLN"].value
    result2 = float(result)
    t.create_text(400, 100, text=str(round(result2 * float(num), 2)), font="Arial 16", fill="black")


def pln_byn(num):
    t.delete(ALL)
    result = rates["PLN"].value
    result2 = rates["BYN"].value
    t.create_text(400, 100, text=str(round(float(result) / float(result2) * float(num), 2)), font="Arial 16", fill="black")


def result_btn(one, two, num):
    if one == "USD" and two == "EUR":
        usd_eur(num)
    elif one == "USD" and two == "RUB":
        usd_rub(num)
    elif one == "USD" and two == "BYN":
        usd_byn(num)
    elif one == "USD" and two == "PLN":
        usd_pln(num)
    elif one == "EUR" and two == "USD":
        eur_usd(num)
    elif one == "EUR" and two == "RUB":
        eur_rub(num)
    elif one == "EUR" and two == "BYN":
        eur_byn(num)
    elif one == "EUR" and two == "PLN":
        eur_pln(num)
    elif one == "RUB" and two == "USD":
        rub_usd(num)
    elif one == "RUB" and two == "EUR":
        rub_eur(num)
    elif one == "RUB" and two == "BYN":
        rub_byn(num)
    elif one == "RUB" and two == "PLN":
        rub_pln(num)
    elif one == "BYN" and two == "USD":
        byn_usd(num)
    elif one == "BYN" and two == "EUR":
        byn_eur(num)
    elif one == "BYN" and two == "RUB":
        byn_rub(num)
    elif one == "BYN" and two == "PLN":
        byn_pln(num)
    elif one == "PLN" and two == "USD":
        pln_usd(num)
    elif one == "PLN" and two == "EUR":
        pln_eur(num)
    elif one == "PLN" and two == "RUB":
        pln_rub(num)
    elif one == "PLN" and two == "BYN":
        pln_byn(num)
    elif one == two:
        t.delete(ALL)
        t.create_text(400, 100, text=str(num), anchor=SW, font="Arial 16", fill="black")


window.mainloop()