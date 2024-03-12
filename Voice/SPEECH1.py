import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr

class SpeechToTextApp:
    def __init__(self, master):
        self.master = master
        master.title("Speech to Text")

        self.label = tk.Label(master, text="Press the button and speak")
        self.label.pack()

        self.textbox = scrolledtext.ScrolledText(master, width=40, height=10)
        self.textbox.pack()

        self.button = tk.Button(master, text="Convert Speech to Text", command=self.convert_speech_to_text)
        self.button.pack()

    def convert_speech_to_text(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            self.label.config(text="Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            self.label.config(text="Processing...")
            text = recognizer.recognize_google(audio)
            self.textbox.insert(tk.END, text + "\n")
            self.label.config(text="Press the button and speak")
        except sr.UnknownValueError:
            self.label.config(text="Could not understand audio")
        except sr.RequestError as e:
            self.label.config(text=f"Error: {e}")

def main():
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
