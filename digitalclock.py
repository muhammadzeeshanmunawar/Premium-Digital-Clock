import customtkinter as ctk
from time import strftime
from tkinter import messagebox

# Setup main window
ctk.set_appearance_mode("dark")   # Modes: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("⏰ Premium Digital Clock with Alarm")
root.geometry("450x420")

# Variables
is_24_hour = False
alarm_time = None
font_size = 50  # Default font size

# Function to update time
def update_time():
    global is_24_hour, alarm_time
    
    # Time format
    if is_24_hour:
        current_time = strftime('%H:%M:%S')
    else:
        current_time = strftime('%I:%M:%S %p')
    
    # Date
    current_date = strftime('%A, %d %B %Y')
    
    # Update labels
    label_time.configure(text=current_time, font=("Helvetica", font_size, "bold"))
    label_date.configure(text=current_date)
    
    # Check alarm
    if alarm_time:
        now = strftime('%H:%M') if is_24_hour else strftime('%I:%M %p')
        if now == alarm_time:
            messagebox.showinfo("Alarm", "⏰ Time's up!")
            alarm_time = None
    
    root.after(1000, update_time)

# Toggle 12/24 hour format
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

# Set alarm
def set_alarm():
    global alarm_time
    alarm_time = entry_alarm.get().strip()
    if alarm_time:
        messagebox.showinfo("Alarm Set", f"✅ Alarm set for {alarm_time}")
    else:
        messagebox.showwarning("Invalid", "⚠️ Please enter a valid time.")

# Open settings panel
def open_settings():
    settings = ctk.CTkToplevel(root)
    settings.title("⚙️ Settings")
    settings.geometry("300x300")
    
    # Theme Selector
    theme_label = ctk.CTkLabel(settings, text="🎨 Select Theme:", font=("Helvetica", 14, "bold"))
    theme_label.pack(pady=10)
    
    def change_theme(choice):
        ctk.set_default_color_theme(choice.lower())
    
    theme_menu = ctk.CTkOptionMenu(settings, values=["Blue", "Green", "Dark-Blue"], command=change_theme)
    theme_menu.pack(pady=5)
    
    # Mode Selector (Dark/Light/System)
    mode_label = ctk.CTkLabel(settings, text="🌗 Appearance Mode:", font=("Helvetica", 14, "bold"))
    mode_label.pack(pady=10)
    
    def change_mode(choice):
        ctk.set_appearance_mode(choice.lower())
    
    mode_menu = ctk.CTkOptionMenu(settings, values=["Light", "Dark", "System"], command=change_mode)
    mode_menu.pack(pady=5)
    
    # Font size slider
    size_label = ctk.CTkLabel(settings, text="🔠 Clock Font Size:", font=("Helvetica", 14, "bold"))
    size_label.pack(pady=10)
    
    def change_size(value):
        global font_size
        font_size = int(value)
    
    size_slider = ctk.CTkSlider(settings, from_=30, to=100, number_of_steps=70, command=change_size)
    size_slider.set(font_size)
    size_slider.pack(pady=5)

# ================= MAIN UI =================
label_time = ctk.CTkLabel(root, text="", font=("Helvetica", font_size, "bold"))
label_time.pack(pady=15)

label_date = ctk.CTkLabel(root, text="", font=("Helvetica", 20))
label_date.pack()

frame_buttons = ctk.CTkFrame(root)
frame_buttons.pack(pady=15)

btn_toggle_format = ctk.CTkButton(frame_buttons, text="Toggle 12/24 Hour", command=toggle_format)
btn_toggle_format.grid(row=0, column=0, padx=10, pady=5)

btn_settings = ctk.CTkButton(frame_buttons, text="⚙️ Settings", command=open_settings)
btn_settings.grid(row=0, column=1, padx=10, pady=5)

# Alarm frame
frame_alarm = ctk.CTkFrame(root)
frame_alarm.pack(pady=10)

entry_alarm = ctk.CTkEntry(frame_alarm, placeholder_text="Enter Alarm (07:30 AM / 19:30)")
entry_alarm.grid(row=0, column=0, padx=5, pady=5)

btn_set_alarm = ctk.CTkButton(frame_alarm, text="Set Alarm", command=set_alarm)
btn_set_alarm.grid(row=0, column=1, padx=5, pady=5)

# Start updating clock
update_time()

root.mainloop()
