from typing import Callable
import customtkinter as ctk
import tkinter as tk
from tkinter import font
from tkinter import filedialog




class Window(ctk.CTk):
    def __init__(self,title:str,geometry:str, on_submit:Callable):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self._on_submit = on_submit


        self.action_dict = {
            "Upload": self.on_upload_file,
            "Clear": self.on_clear,
            "Submit": self.on_submit
        }

        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        fg_color = 'transparent'
        consolas_font = font.Font(family="Consolas", size=14)
        self.m_frame = ctk.CTkFrame(self, fg_color=fg_color, border_width=0)
        self.result_frame = ctk.CTkFrame(self.m_frame, corner_radius=10, fg_color=fg_color, border_width=1)
        self.result_txt = tk.Text(self.result_frame, wrap=ctk.WORD, height=10, relief='flat', bg='black', fg='white', font=consolas_font, padx=10, pady=10)
        self.input_frame = ctk.CTkFrame(self.m_frame, corner_radius=10, fg_color=fg_color, border_width=1)
        self.entry_tb = ctk.CTkTextbox(self.input_frame, font=('Consolas',18), padx=10, pady=10)
        self.upload_box = UploadBox(self.input_frame, corner_radius=10, border_width=1, height=50, fg_color=fg_color)
        self.button_frame = ButtonFrame(self.input_frame, border_width=1, fg_color=fg_color)
        self.button_frame.create_buttons(self.action_dict)
        self.label_frame = ctk.CTkFrame(self.m_frame, corner_radius=10, border_width=1, fg_color=fg_color)
        self.status_label = ctk.CTkLabel(self.label_frame, text="Status: Bereit", anchor="w", padx=0, pady=0)

    def setup_layout(self):
        row_result = 0
        row_input = 1
        row_label = 2

        # fill the whole window with m_frame (main frame)
        self.m_frame.pack(fill="both", expand=True, anchor=tk.N)

        # input_frame area
        # Create a grid and configure grid weights for input_frame
        self.input_frame.grid_columnconfigure(0, weight=1)  # self.entry bekommt mehr Gewicht
        self.input_frame.grid_columnconfigure(1, weight=0)  # self.button_frame bekommt weniger Gewicht
        self.input_frame.grid_rowconfigure(0, weight=1)  # self.entry bekommt mehr Gewicht
        self.input_frame.grid_rowconfigure(1, weight=0)  # self.upload_frame bekommt weniger Gewicht

        # place the widgets inside the input_frame
        self.entry_tb.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.button_frame.grid(row=0, column=1, padx=10, pady=5, sticky="ns")
        self.upload_box.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        # Pack result widget and fill whole of the result_frame
        self.result_txt.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)
        # Pack status_label and fill the label_frame
        self.status_label.pack(side=tk.LEFT, fill="x", expand=True, padx=10, pady=10)

        # Configure grid weights for m_frame (main frame)
        self.m_frame.grid_rowconfigure(0, weight=20)  # text_frame bekommt 70% des Platzes
        self.m_frame.grid_rowconfigure(1, minsize=100, weight=1)  # inp_frame bekommt mindestens 100px
        self.m_frame.grid_rowconfigure(2, weight=0)  # label_frame hat fixe Höhe
        self.m_frame.grid_columnconfigure(0, weight=1)  # Allow the frames to expand horizontally

        self.result_frame.grid(row=row_result, column=0, padx=5, pady=5, sticky="nsew")
        self.input_frame.grid(row=row_input, column=0, padx=5, pady=5, sticky="nsew")
        self.label_frame.grid(row=row_label, column=0, padx=5, pady=5, sticky="ew")

        # Hide the upload_box initially if it is empty
        self.update_upload_box_visibility()

    def on_upload_file(self):
        names = filedialog.askopenfilenames(title="Wähle Dateien aus")
        for name in names:
            self.upload_box.add_filename(name)
        self.update_upload_box_visibility()

    def on_clear(self):
        self.upload_box.clear()
        self.update_upload_box_visibility()

    def on_submit(self):
        if self._on_submit:
            entrytxt = self.entry_tb.get("1.0", "end-1c")
            filenames = self.upload_box.filenames
            self._on_submit(txt=entrytxt,filenames=filenames)
        

    def write_result(self,txt:str):
        self.result_txt.insert(tk.END, txt)
        self.result_txt.see(tk.END)
        self.result_txt.update()

    def change_status_label(self,txt:str):
        self.status_label.configure(text=txt)


    def update_upload_box_visibility(self):
        if self.upload_box.winfo_children():
            self.upload_box.grid()
        else:
            self.upload_box.grid_remove()



class UploadBox(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

    def _create_btn(self, text, filename, fg: str):
        button = ctk.CTkButton(self, text=text, fg_color=fg, width=40, height=40)
        button.filename = filename
        button.pack(side=tk.LEFT, pady=10, padx=10)
        return button

    def add_filename(self, filename):
        self._create_btn(text=str(len(self.winfo_children()) + 1), filename=filename, fg='gray')

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    @property
    def filenames(self):
        return [btn.filename for btn in self.winfo_children()]



class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def create_buttons(self, action_dict):
        row = 0
        col = 0
        for text, command in action_dict.items():            
            if text == "Submit":
                button = ctk.CTkButton(self, text=text, command=command,height=100) 
                button.grid(row=row, column=col, padx=10, pady=20, sticky="s")                
            else:
                button = ctk.CTkButton(self, text=text, command=command)                 
                button.grid(row=row, column=col, padx=10, pady=10, sticky="n")
            row +=1                   


if __name__ == "__main__":
    app = Window(title="Example App",geometry="600x800")
    app.mainloop()
