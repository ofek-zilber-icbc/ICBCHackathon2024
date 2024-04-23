import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

def recognize_from_audiofile():

    load_dotenv()
    speech_key = os.getenv('SPEECH_KEY')
    speech_region = os.getenv('SPEECH_REGION')

    # Create a speech recognizer
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    audio_config = speechsdk.audio.AudioConfig(filename="C:\Git_Repository\case1.m4a")

    try:
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
        result = speech_recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Transcription:", result.text)
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled:", cancellation_details.reason)
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details:", cancellation_details.error_details)
    except Exception as ex:
        print("Exception:", ex)


    

recognize_from_audiofile()