import tkinter as tk
import speech_recognition as sr
import subprocess

def listen():
    """
    Listens to user's voice and performs actions based on the recognized text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak anything")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text_box.insert(tk.END, text + "\n")
            handle_commands(text.lower())
        except sr.UnknownValueError:
            print("Sorry, could not recognize the text")
        except sr.RequestError:
            print("Sorry, could not request results from Google Speech Recognition")

def handle_commands(text):
    """
    Handles commands based on the recognized text.
    """
    commands = {
        "open notepad": "notepad.exe",
        "open explorer": "explorer.exe",
        "open task manager": "taskmgr.exe"
    }
    if text in commands:
        subprocess.Popen(commands[text])

root = tk.Tk()
root.title("Speech Recognizer")

text_box = tk.Text(root, height=10, width=50)
text_box.grid(column=0, row=0, padx=10, pady=10)

listen_button = tk.Button(root, text="Listen", command=listen)
listen_button.grid(column=1, row=0, padx=10, pady=10)

root.mainloop()