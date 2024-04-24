#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Conversation transcription samples for the Microsoft Cognitive Services Speech SDK
"""

import time
import os
import uuid
import json

from scipy.io import wavfile
# from dotenv import load_dotenv
from sentiment_helper import perform_sentiment_analysis

try:
    import azure.cognitiveservices.speech as speechsdk
except ImportError:
    print("""
    Importing the Speech SDK for Python failed.
    Refer to
    https://docs.microsoft.com/azure/cognitive-services/speech-service/quickstart-python for
    installation instructions.
    """)
    import sys
    sys.exit(1)

# Set up the subscription info for the Speech Service:
# Replace with your own subscription key and service region (e.g., "centralus").
# See the limitations in supported regions,
# https://docs.microsoft.com/azure/cognitive-services/speech-service/how-to-use-conversation-transcription
# load_dotenv()
speech_key = os.environ.get('SPEECH_KEY')
service_region = os.environ.get('SPEECH_REGION')

# This sample uses a wavfile which is captured using a supported Speech SDK devices (8 channel, 16kHz, 16-bit PCM)
# See https://docs.microsoft.com/azure/cognitive-services/speech-service/speech-devices-sdk-microphone
conversationfilename = "call2.wav"



# This sample demonstrates how to use conversation transcription.
def conversation_transcription():
    """transcribes a conversation"""
    # Creates speech configuration with subscription information
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    channels = 1
    bits_per_sample = 16
    samples_per_second = 16000

    # Create audio configuration using the push stream
    wave_format = speechsdk.audio.AudioStreamFormat(samples_per_second, bits_per_sample, channels)
    stream = speechsdk.audio.PushAudioInputStream(stream_format=wave_format)
    # Read the whole wave files at once and stream it to sdk
    # _, wav_data = wavfile.read(conversationfilename)
    # stream.write(wav_data.tobytes())
    # stream.close()
    # audio_config = speechsdk.audio.AudioConfig(stream=stream)
    audio_config = speechsdk.AudioConfig(filename=conversationfilename)

    transcriber = speechsdk.transcription.ConversationTranscriber(speech_config, audio_config)

    done = False

    def stop_cb(evt: speechsdk.SessionEventArgs):
        """callback that signals to stop continuous transcription upon receiving an event `evt`"""
        print('CLOSING {}'.format(evt))
        nonlocal done
        done = True
    

    conversation = []
    flags = []
    agent = "Bobby"
    customer = "Emily"

    def add_to_conversation(evt):
        
        # print("add_to_conversation called")
        # nonlocal conversation
        
        curr = {
            "speaker": evt.result.speaker_id,
            "text": evt.result.text
        }
        set_speakers(curr, agent, customer)
        print("curr: {}".format(curr))
        flagged = perform_sentiment_analysis(curr["text"])
        # print("flagged: {}".format(flagged))
        conversation.append(curr)
        # print("conversation: {}".format(conversation))
        for f in flagged:
            flags.append({
                'speaker': curr['speaker'],
                'text': curr['text'],
                'sentiment': f.sentiment,
                'confidenceScores': {
                    'positive': f.confidence_scores.positive,
                    'negative': f.confidence_scores.negative,
                    'neutral': f.confidence_scores.neutral
                }
            })



    # Subscribe to the events fired by the conversation transcriber
    # transcriber.transcribing.connect(lambda evt: print("TRANSCRIBING: {}".format(evt.result)))
    transcriber.transcribed.connect(lambda evt: add_to_conversation(evt))
    transcriber.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
    transcriber.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
    transcriber.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))
    # stop continuous transcription on either session stopped or canceled events
    transcriber.session_stopped.connect(stop_cb)
    transcriber.canceled.connect(stop_cb)

    res = transcriber.start_transcribing_async()
    print("Start response: {}".format(res))

    
    i = 0
    while not done:
        # print("sleeping " + str(i))
        i += 1
        time.sleep(.5)

    result = transcriber.stop_transcribing_async()
    print("stopped: {}".format(result))
    return {
        "representativeName": agent,
        "customerName": customer,
        "date": "04/22/2024",
        "callLength": 20,
        "summary": "This is a call summary",
        "transcription": conversation,
        "flags": flags
    }

def set_speakers(sentence, agent, customer):
    if sentence['speaker'] == 'Guest-1':
        sentence['speaker'] = agent
    if sentence['speaker'] == 'Guest-2':
        sentence['speaker'] = customer

full_conv_flags = conversation_transcription()

# set_speakers(full_conv, "Eddie", "Emily")

with open("full_transcription_flags_" + conversationfilename.replace(".wav", "") + ".json", 'w') as f:
    f.write(json.dumps(full_conv_flags, indent=4))

print("full conversation: {}".format(full_conv_flags['transcription']))
print("all flags: {}".format(full_conv_flags['flags']))