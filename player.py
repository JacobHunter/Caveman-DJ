import tkinter as tk
from tkinter import font as tkFont
from just_playback import Playback
import time

play_obj = Playback()
def sit_down_music():
    play_song("seating_music.mp3")

def party_walk_in():
    play_song("party_walkin.mp3")

def bride_walk_in():
    play_song("bride_walkin.mp3")

def end_of_ceremony():
    play_song("walkout_music.mp3")


fade_rate = .009
wait_time = .03
def fade_out():
    counter = 1
    while counter > 0:
        counter -= fade_rate
        time.sleep(wait_time)
        play_obj.set_volume(counter)
    play_obj.stop()

def fade_in():
    counter = 0
    while counter < 1:
        counter += fade_rate
        time.sleep(wait_time)
        play_obj.set_volume(counter)

def stop():
    play_obj.stop()

def play_song(songLocation):
    time.sleep(1)
    if play_obj.active:
        fade_out()
    play_obj.set_volume(0)
    play_obj.load_file(songLocation)
    play_obj.play()
    fade_in()


root = tk.Tk()
root.title("Caveman DJ")
root.minsize(400,500)
root.maxsize(400,500)
helvFnt = tkFont.Font(family='Helvetica', size=12, weight='bold')

btnSitDownMusic = tk.Button(root,text="Sit Down Music",command=sit_down_music,height=3,width=25,font=helvFnt)
btnSitDownMusic.pack(pady=12)

btnPartyWalkIn = tk.Button(root,text="Party Walk In",command=party_walk_in,height=3,width=25,font=helvFnt)
btnPartyWalkIn.pack(pady=12)

btnBrideWalkIn = tk.Button(root,text="Bride Walk In",command=bride_walk_in,height=3,width=25,font=helvFnt)
btnBrideWalkIn.pack(pady=12)

btnEndOfCeremony = tk.Button(root,text="End of Ceremony",command=end_of_ceremony,height=3,width=25,font=helvFnt)
btnEndOfCeremony.pack(pady=12)

frameStop = tk.Frame(root,height=3,width=25)
frameStop.pack(pady=12)

btnFadeOut = tk.Button(frameStop,text="Fade Out",command=fade_out,height=3,width=19,font=helvFnt,bg="#E97451")
btnFadeOut.grid(row=0,column=0)

btnFadeOut = tk.Button(frameStop,text="STOP",command=stop,height=3,width=6,font=helvFnt,bg="#E97451")
btnFadeOut.grid(row=0,column=1)

# Start the event loop.
root.mainloop()
