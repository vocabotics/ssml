# ssml
SSML encoder for Alexa skill development
# Usage
Import required functions to main lambda_function.py
```
from vocabotics_ssml import ssml_speak
from vocabotics_ssml import ssml_audio
from vocabotics_ssml import ssml_voice
from vocabotics_ssml import ssml_amazon_domain
from vocabotics_ssml import ssml_amazon_effect
from vocabotics_ssml import ssml_amazon_emotion
from vocabotics_ssml import ssml_break
from vocabotics_ssml import ssml_emphasis
from vocabotics_ssml import ssml_lang
from vocabotics_ssml import ssml_p
from vocabotics_ssml import ssml_phoneme
from vocabotics_ssml import ssml_prosody
from vocabotics_ssml import ssml_s
from vocabotics_ssml import ssml_sayas
from vocabotics_ssml import ssml_sub
from vocabotics_ssml import ssml_w
```
# Example usage
SSML blocks can be constructed using the main ssml_speak function to wrap speak tags around 1 or more SSML tags.
```
speak_output = ssml_speak(ssml_audio("intromono.mp3") + ssml_voice("Emma","Welcome to vocabotics") + "test")
speak_output = ssml_speak( ssml_audio("intromono.mp3") + ssml_voice("Emma","Welcome to vocabotics") + "test" )
speak_output = ssml_speak( ssml_amazon_domain("conversational", "Welcome to vocabotics") )
speak_output = ssml_speak( ssml_amazon_effect("whispered", "Welcome to vocabotics") )
speak_output = ssml_speak( ssml_amazon_emotion("disappointed", "high", "Welcome to vocabotics") )        
speak_output = ssml_speak(  "Welcome to " + ssml_break("strong","1000ms") + "vocabotics" )        
speak_output = ssml_speak( "Welcome to" + ssml_emphasis("strong", "the wonderful world of ") + "vocabotics" )
speak_output = ssml_speak( "Welcome to" + ssml_lang("fr-FR", "le monde merveilleux") + "of vocabotics" )
speak_output = ssml_speak( "Welcome to" + ssml_prosody("fast", "high", "loud", "vocabotics")  )
speak_output = ssml_speak( "Welcome to" + ssml_s("vocabotics") )
speak_output = ssml_speak( "Welcome to" + ssml_sayas("characters","","vocabotics") )
speak_output = ssml_speak( "Welcome to vocabotics on " + ssml_sayas("date","mdy","4/3/2022") )
speak_output = ssml_speak( "Welcome to " + ssml_sub("Great Britain","GB") )
speak_output = ssml_speak( "Welcome to " + ssml_w("amazon:VB","vocabotics") )
```        
