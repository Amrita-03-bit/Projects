#🎵 Project 18: Music Player System

#Project Goal: Create a music player system to show songs, play a selected song, add/remove songs, and control the playlist.

songs = [
    "Believer",
    "Perfect",
    "Shape Of You",
    "Lovely",
    "Havana"
]

playlist=[]
def show_song():


    print(songs)

    #play song

    play_song=input("Enter the song you want to play:").title()
    if play_song in songs:
        print("playing:",play_song)
    else:
        print("song not found")   

    while True:

      #Add song

      song_playlist=input("Which song do you want to add the playslist:").title()
      if song_playlist in songs:
        playlist.append(song_playlist)   

        more_song=input("Do you want to add another song? (yes/no)")   
        if more_song=="yes":
           continue
        else:
           print("lets's move on")

        #Remove song

        remove_song=input("Do you want to remove  a song to playlist (yes/no):")
        
        if remove_song=="yes":
            song_remove = input("Which song do you want to remove? ").title()

            if song_remove in playlist:
               playlist.remove(song_remove)
            else:
               print("song not found in playlist")   

        else:
           print("lets's move on")   
        

      else:
        print("song not found")    

      print("your playlist ",playlist)
      break

show_song()