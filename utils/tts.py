from gtts import gTTS
import os
import uuid

def speak_text(text, save=True):
    try:
        filename = f"feedback_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang='en')
        tts.save(filename)

        if not save:
            from playsound import playsound
            playsound(filename)
            os.remove(filename)
            return None
        else:
            return filename  # 👈 Return path for download
    except Exception as e:
        print(f"Error: {e}")
        return None
