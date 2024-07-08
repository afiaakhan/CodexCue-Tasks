import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player by Afia")
        self.root.geometry("300x300")

        pygame.init()

        self.song_label = tk.Label(root, text="", font=("Arial bold", 12))
        self.song_label.pack(pady=20)

        self.select_song_button = tk.Button(root, text="Select Song", command=self.select_song)
        self.select_song_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_song)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_song)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=10)

        self.current_song = ""

    def select_song(self):
        self.current_song = filedialog.askopenfilename(title="Select a song", filetypes=[("Audio files", "*.mp3;*.wav;*.ogg")])
        self.song_label.config(text=self.current_song)

    def play_song(self):
        pygame.mixer.music.load(self.current_song)
        pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()