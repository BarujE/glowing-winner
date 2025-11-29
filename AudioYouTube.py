from pytubefix import YouTube


urls =  input("url:")

vid = YouTube(urls)

video_download = vid.streams.get_highest_resolution()
audio_download = vid.streams.get_audio_only()

entry = YouTube(urls).title
pick = input("pick audio Format mp4, mp3, wav,:")
if pick == "mp4" or pick == "mp3" or pick == "wav":
    print(f"\audio found: {entry}\n")


    print(f"Downloading audio...")
    filename = f"{entry}.{pick}"
    audio_download.download(filename=filename)
    
    print(f"audio Complete")
else:
    print("Invalid Audio Format please select mp4, mp3, or Wav you fucking idiot")

    exit()

print("thank you for using The Youtube audio Downloader Made by Baruj")









