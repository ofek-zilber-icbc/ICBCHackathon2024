import os
import azure.cognitiveservices.speech as speechsdk
import time
# from dotenv import load_dotenv

def recognize_from_audiofile():

    speech_key = os.environ.get('SPEECH_KEY')
    speech_endpoint = os.environ.get('SPEECH_ENDPOINT')
    speech_region = os.environ.get('SPEECH_REGION')

    # Create a speech recognizer
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    audio_config = speechsdk.AudioConfig(filename="PositiveSpecialistNegativeCustomer.wav")

    speech_config.enable_audio_logging()

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, 
                                                   audio_config=audio_config,
                                                   language="en-US")


    done = False

    def on_recognized(evt):
        print("recognized")
        print("RECOGNIZED: {}".format(evt))
        assert (
            evt.result.reason == speechsdk.ResultReason.RecognizedSpeech
        ), "A portion was not recognized"

    def stop_cb(evt):
        print("ending")
        print("CLOSING on: {}".format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True
    
    
    # speech_recognizer.recognized.connect(on_recognized)
    # print("added on_recognized")
    # speech_recognizer.session_stopped.connect(stop_cb)
    # print("added stop_cb")

    speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt)))  
    speech_recognizer.recognized.connect(lambda evt: print('RECOGNIZED: {}'.format(evt)))  
    speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))  
    speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))  
    speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))  
    # stop continuous recognition on either session stopped or canceled events  
    speech_recognizer.session_stopped.connect(stop_cb)  
    speech_recognizer.canceled.connect(stop_cb)  

    # result = speech_recognizer.recognize_once_async().get()

    # print("result: {}".format(result))

    speech_recognizer.start_continuous_recognition()
    
    print("Started recognition")

    while not done:
        print("sleeping")
        time.sleep(0.5)

    speech_recognizer.start_continuous_recognition()

recognize_from_audiofile()

    # try:
    #     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    #     result = speech_recognizer.recognize_once()

    #     if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    #         print("Transcription:", result.text)
    #     elif result.reason == speechsdk.ResultReason.NoMatch:
    #         print("No speech could be recognized")
    #     elif result.reason == speechsdk.ResultReason.Canceled:
    #         cancellation_details = result.cancellation_details
    #         print("Speech Recognition canceled:", cancellation_details.reason)
    #         if cancellation_details.reason == speechsdk.CancellationReason.Error:
    #             print("Error details:", cancellation_details.error_details)
    # except Exception as ex:
    #     print("Exception:", ex)


    
