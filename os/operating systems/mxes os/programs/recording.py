import pyautogui
import time
import keyboard
def on_ctrl_3():
    print("> Exiting")
def on_ctrl_2():
    pyautogui.moveTo(950,1050)
    pyautogui.click()
    pyautogui.typewrite("spotify")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.moveTo(950,1050)
    pyautogui.click()
    pyautogui.typewrite("obs")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.moveTo(1100,1050)
    pyautogui.click()
    pyautogui.moveTo(1900,75)
    pyautogui.click()
def on_ctrl_1():
    pyautogui.moveTo(1200,1050)
    pyautogui.click()
    pyautogui.moveTo(1700,800)
    pyautogui.click()
    pyautogui.moveTo(1240,1050)
    pyautogui.click()
    pyautogui.moveTo(950,950)
    pyautogui.click()
def on_ctrl_0():
    pyautogui.moveTo(1200,1050)
    pyautogui.click()
    pyautogui.moveTo(1700,800)
    pyautogui.click()
    pyautogui.moveTo(1150,575)
    pyautogui.click()
    pyautogui.moveTo(1240,1050)
    pyautogui.click()
    pyautogui.moveTo(400,230)
    pyautogui.click()
    pyautogui.moveTo(950,950)
    pyautogui.click()
while not end:
    keyboard.add_hotkey('ctrl+0', on_ctrl_0)
    keyboard.add_hotkey('ctrl+1', on_ctrl_1)
    keyboard.add_hotkey('ctrl+2', on_ctrl_2)
    keyboard.add_hotkey('ctrl+3', on_ctrl_3)
    print("> Press 'Ctrl + 0' to start recording")
    print("> Press 'Ctrl + 1' to stop recording")
    print("> Press 'Ctrl + 2' to open the software")
    print("> Press 'Ctrl + 3' to exit")
    keyboard.wait('ctrl+3')
    end=True