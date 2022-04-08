from gtts import gTTS
import os

text_="where are you going bro"
language="en"
output=gTTS(text=text_,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")
