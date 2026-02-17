import customtkinter as ctk
from time import strftime
from tkinter import messagebox

# Set the modern style
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("⏰ Premium Clock")
        self.root.geometry("500x480")
        
        # Soft UI Settings
        self.is_24_hour = False
        self.alarm_time = None
        self.font_size = 65
        self.accent_color = "#76D7C4" # Soft Pastel Mint

        self.setup_ui()
        self.update_time()

    def setup_ui(self):
        # Time Display - Main focus
        self.label_time = ctk.CTkLabel(
            self.root, 
            text="", 
            font=("Segoe UI", self.font_size, "bold"), 
            text_color=self.accent_color
        )
        self.label_time.pack(pady=(50, 5))

        self.label_date = ctk.CTkLabel(
            self.root, 
            text="", 
            font=("Segoe UI", 18),
            text_color="#BDC3C7"
        )
        self.label_date.pack(pady=(0, 30))

        # Modern Control Frame
        self.frame_ctrl = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_ctrl.pack(pady=10)

        self.btn_format = ctk.CTkButton(
            self.frame_ctrl, 
            text="12/24H Toggle", 
            command=self.toggle_format, 
            corner_radius=30, # Extra rounded
            fg_color="#34495E",
            hover_color="#2C3E50"
        )
        self.btn_format.grid(row=0, column=0, padx=10)

        self.btn_settings = ctk.CTkButton(
            self.frame_ctrl, 
            text="⚙️ Settings", 
            command=self.open_settings, 
            corner_radius=30,
            fg_color="#34495E",
            hover_color="#2C3E50"
        )
        self.btn_settings.grid(row=0, column=1, padx=10)

        # Soft Alarm Section
        self.alarm_frame = ctk.CTkFrame(self.root, corner_radius=20, border_width=1, border_color="#555")
        self.alarm_frame.pack(pady=30, padx=40, fill="x")

        self.entry_alarm = ctk.CTkEntry(
            self.alarm_frame, 
            placeholder_text="HH:MM (e.g. 07:30)", 
            width=160,
            height=40,
            border_width=0,
            corner_radius=10
        )
        self.entry_alarm.grid(row=0, column=0, padx=20, pady=20)

        self.btn_alarm = ctk.CTkButton(
            self.alarm_frame, 
            text="Set Alarm", 
            command=self.set_alarm, 
            width=110,
            height=40,
            corner_radius=10,
            fg_color=self.accent_color,
            text_color="#1A5276" # Contrast color for readability
        )
        self.btn_alarm.grid(row=0, column=1, padx=(0, 20), pady=20)

    def update_time(self):
        format_str = '%H:%M:%S' if self.is_24_hour else '%I:%M:%S %p'
        current_time = strftime(format_str)
        current_date = strftime('%A, %d %B %Y')
        
        self.label_time.configure(text=current_time)
        self.label_date.configure(text=current_date)
        
        if self.alarm_time:
            check_fmt = '%H:%M' if self.is_24_hour else '%I:%M %p'
            now = strftime(check_fmt)
            if now == self.alarm_time:
                self.alarm_time = None
                messagebox.showinfo("Alarm", "⏰ Time's up!")
        
        self.root.after(1000, self.update_time)

    def toggle_format(self):
        self.is_24_hour = not self.is_24_hour

    def set_alarm(self):
        val = self.entry_alarm.get().strip()
        if val:
            self.alarm_time = val
            messagebox.showinfo("Alarm Set", f"✅ Alarm set for {self.alarm_time}")

    def open_settings(self):
        settings = ctk.CTkToplevel(self.root)
        settings.title("Settings")
        settings.geometry("320x280")
        settings.attributes("-topmost", True)

        ctk.CTkLabel(settings, text="Appearance Mode", font=("Segoe UI", 13, "bold")).pack(pady=10)
        mode_menu = ctk.CTkOptionMenu(settings, values=["Light", "Dark", "System"], 
                                      command=lambda c: ctk.set_appearance_mode(c),
                                      corner_radius=20)
        mode_menu.pack()

        ctk.CTkLabel(settings, text="Clock Size", font=("Segoe UI", 13, "bold")).pack(pady=10)
        size_slider = ctk.CTkSlider(settings, from_=40, to=100, command=self.change_size)
        size_slider.set(self.font_size)
        size_slider.pack()

    def change_size(self, value):
        self.font_size = int(value)
        self.label_time.configure(font=("Segoe UI", self.font_size, "bold"))

if __name__ == "__main__":
    # FIX: Initialize root FIRST, then pass it to the class
    main_root = ctk.CTk() 
    app = DigitalClock(main_root)
    main_root.mainloop()
