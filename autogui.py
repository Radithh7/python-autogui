import pyautogui
import time
import os
from datetime import datetime

print("=== Auto Screenshot Program ===")
print("Program akan berhenti jika file 'stop.txt' ditemukan.\n")

while True:
    try:
        interval = float(input("Masukkan interval screenshot (detik): "))
        break
    except ValueError:
        print("⚠ Masukkan angka yang valid!")

folder = "screenshots"
os.makedirs(folder, exist_ok=True)

print(f"\nInterval diset: {interval} detik")
print("Mulai mengambil screenshot...\n")

while True:
    if os.path.exists("stop.txt"):
        print("stop.txt ditemukan → Program dihentikan.")
        break

    img = pyautogui.screenshot()

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    filepath = os.path.join(folder, filename)

    img.save(filepath)

    print(f"Screenshot disimpan: {filepath}")

    time.sleep(interval)

