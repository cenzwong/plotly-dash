!pip install gTTS

from gtts import gTTS

myText = "Hello"
language = "en"

tts = gTTS(text=text, lang=language, slow=False)
tts.save('hello.mp3')

# https://colab.research.google.com/drive/1JYKPpDVvPzEl4yL_X4G9dcAQAv7keLdJ#scrollTo=HV54gMGBE7q9
