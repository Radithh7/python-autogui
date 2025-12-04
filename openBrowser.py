import pyautogui
import time

library = {
    "wa": "https://web.whatsapp.com",
    "id": "https://www.linkedin.com/",
    "gh": "https://github.com/",
    "yt": "https://www.youtube.com",
}

def openWeb(web, browser):
    pyautogui.press('win')
    time.sleep(0.5)

    pyautogui.write(browser)
    time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.write(web)
    time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(2)
    return

print("List Shortcut:")
for key in library:
    print(f"{key}")
print("q untuk keluar")

while True:
    setAddress = input("Masukkan alamat web (kode shortcut): ").lower()
    setBrowser = input("Masukkan alamat web (pilih browser): ").lower()

    if setAddress in library:
        openWeb(library[setAddress], setBrowser)
    elif setAddress == 'q':
        break
    else:
        print("Kode tidak ditemukan.")
print("Goodbye!")