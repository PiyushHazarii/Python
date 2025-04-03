import pyttsx3
# it is a type of module which is used to convert text to speech
#what ever you write in the double quotes it will speak that text
engine = pyttsx3.init()
engine.say("i will  speak this text ")
engine.runAndWait()