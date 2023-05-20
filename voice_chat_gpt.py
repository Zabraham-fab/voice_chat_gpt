import openai
import speech_recognition as sr

from gtts import gTTS 
from pydub import AudioSegment
from pydub.playback import play

from api_secret import API_KEY
openai.api_key=API_KEY

r=sr.Recognizer()
mic=sr.Microphone(device_index=0)
# print(sr.Microphone.list_microphone_names())

conversation="""sumary_line"""
user_name="Fat"

while True:
    with mic as source:
        print("It is lintening...")
        r.adjust_for_ambient_noise(source, duration=0.3)
        audio=r.listen(source)
    print("Listening is stand by.")

    try:
        user_input=r.recognize_google(audio, language="en")
        print(f"user said: {user_input}")
    except Exception as e:
        print(e)
        continue
    prompt=user_name+": "+user_input+"\nBot:"
    conversation+=prompt

    response=openai.Completion.create(model="text-davinci-003", prompt=conversation, max_tokens=4000, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0)
    response_str=response["choices"][0]["text"].strip()

    print(f"Bot: {str(response_str)}")

    tts=gTTS(response_str, lang="en")
    tts.save("ses.mp3")
    

    audio = AudioSegment.from_file("ses.mp3", format="mp3")
    play(audio)