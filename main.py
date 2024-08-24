import tkinter as tk
import tkinter.messagebox
import functions
import datetime

# Reprinter GUI
reprinter = tk.Tk()
reprinter.title("Reprinter")
reprinter.configure(background="#C1CDCD")
reprinter.bind('<Return>', lambda event: popup_gui())


def popup_gui():
    oid_input_lenght = len(oid_input.get().split("@"))

    if oid_input_lenght == 16 or oid_input_lenght == 17:  # Sve familije imaju 16 "Podataka", samo WH ima 17.

        def print_label():

            if functions.check_date_input(date_input.get()):
                functions.execute_printing(operater=operaterid_input.get(), date_and_time=date_input.get(),
                                           oid_lenght=oid_input_lenght, qr_input=oid_input.get())
                popup.destroy()
                oid_input.delete(0, tk.END)
            else:
                tkinter.messagebox.showinfo("Greska", "Polja moraju biti popunjena u trazenom formatu!")
                popup_gui()

        popup = tk.Toplevel(reprinter)
        popup.attributes('-fullscreen', True)
        popup.overrideredirect(True)  # Disabluje mogucnost gasenja GUI-a.
        popup.bind('<Return>', lambda event: print_label())

        def get_date():
            date_input.delete(0, tk.END)
            date_input.insert(0, datetime.datetime.now().strftime("%d/%m/%Y,%H:%M"))

        operaterid_input_labela = tk.Label(popup, text="Unesi operater ID", font=("Arial", 15))
        operaterid_input_labela.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        operaterid_input = tk.Entry(popup, width=30, font=("Arial", 15))
        operaterid_input.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        operaterid_input.focus_set()

        date_input_labela = tk.Label(popup, text="Unesi datum i vreme u formatu(DATE,TIME)", font=("Arial", 15))
        date_input_labela.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        date_input = tk.Entry(popup, width=30, font=("Arial", 15))
        date_input.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        get_date_button = tk.Button(popup, text="Upisi datum", command=get_date, width=30, height=3)
        get_date_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        print_button = tk.Button(popup, text="Print", command=print_label, width=30, height=3)
        print_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        close_button = tk.Button(popup, text="Zatvori Program", command=lambda: reprinter.destroy(), width=30, height=3)
        close_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    else:

        tkinter.messagebox.showinfo("Greska", "Aztec code nije u dobrom formatu!")
        oid_input.delete(0, tk.END)


# Gageti reprinter GUI-a.

input_labela = tk.Label(reprinter, text="Skeniraj elektro nalepnicu ili OID sheet", font=("Arial", 24))
input_labela.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

oid_input = tk.Entry(reprinter, width=100, font=('Arial 24'))
oid_input.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
oid_input.focus_set()

reprint_button = tk.Button(reprinter, text="Reprint", command=lambda: functions.reprint(), width=30, height=3)
reprint_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

close_button = tk.Button(reprinter, text="Zatvori program", command=lambda: reprinter.destroy(), width=30, height=3)
close_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

reprinter.attributes('-fullscreen', True)
reprinter.mainloop()

