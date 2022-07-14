import tkinter
import tkinter.messagebox
from tkinter.tix import Tree
import customtkinter
import pandas as pd
from tkinter import filedialog as fd
from tkinter import *
import random

from barcode import EAN13
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

FEDEX_KEY = 'l7b66fa3d083c246e68a374612bcad2988'
FEDEX_SECRET = '8d695bc1d139469ea3ad3f7412e6e814'
FEDEX_ACCOUNT = '740561073'

class App(customtkinter.CTk):

    WIDTH = 820
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.authenticated = False

        self.title("Thermal Label Ganarator")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=320,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)

        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.account_type = customtkinter.CTkComboBox(master=self.frame_left,
                                                    values=["FedEx", "UPS"])
        self.account_type.grid(row=0, column=0, columnspan=1, pady=10, padx=20, sticky="we")

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Admin Panel",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.username = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="username")
        self.username.grid(row=2, column=0, pady=20, padx=20, sticky="we")
        self.password = customtkinter.CTkEntry(master=self.frame_left, show='*', placeholder_text="password")
        self.password.grid(row=3, column=0, pady=20, padx=20, sticky="we")


        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Log In", 
                                                command=self.authenticate
                                                )
        self.button_1.grid(row=4, column=0, pady=5, padx=60, sticky="w")

        self.button_logout = customtkinter.CTkButton(master=self.frame_left,
                                                text="Log out", command=self.logout)
        self.button_logout.grid(row=6, column=0, pady=10, padx=60, sticky="w")

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Generate Lables for Thermal Printer" ,
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        # ============== This frame will be used for pop up when require setting up custom client
        
        # self.combobox_shipping_method = customtkinter.CTkComboBox(master=self.frame_right,
        #                                             values=["Air", "Ground", 'get more from online'])
        # self.combobox_shipping_method.grid(row=1, column=2, columnspan=1, pady=10, padx=20, sticky="we")
        # self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="select shipping method")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right, text='FedEx Ground',
        #                                                    variable=self.radio_var,
        #                                                    value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right, text='UPS Air',
        #                                                    variable=self.radio_var,
        #                                                    value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.entry_ac = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="Account number")
        # self.entry_ac.grid(row=4, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        # self.entry_ref = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="Reference note")
        # self.entry_ref.grid(row=4, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        # self.entry_car = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="shipping carrier")
        # self.entry_car.grid(row=5, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        # self.entry_met = customtkinter.CTkEntry(master=self.frame_right,
        #                                     width=120,
        #                                     placeholder_text="shipping method")
        # self.entry_met.grid(row=5, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        # self.label_info_2 = customtkinter.CTkLabel(master=self.frame_right,
        #                                            text="OR" ,
        #                                            height=30,
        #                                            fg_color=("white", "gray38"),  # <- custom tuple-color
        #                                            justify=tkinter.LEFT)
        # self.label_info_2.grid(column=0, row=6, columnspan=2, sticky="nwe", padx=15, pady=10)

        self.button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                text="select data file",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.select_file)
        self.button_3.grid(row=7, column=0, columnspan=1, pady=10, padx=20, sticky="we")


        self.switch_save = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="save labels")
        self.switch_save.grid(row=8, column=0, columnspan=1, pady=0, padx=20, sticky="we")

        self.switch_print = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="print labels")
        self.switch_print.grid(row=8, column=1, columnspan=1, pady=0, padx=20, sticky="we")


        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Generate",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,
                                                command=self.generate_labels)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")
        self.account_type.set("select account")
        self.switch_print.select()

    def select_file(self):
        '''
        functoin to open excel file from the local storage
        '''

        if self.authenticated:
            ask_open_file = fd.askopenfilename(title='Select a File', filetypes=(('excel files', '*.xlsx'),))
            self.data_file = pd.read_excel(ask_open_file)
            fl_name = ask_open_file.split('/')[-1]
            self.label_info_1.set_text(f"opened the file: {fl_name}")
            print('=>>>>>>>>>>>: ',self.data_file.columns)
            print('=>>>>>>>>>>>: ',self.data_file[1:2])
            self.payload = {
                
            }
        else:
            self.label_info_1.set_text('Please login before you proceed')

    def generate_labels(self):
        """
        use FedEx and UPS APIs to generate labels
        """
        ...

# < ------------- Users' handling ------------->

    def logout(self):
        self.authenticated = False
        
    def authenticate(self):
        '''
        function to authenticate the user
        '''
        data = (self.username.get(), self.password.get())
        company = self.account_type.get()
        ...

# </ ------------- Users' handling ------------->


    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

'''===================================================================='''
