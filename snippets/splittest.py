import customtkinter as ctk
from tkinter import ttk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("CustomTkinter PanedWindow Beispiel")
        self._initlayout()

    def _initlayout(self):
        # Erstellen Sie ein PanedWindow-Widget
        paned_window = ttk.PanedWindow(self, orient="vertical")
        paned_window.pack(fill="both", expand=True)

        # Erstellen Sie zwei Frames für die Bereiche
        frame1 = ctk.CTkFrame(paned_window, corner_radius=10, border_width=1)
        frame2 = ctk.CTkFrame(paned_window, corner_radius=10, border_width=1)

        # Fügen Sie die Frames zum PanedWindow hinzu
        paned_window.add(frame1)
        paned_window.add(frame2)

        # Fügen Sie Inhalte zu den Frames hinzu (optional)
        label1 = ctk.CTkLabel(frame1, text="Bereich 1")
        label1.pack(pady=10, padx=10)

        label2 = ctk.CTkLabel(frame2, text="Bereich 2")
        label2.pack(pady=10, padx=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()