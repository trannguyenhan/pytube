from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=5NUYOT74BFU&t=23s";
yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download()
print("Completed!")