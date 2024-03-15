import tkinter as tk
import speech_recognition as sr
import threading

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    while True:
        with microphone as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # Error checking
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            text_var.set(f"You said: {text}")  # Update text_var with recognized speech
        except sr.UnknownValueError:
            text_var.set("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            text_var.set(f"Error: {str(e)}")

def start_recognizing():
    threading.Thread(target=recognize_speech, daemon=True).start()

# Create a main window
blank_world = tk.Tk()
blank_world.title("Live Speech Translation")
 
# Create a StringVar to store the recognized text
text_var = tk.StringVar()
text_var.set("Listening...")

# Create a label to display the spoken text
label = tk.Label(blank_world, textvariable=text_var, font=("Arial", 12), wraplength=400)
label.pack(padx=20, pady=20)

# Create a button to start recognizing speech
button = tk.Button(blank_world, text="Start Recognizing", command=start_recognizing)
button.pack(pady=10)

blank_world.mainloop()

