import openai
import speech_recognition as sr
import pyttsx3
import time 


# Inicialización API Openai(ChatGPT_3)
openai.api_key = "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"
# Inicialización de motor encargado de sustituir el texto por voz
engine=pyttsx3.init()


def transcribe_audio_to_test(filename):
    recogizer=sr.Recognizer()
    with sr.AudioFile(filename)as source:
        audio=recogizer.record(source) 
    try:
        return recogizer.recognize_google(audio, language="es")
    except:
        print("No se que ha pasado")

def generate_response(prompt):
    response= openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response ["choices"][0]["text"]

# Configuración de la voz en español para el motor de texto a voz

voices = engine.getProperty('voices')
spanish_voice = None
for voice in voices:
    if "spanish" in voice.languages:
        spanish_voice = voice.id
if spanish_voice is not None:
    engine.setProperty('voice', spanish_voice)

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        #Waith for user say "Hola"
        print("Di 'Hola' para empezar a grabar")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            audio=recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio, language="es")
                if transcription.lower()=="hola":
                    #Grabar audio
                    filename ="input.wav"
                    print("Dime que quieres mozo")
                    with sr.Microphone() as source:
                        recognizer=sr.Recognizer()
                        source.pause_threshold=1
                        audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename,"wb")as f:
                            f.write(audio.get_wav_data())
                    #transcribir audio para probar 
                    text=transcribe_audio_to_test(filename)
                    if text:
                        print(f"Yo {text}")
                        
                        #Generar la respuesta 
                        response = generate_response(text)
                        print(f"Eva ese dice: {response}")
                            
                        #Leer la respuesta usando la herramienta de GPT_3
                        #Usando su versión davinci_003
                        speak_text(response)
            except Exception as e:
                
                print("No puedo generar algo, hay un problema  : {}".format(e))
if __name__=="__main__":
    main()