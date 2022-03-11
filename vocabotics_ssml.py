#SSML generation functions for common SSML tags supported by Alexa Skills
#Created by vocabotics

from utils import create_presigned_url
from xml.sax.saxutils import escape


#Main speak function - pass in plain text, or call the functions below and combine where necessary. 
def ssml_speak(text):
    speak_ssml = "<speak>" + text + "</speak>"
    return speak_ssml

#Plays an MP3 that is less than 240 sec long, bit rate 48kbps, sample rate must be 22050Hz, 24000Hz, or 16000Hz.
def ssml_audio(filename):
    audio_url = escape(create_presigned_url("Media/" + filename))
    audio_ssml = "<audio src=\"" + audio_url + "\"/>"
    return audio_ssml

#Applies specific voice to the spoken text:American (en-US) - Ivy, Joanna, Joey, Justin, Kendra, Kimberly, Matthew, Salli. Australian (en-AU) Nicole, Russell. English, British (en-GB) Amy, Brian, Emma
#Full list of voices at https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#voice
def ssml_voice(voice, text):
    voice_ssml = "<voice name = \"" + voice + "\">" + text + "</voice>"
    return voice_ssml

#Applies speaking styles to the spech options for name are: conversational, long-form, music, news, fun
def ssml_amazon_domain(name, text):
    domain_ssml = "<amazon:domain name=\"" + name + "\">" + text + "</amazon:domain>"
    return domain_ssml

#Applies effects to the spech options for name are: whispered
def ssml_amazon_effect(name, text):
    effect_ssml = "<amazon:effect name=\"" + name + "\">" + text + "</amazon:effect>"
    return effect_ssml

#Applies emotion to the spech options for name are: excited, disappointed, for intensity: low,medium,high
def ssml_amazon_emotion(name, intensity, text):
    emotion_ssml = "<amazon:emotion name=\"" + name + "\" intensity=\"" + intensity + "\">" + text + "</amazon:emotion>"
    return emotion_ssml

#Applies break to the speech options for strength are: none, x-weak, weak, medium(default), strong, x-strong. Time specified as string e.g. 1000ms or 5s
def ssml_break(strength, time):
    break_ssml = "<break strength=\"" + strength + "\" time=\"" + time + "\"/>"
    return break_ssml

#Applies emphasis to the speech options for level are: strong, moderate, reduced
def ssml_emphasis(level, text):
    emphasis_ssml = "<emphasis level=\"" + level + "\">" + text + "</emphasis>"
    return emphasis_ssml

#Switches language to chosen language: de-DE,en-AU,en-CA,en-GB,en-IN,en-US,es-ES,es-MX,es-US,fr-CA,fr-FR,hi-IN,it-IT,ja-JP,pt-BR
def ssml_lang(lang, text):
    lang_ssml = "<lang xml:lang=\"" + lang + "\">" + text + "</lang>"
    return lang_ssml

#Adds a paragraph pause - equivalent of a x-strong break
def ssml_p(text):
    p_ssml = "<p>" + text + "</p>"
    return p_ssml

#Pronounces phonetically spelt version of text. Alphabet options: ipa, x-sampa. ph - see supported characters https://developer.amazon.com/en-US/docs/alexa/custom-skills/speech-synthesis-markup-language-ssml-reference.html#amazon-emotion
def ssml_phoneme(alphabet, ph, text):
    phoneme_ssml = "<phoneme alphabet=\"" + alphabet + "\" ph=\"" + ph + "\">" + text + "</phoneme>" 
    return phoneme_ssml

#Modifies the rate (x-slow, slow, medium, fast, x-fast, n%), pitch (x-low, low, medium, high, x-high, +n%, -n%), and volume(silent, x-soft, soft, medium, loud, x-loud, +ndB, -ndB) of speech     
def ssml_prosody(rate, pitch, volume, text):
    prosody_ssml = "<prosody rate=\"" + rate + "\" pitch=\"" + pitch + "\" volume=\"" + volume + "\">" + text + "</prosody>" 
    return prosody_ssml

#Adds a sentence pause - equivalent of a strong break or ending a sentence with a .
def ssml_s(text):
    s_ssml = "<s>" + text + "</s>"
    return s_ssml

#Inteprets text in different ways. interpret-as:characters, spell-out,cardinal, number,ordinal,digits,fraction,unit,date, time, telephone, address, interjection, expletive. For date format can be specified: mdy,dmy,ymd,md,dm,ym,my,d,m,y
def ssml_sayas(interpretas, format, text):
    if interpretas == "date":
        ssml_sayas = "<say-as interpret-as=\"" + interpretas + "\" format=\"" + format + "\">" + text + "</say-as>"
    else:
        ssml_sayas = "<say-as interpret-as=\"" + interpretas + "\">" + text + "</say-as>"
        
    return ssml_sayas

#Pronounces word or phrases as a different word as specified with alias attribute
def ssml_sub(alias,text):
    ssml_sub = "<sub alias=\"" + alias + "\">" + text + "</sub>"
    return ssml_sub

#Similar to say-as but defines a role: amazon:VB, amazon:VBD, amazon:NN, amazon:SENSE_1
def ssml_w(role,text):
    ssml_w = "<w role=\"" + role + "\">" + text + "</w>"
    return ssml_w
    
    
    