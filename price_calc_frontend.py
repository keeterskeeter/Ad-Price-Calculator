from tkinter import *
from price_calc_backend import price_ad_bw


light_green_offset = "#a9bd28"
aqua = "#32a8a0"
dark_green = "#006666"
light_green = "#c1d72e"


class Price_calc():
    def __init__(self):
        self.window = Tk()
        self.window.title("Classified Ad Price Calc")
        self.window.resizable(False, False)
        self.window1 = Frame(master=self.window, bg=dark_green)
        self.window1.rowconfigure([0, 1, 2], weight=1, minsize=50)
        self.window1.columnconfigure(0, weight=1, minsize=50)
        self.window1.columnconfigure(1, weight=1, minsize=20)
        self.window1.columnconfigure(2, weight=1, minsize=20)
        self.window1.pack(fill=BOTH, expand=True)
        self.frame1 = Frame(
            master=self.window1,
            borderwidth=1,
            bg=aqua
        )
        self.frame1.grid(row=0, column=0, padx=30, pady=30)
        self.text_box_lbl = Label(
            master=self.frame1,
            text="Enter ad here",
            font=("Noto Mono", 10),
            bg=light_green
        )
        self.text_box_lbl.pack()
        self.frame2 = Frame(
            master=self.window1,
            borderwidth=1,
            bg=aqua
        )
        self.frame2.grid(row=1, column=0, padx=20)
        self.text_box = Text(
            master=self.frame2,
            width=50,
            height=17,
            borderwidth=1
        )
        self.text_box.pack(expand=True)
        self.frame3 = Frame(
            master=self.window1,
            borderwidth=1,
            bg=dark_green
        )
        self.frame3.grid(row=2, column=0, pady=30)
        self.sub_btn = Button(
            master=self.frame3,
            text="Submit",
            borderwidth=2,
            font=("Noto Mono", 10),
            bg=light_green,
            activebackground=light_green_offset,
        )
        self.sub_btn.bind("<Button-1>", self.get_ad)
        self.sub_btn.pack()
        self.quit_btn = Button(
            master=self.frame3,
            text="Quit",
            borderwidth=2,
            font=("Noto Mono", 10),
            bg=light_green,
            activebackground=light_green_offset,
            command=self.window.destroy,
        )
        self.clear_btn = Button(
            master=self.frame3,
            text="Clear",
            borderwidth=2,
            font=("Noto Mono", 10),
            bg=light_green,
            activebackground=light_green_offset,
            command=self.run_again,
        )
        self.frame4 = Frame(
            master=self.window1,
            borderwidth=2,
            relief=GROOVE,
            bg=aqua,
        )
        self.frame4.rowconfigure(0, weight=1, minsize=100)
        self.frame4.rowconfigure(1, weight=1, minsize=50)
        self.frame4.columnconfigure(0, weight=1, minsize=50)
        self.frame4.grid(row=1, column=1)
        self.aditional_opt_lbl = Label(
            master=self.frame4,
            text="Additional\noptions:",
            pady=1,
            font=("Noto Mono", 10),
            relief=SUNKEN,
            bg=light_green
        )
        self.aditional_opt_lbl.grid(row=0, column=0, sticky="n", ipadx=75,)
        self.frame5 = Frame(
            master=self.frame4,
            borderwidth=0,
            bg=aqua
        )
        self.frame5.rowconfigure([0, 1, 2, 3, 4], minsize=75)
        self.frame5.columnconfigure(0, minsize=50)
        self.frame5.grid(row=1, column=0)

        self.entry_text = StringVar()
        self.entry_text.set("How many?")
        self.photo_amount_ent = Entry(
            master=self.frame5,
            width=10,
            bg=dark_green,
            textvariable=self.entry_text
        )
        self.photo_amount_ent.bind("<Button-1>", self.clear_default)
        self.bg_color_var = BooleanVar()
        self.bg_color_cb = Checkbutton(
            master=self.frame5,
            text="background color",
            variable=self.bg_color_var,
            onvalue=1,
            offvalue=0,
            font=("Noto Mono", 10),
            activebackground=dark_green,
            bg=aqua,
            highlightthickness=0,
        )
        self.bg_color_cb.grid(
            row=0,
            column=0,
            sticky="nw",
        )
        self.centered_text_var = BooleanVar()
        self.centered_text_cb = Checkbutton(
            master=self.frame5,
            text="centered text",
            variable=self.centered_text_var,
            onvalue=1,
            offvalue=0,
            font=("Noto Mono", 10),
            activebackground=dark_green,
            bg=aqua,
            highlightthickness=0,
        )
        self.centered_text_cb.grid(
            row=1,
            column=0,
            sticky="nw"
        )
        self.line_breaks_var = BooleanVar()
        self.line_breaks_cb = Checkbutton(
            master=self.frame5,
            text="line breaks",
            variable=self.line_breaks_var,
            onvalue=True,
            offvalue=False,
            font=("Noto Mono", 10),
            activebackground=dark_green,
            highlightthickness=0,
            bg=aqua
        )
        self.line_breaks_cb.grid(
            row=2,
            column=0,
            sticky="nw"
        )
        self.extra_bold_words_var = BooleanVar()
        self.extra_bold_words_cb = Checkbutton(
            master=self.frame5,
            text="extra bold words",
            variable=self.extra_bold_words_var,
            onvalue=1,
            offvalue=0,
            font=("Noto Mono", 10),
            bg=aqua,
            highlightthickness=0,
            activebackground=dark_green
        )
        self.extra_bold_words_cb.grid(
            row=3,
            column=0,
            sticky="nw"
        )
        self.photo_var = BooleanVar()
        self.photo_cb = Checkbutton(
            master=self.frame5,
            bg=aqua,
            activebackground=dark_green,
            text="photo",
            variable=self.photo_var,
            onvalue=1,
            offvalue=0,
            font=("Noto Mono", 10),
            highlightthickness=0,
            command=self.photo_amount
        )
        self.photo_cb.grid(
            row=4,
            column=0,
            sticky="nw",
        )
        self.window.mainloop()

    def run_again(self):
        self.window.destroy()
        new = Price_calc()
        return new

    def get_ad(self, event):
        price_bw = price_ad_bw(self.text_box.get("1.0", END))[0]
        word_count = price_ad_bw(self.text_box.get("1.0", END))[1]
        check_butts = [
            self.centered_text_var,
            self.extra_bold_words_var,
            self.line_breaks_var,
            self.bg_color_var
        ]
        for i in check_butts:
            if i.get():
                price_bw += 3
        try:
            if self.photo_var.get() and int(self.photo_amount_ent.get()) <= 3:
                for _ in range(int(self.photo_amount_ent.get())):
                    price_bw += 5
                self.text_box.pack_forget()
                self.aditional_opt_lbl.pack_forget()
                self.frame5.grid_forget()
                self.frame4.grid_forget()
                self.frame1.grid_forget()
                self.sub_btn.pack_forget()
                price_lbl = Label(
                    master=self.frame2,
                    text=f"Your total comes out to ${price_bw} for {word_count} words",
                    padx=30,
                    pady=30,
                    font=("Noto Mono", 10),
                    relief=SUNKEN,
                    borderwidth=2,
                    bg=light_green_offset
                )
                price_lbl.pack()
                self.quit_btn.grid(row=0, column=1, padx=30)
                self.clear_btn.grid(row=0, column=0, padx=30)
            elif self.photo_var.get() and int(self.photo_amount_ent.get()) >= 4:
                self.pop_up_window = Tk()
                self.pop_up_window.title("Error")
                self.pop_up_window.resizable(False, False)
                self.pop_up_frm = Frame(master=self.pop_up_window, width=200)
                self.pop_up_frm.pack(fill=BOTH)
                self.pop_up_lbl = Label(master=self.pop_up_frm, text="3 Photo max!")
                self.pop_up_lbl.pack()
                self.pop_up_window.mainloop()
            elif self.photo_var.get() == False:
                self.text_box.pack_forget()
                self.aditional_opt_lbl.pack_forget()
                self.frame5.grid_forget()
                self.frame4.grid_forget()
                self.frame1.grid_forget()
                self.sub_btn.pack_forget()
                price_lbl = Label(
                    master=self.frame2,
                    text=f"Your total comes out to ${price_bw} for {word_count} words",
                    padx=30,
                    pady=30,
                    font=("Noto Mono", 10),
                    relief=SUNKEN,
                    borderwidth=2,
                    bg=light_green_offset
                )
                price_lbl.pack()
                self.quit_btn.grid(row=0, column=1, padx=30)
                self.clear_btn.grid(row=0, column=0, padx=30)
        except ValueError:
            self.pop_up_window = Tk()
            self.pop_up_window.title("Error")
            self.pop_up_window.resizable(False, False)
            self.pop_up_frm = Frame(master=self.pop_up_window, width=200)
            self.pop_up_frm.pack(fill=BOTH)
            self.pop_up_lbl = Label(master=self.pop_up_frm, text="Photo amount must be number!")
            self.pop_up_lbl.pack()
            self.pop_up_window.mainloop()

    def photo_amount(self):
        self.photo_cb.grid_forget()
        self.photo_amount_ent.grid(row=4, column=0, sticky="nw", padx=8)

    def clear_default(self, event):
        if self.photo_amount_ent.get() == "How many?":
            self.photo_amount_ent.delete(0, END)
        else:
            pass


woot = Price_calc()
