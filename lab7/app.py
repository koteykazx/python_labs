import speech_recognition as sr

#sr.recognize_google()
#sr.recognize_google_cloud()
#sr.recognize_ibm()
 
mic_list = sr.Microphone.list_microphone_names()
[print(i, mic_list[i]) for i in range(0, len(mic_list))]

mic = sr.Microphone(device_index=1)
 
r = sr.Recognizer()
with mic as source:
   print("Say something in English!")
   audio = r.listen(source)
try:
   a = r.recognize_google(audio, language="ru-RU")
   print("You said: " + a + "?")
except sr.UnknownValueError:
   print("Text is not understandable.")
except sr.RequestError as e:
   print("Google could not request result prom API.")
