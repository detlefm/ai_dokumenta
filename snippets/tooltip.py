import customtkinter as ctk
import tkinter as tk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="yellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("CustomTkinter Tooltip Beispiel")
        self._initlayout()

    def _initlayout(self):
        # Erstellen Sie einen Button
        self.button = ctk.CTkButton(self, text="Hover over me", command=self.button_click)
        self.button.pack(pady=20)

        # Fügen Sie einen Tooltip hinzu
        Tooltip(self.button, "Dies ist ein Tooltip")

    def button_click(self):
        print("Button geklickt!")

if __name__ == "__main__":
    app = App()
    app.mainloop()