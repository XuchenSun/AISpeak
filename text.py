"Author: Xuchen Sun"
"gtts: Google text to speech lib with MIT licence"

import os
from gtts import gTTS

myText="Hi,Xander. Sorry to bother you on vacation. We need your help"
language='en-IN'
output=gTTS(text=myText,lang=language,slow=False)
output.save("output.mp3")

