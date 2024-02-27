import time
from bs4 import BeautifulSoup
import pyautogui
import pyperclip

# position = pyautogui.position()
# print(position)

# 讀取 txt 檔
with open("links.txt", "r") as f:
    links = f.readlines()

# 迴圈處理每個連結
for link in links:
    pyautogui.moveTo(x=700,y=60)
    pyautogui.click()
    pyautogui.write(link)
    time.sleep(15)
    pyautogui.press('enter')
    time.sleep(5)
    try:
        pyautogui.moveTo(x=112,y=829)
        pyautogui.rightClick()
        pyautogui.moveTo(x=229,y=445)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(x=400,y=447)
        pyautogui.click()

        with open("temp.html", "w", encoding="utf-8") as f:
            f.write(pyperclip.paste())

        with open("temp.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        # 尋找id以"youtube"開頭的iframe
        video_block = soup.find("iframe", id=lambda x: x and x.startswith('youtube'))

        if video_block:
            # 提取影片網址
            video_url = video_block.get("src")

            # 輸出影片網址
            print(video_url)
        else:
            print("找不到符合條件的影片區塊")
    except Exception as e:
        print(f"抓取影片網址失敗：{e}")