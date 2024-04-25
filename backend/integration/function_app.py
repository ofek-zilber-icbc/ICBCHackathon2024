import azure.functions as func
import logging
import json
from datetime import datetime

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="HttpIntegration")
def HttpIntegration(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    
    response = {
        "calls": [
            {
    "short": {
        "audioFile": "/call2.wav",
        "representativeName": "Bobby",
        "customerName": "Emily",
        "date": "04/22/2024",
        "callLength": 20,
        "summary": "This is a call summary",
        "transcription": [
            {
                "speaker": "Bobby",
                "text": "Hi, this is Bobby calling from ICBC's assembly."
            },
            {
                "speaker": "Bobby",
                "text": "Hi, this is Emily. Yes."
            },
            {
                "speaker": "Bobby",
                "text": "Oh, hi, Emily. I'm glad I got ahold of. It's been really hard to reach you. I've been trying."
            },
            {
                "speaker": "Bobby",
                "text": "To call you for a."
            },
            {
                "speaker": "Bobby",
                "text": "While who has it? Yeah, it has. But I guess you're really busy, so I'm glad that I got ahold of you and I wanted to talk to you about your treatment and your injury claim."
            },
            {
                "speaker": "Emily",
                "text": "OK. What did you want to talk about specifically? Well."
            },
            {
                "speaker": "Bobby",
                "text": "I want to talk to you about how your treatment is going, So I've noticed that."
            },
            {
                "speaker": "Bobby",
                "text": "Been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist. I see that your doctor had recommended it to before and I want to follow up to see if you've been doing that or if you've talked."
            },
            {
                "speaker": "Emily",
                "text": "To them, yeah, it's been kind of easier just to go to my massage therapist because I can get appointments. I was hoping I could find a physiotherapist in the same clinic, but I couldn't, so I thought it was just easier to keep going to my massage."
            },
            {
                "speaker": "Bobby",
                "text": "Therapist. OK, well, I want you to know that it's been."
            },
            {
                "speaker": "Bobby",
                "text": "About a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time."
            },
            {
                "speaker": "Emily",
                "text": "Oh, OK Well, my massage therapist kept booking me in, so I thought I was just good to keep going."
            },
            {
                "speaker": "Bobby",
                "text": "There. Yeah, I can see that. And we approved the last treatment request that your massage therapy sent in. But to be honest with you, I'm not going to prove the next one. I did talk to you about talking to your physiotherapist and making that call. So you're going to need to do that if you want to keep having treatment."
            },
            {
                "speaker": "Bobby",
                "text": "Provided under your claim."
            },
            {
                "speaker": "Bobby",
                "text": "Well, you mentioned that you're still having problems with your knee and you're fine now. Is that what you're saying?"
            },
            {
                "speaker": "Emily",
                "text": "Yeah, I mean, it still hurts, but I think, you know, it could be worse. So."
            },
            {
                "speaker": "Bobby",
                "text": "Well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards, so."
            },
            {
                "speaker": "Bobby",
                "text": "When we talked and I gave you the information I you are expected to follow it. You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better."
            },
            {
                "speaker": "Emily",
                "text": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too if I don't get any more."
            },
            {
                "speaker": "Bobby",
                "text": "Treatment. Well, I really want you to reach out and call your physiotherapist since you haven't done it yet and this is the third time you've talked about it. If you could please give me a call back next week."
            },
            {
                "speaker": "Bobby",
                "text": "Let's try to do that so that you're talking to them by then and I would like to get an update from you. If I don't, then I don't think I'll be able to approve any more of."
            },
            {
                "speaker": "Emily",
                "text": "The massage either OK, So what happens if I need more treatment, though, or if I feel like I'm still in pain or I'm not able to?"
            },
            {
                "speaker": "Bobby",
                "text": "Do all of my regular stuff well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back. But if you're going to pause and stop treatment, it's going to be really difficult for us to approve any more for you."
            },
            {
                "speaker": "Bobby",
                "text": "Really. I mean, I've talked to you before and I put the notes in your file here that you're not following the advice that."
            },
            {
                "speaker": "Emily",
                "text": "You were given. Oh, OK. Well, I'm really sorry. I didn't mean to not follow the advice like I I typically do like to follow what you tell me. I just messed up. Forgot. But yeah, OK, I can do what you told me and I'll. I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there. But if not, I guess I just won't bother you anymore."
            },
            {
                "speaker": "Bobby",
                "text": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next. Again, if I don't hear back from by next week, then we won't be approving any more."
            },
            {
                "speaker": "Bobby",
                "text": "Treatment."
            },
            {
                "speaker": "Emily",
                "text": "OK. OK. Well, I'll try to follow up then with the physiotherapist and I'll try to get back to you next week is."
            },
            {
                "speaker": "Bobby",
                "text": "There anything else that I should be doing? No. You have my number and like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of."
            },
            {
                "speaker": "Bobby",
                "text": "You so you know what time I work, so please give me a call. OK. I'm really sorry about that. Thanks so much for calling me today."
            },
            {
                "speaker": "Bobby",
                "text": "OK. Bye."
            }
        ],
        "flags": [
            {
                "speaker": "Bobby",
                "text": "Oh, hi, Emily. I'm glad I got ahold of. It's been really hard to reach you. I've been trying.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.01,
                    "negative": 0.93,
                    "neutral": 0.06
                }
            },
            {
                "speaker": "Bobby",
                "text": "Do all of my regular stuff well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back. But if you're going to pause and stop treatment, it's going to be really difficult for us to approve any more for you.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.01,
                    "negative": 0.87,
                    "neutral": 0.11
                }
            },
            {
                "speaker": "Emily",
                "text": "You were given. Oh, OK. Well, I'm really sorry. I didn't mean to not follow the advice like I I typically do like to follow what you tell me. I just messed up. Forgot. But yeah, OK, I can do what you told me and I'll. I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there. But if not, I guess I just won't bother you anymore.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.01,
                    "negative": 0.94,
                    "neutral": 0.05
                }
            },
            {
                "speaker": "Bobby",
                "text": "You so you know what time I work, so please give me a call. OK. I'm really sorry about that. Thanks so much for calling me today.",
                "sentiment": "negative",
                "confidenceScores": {
                    "positive": 0.02,
                    "negative": 0.93,
                    "neutral": 0.05
                }
            }
        ]
    },
    "long": {
      "durationInTicks": 2603500000,
      "conversations": [
        {
          "id": 0,
          "offset": "PT3.6S",
          "offset_in_ticks": 36000000.0,
          "duration_in_ticks": 30400000.0,
          "text": "Hi, this is Bobby calling from ICBCS Assembly.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 1,
          "offset": "PT6.76S",
          "offset_in_ticks": 67600000.0,
          "duration_in_ticks": 9200000.0,
          "text": "Hi, this is Emily.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 2,
          "offset": "PT7.68S",
          "offset_in_ticks": 76800000.0,
          "duration_in_ticks": 2000000.0,
          "text": "Yes.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 3,
          "offset": "PT8.4S",
          "offset_in_ticks": 84000000.0,
          "duration_in_ticks": 7600000.0,
          "text": "Oh, hi, Emily.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 4,
          "offset": "PT9.16S",
          "offset_in_ticks": 91600000.0,
          "duration_in_ticks": 14000000.0,
          "text": "I'm glad I got a hold of you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 5,
          "offset": "PT10.56S",
          "offset_in_ticks": 105600000.0,
          "duration_in_ticks": 10000000.0,
          "text": "It's been really hard to reach you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 6,
          "offset": "PT11.56S",
          "offset_in_ticks": 115600000.0,
          "duration_in_ticks": 14800000.0,
          "text": "I've been trying to call you for a while.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 7,
          "offset": "PT13.48S",
          "offset_in_ticks": 134800000.0,
          "duration_in_ticks": 5200000.0,
          "text": "Oh, has it?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 8,
          "offset": "PT14.68S",
          "offset_in_ticks": 146800000.0,
          "duration_in_ticks": 8000000.0,
          "text": "Yeah, it has.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 9,
          "offset": "PT15.48S",
          "offset_in_ticks": 154800000.0,
          "duration_in_ticks": 18800000.0,
          "text": "But I guess you're really busy.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 10,
          "offset": "PT17.4S",
          "offset_in_ticks": 174000000.0,
          "duration_in_ticks": 16400000.0,
          "text": "So I'm glad that I got a hold of you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 11,
          "offset": "PT19.52S",
          "offset_in_ticks": 195200000.0,
          "duration_in_ticks": 44800000.0,
          "text": "And I wanted to talk to you about your treatment and your injury claim.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 12,
          "offset": "PT24.56S",
          "offset_in_ticks": 245600000.0,
          "duration_in_ticks": 5600000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 13,
          "offset": "PT25.56S",
          "offset_in_ticks": 255600000.0,
          "duration_in_ticks": 20000000.0,
          "text": "What did you want to talk about specifically?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 14,
          "offset": "PT28.68S",
          "offset_in_ticks": 286800000.0,
          "duration_in_ticks": 24400000.0,
          "text": "Well, I want to talk to you about how your treatment is going.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 15,
          "offset": "PT31.16S",
          "offset_in_ticks": 311600000.0,
          "duration_in_ticks": 111600000.0,
          "text": "So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 16,
          "offset": "PT42.32S",
          "offset_in_ticks": 423200000.0,
          "duration_in_ticks": 63600000.0,
          "text": "I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 17,
          "offset": "PT50S",
          "offset_in_ticks": 500000000.0,
          "duration_in_ticks": 44400000.0,
          "text": "Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 18,
          "offset": "PT55.56S",
          "offset_in_ticks": 555600000.0,
          "duration_in_ticks": 38400000.0,
          "text": "I was hoping I could find a physiotherapist in the same clinic, but I couldn't.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 19,
          "offset": "PT59.4S",
          "offset_in_ticks": 594000000.0,
          "duration_in_ticks": 29600000.0,
          "text": "So I thought it was just easier to keep going to my massage therapist.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 20,
          "offset": "PT1M3.16S",
          "offset_in_ticks": 631600000.0,
          "duration_in_ticks": 114000000.0,
          "text": "OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 21,
          "offset": "PT1M15.96S",
          "offset_in_ticks": 759600000.0,
          "duration_in_ticks": 56400000.0,
          "text": "Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 22,
          "offset": "PT1M22.24S",
          "offset_in_ticks": 822400000.0,
          "duration_in_ticks": 10400000.0,
          "text": "Yeah, I can see that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 23,
          "offset": "PT1M23.28S",
          "offset_in_ticks": 832800000.0,
          "duration_in_ticks": 48800000.0,
          "text": "And we approved the last treatment request that your massage therapist sent in.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 24,
          "offset": "PT1M28.36S",
          "offset_in_ticks": 883600000.0,
          "duration_in_ticks": 21200000.0,
          "text": "But to be honest with you, I'm not going to approve the next one.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 25,
          "offset": "PT1M30.88S",
          "offset_in_ticks": 908800000.0,
          "duration_in_ticks": 32000000.0,
          "text": "I did talk to you about talking to your physiotherapist and making that call.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 26,
          "offset": "PT1M34.28S",
          "offset_in_ticks": 942800000.0,
          "duration_in_ticks": 47200000.0,
          "text": "So you're going to need to do that if you want to keep having treatment provided under your claim.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 27,
          "offset": "PT1M39.36S",
          "offset_in_ticks": 993600000.0,
          "duration_in_ticks": 10400000.0,
          "text": "OK, that makes sense.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 28,
          "offset": "PT1M40.76S",
          "offset_in_ticks": 1007600000.0,
          "duration_in_ticks": 5600000.0,
          "text": "I can do that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 29,
          "offset": "PT1M41.4S",
          "offset_in_ticks": 1014000000.0,
          "duration_in_ticks": 3600000.0,
          "text": "You know what?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 30,
          "offset": "PT1M41.76S",
          "offset_in_ticks": 1017600000.0,
          "duration_in_ticks": 47600000.0,
          "text": "I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 31,
          "offset": "PT1M49.48S",
          "offset_in_ticks": 1094800000.0,
          "duration_in_ticks": 54400000.0,
          "text": "Well, you mentioned that you're still having problems with your knee and you're fine now.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 32,
          "offset": "PT1M54.92S",
          "offset_in_ticks": 1149200000.0,
          "duration_in_ticks": 8400000.0,
          "text": "Is that what you're saying?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 33,
          "offset": "PT1M56.32S",
          "offset_in_ticks": 1163200000.0,
          "duration_in_ticks": 3600000.0,
          "text": "Yeah.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 34,
          "offset": "PT1M56.68S",
          "offset_in_ticks": 1166800000.0,
          "duration_in_ticks": 38400000.0,
          "text": "I mean, it still hurts, but I think, you know, it could be worse.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 35,
          "offset": "PT2M0.76S",
          "offset_in_ticks": 1207600000.0,
          "duration_in_ticks": 92000000.0,
          "text": "So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 36,
          "offset": "PT2M9.96S",
          "offset_in_ticks": 1299600000.0,
          "duration_in_ticks": 52800000.0,
          "text": "So when we talked and I gave you the information, I you are expected to follow it.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 37,
          "offset": "PT2M15.24S",
          "offset_in_ticks": 1352400000.0,
          "duration_in_ticks": 78400000.0,
          "text": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 38,
          "offset": "PT2M23.72S",
          "offset_in_ticks": 1437200000.0,
          "duration_in_ticks": 86400000.0,
          "text": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 39,
          "offset": "PT2M32.36S",
          "offset_in_ticks": 1523600000.0,
          "duration_in_ticks": 53600000.0,
          "text": "If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 40,
          "offset": "PT2M37.72S",
          "offset_in_ticks": 1577200000.0,
          "duration_in_ticks": 58000000.0,
          "text": "And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 41,
          "offset": "PT2M43.72S",
          "offset_in_ticks": 1637200000.0,
          "duration_in_ticks": 23600000.0,
          "text": "Let's try to do that so that you're talking to them by then.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 42,
          "offset": "PT2M46.08S",
          "offset_in_ticks": 1660800000.0,
          "duration_in_ticks": 14400000.0,
          "text": "And I would like to get an update from you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 43,
          "offset": "PT2M47.88S",
          "offset_in_ticks": 1678800000.0,
          "duration_in_ticks": 50000000.0,
          "text": "If I don't, then I don't think I'll be able to approve any more of the massage either.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 44,
          "offset": "PT2M53.44S",
          "offset_in_ticks": 1734400000.0,
          "duration_in_ticks": 4400000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 45,
          "offset": "PT2M53.88S",
          "offset_in_ticks": 1738800000.0,
          "duration_in_ticks": 79200000.0,
          "text": "So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 46,
          "offset": "PT3M2.2S",
          "offset_in_ticks": 1822000000.0,
          "duration_in_ticks": 71600000.0,
          "text": "Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 47,
          "offset": "PT3M9.36S",
          "offset_in_ticks": 1893600000.0,
          "duration_in_ticks": 57200000.0,
          "text": "But if you're going to pause and stop treatment, it's going to be really difficult for us to approve any more for you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 48,
          "offset": "PT3M16.16S",
          "offset_in_ticks": 1961600000.0,
          "duration_in_ticks": 3600000.0,
          "text": "Really.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 49,
          "offset": "PT3M16.52S",
          "offset_in_ticks": 1965200000.0,
          "duration_in_ticks": 53600000.0,
          "text": "I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 50,
          "offset": "PT3M23S",
          "offset_in_ticks": 2030000000.0,
          "duration_in_ticks": 8000000.0,
          "text": "Oh, OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 51,
          "offset": "PT3M24S",
          "offset_in_ticks": 2040000000.0,
          "duration_in_ticks": 14000000.0,
          "text": "Well, I'm really sorry.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 52,
          "offset": "PT3M25.4S",
          "offset_in_ticks": 2054000000.0,
          "duration_in_ticks": 57600000.0,
          "text": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 53,
          "offset": "PT3M31.16S",
          "offset_in_ticks": 2111600000.0,
          "duration_in_ticks": 49600000.0,
          "text": "I just must have forgot, but yeah, OK, I can do what you told me and I'll.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 54,
          "offset": "PT3M36.12S",
          "offset_in_ticks": 2161200000.0,
          "duration_in_ticks": 41200000.0,
          "text": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 55,
          "offset": "PT3M40.24S",
          "offset_in_ticks": 2202400000.0,
          "duration_in_ticks": 42000000.0,
          "text": "But if not, I guess I just won't bother you anymore.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 56,
          "offset": "PT3M45.24S",
          "offset_in_ticks": 2252400000.0,
          "duration_in_ticks": 44000000.0,
          "text": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 57,
          "offset": "PT3M49.88S",
          "offset_in_ticks": 2298800000.0,
          "duration_in_ticks": 45200000.0,
          "text": "Again, if I don't hear back from by next week, then we won't be approving any more treatment.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 58,
          "offset": "PT3M55.6S",
          "offset_in_ticks": 2356000000.0,
          "duration_in_ticks": 4800000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 59,
          "offset": "PT3M56.24S",
          "offset_in_ticks": 2362400000.0,
          "duration_in_ticks": 40400000.0,
          "text": "OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 60,
          "offset": "PT4M0.28S",
          "offset_in_ticks": 2402800000.0,
          "duration_in_ticks": 16000000.0,
          "text": "Is there anything else that I should be doing?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 61,
          "offset": "PT4M2.28S",
          "offset_in_ticks": 2422800000.0,
          "duration_in_ticks": 2000000.0,
          "text": "No.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 62,
          "offset": "PT4M2.48S",
          "offset_in_ticks": 2424800000.0,
          "duration_in_ticks": 6800000.0,
          "text": "You have my number.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 63,
          "offset": "PT4M3.16S",
          "offset_in_ticks": 2431600000.0,
          "duration_in_ticks": 44800000.0,
          "text": "And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 64,
          "offset": "PT4M7.64S",
          "offset_in_ticks": 2476400000.0,
          "duration_in_ticks": 19600000.0,
          "text": "So you know what time I work.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 65,
          "offset": "PT4M9.6S",
          "offset_in_ticks": 2496000000.0,
          "duration_in_ticks": 8800000.0,
          "text": "So please give me a call.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 66,
          "offset": "PT4M10.64S",
          "offset_in_ticks": 2506400000.0,
          "duration_in_ticks": 4000000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 67,
          "offset": "PT4M11.04S",
          "offset_in_ticks": 2510400000.0,
          "duration_in_ticks": 10400000.0,
          "text": "I'm really sorry about that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 68,
          "offset": "PT4M12.4S",
          "offset_in_ticks": 2524000000.0,
          "duration_in_ticks": 12800000.0,
          "text": "Thanks so much for calling me today.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 69,
          "offset": "PT4M14S",
          "offset_in_ticks": 2540000000.0,
          "duration_in_ticks": 4000000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 70,
          "offset": "PT4M14.48S",
          "offset_in_ticks": 2544800000.0,
          "duration_in_ticks": 2000000.0,
          "text": "Bye.",
          "role": "Agent",
          "participantId": 0
        }
      ]
    }
},
{
    "short": {
      "audioFile": "/call3.wav",
      "representativeName": "Eddie",
      "customerName": "Emily",
      "date": "04/15/2024",
      "callLength": 4,
      "summary": "This is a call summary",
      "transcription": [
          {
              "speaker": "Eddie",
              "text": "Hi there. I'm calling from ICBC. My name is Eddie. I'm looking for Emily, please."
          },
          {
              "speaker": "Eddie",
              "text": "This is Emily."
          },
          {
              "speaker": "Eddie",
              "text": "Hey Emily, how are?"
          },
          {
              "speaker": "Emily",
              "text": "You. I'm OK. How are you?"
          },
          {
              "speaker": "Eddie",
              "text": "I'm doing pretty good. How How was the oven repair that you had the other day? Did that work out?"
          },
          {
              "speaker": "Emily",
              "text": "OK, oh, actually they weren't able to fix it and I have to have them come."
          },
          {
              "speaker": "Eddie",
              "text": "Back another day next week. Oh no, I hope that goes well. And yeah, but you know, hopefully it doesn't cost too much or anything. But yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery. And we did get a chance to review your treatment plan. How does that sound?"
          },
          {
              "speaker": "Eddie",
              "text": "Thanks. Now is a good time. OK, great. This will probably last maybe 5 minutes or so, maybe even less. But you know, throughout this conversation, just don't hesitate to ask any questions and like we usually do, but I've got some interesting news here because we have had a chance to review the treatment that you're going through. And as you know, we've had a couple steps leading up to today and that involves, for example, our medical assessment. We've had a chance to speak with your care team as well."
          },
          {
              "speaker": "Eddie",
              "text": "Really just to take a look at how your recovery is going. So I just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that. Before I go into that, did you have any questions about what we've been doing so far?"
          },
          {
              "speaker": "Emily",
              "text": "No, that makes sense. I'm curious to know what the next steps are and and you know what the decision is regarding the treatment."
          },
          {
              "speaker": "Eddie",
              "text": "Really happy to go over it and really want to give you as much details as possible on this and."
          },
          {
              "speaker": "Eddie",
              "text": "Basically after our review cycle that we've had, we've had the medical assessment like I mentioned and then talked to the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan. We took took a look at some of the progress. We took a look at some of the limitations that you've had. I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs. You also have some challenges with raising your arm up above."
          },
          {
              "speaker": "Eddie",
              "text": "Your shoulder and a lot of that is resolved based on what we can see here. You're also able to get back to most of your daily activities. So I think you mentioned something along the lines of playing soccer. You're back to playing about 90% of those games and while there is a little bit of pain, you're able to go through all of it. So reviewing all the information there at this point, it doesn't look like we can approve further treatment for your physiotherapy. What we can do and and offer is."
          },
          {
              "speaker": "Eddie",
              "text": "To help get you into something more active, just to really help you get to that next level of your recovery and move you move you past the passive treatments here. How does that sound?"
          },
          {
              "speaker": "Emily",
              "text": "OK. What do you mean something more active have?"
          },
          {
              "speaker": "Eddie",
              "text": "You have you had a chance to try kinesiology or any self self-guided training gym programs? Any of those before?"
          },
          {
              "speaker": "Emily",
              "text": "No, I think I've seen a sign for it at the clinic I go to, but no, I haven't."
          },
          {
              "speaker": "Eddie",
              "text": "Fair enough, and happy to go over some of those details with you. I think there's a couple of things we can definitely do with you and we want to find something that works for you as well. Umm, do you have any actually because they're probably the soccer team. Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active?"
          },
          {
              "speaker": "Emily",
              "text": "Oh, actually, you know what? I think someone on my team might be a kinesiologist themselves. Yeah, maybe I'll reach out to them."
          },
          {
              "speaker": "Eddie",
              "text": "I think that's a great idea. That's a great start. Kind of see what works for them and then you can let me know if there's also any equipment or anything that might help you become more independent in your training."
          },
          {
              "speaker": "Eddie",
              "text": "Just to really get you to that final step, your recovery, and once you're done that part, then we can probably look at discharging the claim. How does that sound? Did you want to go check in with your teammate? And then we can have a conversation about, let's say, next Thursday, may I call you around the same time and then we can look at some of those."
          },
          {
              "speaker": "Emily",
              "text": "Options together? Yeah, that sounds good. Next Thursday works for me. So we can chat then."
          },
          {
              "speaker": "Eddie",
              "text": "Maybe we'll get some updates and some good news on repairing your oven as well. So before I wrap up here, though, since you've got me any other questions like anything else I can help you out with."
          },
          {
              "speaker": "Emily",
              "text": "No, I think that's it for now. I'll talk to them and then I'll try to think of any questions before we speak next Thursday."
          },
          {
              "speaker": "Eddie",
              "text": "Absolutely. Fantastic. I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job and I think we'll get you to that last step and we'll move forward together on that, OK. So we'll chat next week then. OK. Fantastic. Bye for now."
          }
      ],
      "flags": []
  },
    "long": {
      "durationInTicks": 2938500000,
      "conversations": [
        {
          "id": 0,
          "offset": "PT3.32S",
          "offset_in_ticks": 33200000.0,
          "duration_in_ticks": 4400000.0,
          "text": "Hi there.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 1,
          "offset": "PT4.16S",
          "offset_in_ticks": 41600000.0,
          "duration_in_ticks": 12800000.0,
          "text": "I'm calling from ICBC.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 2,
          "offset": "PT5.44S",
          "offset_in_ticks": 54400000.0,
          "duration_in_ticks": 11600000.0,
          "text": "My name is Eddie.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 3,
          "offset": "PT6.6S",
          "offset_in_ticks": 66000000.0,
          "duration_in_ticks": 17200000.0,
          "text": "I'm looking for Emily, please.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 4,
          "offset": "PT7.72S",
          "offset_in_ticks": 77200000.0,
          "duration_in_ticks": 5600000.0,
          "text": "Please.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 5,
          "offset": "PT8.32S",
          "offset_in_ticks": 83200000.0,
          "duration_in_ticks": 9200000.0,
          "text": "Hey, Emily.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 6,
          "offset": "PT9.92S",
          "offset_in_ticks": 99200000.0,
          "duration_in_ticks": 4800000.0,
          "text": "Hey, Emily.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 7,
          "offset": "PT10.4S",
          "offset_in_ticks": 104000000.0,
          "duration_in_ticks": 4400000.0,
          "text": "How are you?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 8,
          "offset": "PT10.84S",
          "offset_in_ticks": 108400000.0,
          "duration_in_ticks": 11200000.0,
          "text": "I'm OK.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 9,
          "offset": "PT11.96S",
          "offset_in_ticks": 119600000.0,
          "duration_in_ticks": 3600000.0,
          "text": "How are you?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 10,
          "offset": "PT12.68S",
          "offset_in_ticks": 126800000.0,
          "duration_in_ticks": 10400000.0,
          "text": "I'm doing pretty good.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 11,
          "offset": "PT13.72S",
          "offset_in_ticks": 137200000.0,
          "duration_in_ticks": 35200000.0,
          "text": "How How was the oven repair that you had the other day?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 12,
          "offset": "PT17.44S",
          "offset_in_ticks": 174400000.0,
          "duration_in_ticks": 11600000.0,
          "text": "Did that work out OK?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 13,
          "offset": "PT18.8S",
          "offset_in_ticks": 188000000.0,
          "duration_in_ticks": 32000000.0,
          "text": "Oh, actually, they weren't able to fix it.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 14,
          "offset": "PT22S",
          "offset_in_ticks": 220000000.0,
          "duration_in_ticks": 22000000.0,
          "text": "And I have to have them come back another day next week.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 15,
          "offset": "PT24.6S",
          "offset_in_ticks": 246000000.0,
          "duration_in_ticks": 3600000.0,
          "text": "Oh, no.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 16,
          "offset": "PT24.96S",
          "offset_in_ticks": 249600000.0,
          "duration_in_ticks": 2400000.0,
          "text": "I hope.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 17,
          "offset": "PT25.32S",
          "offset_in_ticks": 253200000.0,
          "duration_in_ticks": 9600000.0,
          "text": "Hope that goes well.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 18,
          "offset": "PT26.28S",
          "offset_in_ticks": 262800000.0,
          "duration_in_ticks": 39600000.0,
          "text": "And yeah, but you know, hopefully it doesn't cost too much or anything.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 19,
          "offset": "PT30.24S",
          "offset_in_ticks": 302400000.0,
          "duration_in_ticks": 46800000.0,
          "text": "But yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 20,
          "offset": "PT34.92S",
          "offset_in_ticks": 349200000.0,
          "duration_in_ticks": 19600000.0,
          "text": "And we did get a chance to review your treatment plan.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 21,
          "offset": "PT36.88S",
          "offset_in_ticks": 368800000.0,
          "duration_in_ticks": 6000000.0,
          "text": "How's that sound?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 22,
          "offset": "PT37.48S",
          "offset_in_ticks": 374800000.0,
          "duration_in_ticks": 1200000.0,
          "text": "Good.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 23,
          "offset": "PT38.4S",
          "offset_in_ticks": 384000000.0,
          "duration_in_ticks": 2800000.0,
          "text": "Thanks.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 24,
          "offset": "PT39.04S",
          "offset_in_ticks": 390400000.0,
          "duration_in_ticks": 10000000.0,
          "text": "Yeah, this is a good time.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 25,
          "offset": "PT40.12S",
          "offset_in_ticks": 401200000.0,
          "duration_in_ticks": 6400000.0,
          "text": "OK, great.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 26,
          "offset": "PT40.76S",
          "offset_in_ticks": 407600000.0,
          "duration_in_ticks": 41200000.0,
          "text": "This will probably last maybe 5 minutes or so, maybe even less.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 27,
          "offset": "PT44.88S",
          "offset_in_ticks": 448800000.0,
          "duration_in_ticks": 38400000.0,
          "text": "But you know, throughout this conversation, just don't hesitate to ask any questions.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 28,
          "offset": "PT48.72S",
          "offset_in_ticks": 487200000.0,
          "duration_in_ticks": 80400000.0,
          "text": "And like we usually do, but got some interesting news here because we have had a chance to review the treatment that you're going through.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 29,
          "offset": "PT56.76S",
          "offset_in_ticks": 567600000.0,
          "duration_in_ticks": 73600000.0,
          "text": "And as you know, we've had a couple steps leading up to today and that involved, for example, our medical assessment.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 30,
          "offset": "PT1M4.56S",
          "offset_in_ticks": 645600000.0,
          "duration_in_ticks": 59200000.0,
          "text": "We've had a chance to speak with your care team as well, really just to take a look at how your recovery is going.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 31,
          "offset": "PT1M10.48S",
          "offset_in_ticks": 704800000.0,
          "duration_in_ticks": 89600000.0,
          "text": "So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 32,
          "offset": "PT1M19.88S",
          "offset_in_ticks": 798800000.0,
          "duration_in_ticks": 34400000.0,
          "text": "Before I go into that, did you have any questions about what we've been doing so far?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 33,
          "offset": "PT1M24.76S",
          "offset_in_ticks": 847600000.0,
          "duration_in_ticks": 9200000.0,
          "text": "No, that makes sense.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 34,
          "offset": "PT1M25.68S",
          "offset_in_ticks": 856800000.0,
          "duration_in_ticks": 57600000.0,
          "text": "I'm, I'm curious to know what the next steps are and and you know what the decision is regarding the treatment.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 35,
          "offset": "PT1M32.68S",
          "offset_in_ticks": 926800000.0,
          "duration_in_ticks": 48000000.0,
          "text": "I'm really happy to go over it and really want to give you as much details as possible on this.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 36,
          "offset": "PT1M37.48S",
          "offset_in_ticks": 974800000.0,
          "duration_in_ticks": 134000000.0,
          "text": "And basically after our review cycle that we've had, we've had the medical assessment like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 37,
          "offset": "PT1M51.2S",
          "offset_in_ticks": 1112000000.0,
          "duration_in_ticks": 21200000.0,
          "text": "We took took a look at some of the progress.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 38,
          "offset": "PT1M53.8S",
          "offset_in_ticks": 1138000000.0,
          "duration_in_ticks": 31200000.0,
          "text": "We took a look at some of the limitations that you've had.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 39,
          "offset": "PT1M57.16S",
          "offset_in_ticks": 1171600000.0,
          "duration_in_ticks": 152400000.0,
          "text": "I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs, you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 40,
          "offset": "PT2M13.04S",
          "offset_in_ticks": 1330400000.0,
          "duration_in_ticks": 30400000.0,
          "text": "You're also able to get back to most of your daily activities.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 41,
          "offset": "PT2M16.08S",
          "offset_in_ticks": 1360800000.0,
          "duration_in_ticks": 37600000.0,
          "text": "So I think you mentioned something along the lines of playing soccer.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 42,
          "offset": "PT2M20.12S",
          "offset_in_ticks": 1401200000.0,
          "duration_in_ticks": 80800000.0,
          "text": "You're back to playing about 90% of those games and while there is a little bit of pain, you're you're able to go through all of it.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 43,
          "offset": "PT2M28.2S",
          "offset_in_ticks": 1482000000.0,
          "duration_in_ticks": 76400000.0,
          "text": "So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 44,
          "offset": "PT2M36.64S",
          "offset_in_ticks": 1566400000.0,
          "duration_in_ticks": 118800000.0,
          "text": "What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you, move you past the passive treatments here.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 45,
          "offset": "PT2M48.52S",
          "offset_in_ticks": 1685200000.0,
          "duration_in_ticks": 32000000.0,
          "text": "How does that sound OK, what do you mean something more active?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 46,
          "offset": "PT2M53S",
          "offset_in_ticks": 1730000000.0,
          "duration_in_ticks": 89200000.0,
          "text": "Have you, have you had a chance to try kinesiology or any self self-guided training gym programs?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 47,
          "offset": "PT3M1.92S",
          "offset_in_ticks": 1819200000.0,
          "duration_in_ticks": 9200000.0,
          "text": "Any of those before?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 48,
          "offset": "PT3M3.8S",
          "offset_in_ticks": 1838000000.0,
          "duration_in_ticks": 3200000.0,
          "text": "No.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 49,
          "offset": "PT3M4.12S",
          "offset_in_ticks": 1841200000.0,
          "duration_in_ticks": 39600000.0,
          "text": "I think I've seen a sign for it at the clinic I go to, but no, I haven't.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 50,
          "offset": "PT3M9.84S",
          "offset_in_ticks": 1898400000.0,
          "duration_in_ticks": 7200000.0,
          "text": "Oh, fair enough.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 51,
          "offset": "PT3M10.56S",
          "offset_in_ticks": 1905600000.0,
          "duration_in_ticks": 21200000.0,
          "text": "And happy to go over some of those details with you.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 52,
          "offset": "PT3M12.68S",
          "offset_in_ticks": 1926800000.0,
          "duration_in_ticks": 47600000.0,
          "text": "I think there's a couple of things we can definitely do with you and we want to find something that works for you as well.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 53,
          "offset": "PT3M18.6S",
          "offset_in_ticks": 1986000000.0,
          "duration_in_ticks": 27600000.0,
          "text": "Do you have any actually, because they're part of the soccer team.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 54,
          "offset": "PT3M21.72S",
          "offset_in_ticks": 2017200000.0,
          "duration_in_ticks": 78400000.0,
          "text": "Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 55,
          "offset": "PT3M30.12S",
          "offset_in_ticks": 2101200000.0,
          "duration_in_ticks": 9200000.0,
          "text": "Oh, actually, you know what?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 56,
          "offset": "PT3M31.04S",
          "offset_in_ticks": 2110400000.0,
          "duration_in_ticks": 39200000.0,
          "text": "I think someone on my team might be a kinesiologist themselves.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 57,
          "offset": "PT3M34.96S",
          "offset_in_ticks": 2149600000.0,
          "duration_in_ticks": 13600000.0,
          "text": "Yeah, maybe I'll reach out to them.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 58,
          "offset": "PT3M37.16S",
          "offset_in_ticks": 2171600000.0,
          "duration_in_ticks": 8400000.0,
          "text": "I think that's a great idea.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 59,
          "offset": "PT3M38S",
          "offset_in_ticks": 2180000000.0,
          "duration_in_ticks": 8400000.0,
          "text": "That's a great start.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 60,
          "offset": "PT3M38.84S",
          "offset_in_ticks": 2188400000.0,
          "duration_in_ticks": 13200000.0,
          "text": "Kind of see what works for them.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 61,
          "offset": "PT3M40.8S",
          "offset_in_ticks": 2208000000.0,
          "duration_in_ticks": 89200000.0,
          "text": "And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step, your recovery.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 62,
          "offset": "PT3M49.72S",
          "offset_in_ticks": 2297200000.0,
          "duration_in_ticks": 46800000.0,
          "text": "And once you're done that part, then we can probably look at discharging the claim.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 63,
          "offset": "PT3M55.48S",
          "offset_in_ticks": 2354800000.0,
          "duration_in_ticks": 7200000.0,
          "text": "How does that sound?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 64,
          "offset": "PT3M56.2S",
          "offset_in_ticks": 2362000000.0,
          "duration_in_ticks": 33600000.0,
          "text": "Did you want to go check in with your teammate?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 65,
          "offset": "PT4M0.12S",
          "offset_in_ticks": 2401200000.0,
          "duration_in_ticks": 40800000.0,
          "text": "And then we can have a conversation about, let's say, next Thursday.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 66,
          "offset": "PT4M4.4S",
          "offset_in_ticks": 2444000000.0,
          "duration_in_ticks": 38800000.0,
          "text": "Maybe I'll call you around the same time and then we can look at some of those options together.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 67,
          "offset": "PT4M8.28S",
          "offset_in_ticks": 2482800000.0,
          "duration_in_ticks": 13600000.0,
          "text": "Yep, that sounds good.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 68,
          "offset": "PT4M9.64S",
          "offset_in_ticks": 2496400000.0,
          "duration_in_ticks": 73600000.0,
          "text": "Next Thursday works for me, so we can chat, then maybe we'll get some updates and some good news on repairing your oven as well.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 69,
          "offset": "PT4M17S",
          "offset_in_ticks": 2570000000.0,
          "duration_in_ticks": 53200000.0,
          "text": "So before I wrap up here though, since you've got me any other questions like anything else I can help you out with?",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 70,
          "offset": "PT4M23.8S",
          "offset_in_ticks": 2638000000.0,
          "duration_in_ticks": 15600000.0,
          "text": "No, I think that's it for now.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 71,
          "offset": "PT4M25.36S",
          "offset_in_ticks": 2653600000.0,
          "duration_in_ticks": 42000000.0,
          "text": "I'll talk to them and then I'll try to think of any questions before we speak next Thursday.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 72,
          "offset": "PT4M30.4S",
          "offset_in_ticks": 2704000000.0,
          "duration_in_ticks": 9200000.0,
          "text": "Absolutely Fantastic.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 73,
          "offset": "PT4M31.32S",
          "offset_in_ticks": 2713200000.0,
          "duration_in_ticks": 108400000.0,
          "text": "I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 74,
          "offset": "PT4M42.16S",
          "offset_in_ticks": 2821600000.0,
          "duration_in_ticks": 38000000.0,
          "text": "And I think we'll get you to that last step and we'll move forward together on that.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 75,
          "offset": "PT4M45.96S",
          "offset_in_ticks": 2859600000.0,
          "duration_in_ticks": 3200000.0,
          "text": "OK.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 76,
          "offset": "PT4M46.6S",
          "offset_in_ticks": 2866000000.0,
          "duration_in_ticks": 17600000.0,
          "text": "So we'll chat next week then.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 77,
          "offset": "PT4M48.68S",
          "offset_in_ticks": 2886800000.0,
          "duration_in_ticks": 2400000.0,
          "text": "OK.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 78,
          "offset": "PT4M49.72S",
          "offset_in_ticks": 2897200000.0,
          "duration_in_ticks": 5200000.0,
          "text": "Thank you.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 79,
          "offset": "PT4M50.64S",
          "offset_in_ticks": 2906400000.0,
          "duration_in_ticks": 5200000.0,
          "text": "Bye for now.",
          "role": "Customer",
          "participantId": 1
        }
      ]
    }
},
{
    "short": {
      "audioFile": "/call4.wav",
      "representativeName": "Eddie",
      "customerName": "Bobby",
      "date": "04/22/2024",
      "callLength": 5,
      "summary": "This is a call summary",
      "transcription": [
          {
              "speaker": "Eddie",
              "text": "Hey there, I'm calling from ICBC. My name is Eddie. Looking to speak with Bobby. Please."
          },
          {
              "speaker": "Eddie",
              "text": "Bobby speaking."
          },
          {
              "speaker": "Eddie",
              "text": "Hey there, Bobby, just calling for let's say 10 to 15 minutes just to give you a bit of an update. Is this a?"
          },
          {
              "speaker": "Eddie",
              "text": "Good time? Not sure."
          },
          {
              "speaker": "Eddie",
              "text": "Absolutely. Fantastic. Thank you so much. Yeah, we'll make sure we go over. My role, of course as, as you know, is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better. And part of that involves your treatment and."
          },
          {
              "speaker": "Eddie",
              "text": "Treatment plans that we receive. So we'll go over some of the decisions we've made and I want to make sure that you really understand that as."
          },
          {
              "speaker": "Bobby",
              "text": "Well, yeah. OK, sure."
          },
          {
              "speaker": "Eddie",
              "text": "Jump into that. Do you have any questions I can help you out with?"
          },
          {
              "speaker": "Bobby",
              "text": "No, not really."
          },
          {
              "speaker": "Eddie",
              "text": "No, anything about your mileage expenses or anything about your equipment that you've recently purchased. How's that been going?"
          },
          {
              "speaker": "Bobby",
              "text": "No, not really. What do you mean by equipment?"
          },
          {
              "speaker": "Eddie",
              "text": "I'm glad you asked. Some of the equipment that your physiotherapist recommended. Umm, do you remember about? I think there was the I'm just taking a look at my notes, I think there was the foam roller and the therapeans. How, how, how's that exercise been going?"
          },
          {
              "speaker": "Bobby",
              "text": "Oh, fine."
          },
          {
              "speaker": "Eddie",
              "text": "Anything else you'd like to share about working with that physiotherapist that we should know about though?"
          },
          {
              "speaker": "Bobby",
              "text": "No, it's been good. The, the equipment's working. It's good."
          },
          {
              "speaker": "Eddie",
              "text": "That's great to hear."
          },
          {
              "speaker": "Eddie",
              "text": "Thanks so much for sharing and and for yourself. How are you finding the progress? Are you getting back to where you were before the?"
          },
          {
              "speaker": "Bobby",
              "text": "Crash I I guess. I guess it's been OK, yeah."
          },
          {
              "speaker": "Eddie",
              "text": "How I guess can you share how close are you getting to that in terms of your recovery?"
          },
          {
              "speaker": "Bobby",
              "text": "I guess I'm doing fine. The physiotherapist seems to think it's going OK. So I good, I guess."
          },
          {
              "speaker": "Eddie",
              "text": "I think you're doing really, I think you're really doing really good. I mean, looking at the progress that you're making, I'm looking at the treatment plans, I'm looking at our consultation that we had with your physiotherapist. I think you're doing really great actually. So you might be selling yourself a little bit short here, but I think we're seeing some great progress."
          },
          {
              "speaker": "Eddie",
              "text": "Great. So just working with you on some of your other benefits as well. I just want to make sure I touch on your mileage."
          },
          {
              "speaker": "Eddie",
              "text": "How's the submission been? Like, have you had all your reimbursements received properly?"
          },
          {
              "speaker": "Eddie",
              "text": "Any time it works, whichever is convenient for you, we have technically up to 180 days from the date that you incur them, OK?"
          },
          {
              "speaker": "Bobby",
              "text": "I thought that's OK. Thanks. OK."
          },
          {
              "speaker": "Eddie",
              "text": "Great. Now before I go into the treatment plan in itself and I'll share a little bit about the details here."
          },
          {
              "speaker": "Eddie",
              "text": "Um, I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered and at this point you're ready for discharge from the physiotherapy services. So with this treatment plan, I think you do still have two more treatments left and you'll be able to finish those last two and go from there. How's that sound?"
          },
          {
              "speaker": "Bobby",
              "text": "That's good. That's good to know. Is there anything else that you need from me? Anything else I need to do?"
          },
          {
              "speaker": "Eddie",
              "text": "At this point, I think it really comes down to for yourself, like anything that you feel like you need before you so that you can get back to where you were before the."
          },
          {
              "speaker": "Bobby",
              "text": "Crash. I guess I'm OK. I."
          },
          {
              "speaker": "Eddie",
              "text": "Mine is also good, So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions."
          },
          {
              "speaker": "Eddie",
              "text": "I just want to really encourage you to give me a call, e-mail me. I'll be available for you on Monday to Friday and 8:00 to 4:00. So as you know, just give me a shout and then I'm happy to walk through those options with you if they have any further."
          },
          {
              "speaker": "Eddie",
              "text": "Not a problem, Not a problem. And what I'll do is I will send you an e-mail. I'll actually summarize what we talked about today for you."
          },
          {
              "speaker": "Eddie",
              "text": "And really just celebrate what a great job you've done in your recovery. And then also, I'll be checking in with you in two weeks. Would you prefer that I e-mail you? Would you prefer that I call you or you just give me a call when you're ready? What's?"
          },
          {
              "speaker": "Eddie",
              "text": "Easier for you."
          },
          {
              "speaker": "Bobby",
              "text": "Anything works for me, really. It's it's fine whichever when you want to do sure."
          },
          {
              "speaker": "Eddie",
              "text": "To close the file in three weeks and if I don't hear back from you."
          },
          {
              "speaker": "Eddie",
              "text": "Then we'll close it. But if you do have anything that comes up in the meantime, then just give me a call how?"
          },
          {
              "speaker": "Bobby",
              "text": "About that, yeah, that sounds good. Thanks."
          },
          {
              "speaker": "Eddie",
              "text": "Okay. Absolutely fantastic. It's always a pleasure talking to you. I really enjoy sharing this update with you, working with you on this, so anything else just give me."
          },
          {
              "speaker": "Bobby",
              "text": "A call. OK. Thanks, Eddie."
          },
          {
              "speaker": "Eddie",
              "text": "Great. Thank you."
          }
      ],
      "flags": []
  },
    "long": {
      "durationInTicks": 3374700000,
      "conversations": [
        {
          "id": 0,
          "offset": "PT3.24S",
          "offset_in_ticks": 32400000.0,
          "duration_in_ticks": 2000000.0,
          "text": "Hey there.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 1,
          "offset": "PT3.44S",
          "offset_in_ticks": 34400000.0,
          "duration_in_ticks": 10800000.0,
          "text": "I'm calling from ICBC.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 2,
          "offset": "PT4.52S",
          "offset_in_ticks": 45200000.0,
          "duration_in_ticks": 11200000.0,
          "text": "My name is Eddie.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 3,
          "offset": "PT5.64S",
          "offset_in_ticks": 56400000.0,
          "duration_in_ticks": 34800000.0,
          "text": "Looking to speak with Bobby, please, Bobby speaking.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 4,
          "offset": "PT10.08S",
          "offset_in_ticks": 100800000.0,
          "duration_in_ticks": 8000000.0,
          "text": "Hey there, Bobby.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 5,
          "offset": "PT11.04S",
          "offset_in_ticks": 110400000.0,
          "duration_in_ticks": 51600000.0,
          "text": "Just calling for, let's say, 10 to 15 minutes just to give you a bit of an update.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 6,
          "offset": "PT16.2S",
          "offset_in_ticks": 162000000.0,
          "duration_in_ticks": 10400000.0,
          "text": "Is this a good time?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 7,
          "offset": "PT18.2S",
          "offset_in_ticks": 182000000.0,
          "duration_in_ticks": 1200000.0,
          "text": "Sure.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 8,
          "offset": "PT19.12S",
          "offset_in_ticks": 191200000.0,
          "duration_in_ticks": 4400000.0,
          "text": "Absolutely.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 9,
          "offset": "PT19.56S",
          "offset_in_ticks": 195600000.0,
          "duration_in_ticks": 6400000.0,
          "text": "Fantastic.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 10,
          "offset": "PT20.2S",
          "offset_in_ticks": 202000000.0,
          "duration_in_ticks": 8800000.0,
          "text": "Thank you so much.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 11,
          "offset": "PT21.72S",
          "offset_in_ticks": 217200000.0,
          "duration_in_ticks": 24000000.0,
          "text": "Yeah, we'll make sure we go over.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 12,
          "offset": "PT24.84S",
          "offset_in_ticks": 248400000.0,
          "duration_in_ticks": 98000000.0,
          "text": "My role, of course, is, as you know, is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 13,
          "offset": "PT34.64S",
          "offset_in_ticks": 346400000.0,
          "duration_in_ticks": 52800000.0,
          "text": "And part of that involves your treatment and the treatment plans that we receive.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 14,
          "offset": "PT41.04S",
          "offset_in_ticks": 410400000.0,
          "duration_in_ticks": 74400000.0,
          "text": "So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 15,
          "offset": "PT49.48S",
          "offset_in_ticks": 494800000.0,
          "duration_in_ticks": 26400000.0,
          "text": "Yeah, OK, sure, jump into that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 16,
          "offset": "PT52.12S",
          "offset_in_ticks": 521200000.0,
          "duration_in_ticks": 22400000.0,
          "text": "Do you have any questions I can help you out with?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 17,
          "offset": "PT55.48S",
          "offset_in_ticks": 554800000.0,
          "duration_in_ticks": 7200000.0,
          "text": "No, not really.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 18,
          "offset": "PT56.64S",
          "offset_in_ticks": 566400000.0,
          "duration_in_ticks": 3600000.0,
          "text": "Nope.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 19,
          "offset": "PT57.36S",
          "offset_in_ticks": 573600000.0,
          "duration_in_ticks": 79200000.0,
          "text": "Anything about your mileage, expenses, or anything about your equipment that you've recently purchased.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 20,
          "offset": "PT1M5.28S",
          "offset_in_ticks": 652800000.0,
          "duration_in_ticks": 8800000.0,
          "text": "How's that been going?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 21,
          "offset": "PT1M7.8S",
          "offset_in_ticks": 678000000.0,
          "duration_in_ticks": 11200000.0,
          "text": "No, not really.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 22,
          "offset": "PT1M9.44S",
          "offset_in_ticks": 694400000.0,
          "duration_in_ticks": 11600000.0,
          "text": "What do you mean by equipment?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 23,
          "offset": "PT1M11.84S",
          "offset_in_ticks": 718400000.0,
          "duration_in_ticks": 9600000.0,
          "text": "I'm glad you asked.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 24,
          "offset": "PT1M13.36S",
          "offset_in_ticks": 733600000.0,
          "duration_in_ticks": 82800000.0,
          "text": "Some of the equipment that your physiotherapist recommended, do you remember about, I think there was the, I'm just taking a look at my notes.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 25,
          "offset": "PT1M21.64S",
          "offset_in_ticks": 816400000.0,
          "duration_in_ticks": 52000000.0,
          "text": "I think there was the foam roller and the therapans.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 26,
          "offset": "PT1M26.84S",
          "offset_in_ticks": 868400000.0,
          "duration_in_ticks": 19200000.0,
          "text": "How, how, how's that exercise been going?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 27,
          "offset": "PT1M30.32S",
          "offset_in_ticks": 903200000.0,
          "duration_in_ticks": 6400000.0,
          "text": "Oh, fine.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 28,
          "offset": "PT1M32.96S",
          "offset_in_ticks": 929600000.0,
          "duration_in_ticks": 47200000.0,
          "text": "Anything else you'd like to share about working with that physiotherapist that we should know about though?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 29,
          "offset": "PT1M38.24S",
          "offset_in_ticks": 982400000.0,
          "duration_in_ticks": 8000000.0,
          "text": "No, it's been good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 30,
          "offset": "PT1M39.12S",
          "offset_in_ticks": 991200000.0,
          "duration_in_ticks": 18000000.0,
          "text": "The the equipment's working.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 31,
          "offset": "PT1M40.88S",
          "offset_in_ticks": 1008800000.0,
          "duration_in_ticks": 4000000.0,
          "text": "It's good.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 32,
          "offset": "PT1M42.6S",
          "offset_in_ticks": 1026000000.0,
          "duration_in_ticks": 7200000.0,
          "text": "That's great to hear.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 33,
          "offset": "PT1M43.92S",
          "offset_in_ticks": 1039200000.0,
          "duration_in_ticks": 25600000.0,
          "text": "Thanks so much for sharing and and for yourself.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 34,
          "offset": "PT1M46.48S",
          "offset_in_ticks": 1064800000.0,
          "duration_in_ticks": 18000000.0,
          "text": "How are you finding the progress?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 35,
          "offset": "PT1M48.28S",
          "offset_in_ticks": 1082800000.0,
          "duration_in_ticks": 31600000.0,
          "text": "Are you getting back to where you were before the crash?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 36,
          "offset": "PT1M51.88S",
          "offset_in_ticks": 1118800000.0,
          "duration_in_ticks": 7600000.0,
          "text": "I I guess.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 37,
          "offset": "PT1M52.64S",
          "offset_in_ticks": 1126400000.0,
          "duration_in_ticks": 9200000.0,
          "text": "I guess it's been OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 38,
          "offset": "PT1M53.68S",
          "offset_in_ticks": 1136800000.0,
          "duration_in_ticks": 3200000.0,
          "text": "Yeah.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 39,
          "offset": "PT1M55.64S",
          "offset_in_ticks": 1156400000.0,
          "duration_in_ticks": 64400000.0,
          "text": "How I guess can you share how close are you getting to that in terms of your recovery?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 40,
          "offset": "PT2M3.2S",
          "offset_in_ticks": 1232000000.0,
          "duration_in_ticks": 18400000.0,
          "text": "I guess I'm doing fine.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 41,
          "offset": "PT2M5.24S",
          "offset_in_ticks": 1252400000.0,
          "duration_in_ticks": 26000000.0,
          "text": "The physiotherapist seems to think it's going OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 42,
          "offset": "PT2M7.84S",
          "offset_in_ticks": 1278400000.0,
          "duration_in_ticks": 14000000.0,
          "text": "So I good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 43,
          "offset": "PT2M9.24S",
          "offset_in_ticks": 1292400000.0,
          "duration_in_ticks": 51200000.0,
          "text": "I guess I think you're doing really, I think you're really doing really good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 44,
          "offset": "PT2M14.36S",
          "offset_in_ticks": 1343600000.0,
          "duration_in_ticks": 88000000.0,
          "text": "I mean looking at the progress that you're making, I'm looking at the treatment plans, I'm looking at our consultation that we had with your physiotherapist.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 45,
          "offset": "PT2M23.16S",
          "offset_in_ticks": 1431600000.0,
          "duration_in_ticks": 16800000.0,
          "text": "I think you're doing really great actually.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 46,
          "offset": "PT2M24.84S",
          "offset_in_ticks": 1448400000.0,
          "duration_in_ticks": 60000000.0,
          "text": "So you might be selling yourself a little bit short here, but I think we're seeing some great progress.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 47,
          "offset": "PT2M31.52S",
          "offset_in_ticks": 1515200000.0,
          "duration_in_ticks": 10400000.0,
          "text": "Oh, OK, good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 48,
          "offset": "PT2M32.68S",
          "offset_in_ticks": 1526800000.0,
          "duration_in_ticks": 4800000.0,
          "text": "Good to know.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 49,
          "offset": "PT2M33.4S",
          "offset_in_ticks": 1534000000.0,
          "duration_in_ticks": 2800000.0,
          "text": "Thanks.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 50,
          "offset": "PT2M35.16S",
          "offset_in_ticks": 1551600000.0,
          "duration_in_ticks": 4800000.0,
          "text": "Great.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 51,
          "offset": "PT2M35.84S",
          "offset_in_ticks": 1558400000.0,
          "duration_in_ticks": 32400000.0,
          "text": "So just working with you on some of your other benefits as well.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 52,
          "offset": "PT2M39.08S",
          "offset_in_ticks": 1590800000.0,
          "duration_in_ticks": 31600000.0,
          "text": "I just want to make sure I touch on your mileage.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 53,
          "offset": "PT2M43.4S",
          "offset_in_ticks": 1634000000.0,
          "duration_in_ticks": 22000000.0,
          "text": "How's the submission been?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 54,
          "offset": "PT2M45.6S",
          "offset_in_ticks": 1656000000.0,
          "duration_in_ticks": 29200000.0,
          "text": "Like have you had all your reimbursements received properly?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 55,
          "offset": "PT2M49.76S",
          "offset_in_ticks": 1697600000.0,
          "duration_in_ticks": 74400000.0,
          "text": "I think so when do I have to have them in by anytime works, whichever is convenient for you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 56,
          "offset": "PT2M57.2S",
          "offset_in_ticks": 1772000000.0,
          "duration_in_ticks": 50400000.0,
          "text": "We have technically up to 180 days from the date that you incur them.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 57,
          "offset": "PT3M2.24S",
          "offset_in_ticks": 1822400000.0,
          "duration_in_ticks": 17200000.0,
          "text": "OK, fine.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 58,
          "offset": "PT3M4S",
          "offset_in_ticks": 1840000000.0,
          "duration_in_ticks": 6400000.0,
          "text": "That, that's OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 59,
          "offset": "PT3M4.64S",
          "offset_in_ticks": 1846400000.0,
          "duration_in_ticks": 3600000.0,
          "text": "Thanks.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 60,
          "offset": "PT3M5S",
          "offset_in_ticks": 1850000000.0,
          "duration_in_ticks": 14400000.0,
          "text": "OK, great.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 61,
          "offset": "PT3M7.96S",
          "offset_in_ticks": 1879600000.0,
          "duration_in_ticks": 165200000.0,
          "text": "Now before I go into the treatment plan in itself, and I'll share a little bit about the details here, I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 62,
          "offset": "PT3M24.68S",
          "offset_in_ticks": 2046800000.0,
          "duration_in_ticks": 55600000.0,
          "text": "And at this point, you're ready for discharge from the physiotherapy services.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 63,
          "offset": "PT3M30.52S",
          "offset_in_ticks": 2105200000.0,
          "duration_in_ticks": 84000000.0,
          "text": "So with this treatment plan, I think you do have two more treatments left and you'll be able to finish those last two and go from there.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 64,
          "offset": "PT3M38.92S",
          "offset_in_ticks": 2189200000.0,
          "duration_in_ticks": 6800000.0,
          "text": "How's that sound?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 65,
          "offset": "PT3M40.44S",
          "offset_in_ticks": 2204400000.0,
          "duration_in_ticks": 5600000.0,
          "text": "That's good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 66,
          "offset": "PT3M41S",
          "offset_in_ticks": 2210000000.0,
          "duration_in_ticks": 8400000.0,
          "text": "That's good to know.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 67,
          "offset": "PT3M42.36S",
          "offset_in_ticks": 2223600000.0,
          "duration_in_ticks": 59600000.0,
          "text": "Is there anything I else that you need from me, Anything else I need to do at this point?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 68,
          "offset": "PT3M48.32S",
          "offset_in_ticks": 2283200000.0,
          "duration_in_ticks": 70000000.0,
          "text": "I think it really comes down to for yourself, like anything that you feel like you need before you so that you can get back to where you were before the crash.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 69,
          "offset": "PT3M56.24S",
          "offset_in_ticks": 2362400000.0,
          "duration_in_ticks": 8000000.0,
          "text": "I guess I'm OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 70,
          "offset": "PT3M57.04S",
          "offset_in_ticks": 2370400000.0,
          "duration_in_ticks": 16800000.0,
          "text": "I think it's going fine.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 71,
          "offset": "PT4M1.12S",
          "offset_in_ticks": 2411200000.0,
          "duration_in_ticks": 8800000.0,
          "text": "Mine is also good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 72,
          "offset": "PT4M2.16S",
          "offset_in_ticks": 2421600000.0,
          "duration_in_ticks": 133600000.0,
          "text": "So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions, I just want to really encourage you to give me a call, e-mail me.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 73,
          "offset": "PT4M16.12S",
          "offset_in_ticks": 2561200000.0,
          "duration_in_ticks": 39200000.0,
          "text": "I'll be available for you on Monday to Friday and 8:00 to 4:00.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 74,
          "offset": "PT4M20.24S",
          "offset_in_ticks": 2602400000.0,
          "duration_in_ticks": 64400000.0,
          "text": "So as you know, just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 75,
          "offset": "PT4M27.12S",
          "offset_in_ticks": 2671200000.0,
          "duration_in_ticks": 5200000.0,
          "text": "Sounds good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 76,
          "offset": "PT4M28.16S",
          "offset_in_ticks": 2681600000.0,
          "duration_in_ticks": 14400000.0,
          "text": "I think I've lost your e-mail address.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 77,
          "offset": "PT4M29.6S",
          "offset_in_ticks": 2696000000.0,
          "duration_in_ticks": 21200000.0,
          "text": "Can you e-mail that to me again?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 78,
          "offset": "PT4M31.72S",
          "offset_in_ticks": 2717200000.0,
          "duration_in_ticks": 38400000.0,
          "text": "Yeah, not a problem, not a problem.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 79,
          "offset": "PT4M35.56S",
          "offset_in_ticks": 2755600000.0,
          "duration_in_ticks": 36800000.0,
          "text": "And what I'll do is I will send you an e-mail.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 80,
          "offset": "PT4M39.24S",
          "offset_in_ticks": 2792400000.0,
          "duration_in_ticks": 64400000.0,
          "text": "I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 81,
          "offset": "PT4M45.92S",
          "offset_in_ticks": 2859200000.0,
          "duration_in_ticks": 44400000.0,
          "text": "And then also, I'll be checking in with you in two weeks.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 82,
          "offset": "PT4M50.76S",
          "offset_in_ticks": 2907600000.0,
          "duration_in_ticks": 21200000.0,
          "text": "Would you prefer that I e-mail you?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 83,
          "offset": "PT4M52.88S",
          "offset_in_ticks": 2928800000.0,
          "duration_in_ticks": 38400000.0,
          "text": "Would you prefer that I call you or you just give me a call when you're ready?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 84,
          "offset": "PT4M56.72S",
          "offset_in_ticks": 2967200000.0,
          "duration_in_ticks": 9600000.0,
          "text": "What's easier for you?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 85,
          "offset": "PT4M58.88S",
          "offset_in_ticks": 2988800000.0,
          "duration_in_ticks": 12800000.0,
          "text": "Anything works for me, really.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 86,
          "offset": "PT5M0.16S",
          "offset_in_ticks": 3001600000.0,
          "duration_in_ticks": 6400000.0,
          "text": "It's it's fine.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 87,
          "offset": "PT5M0.8S",
          "offset_in_ticks": 3008000000.0,
          "duration_in_ticks": 28800000.0,
          "text": "Whichever one you want to do, sure.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 88,
          "offset": "PT5M3.68S",
          "offset_in_ticks": 3036800000.0,
          "duration_in_ticks": 21600000.0,
          "text": "If that's the case then why don't we do this?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 89,
          "offset": "PT5M6.72S",
          "offset_in_ticks": 3067200000.0,
          "duration_in_ticks": 97600000.0,
          "text": "I'll just mark this file to to close the file in three weeks and if I don't hear back from you, then we'll close it.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 90,
          "offset": "PT5M16.48S",
          "offset_in_ticks": 3164800000.0,
          "duration_in_ticks": 36400000.0,
          "text": "But if you do have anything that comes up in the meantime, then just give me a call.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 91,
          "offset": "PT5M20.16S",
          "offset_in_ticks": 3201600000.0,
          "duration_in_ticks": 6400000.0,
          "text": "How about that?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 92,
          "offset": "PT5M21.36S",
          "offset_in_ticks": 3213600000.0,
          "duration_in_ticks": 2400000.0,
          "text": "Yeah.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 93,
          "offset": "PT5M21.6S",
          "offset_in_ticks": 3216000000.0,
          "duration_in_ticks": 11600000.0,
          "text": "And that that sounds good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 94,
          "offset": "PT5M22.8S",
          "offset_in_ticks": 3228000000.0,
          "duration_in_ticks": 4400000.0,
          "text": "Thanks.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 95,
          "offset": "PT5M23.96S",
          "offset_in_ticks": 3239600000.0,
          "duration_in_ticks": 3200000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 96,
          "offset": "PT5M24.32S",
          "offset_in_ticks": 3243200000.0,
          "duration_in_ticks": 9600000.0,
          "text": "Absolutely fantastic.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 97,
          "offset": "PT5M25.28S",
          "offset_in_ticks": 3252800000.0,
          "duration_in_ticks": 21600000.0,
          "text": "It's always a pleasure talking to you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 98,
          "offset": "PT5M27.44S",
          "offset_in_ticks": 3274400000.0,
          "duration_in_ticks": 34000000.0,
          "text": "Really enjoy sharing this update with you and working with you on this.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 99,
          "offset": "PT5M30.84S",
          "offset_in_ticks": 3308400000.0,
          "duration_in_ticks": 21200000.0,
          "text": "So anything else, just give me a call.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 100,
          "offset": "PT5M33.28S",
          "offset_in_ticks": 3332800000.0,
          "duration_in_ticks": 1600000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 101,
          "offset": "PT5M33.48S",
          "offset_in_ticks": 3334800000.0,
          "duration_in_ticks": 6000000.0,
          "text": "Thanks, Eddie.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 102,
          "offset": "PT5M34.52S",
          "offset_in_ticks": 3345200000.0,
          "duration_in_ticks": 2000000.0,
          "text": "Great.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 103,
          "offset": "PT5M34.8S",
          "offset_in_ticks": 3348000000.0,
          "duration_in_ticks": 4000000.0,
          "text": "Thank you.",
          "role": "Agent",
          "participantId": 0
        }
      ]
    }
},
{
    "short": {
      "audioFile": "/PositiveSpecialistNegativeCustomer.wav",
      "representativeName": "Bobby",
      "customerName": "Emily",
      "date": "04/20/2024",
      "callLength": 4,
      "summary": "This is a call summary",
      "transcription": [
          {
              "speaker": "Bobby",
              "text": "Hi, may I speak to Emily, please?"
          },
          {
              "speaker": "Bobby",
              "text": "Yep, this is Emily."
          },
          {
              "speaker": "Bobby",
              "text": "I'm OK. I'm kind of busy. What do you?"
          },
          {
              "speaker": "Bobby",
              "text": "Need. Oh, I'm sorry to hear that. Is there a better time to reach her? Do you have a?"
          },
          {
              "speaker": "Bobby",
              "text": "OK. And how are things going with you right now?"
          },
          {
              "speaker": "Emily",
              "text": "Not good. Like every morning I wake up, I'm in so much pain. I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything."
          },
          {
              "speaker": "Emily",
              "text": "Like, I need treatment. My doctor agrees I need treatment too. What's going on?"
          },
          {
              "speaker": "Emily",
              "text": "I don't know. It feels like a really long time, like at least eight weeks or so."
          },
          {
              "speaker": "Bobby",
              "text": "OK. Yeah, that that shouldn't happen. And let's look into that right now so we can sort things out for you if you have a few minutes. I'm just going to ask you from the last couple of physios that you did, how you felt things were going."
          },
          {
              "speaker": "Bobby",
              "text": "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can."
          },
          {
              "speaker": "Emily",
              "text": "Do Honestly, it's been like a year and a half and I don't feel like I've made any progress at all. Like, I, you know, it's so disruptive to my life. I go to treatment three times a week now. I've been paying for it out of pocket the last two months and I'm not feeling any better."
          },
          {
              "speaker": "Bobby",
              "text": "OK. I'm, I'm sorry again to hear about the you're paying out of pocket."
          },
          {
              "speaker": "Bobby",
              "text": "That technically, we that shouldn't be happening. So let's take care of that for you. I'll get that information from you."
          },
          {
              "speaker": "Bobby",
              "text": "In a second, but also I'm a little concerned for you about your treatment and that you haven't been able to go."
          },
          {
              "speaker": "Bobby",
              "text": "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist. I'm just wondering why?"
          },
          {
              "speaker": "Bobby",
              "text": "You were thinking you weren't able to go serve a reason, Yeah."
          },
          {
              "speaker": "Emily",
              "text": "They told me that the treatment was cut off by ACDC and I had to pay. Sorry, who? Who told you that? The physiotherapist."
          },
          {
              "speaker": "Bobby",
              "text": "I'm really sorry to hear that. OK, we can clear that up with them. But there there are some sessions left. But you know what? I don't want you to have to worry about this. You leave that with me."
          },
          {
              "speaker": "Bobby",
              "text": "I will contact your physiotherapist and follow up with you. I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery. Is there anything else that's going on right now that I?"
          },
          {
              "speaker": "Emily",
              "text": "Can help with, yeah, I mean, you know, whatever. If my treatment is going to be cut off, like you know, that's annoying. It's unfair because I still need treatment. But I guess, you know, we can also just settle the claim up and and I can have my compensation now."
          },
          {
              "speaker": "Emily",
              "text": "What? What's your offer today?"
          },
          {
              "speaker": "Bobby",
              "text": "You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you were clear that we actually don't do that. ICBC doesn't supply compensation for your claim since we started with enhanced care, We talked about this in the beginning reclaim. So I wanted to make sure that you understand and please ask me any questions about it. But overall, what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment you mentioned that you've been going to physio for about a year and a half. So that's part of the benefits that you get with your claim."
          },
          {
              "speaker": "Bobby",
              "text": "And I know that we followed up with your doctor as well to check on your recovery and how you're doing. Those are are the things that we want to do to support you. There isn't any compensation amount."
          },
          {
              "speaker": "Emily",
              "text": "What? There's no more compensation, so I've been struggling with this injury. I have been wasting all my time going to treatment and I'm not even going to get any money for."
          },
          {
              "speaker": "Bobby",
              "text": "It we we don't have compensation anymore, Emily. That is correct."
          },
          {
              "speaker": "Emily",
              "text": "OK, whatever. Bye."
          }
      ],
      "flags": [
          {
              "speaker": "Bobby",
              "text": "Need. Oh, I'm sorry to hear that. Is there a better time to reach her? Do you have a?",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.02,
                  "negative": 0.93,
                  "neutral": 0.05
              }
          },
          {
              "speaker": "Emily",
              "text": "Not good. Like every morning I wake up, I'm in so much pain. I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.0,
                  "negative": 0.98,
                  "neutral": 0.02
              }
          },
          {
              "speaker": "Emily",
              "text": "Not good. Like every morning I wake up, I'm in so much pain. I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.0,
                  "negative": 0.97,
                  "neutral": 0.03
              }
          },
          {
              "speaker": "Emily",
              "text": "Do Honestly, it's been like a year and a half and I don't feel like I've made any progress at all. Like, I, you know, it's so disruptive to my life. I go to treatment three times a week now. I've been paying for it out of pocket the last two months and I'm not feeling any better.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.01,
                  "negative": 0.94,
                  "neutral": 0.06
              }
          },
          {
              "speaker": "Bobby",
              "text": "OK. I'm, I'm sorry again to hear about the you're paying out of pocket.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.04,
                  "negative": 0.85,
                  "neutral": 0.12
              }
          },
          {
              "speaker": "Bobby",
              "text": "I'm really sorry to hear that. OK, we can clear that up with them. But there there are some sessions left. But you know what? I don't want you to have to worry about this. You leave that with me.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.02,
                  "negative": 0.94,
                  "neutral": 0.04
              }
          },
          {
              "speaker": "Emily",
              "text": "Can help with, yeah, I mean, you know, whatever. If my treatment is going to be cut off, like you know, that's annoying. It's unfair because I still need treatment. But I guess, you know, we can also just settle the claim up and and I can have my compensation now.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.0,
                  "negative": 0.98,
                  "neutral": 0.02
              }
          },
          {
              "speaker": "Emily",
              "text": "Can help with, yeah, I mean, you know, whatever. If my treatment is going to be cut off, like you know, that's annoying. It's unfair because I still need treatment. But I guess, you know, we can also just settle the claim up and and I can have my compensation now.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.01,
                  "negative": 0.91,
                  "neutral": 0.09
              }
          },
          {
              "speaker": "Emily",
              "text": "What? There's no more compensation, so I've been struggling with this injury. I have been wasting all my time going to treatment and I'm not even going to get any money for.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.0,
                  "negative": 0.98,
                  "neutral": 0.02
              }
          },
          {
              "speaker": "Emily",
              "text": "What? There's no more compensation, so I've been struggling with this injury. I have been wasting all my time going to treatment and I'm not even going to get any money for.",
              "sentiment": "negative",
              "confidenceScores": {
                  "positive": 0.0,
                  "negative": 0.96,
                  "neutral": 0.03
              }
          }
      ]
  },
    "long": {
      "durationInTicks": 2427300000,
      "conversations": [
        {
          "id": 0,
          "offset": "PT2.88S",
          "offset_in_ticks": 28800000.0,
          "duration_in_ticks": 2800000.0,
          "text": "Hi.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 1,
          "offset": "PT3.16S",
          "offset_in_ticks": 31600000.0,
          "duration_in_ticks": 13600000.0,
          "text": "May I speak to Emily, please?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 2,
          "offset": "PT4.68S",
          "offset_in_ticks": 46800000.0,
          "duration_in_ticks": 11600000.0,
          "text": "Yep, this is Emily.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 3,
          "offset": "PT6.24S",
          "offset_in_ticks": 62400000.0,
          "duration_in_ticks": 7200000.0,
          "text": "Hi, Emily.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 4,
          "offset": "PT6.96S",
          "offset_in_ticks": 69600000.0,
          "duration_in_ticks": 17200000.0,
          "text": "This is Bobby calling from ICBC.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 5,
          "offset": "PT8.68S",
          "offset_in_ticks": 86800000.0,
          "duration_in_ticks": 7600000.0,
          "text": "How are you doing?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 6,
          "offset": "PT10.92S",
          "offset_in_ticks": 109200000.0,
          "duration_in_ticks": 4400000.0,
          "text": "I'm OK.",
          "role": "Customer",
          "participantId": 1
        },
        {
          "id": 7,
          "offset": "PT11.36S",
          "offset_in_ticks": 113600000.0,
          "duration_in_ticks": 8400000.0,
          "text": "I'm kind of busy.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 8,
          "offset": "PT12.24S",
          "offset_in_ticks": 122400000.0,
          "duration_in_ticks": 6400000.0,
          "text": "What do you need?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 9,
          "offset": "PT13.64S",
          "offset_in_ticks": 136400000.0,
          "duration_in_ticks": 12800000.0,
          "text": "Oh, I'm sorry to hear that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 10,
          "offset": "PT14.92S",
          "offset_in_ticks": 149200000.0,
          "duration_in_ticks": 12000000.0,
          "text": "Is there a better time to reach her?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 11,
          "offset": "PT16.12S",
          "offset_in_ticks": 161200000.0,
          "duration_in_ticks": 20400000.0,
          "text": "Do you have a few minutes now to talk about your claim?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 12,
          "offset": "PT18.2S",
          "offset_in_ticks": 182000000.0,
          "duration_in_ticks": 24400000.0,
          "text": "Yeah, I guess we can talk now if we have to.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 13,
          "offset": "PT21.96S",
          "offset_in_ticks": 219600000.0,
          "duration_in_ticks": 5600000.0,
          "text": "OK.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 14,
          "offset": "PT22.52S",
          "offset_in_ticks": 225200000.0,
          "duration_in_ticks": 20800000.0,
          "text": "And how are things going with you right now?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 15,
          "offset": "PT24.8S",
          "offset_in_ticks": 248000000.0,
          "duration_in_ticks": 8000000.0,
          "text": "Not good.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 16,
          "offset": "PT25.6S",
          "offset_in_ticks": 256000000.0,
          "duration_in_ticks": 31200000.0,
          "text": "Like every morning I wake up, I'm in so much pain.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 17,
          "offset": "PT29.08S",
          "offset_in_ticks": 290800000.0,
          "duration_in_ticks": 71200000.0,
          "text": "I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 18,
          "offset": "PT36.2S",
          "offset_in_ticks": 362000000.0,
          "duration_in_ticks": 19600000.0,
          "text": "My doctor agrees I need treatment too.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 19,
          "offset": "PT38.16S",
          "offset_in_ticks": 381600000.0,
          "duration_in_ticks": 8400000.0,
          "text": "What's going on?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 20,
          "offset": "PT39.08S",
          "offset_in_ticks": 390800000.0,
          "duration_in_ticks": 20400000.0,
          "text": "I'm actually really sorry to hear that, Emily.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 21,
          "offset": "PT41.12S",
          "offset_in_ticks": 411200000.0,
          "duration_in_ticks": 32000000.0,
          "text": "I can understand that you'd be frustrated if you haven't heard back.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 22,
          "offset": "PT45.4S",
          "offset_in_ticks": 454000000.0,
          "duration_in_ticks": 35200000.0,
          "text": "Can I ask, when the last time was that you did hear an update?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 23,
          "offset": "PT50.6S",
          "offset_in_ticks": 506000000.0,
          "duration_in_ticks": 4400000.0,
          "text": "I don't know.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 24,
          "offset": "PT51.04S",
          "offset_in_ticks": 510400000.0,
          "duration_in_ticks": 32800000.0,
          "text": "It feels like a really long time, like at least eight weeks or so.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 25,
          "offset": "PT54.52S",
          "offset_in_ticks": 545200000.0,
          "duration_in_ticks": 19600000.0,
          "text": "OK, Yeah, that that shouldn't happen.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 26,
          "offset": "PT56.48S",
          "offset_in_ticks": 564800000.0,
          "duration_in_ticks": 46000000.0,
          "text": "And let's look into that right now so we can sort things out for you if you have a few minutes.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 27,
          "offset": "PT1M1.52S",
          "offset_in_ticks": 615200000.0,
          "duration_in_ticks": 64400000.0,
          "text": "I'm just going to ask you from the last couple of physios that you did, how you felt things were going.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 28,
          "offset": "PT1M7.96S",
          "offset_in_ticks": 679600000.0,
          "duration_in_ticks": 112400000.0,
          "text": "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can do.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 29,
          "offset": "PT1M19.68S",
          "offset_in_ticks": 796800000.0,
          "duration_in_ticks": 50400000.0,
          "text": "Honestly, it's been like a year and a half and I don't feel like I've made any progress at all.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 30,
          "offset": "PT1M25.28S",
          "offset_in_ticks": 852800000.0,
          "duration_in_ticks": 24800000.0,
          "text": "Like I, you know, it's so disruptive to my life.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 31,
          "offset": "PT1M27.76S",
          "offset_in_ticks": 877600000.0,
          "duration_in_ticks": 24400000.0,
          "text": "I go to treatment three times a week now.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 32,
          "offset": "PT1M30.2S",
          "offset_in_ticks": 902000000.0,
          "duration_in_ticks": 62800000.0,
          "text": "I've been paying for it out of pocket the last two months and I'm not feeling any better.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 33,
          "offset": "PT1M36.6S",
          "offset_in_ticks": 966000000.0,
          "duration_in_ticks": 9600000.0,
          "text": "OK, I'm.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 34,
          "offset": "PT1M37.84S",
          "offset_in_ticks": 978400000.0,
          "duration_in_ticks": 52800000.0,
          "text": "I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 35,
          "offset": "PT1M43.12S",
          "offset_in_ticks": 1031200000.0,
          "duration_in_ticks": 13600000.0,
          "text": "So let's take care of that for you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 36,
          "offset": "PT1M44.48S",
          "offset_in_ticks": 1044800000.0,
          "duration_in_ticks": 26800000.0,
          "text": "I'll get that information from you in a second.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 37,
          "offset": "PT1M47.16S",
          "offset_in_ticks": 1071600000.0,
          "duration_in_ticks": 53200000.0,
          "text": "But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 38,
          "offset": "PT1M53.6S",
          "offset_in_ticks": 1136000000.0,
          "duration_in_ticks": 73600000.0,
          "text": "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 39,
          "offset": "PT2M1.24S",
          "offset_in_ticks": 1212400000.0,
          "duration_in_ticks": 58400000.0,
          "text": "I'm just wondering why you were thinking you weren't able to go for a reason.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 40,
          "offset": "PT2M7.28S",
          "offset_in_ticks": 1272800000.0,
          "duration_in_ticks": 2800000.0,
          "text": "Yeah.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 41,
          "offset": "PT2M7.6S",
          "offset_in_ticks": 1276000000.0,
          "duration_in_ticks": 32800000.0,
          "text": "They told me that the treatment was cut off by ACDC and I had to pay.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 42,
          "offset": "PT2M11.32S",
          "offset_in_ticks": 1313200000.0,
          "duration_in_ticks": 3200000.0,
          "text": "Sorry.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 43,
          "offset": "PT2M11.64S",
          "offset_in_ticks": 1316400000.0,
          "duration_in_ticks": 2400000.0,
          "text": "Who?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 44,
          "offset": "PT2M11.96S",
          "offset_in_ticks": 1319600000.0,
          "duration_in_ticks": 8400000.0,
          "text": "Who told you that?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 45,
          "offset": "PT2M12.92S",
          "offset_in_ticks": 1329200000.0,
          "duration_in_ticks": 11600000.0,
          "text": "The physiotherapist.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 46,
          "offset": "PT2M14.4S",
          "offset_in_ticks": 1344000000.0,
          "duration_in_ticks": 13600000.0,
          "text": "I'm really sorry to hear that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 47,
          "offset": "PT2M15.76S",
          "offset_in_ticks": 1357600000.0,
          "duration_in_ticks": 15600000.0,
          "text": "OK, we can clear that up with them.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 48,
          "offset": "PT2M17.32S",
          "offset_in_ticks": 1373200000.0,
          "duration_in_ticks": 20400000.0,
          "text": "But there there are some sessions left.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 49,
          "offset": "PT2M20.24S",
          "offset_in_ticks": 1402400000.0,
          "duration_in_ticks": 7200000.0,
          "text": "But you know what?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 50,
          "offset": "PT2M20.96S",
          "offset_in_ticks": 1409600000.0,
          "duration_in_ticks": 22000000.0,
          "text": "I don't want you to have to worry about this.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 51,
          "offset": "PT2M23.16S",
          "offset_in_ticks": 1431600000.0,
          "duration_in_ticks": 10400000.0,
          "text": "You leave that with me.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 52,
          "offset": "PT2M24.48S",
          "offset_in_ticks": 1444800000.0,
          "duration_in_ticks": 35600000.0,
          "text": "I will contact your physiotherapist and follow up with you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 53,
          "offset": "PT2M28.08S",
          "offset_in_ticks": 1480800000.0,
          "duration_in_ticks": 74400000.0,
          "text": "I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 54,
          "offset": "PT2M35.92S",
          "offset_in_ticks": 1559200000.0,
          "duration_in_ticks": 29200000.0,
          "text": "Is there anything else that's going on right now that I can help with?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 55,
          "offset": "PT2M39S",
          "offset_in_ticks": 1590000000.0,
          "duration_in_ticks": 20000000.0,
          "text": "Yeah, I mean, you know, whatever.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 56,
          "offset": "PT2M41S",
          "offset_in_ticks": 1610000000.0,
          "duration_in_ticks": 47200000.0,
          "text": "If my treatment is going to be cut off, like, you know, that's annoying.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 57,
          "offset": "PT2M45.72S",
          "offset_in_ticks": 1657200000.0,
          "duration_in_ticks": 18400000.0,
          "text": "It's unfair because I still need treatment.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 58,
          "offset": "PT2M48.16S",
          "offset_in_ticks": 1681600000.0,
          "duration_in_ticks": 66800000.0,
          "text": "But I guess, you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today?",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 59,
          "offset": "PT2M56.52S",
          "offset_in_ticks": 1765200000.0,
          "duration_in_ticks": 78400000.0,
          "text": "You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you are clear that we actually don't do that.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 60,
          "offset": "PT3M4.36S",
          "offset_in_ticks": 1843600000.0,
          "duration_in_ticks": 71600000.0,
          "text": "ICBC doesn't supply compensation for your claim since we started with enhanced care.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 61,
          "offset": "PT3M12S",
          "offset_in_ticks": 1920000000.0,
          "duration_in_ticks": 16800000.0,
          "text": "We talked about this in the beginning of your claim.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 62,
          "offset": "PT3M13.68S",
          "offset_in_ticks": 1936800000.0,
          "duration_in_ticks": 38400000.0,
          "text": "So I wanted to make sure that you understand and please ask me any questions about it.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 63,
          "offset": "PT3M17.52S",
          "offset_in_ticks": 1975200000.0,
          "duration_in_ticks": 80000000.0,
          "text": "But overall what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 64,
          "offset": "PT3M25.8S",
          "offset_in_ticks": 2058000000.0,
          "duration_in_ticks": 22400000.0,
          "text": "You mentioned that you've been going to physio for about a year and a half.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 65,
          "offset": "PT3M28.04S",
          "offset_in_ticks": 2080400000.0,
          "duration_in_ticks": 30400000.0,
          "text": "So that's part of the benefits that you get with your claim.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 66,
          "offset": "PT3M31.4S",
          "offset_in_ticks": 2114000000.0,
          "duration_in_ticks": 54400000.0,
          "text": "And I know that we followed up with your doctor as well to check on your recovery and how you're doing.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 67,
          "offset": "PT3M37.16S",
          "offset_in_ticks": 2171600000.0,
          "duration_in_ticks": 22400000.0,
          "text": "Those are are the things that we want to do to support you.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 68,
          "offset": "PT3M39.4S",
          "offset_in_ticks": 2194000000.0,
          "duration_in_ticks": 20400000.0,
          "text": "There isn't any compensation amount.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 69,
          "offset": "PT3M41.52S",
          "offset_in_ticks": 2215200000.0,
          "duration_in_ticks": 28400000.0,
          "text": "What there's no more compensation.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 70,
          "offset": "PT3M44.8S",
          "offset_in_ticks": 2248000000.0,
          "duration_in_ticks": 32400000.0,
          "text": "So I've been struggling with this injury.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 71,
          "offset": "PT3M48.04S",
          "offset_in_ticks": 2280400000.0,
          "duration_in_ticks": 48400000.0,
          "text": "I have been wasting all my time going to treatment and I'm not even going to get any money for it.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 72,
          "offset": "PT3M53.76S",
          "offset_in_ticks": 2337600000.0,
          "duration_in_ticks": 18000000.0,
          "text": "We we don't have compensation anymore.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 73,
          "offset": "PT3M55.56S",
          "offset_in_ticks": 2355600000.0,
          "duration_in_ticks": 12400000.0,
          "text": "Emily, that is correct.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 74,
          "offset": "PT3M57.92S",
          "offset_in_ticks": 2379200000.0,
          "duration_in_ticks": 12000000.0,
          "text": "OK, whatever.",
          "role": "Agent",
          "participantId": 0
        },
        {
          "id": 75,
          "offset": "PT3M59.36S",
          "offset_in_ticks": 2393600000.0,
          "duration_in_ticks": 3200000.0,
          "text": "Bye.",
          "role": "Agent",
          "participantId": 0
        }
      ]
    }
}
        ]
    }

    # response = {
    #     "calls": [
    #         {
    #             "representativeName": "Adrian Smith",
    #     "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
    #     "customerName": "Bobby",
    #     "summary": "Call the customer to check status of treatment plan",
    #     "callLength": 15,
    #     "date": "04/21/2024",
    #     "flags": [
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 2
    #             },
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": True,
    #                 "timestamp": 4
    #             },
    #             {
    #                 "isCustomer": False,
    #                 "isRepresentative": True,
    #                 "timestamp": 10
    #             }
    #         ]
    #         },
    #         {
    #             "representativeName": "Emma Park",
    #     "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
    #     "customerName": "Jane Doe",
    #     "summary": "Call the customer to check about expenses",
    #     "callLength": 20,
    #     "date": "04/23/2024",
    #     "flags": [
    #         ]
    #         },
    #         {
    #             "representativeName": "Eddie Edwards",
    #     "transcription": '"Speaker0": Hi there. I\'m caller from ICBC. My name is Eddie. I\'m just here looking for Bobby, please. "Speaker1": Hi, Eddie, this is Bobby speaking.',
    #     "customerName": "Alex Black",
    #     "summary": "Call about claimstatus",
    #     "callLength": 27,
    #     "date": "04/12/2024",
    #     "flags": [
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 2
    #             },
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 4
    #             },
    #             {
    #                 "isCustomer": True,
    #                 "isRepresentative": False,
    #                 "timestamp": 10
    #             }
    #         ]
    #         }
    #     ]
        
    # }

    return func.HttpResponse(json.dumps(response, default=str),
                status_code=200                
            )
    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )