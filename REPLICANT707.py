#SpeechRecognitionRecognition
import speech_recognition as sr

#TextToSpeech-Pyttsx3
import pyttsx3

#TextToSpeech-API_ElevenLab
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

#Date & Time
from datetime import datetime

#Wikipedia
import wikipedia

#JOKES
import pyjokes

import sys


def SpeechRecognition():
    ME = None
    while ME is None:
        speak = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            print("Listening:... ")
            audio = speak.listen(source)
            
        try:
            text = speak.recognize_google(audio, language = "vi").upper()
            return text
        
        except sr.UnknownValueError:
            print("Unable to recognize voice.")
        except sr.RequestError:
            print("Unable to connect to Google Speech Recognition.")
        
    


def Training_Bot(ME):
    
    # datetime object containing current date and time
    now = datetime.now()
        
    if any(word in ME for word in ["MY NAME IS", "TÔI TÊN LÀ", "TÊN TÔI LÀ"]):
        
        # Tìm vị trí của "IS" hoặc "LÀ"
        index_is = ME.find("IS") + len("IS") if "IS" in ME else -1
        index_là = ME.find("LÀ") + len("LÀ") if "LÀ" in ME else -1

        # Chọn vị trí hợp lệ (không phải -1)
        index = max(index_is, index_là)

        # Nếu tìm thấy vị trí hợp lệ
        if index != -1:
            name = ME[index:]

            bot_text = (
            f"Hello {name}\n"
            "I'm REPLICANT707 - your AI assistant ;))\n"
            "How can I assist you today? What's on your mind?"
            )
        
    elif any(word in ME for word in ["TODAY", "DATE", "HÔM NAY"]):
        # dd/mm/YY 
        dt_string = now.strftime("%d/%m/%Y")
        bot_text = (f"Current Date: {dt_string}")
        
    elif any(word in ME for word in ["TIME", "GIỜ"]):
        #H:M:S
        dt_string = now.strftime("%Hh:%Mm:%Ss")
        bot_text = (f"Current Time: {dt_string}")
        
    elif "WIKIPEDIA" in ME:
        
        if "TIẾNG VIỆT" in ME:
            print("Từ khóa bạn muốn tìm kiếm là gì?")
            language = "vi"
        elif any(word in ME for word in ["TIẾNG ANH", "ENGLISH"]):
            print("What keyword do you want to search for?")
            language = "en"
        else:
            print("What keyword do you want to search for?")
            language = "en"
            
        search_wikipedia(ME, language)
        bot_text = "This is the result I able to find."
        
    elif "HIẾU" in ME:
        bot_text = (
        "Ý bạn là MAI TRUNG HIẾU - người đã tạo ra tôi đúng không? \n"
        "Anh ấy là người rất tuyệt vời đó !!! "
        )
    
    elif "THẰNG" in ME:
        
        index = ME.find("THẰNG") + len("THẰNG")

        # Lấy phần văn bản sau từ "thằng" và tách thành danh sách các từ
        words_after_thang = ME[index:].strip().split()

        # Lấy từ đầu tiên sau "thằng"
        name = words_after_thang[0] if words_after_thang else ""
        
        bot_text = (f"Nói nhỏ nhé...Thằng {name} ngáo cực kì luôn!!!")
        
        
    elif any(word in ME for word in ["BYE", "GOODBYE", "SEE YOU", "TẠM BIỆT"]):
        bot_text = "BYE BYE, SEE U AGAIN!!!"
    
    elif any(word in ME for word in ["JOKE", "JOKES", "ĐÙA", "HÀI", "CƯỜI"]):
        joke = (pyjokes.get_joke())
        bot_text = (joke)
        
    else:
        bot_text = ("Can't recognize what u say :(((")
        
    return bot_text


def TextTSpeech_Pyttsx3(BOT):
    
    #SETUP
    engine = pyttsx3.init() # object creation
    # RATE
    rate = engine.getProperty('rate')   # getting details of current speaking rate                   
    engine.setProperty('rate', 170)     # setting up new voice rate
    # VOLUME
    volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)                        
    engine.setProperty('volume',1.0) 
    # VOICE
    voices = engine.getProperty('voices')       # getting details of current voice
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0/1/2 (Male/Viet/Female)
    
    engine.say(BOT)
    engine.runAndWait()
    engine.stop()

"""
def TextToSpeech_API(BOT):
    
    load_dotenv()

    client = ElevenLabs(
        api_key='sk_85c553b137d16cac389c76381a2f87f602c2536f94940e8d',
        )

    audio = client.text_to_speech.convert(
        text= BOT,
        voice_id="asDeXBMC8hUkhqqL7agO",
        model_id="eleven_turbo_v2_5",
    )
    
    play(audio)
"""
    
def search_wikipedia(ME, language):
    
    # Nghe từ khóa tìm kiếm từ người dùng
    ask = SpeechRecognition()
    print(ask)

    # Đặt ngôn ngữ 
    wikipedia.set_lang(language)
    try:
        # Tìm kiếm bài viết
        search = wikipedia.page(ask)
        # In ra phần tóm tắt của bài viết
        print(search.summary)
    except wikipedia.exceptions.PageError:
        print("Sorry, i can't find any articles that match your search..")
 
def main():
    
    #HELLO
    print("HELLO!!!")
    print("What's is ur name?")
    
    valid = False
    while not valid:    
        
        #SpeechRecognition
        ME = SpeechRecognition()
        print(f"YOU: {ME}")

        #Training_Bot
        BOT = Training_Bot(ME)
        print(f"REPLICANT707: {BOT}")
        
        #TextTSpeech_Pyttsx3
        TextTSpeech_Pyttsx3(BOT)
        
        #TextToSpeech_API
        #TextToSpeech_API(BOT)
        
        print("")
        
        if BOT == "BYE BYE, SEE U AGAIN!!!":
            valid = True
            
    sys.exit(0)    
    
main()