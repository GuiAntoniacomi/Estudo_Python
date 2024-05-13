import pyautogui as pgui
import time
import pandas as pd

df = pd.read_csv('D:\\Users\\eugen\\Documents\\Gui\\ESTUDOS\\Python\\Estudo_Python\\Hashtag\\produtos.csv')

time.sleep(5)

print(pgui.position())
