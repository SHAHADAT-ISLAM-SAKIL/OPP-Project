import pyautogui
n = input()
n = int(n)
print(n)
for _ in range(n):  
    pyautogui.press('#')  
    print('#'*(_+ 1))