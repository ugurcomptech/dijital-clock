from pathlib import Path
from tkinter import Tk, Canvas, Button, font, messagebox
import tkinter as tk
from tkinter import ttk
import time
import pygame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\uğur\Desktop\scripts\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Mevcut zamanı saat:dakika:saniye formatında alın
    canvas.itemconfig(clock_label, text=current_time)  # Saati etikete yazdır

    check_alarms(current_time)  # Alarm kontrolü yap

    canvas.after(1000, update_time)  # Her 1 saniyede bir saat güncellemesini yap

def check_alarms(current_time):
    for alarm in alarms:
        if current_time == alarm and not alarm_triggered[0]:
            pygame.mixer.music.load("C:/Users/uğur/Desktop/scripts/ses.mp3")
            pygame.mixer.music.play()  # Alarm sesini çal
            alarm_triggered[0] = True

def set_alarm():
    hour = hour_entry.get()
    minute = minute_entry.get()
    second = second_entry.get()

    alarm_time = f"{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}"
    alarms.append(alarm_time)
    
    messagebox.showinfo("Alarm Ayarlandı", f"{alarm_time} saatine alarm ayarlandı.")

def stop_alarm():
    pygame.mixer.music.stop()
    alarm_triggered[0] = False

window = Tk()

window.geometry("1488x1026")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1026,
    width=1488,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    6.0,
    0.0,
    1500.0,
    1026.0,
    fill="#5B1616",
    outline="")

clock_text = "Digital clock"
canvas.create_text(
    753.0,
    115.0,
    anchor="center",
    text=clock_text,
    fill="#FFFFFF",
    font=("IndieFlower Regular", 96 * -1)
)

canvas.create_rectangle(
    220.93341064453125,
    250.22621154785156,
    1309.7974243164062,
    262.7327575683594,
    fill="#FFFFFF",
    outline="")

clock_label = canvas.create_text(
    765.0,
    316.0,
    anchor="center",
    text="00:00:00",
    fill="#FFFFFF",
    font=("Koulen", 48 * -1)
)

# Alarm Ayarlama Butonu
alarm_button = Button(
    window,
    text="Alarım Ayarla",
    font=("Kadwa Regular", 32),
    bg="#E5A01A",
    fg="#000000",
    relief="ridge",
    borderwidth=10,
    command=set_alarm
)
alarm_button_window = canvas.create_window(
    232.0,
    636.0,
    anchor="nw",
    window=alarm_button
)

# Alarm Durdurma Butonu
stop_button = Button(
    window,
    text="Alarımı Durdur",
    font=("Kadwa Regular", 32),
    bg="#E5A11B",
    fg="#000000",
    relief="ridge",
    borderwidth=10,
    command=stop_alarm
)
stop_button_window = canvas.create_window(
    1007.0,
    636.0,
    anchor="nw",
    window=stop_button
)

window.resizable(False, False)

# Saat ayarlama kısmı
frame = ttk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Orta noktaya yerleştirme

hour_label = ttk.Label(frame, text="Saat:", font=("Courier", 16), background="")  # Saat etiketi (kırmızı arka plan)
hour_label.grid(row=0, column=0, padx=5, pady=5)

hour_entry = ttk.Entry(frame, font=("Courier", 16), justify=tk.CENTER, background="white")  # Saat giriş alanı
hour_entry.grid(row=0, column=1, padx=5, pady=5)

minute_label = ttk.Label(frame, text="Dakika:", font=("Courier", 16), background="")  # Dakika etiketi (kırmızı arka plan)
minute_label.grid(row=0, column=2, padx=5, pady=5)

minute_entry = ttk.Entry(frame, font=("Courier", 16), justify=tk.CENTER, background="white")  # Dakika giriş alanı
minute_entry.grid(row=0, column=3, padx=5, pady=5)

second_label = ttk.Label(frame, text="Saniye:", font=("Courier", 16), background="")  # Saniye etiketi (kırmızı arka plan)
second_label.grid(row=0, column=4, padx=5, pady=5)

second_entry = ttk.Entry(frame, font=("Courier", 16), justify=tk.CENTER, background="white")  # Saniye giriş alanı
second_entry.grid(row=0, column=5, padx=5, pady=5)

pygame.init()  # Pygame'i başlat

# Alarmları depolamak için liste oluştur
alarms = []
alarm_triggered = [False]

update_time()  # Saati güncellemeye başla

window.mainloop()
