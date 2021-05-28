from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import os
class Music_Player:
    global playlist
    def __init__(self,root):
        self.root=root
        self.root.geometry("500x500+200+50")
        self.root.title("MUSIC_PLAYER |developed by MS coproration")
        self.root.resizable(False,False)
        title=Label(self.root,text="      MUSIC PLAYER",font=("times new roman",40),bg='darkblue',fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        music_frame=Frame(self.root,bd=2,relief=RIDGE,bg='grey',)
        music_frame.place(x=0,y=67,width=500,height=500)
        mixer.init()
        self.songstatus=StringVar()
        self.songstatus.set('choosing')
        img_play_btn=Button(music_frame,command=self.play,bg="blue",fg="white",text="PLAY",font=("timesnew roman",10,'bold'),border=2).place(x=125,y=270,width=50,height=50)
        img_pause_btn=Button(music_frame,command=self.pause,bg="grey",fg="white",text="PAUSE",font=("timesnew roman",10,'bold'),border=2).place(x=222,y=270,width=50,height=50)
        img_stop_btn=Button(music_frame,command=self.stop,bg="red",fg="white",text="STOP",font=("timesnew roman",10,'bold'),border=2).place(x=320,y=270,width=50,height=50)
        img_resume_btn=Button(music_frame,command=self.resume,bg="lightblue",fg="white",text="RESUME",font=("timesnew roman",10,'bold'),border=2).place(x=222,y=325,width=50,height=50)
        self.playlist=Listbox(music_frame,selectmode=SINGLE,bg="lightblue",fg="black",font=("arial",15),width=50)
        self.playlist.grid(columnspan=5)
        os.chdir(r'C:\\Users\\DELL\\Music')
        songs=os.listdir()
        for s in songs:
            self.playlist.insert(END,s)
    def play(self):
        print("play")
        currentsong= self.playlist.get(ACTIVE)
        print(currentsong)
        mixer.music.load(currentsong)
        self.songstatus.set('Playing')
        mixer.music.play()
        
    def pause(self):
        print("paused")
        self.songstatus.set('paused')
        mixer.music.pause()
    def stop(self):
        print("stop")
        self.songstatus.set("stopped")
        mixer.music.stop()
    def resume(self):
        print("resuming")
        mixer.music.unpause()
root=Tk()
obj=Music_Player(root)
root.mainloop()

