import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone(device_index=0) as source:
    print("Sizi dinliyorum.Birşeyler söyleyin!")
    audio = r.listen(source)
    
try:
    print("Sizin söylediğiniz: ", r.recognize_google(audio, language="tr"))
except sr.UnknownValueError:
    print("Hmm, bu ses algılanamadı.")
except sr.RequestError as e:
    print("Hmm, herhangi bir çıkarım yapılamadı:{0}".format(e))