from pytube import YouTube
#this variable store audio/video in this directory
Save_Path = "D:/python_programme/up_grade_projects"
try:
    yt = YouTube(link)
except:
    print("connection error!")

#this fucn for downloading youtube videos   
def video_downloader():
    print('Choose the video Resolution:')
    user_input = int(input('1.360p\n2.480p\n3.720p\n4.1080p\n:-')) 
    #I know that this is a bad method , near future i'll solve this..
    try:
        if user_input == 1:
            print('working...')
            yt.streams.filter(res="360p").first().download(Save_Path)
            Anime_Down_Proc()
        elif user_input ==2:
            yt.streams.filter(res="480p").first().download(Save_Path)
            Anime_Down_Proc()
        elif user_input == 3:
            yt.streams.filter(res="720p").first().download(Save_Path)
            Anime_Down_Proc()
        elif user_input == 4:
            yt.streams.filter(res="1080p").first().download(Save_Path)
            Anime_Down_Proc()
    except:
        print("some error")
# This function give a audio downloading power..
def audio_downloader():
    import pafy
    video = pafy.new(link)
    index = 0
    string = "prefer to choose '.m4a'"
    #i'll show users note in center 
    #so i make a another variable to use center function
    new_string = string.center(20,'-')
    print(new_string)
    audiostreams = video.audiostreams #to get all audio stream 
    print('---------------------------')
    for a in audiostreams:
        HumanReadableSize = a.get_filesize()//(1024) #convert byte size into kilobyte(kb)
        print(f"{str(index)+'.'}{a.extension} | {a.bitrate} | {HumanReadableSize} kb")
        index +=1
    #to take user's input for download formates or quality
    print('---------------------------')
    user_input = int(input("Choose one:"))
    print('---------------------------')
    try:
        audiostreams[user_input].download(Save_Path)
        Anime_Down_Proc()
    except:
        print('sorry but choose another bitrate(qulity)')
            
def Anime_Down_Proc():
    print('downloading finished your video/audio in',Save_Path)

def restart_programme():
    user_input = input("Press (Q)uit or (Y)es").lower()
    if user_input == 'q':
        quit()
    elif user_input == 'y':
        main_menu()
    else:
        print('invalid syntex')
        restart_programme()
def main_menu():
    string = "Video Downloader by Phantom"
    new_string = string.center(50,'-')
    print(new_string)
    global link
    link = input('Paste your video URL:')
    user_choice = int(input('Choose one for download-\n1.Video\n2.Audio\n# '))
    # here i use try/except statement because i won't want error..
    try:
        if user_choice == 1:
            video_downloader()
        if user_choice == 2:
            audio_downloader()
    except:
        print('invalid input...')

if __name__=="__main__":
    restart_programme()
