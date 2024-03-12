import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech to Text App")

        # Create a SpeechRecognition object
        self.recognizer = sr.Recognizer()

        # UI components
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Listening", command=self.start_listening)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop Listening", command=self.stop_listening, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_listening(self):
        # Enable the Stop button and disable the Start button
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            self.text_area.insert(tk.END, f"{text}\n")
        except sr.UnknownValueError:
            self.text_area.insert(tk.END, "Speech Recognition could not understand audio.\n")
        except sr.RequestError as e:
            self.text_area.insert(tk.END, f"Could not request results from Google Speech Recognition service; {e}\n")

        # Enable the Start button and disable the Stop button
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def stop_listening(self):
        # Disable the Stop button and enable the Start button
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.recognizer.stop_listening()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
