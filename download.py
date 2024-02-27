from pytube import YouTube

# 读取包含YouTube视频链接的文件
with open('youtube_urls.txt', 'r') as file:
    urls = file.readlines()

# 下载每个视频
for url in urls:
    try:
        yt = YouTube(url)
        # 选择最高质量的视频流进行下载
        stream = yt.streams.get_highest_resolution()
        print("正在下载视频:", yt.title)
        stream.download(output_path='downloads')
        print("视频下载完成:", yt.title)
    except Exception as e:
        print("下载出错:", str(e))