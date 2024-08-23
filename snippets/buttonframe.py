import customtkinter as ctk
from tkinter import ttk

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master,  button_size=50, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.button_size = button_size

        # Verwenden Sie die fg_color-Eigenschaft des Master-Widgets
        #self._fg_color = master.fg_color

        self.canvas = ctk.CTkCanvas(self,  highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set if orientation == "vertical" else self.canvas.xview_moveto)

        if orientation == "vertical":
            self.canvas.pack(side="left", fill="both", expand=True)
            self.scrollbar.pack(side="right", fill="y")
        else:
            self.canvas.pack(side="top", fill="both", expand=True)
            self.scrollbar.pack(side="bottom", fill="x")

    def add_button(self, text):
        button = ctk.CTkButton(self.scrollable_frame, text=text, width=self.button_size, height=self.button_size)
        if self.orientation == "vertical":
            button.pack(side="top", pady=5)
        else:
            button.pack(side="left", padx=5)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("CustomTkinter ButtonFrame Beispiel")
        self._initlayout()

    def _initlayout(self):
        # Erstellen Sie einen vertikalen ButtonFrame
        self.button_frame_vertical = ButtonFrame(self, orientation="vertical")
        self.button_frame_vertical.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Fügen Sie einige Buttons hinzu
        for i in range(20):
            self.button_frame_vertical.add_button(f"Button {i+1}")

        # Erstellen Sie einen horizontalen ButtonFrame
        self.button_frame_horizontal = ButtonFrame(self, orientation="horizontal")
        self.button_frame_horizontal.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Fügen Sie einige Buttons hinzu
        for i in range(20):
            self.button_frame_horizontal.add_button(f"Button {i+1}")

if __name__ == "__main__":
    app = App()
    app.mainloop()