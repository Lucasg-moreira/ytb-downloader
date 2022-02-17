from pytube import YouTube
from pytube import Search
from pytube import Playlist



choose = int(input("Do you want download music or video? For download both use *pytube 'url'* in terminal\n1- Video\n2- music\n3- Search\n4- Playlist\ninput: "))
if choose == 1:
    input_url = input("Input url: ")
    yt = YouTube(input_url)
    def downloadYtbVideo():
        ytdownload = yt.streams.filter(progressive=True, file_extension='mp4')
        print(ytdownload)
        itag = int(input("Select itag(resolution)\ninput: "))
        itagVideo = yt.streams.filter(progressive=True, file_extension='mp4').get_by_itag(itag)
        itagVideo.download()    
    
    def resume():
        title = yt.title
        desc = yt.description
        thumb = yt.thumbnail_url
        print("Title: ", title)
        print("Thumbanail link: ", thumb)
        print("Video description:", desc)

    print("Processing all informations . . .")
    downloadYtbVideo()
    print("The download has been completed")
    displayResume = int(input("Display resume?\n1- Yes\n2- No\ninput: "))  
    
    if displayResume == 1:
        print("-" * 100)
        print("**RESUME**")
        resume()
    else:
        print("closing. . . . .")
elif choose == 2:
    def resume():
        title = yt.title
        desc = yt.description
        thumb = yt.thumbnail_url
        print("-" * 100)
        print("Resume: ")
        print("Title: ", title)
        print("Thumbanail link: ", thumb)
        print("Video description:", desc)
    inputAudio = str(input("Input url to extract audio: "))
    yt = YouTube(url=(inputAudio))
    downloadAudio = yt.streams.filter(only_audio=True).desc().first().download()
    print(downloadAudio)
    resume()
    print("Audio downloaded.\n Exiting. . . .")
elif choose == 3:
    search_string = input("Enter what do you want search: ")
    search = Search(search_string)
    results = search.results
    length = len(results)

    print(results)
    print(length)
else: 
    playlist = str(input("Enter the playlist what do you wanna download: "))
    playlist = Playlist(playlist)
    print("Downloading: {playlist.title}".format)
    playask = input("Audio or video?")
    if playask == 1:
        for video in playlist.videos: 
            video.streams.desc().first().download()
    else:
        for audio in  playlist.videos:
            audio.streams.filter(only_audio=True).desc().first().download()











