from gtts import gTTS
# from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

tts=gTTS("Merhaba arkadaşlar bu bir test çalışmasıdır", lang="tr", slow=True)

# tts=gTTS("Merhaba arkadaşlar bu bir test çalışmasıdır")

tts.save("ses.mp3")
# playsound("ses.mp3")

audio = AudioSegment.from_file("ses.mp3", format="mp3")
play(audio)