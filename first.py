import pyttsx3
engine = pyttsx3.init(driverName='espeak')
engine.say("Hello, world!")
engine.runAndWait()
