from bs4 import BeautifulSoup

# 打開 HTML 檔案並讀取內容
with open("test.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, "html.parser")

# 範例：找到所有 <a> 標籤
links = soup.find_all("a")

# 範例：打印所有連結的 href 屬性值
for link in links:
    href = link.get("href")
    if href and href.startswith("https://www.yes588.com.tw/courses/50ton5/lesson"):
        print(href)