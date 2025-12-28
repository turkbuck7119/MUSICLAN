import tkinter as tk
import pygame
import os
import sys

pygame.mixer.init()

def program_klasoru():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

def ses_cal(dosya):
    yol = os.path.join(program_klasoru(), dosya)
    pygame.mixer.music.load(yol)
    pygame.mixer.music.play()

def durdur():
    pygame.mixer.music.stop()

pencere = tk.Tk()
pencere.title("MUSICLAN")
pencere.geometry("350x320")

sesler = [
    ("Smoke it off", "SMOKE IT OFF.mp3"),
    ("Heavy Love", "HEAVY LOVE.mp3"),
    ("Lonely Lonely", "LONELY LONELY.mp3"),
    ("Youre too slow", "YOURE TOO SLOW.mp3"),
    ("GMFU", "GMFU.mp3"),
]

for isim, dosya in sesler:
    tk.Button(
        pencere,
        text=isim,
        width=25,
        command=lambda d=dosya: ses_cal(d)
    ).pack(pady=5)

tk.Button(pencere, text="⏹ Durdur", width=25, command=durdur).pack(pady=10)

pencere.mainloop()
