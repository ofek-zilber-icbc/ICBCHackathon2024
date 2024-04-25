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
        "summary": "The discussion revolves around a customer's treatment and injury claim, with emphasis on following recommendations for recovery. The representative sets a deadline for follow-up and stresses the importance of communication for treatment approval.",
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
      "transcription": {
        "source": "https://github.com/ofek-zilber-icbc/ICBCHackathon2024/raw/main/backend/azure_related/call2.wav",
        "timestamp": "2024-04-25T06:04:25Z",
        "durationInTicks": 2603600000,
        "duration": "PT4M20.36S",
        "combinedRecognizedPhrases": [
          {
            "channel": 0,
            "lexical": "hi this is bobby calling from I C B C S assembly hi this is emily yes oh hi emily i'm glad i got a hold of you it's been really hard to reach you i've been trying to call you for a while oh has it yeah it has but i guess you're really busy so i'm glad that i got a hold of you and i wanted to talk to you about your treatment and your injury claim OK what did you want to talk about specifically well i want to talk to you about how your treatment is going so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments i was hoping i could find a physiotherapist in the same clinic but i couldn't so i thought it was just easier to keep going to my massage therapist OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there yeah i can see that and we approved the last treatment request that your massage therapist sent in but to be honest with you i'm not going to prove the next one i did talk to you about talking to your physiotherapist and making that call so you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense i can do that you know what i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment well you mentioned that you're still having problems with your knee and you're fine now is that what you're saying yeah i mean it still hurts but i think you know it could be worse so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards so when we talked and i gave you the information i you are expected to follow it you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too if i don't get any more treatment well i really want you to reach out and call your physiotherapist and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week let's try to do that so that you're talking to them by then and i would like to get an update from you if i don't then i don't think i'll be able to approve any more of the massage either OK so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you really i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given oh OK well i'm really sorry i didn't mean to not follow the advice like i i typically do like to follow what you tell me i just must have forgot but yeah OK i can do what you told me and i'll i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there but if not i guess i just won't bother you anymore well i've noted that down your file and you've been given all the information so you know what needs to happen next again if i don't hear back from by next week then we won't be approving any more treatment OK OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week is there anything else that i should be doing no you have my number and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you so you know what time i work so please give me a call OK i'm really sorry about that thanks so much for calling me today OK bye",
            "itn": "hi this is bobby calling from ICBCS assembly hi this is emily yes oh hi emily i'm glad i got a hold of you it's been really hard to reach you i've been trying to call you for a while oh has it yeah it has but i guess you're really busy so i'm glad that i got a hold of you and i wanted to talk to you about your treatment and your injury claim OK what did you want to talk about specifically well i want to talk to you about how your treatment is going so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments i was hoping i could find a physiotherapist in the same clinic but i couldn't so i thought it was just easier to keep going to my massage therapist OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there yeah i can see that and we approved the last treatment request that your massage therapist sent in but to be honest with you i'm not going to prove the next one i did talk to you about talking to your physiotherapist and making that call so you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense i can do that you know what i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment well you mentioned that you're still having problems with your knee and you're fine now is that what you're saying yeah i mean it still hurts but i think you know it could be worse so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards so when we talked and i gave you the information i you are expected to follow it you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too if i don't get any more treatment well i really want you to reach out and call your physiotherapist and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week let's try to do that so that you're talking to them by then and i would like to get an update from you if i don't then i don't think i'll be able to approve any more of the massage either OK so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you really i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given oh OK well i'm really sorry i didn't mean to not follow the advice like i i typically do like to follow what you tell me i just must have forgot but yeah OK i can do what you told me and i'll i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there but if not i guess i just won't bother you anymore well i've noted that down your file and you've been given all the information so you know what needs to happen next again if i don't hear back from by next week then we won't be approving any more treatment OK OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week is there anything else that i should be doing no you have my number and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you so you know what time i work so please give me a call OK i'm really sorry about that thanks so much for calling me today OK bye",
            "maskedITN": "Hi this is Bobby calling from ICBCS Assembly Hi this is Emily Yes Oh hi Emily I'm glad I got a hold of you It's been really hard to reach you I've been trying to call you for a while Oh has it Yeah it has But I guess you're really busy So I'm glad that I got a hold of you And I wanted to talk to you about your treatment and your injury claim OK What did you want to talk about specifically Well I want to talk to you about how your treatment is going So I've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist I see that your doctor had recommended it too before and I want to follow up to see if you've been doing that or if you've talked to them Yeah it's been kind of easier just to go to my massage therapist 'cause I can get appointments I was hoping I could find a physiotherapist in the same clinic but I couldn't So I thought it was just easier to keep going to my massage therapist OK well I want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time Oh OK Well my massage therapist kept booking me in so I thought I was just good to keep going there Yeah I can see that And we approved the last treatment request that your massage therapist sent in But to be honest with you I'm not going to prove the next one I did talk to you about talking to your physiotherapist and making that call So you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense I can do that You know what I'm feeling pretty good anyways so I don't even know if I'm going to need any more treatment Well you mentioned that you're still having problems with your knee and you're fine now Is that what you're saying Yeah I mean it still hurts but I think you know it could be worse So well I like I told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards So when we talked and I gave you the information I you are expected to follow it You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well I guess I could always talk to my massage therapist and then yeah I could try calling around some physiotherapy clinics but if I don't it's OK too If I don't get any more treatment well I really want you to reach out and call your physiotherapist And since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week Let's try to do that so that you're talking to them by then And I would like to get an update from you If I don't then I don't think I'll be able to approve any more of the massage either OK So what happens if I need more treatment though or if I feel like I'm still in pain or I'm not able to do all of my regular stuff Well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back But if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you Really I think I've talked to you before and I put the notes in your file here that you're not following the advice that you were given Oh OK Well I'm really sorry I didn't mean to not follow the advice like I I typically do like to follow what you tell me I just must have forgot but yeah OK I can do what you told me and I'll I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there But if not I guess I just won't bother you anymore Well I've noted that down your file and you've been given all the information so you know what needs to happen next Again if I don't hear back from by next week then we won't be approving any more treatment OK OK well I'll try to follow up then with a physiotherapist and I'll try to get back to you next week Is there anything else that I should be doing No You have my number And like I mentioned I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you So you know what time I work So please give me a call OK I'm really sorry about that Thanks so much for calling me today OK Bye",
            "display": "Hi, this is Bobby calling from ICBCS Assembly. Hi, this is Emily. Yes. Oh, hi, Emily. I'm glad I got a hold of you. It's been really hard to reach you. I've been trying to call you for a while. Oh, has it? Yeah, it has. But I guess you're really busy. So I'm glad that I got a hold of you. And I wanted to talk to you about your treatment and your injury claim. OK. What did you want to talk about specifically? Well, I want to talk to you about how your treatment is going. So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist. I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them. Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments. I was hoping I could find a physiotherapist in the same clinic, but I couldn't. So I thought it was just easier to keep going to my massage therapist. OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time. Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there. Yeah, I can see that. And we approved the last treatment request that your massage therapist sent in. But to be honest with you, I'm not going to prove the next one. I did talk to you about talking to your physiotherapist and making that call. So you're going to need to do that if you want to keep having treatment provided under your claim. OK, that makes sense. I can do that. You know what? I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment. Well, you mentioned that you're still having problems with your knee and you're fine now. Is that what you're saying? Yeah. I mean, it still hurts, but I think, you know, it could be worse. So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards. So when we talked and I gave you the information, I you are expected to follow it. You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better. OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too. If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist. And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week. Let's try to do that so that you're talking to them by then. And I would like to get an update from you. If I don't, then I don't think I'll be able to approve any more of the massage either. OK. So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff? Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back. But if you're going to pause and stop treatment, it's gonna be really difficult for us to approve any more for you. Really. I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given. Oh, OK. Well, I'm really sorry. I didn't mean to not follow the advice like I I typically do like to follow what you tell me. I just must have forgot, but yeah, OK, I can do what you told me and I'll. I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there. But if not, I guess I just won't bother you anymore. Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next. Again, if I don't hear back from by next week, then we won't be approving any more treatment. OK. OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week. Is there anything else that I should be doing? No. You have my number. And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you. So you know what time I work. So please give me a call. OK. I'm really sorry about that. Thanks so much for calling me today. OK. Bye."
          },
          {
            "channel": 1,
            "lexical": "hi this is bobby calling from I C B C S assembly hi this is emily yes oh hi emily i'm glad i got a hold of you it's been really hard to reach you i've been trying to call you for a while oh has it yeah it has but i guess you're really busy so i'm glad that i got a hold of you and i wanted to talk to you about your treatment and your injury claim OK what did you want to talk about specifically well i want to talk to you about how your treatment is going so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments i was hoping i could find a physiotherapist in the same clinic but i couldn't so i thought it was just easier to keep going to my massage therapist OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there yeah i can see that and we approved the last treatment request that your massage therapist sent in but to be honest with you i'm not going to prove the next one i did talk to you about talking to your physiotherapist and making that call so you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense i can do that you know what i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment well you mentioned that you're still having problems with your knee and you're fine now is that what you're saying yeah i mean it still hurts but i think you know it could be worse so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards so when we talked and i gave you the information i you are expected to follow it you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too if i don't get any more treatment well i really want you to reach out and call your physiotherapist and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week let's try to do that so that you're talking to them by then and i would like to get an update from you if i don't then i don't think i'll be able to approve any more of the massage either OK so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you really i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given oh OK well i'm really sorry i didn't mean to not follow the advice like i i typically do like to follow what you tell me i just must have forgot but yeah OK i can do what you told me and i'll i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there but if not i guess i just won't bother you anymore well i've noted that down your file and you've been given all the information so you know what needs to happen next again if i don't hear back from by next week then we won't be approving any more treatment OK OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week is there anything else that i should be doing no you have my number and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you so you know what time i work so please give me a call OK i'm really sorry about that thanks so much for calling me today OK bye",
            "itn": "hi this is bobby calling from ICBCS assembly hi this is emily yes oh hi emily i'm glad i got a hold of you it's been really hard to reach you i've been trying to call you for a while oh has it yeah it has but i guess you're really busy so i'm glad that i got a hold of you and i wanted to talk to you about your treatment and your injury claim OK what did you want to talk about specifically well i want to talk to you about how your treatment is going so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments i was hoping i could find a physiotherapist in the same clinic but i couldn't so i thought it was just easier to keep going to my massage therapist OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there yeah i can see that and we approved the last treatment request that your massage therapist sent in but to be honest with you i'm not going to prove the next one i did talk to you about talking to your physiotherapist and making that call so you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense i can do that you know what i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment well you mentioned that you're still having problems with your knee and you're fine now is that what you're saying yeah i mean it still hurts but i think you know it could be worse so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards so when we talked and i gave you the information i you are expected to follow it you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too if i don't get any more treatment well i really want you to reach out and call your physiotherapist and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week let's try to do that so that you're talking to them by then and i would like to get an update from you if i don't then i don't think i'll be able to approve any more of the massage either OK so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you really i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given oh OK well i'm really sorry i didn't mean to not follow the advice like i i typically do like to follow what you tell me i just must have forgot but yeah OK i can do what you told me and i'll i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there but if not i guess i just won't bother you anymore well i've noted that down your file and you've been given all the information so you know what needs to happen next again if i don't hear back from by next week then we won't be approving any more treatment OK OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week is there anything else that i should be doing no you have my number and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you so you know what time i work so please give me a call OK i'm really sorry about that thanks so much for calling me today OK bye",
            "maskedITN": "Hi this is Bobby calling from ICBCS Assembly Hi this is Emily Yes Oh hi Emily I'm glad I got a hold of you It's been really hard to reach you I've been trying to call you for a while Oh has it Yeah it has But I guess you're really busy So I'm glad that I got a hold of you And I wanted to talk to you about your treatment and your injury claim OK What did you want to talk about specifically Well I want to talk to you about how your treatment is going So I've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist I see that your doctor had recommended it too before and I want to follow up to see if you've been doing that or if you've talked to them Yeah it's been kind of easier just to go to my massage therapist 'cause I can get appointments I was hoping I could find a physiotherapist in the same clinic but I couldn't So I thought it was just easier to keep going to my massage therapist OK well I want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time Oh OK Well my massage therapist kept booking me in so I thought I was just good to keep going there Yeah I can see that And we approved the last treatment request that your massage therapist sent in But to be honest with you I'm not going to prove the next one I did talk to you about talking to your physiotherapist and making that call So you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense I can do that You know what I'm feeling pretty good anyways so I don't even know if I'm going to need any more treatment Well you mentioned that you're still having problems with your knee and you're fine now Is that what you're saying Yeah I mean it still hurts but I think you know it could be worse So well I like I told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards So when we talked and I gave you the information I you are expected to follow it You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well I guess I could always talk to my massage therapist and then yeah I could try calling around some physiotherapy clinics but if I don't it's OK too If I don't get any more treatment well I really want you to reach out and call your physiotherapist And since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week Let's try to do that so that you're talking to them by then And I would like to get an update from you If I don't then I don't think I'll be able to approve any more of the massage either OK So what happens if I need more treatment though or if I feel like I'm still in pain or I'm not able to do all of my regular stuff Well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back But if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you Really I think I've talked to you before and I put the notes in your file here that you're not following the advice that you were given Oh OK Well I'm really sorry I didn't mean to not follow the advice like I I typically do like to follow what you tell me I just must have forgot but yeah OK I can do what you told me and I'll I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there But if not I guess I just won't bother you anymore Well I've noted that down your file and you've been given all the information so you know what needs to happen next Again if I don't hear back from by next week then we won't be approving any more treatment OK OK well I'll try to follow up then with a physiotherapist and I'll try to get back to you next week Is there anything else that I should be doing No You have my number And like I mentioned I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you So you know what time I work So please give me a call OK I'm really sorry about that Thanks so much for calling me today OK Bye",
            "display": "Hi, this is Bobby calling from ICBCS Assembly. Hi, this is Emily. Yes. Oh, hi, Emily. I'm glad I got a hold of you. It's been really hard to reach you. I've been trying to call you for a while. Oh, has it? Yeah, it has. But I guess you're really busy. So I'm glad that I got a hold of you. And I wanted to talk to you about your treatment and your injury claim. OK. What did you want to talk about specifically? Well, I want to talk to you about how your treatment is going. So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist. I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them. Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments. I was hoping I could find a physiotherapist in the same clinic, but I couldn't. So I thought it was just easier to keep going to my massage therapist. OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time. Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there. Yeah, I can see that. And we approved the last treatment request that your massage therapist sent in. But to be honest with you, I'm not going to prove the next one. I did talk to you about talking to your physiotherapist and making that call. So you're going to need to do that if you want to keep having treatment provided under your claim. OK, that makes sense. I can do that. You know what? I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment. Well, you mentioned that you're still having problems with your knee and you're fine now. Is that what you're saying? Yeah. I mean, it still hurts, but I think, you know, it could be worse. So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards. So when we talked and I gave you the information, I you are expected to follow it. You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better. OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too. If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist. And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week. Let's try to do that so that you're talking to them by then. And I would like to get an update from you. If I don't, then I don't think I'll be able to approve any more of the massage either. OK. So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff? Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back. But if you're going to pause and stop treatment, it's gonna be really difficult for us to approve any more for you. Really. I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given. Oh, OK. Well, I'm really sorry. I didn't mean to not follow the advice like I I typically do like to follow what you tell me. I just must have forgot, but yeah, OK, I can do what you told me and I'll. I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there. But if not, I guess I just won't bother you anymore. Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next. Again, if I don't hear back from by next week, then we won't be approving any more treatment. OK. OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week. Is there anything else that I should be doing? No. You have my number. And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you. So you know what time I work. So please give me a call. OK. I'm really sorry about that. Thanks so much for calling me today. OK. Bye."
          }
        ],
        "recognizedPhrases": [
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3.6S",
            "duration": "PT3.04S",
            "offsetInTicks": 36000000.0,
            "durationInTicks": 30400000.0,
            "nBest": [
              {
                "confidence": 0.5737923,
                "lexical": "hi this is bobby calling from I C B C S assembly",
                "itn": "hi this is bobby calling from ICBCS assembly",
                "maskedITN": "Hi this is Bobby calling from ICBCS Assembly",
                "display": "Hi, this is Bobby calling from ICBCS Assembly.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3.6S",
            "duration": "PT3.04S",
            "offsetInTicks": 36000000.0,
            "durationInTicks": 30400000.0,
            "nBest": [
              {
                "confidence": 0.5737923,
                "lexical": "hi this is bobby calling from I C B C S assembly",
                "itn": "hi this is bobby calling from ICBCS assembly",
                "maskedITN": "Hi this is Bobby calling from ICBCS Assembly",
                "display": "Hi, this is Bobby calling from ICBCS Assembly.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT6.76S",
            "duration": "PT0.92S",
            "offsetInTicks": 67600000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.7999102,
                "lexical": "hi this is emily",
                "itn": "hi this is emily",
                "maskedITN": "Hi this is Emily",
                "display": "Hi, this is Emily.",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.81,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT6.76S",
            "duration": "PT0.92S",
            "offsetInTicks": 67600000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.7999102,
                "lexical": "hi this is emily",
                "itn": "hi this is emily",
                "maskedITN": "Hi this is Emily",
                "display": "Hi, this is Emily.",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.81,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT7.68S",
            "duration": "PT0.16S",
            "offsetInTicks": 76800000.0,
            "durationInTicks": 1600000.0,
            "nBest": [
              {
                "confidence": 0.5896488,
                "lexical": "yes",
                "itn": "yes",
                "maskedITN": "Yes",
                "display": "Yes.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT7.68S",
            "duration": "PT0.16S",
            "offsetInTicks": 76800000.0,
            "durationInTicks": 1600000.0,
            "nBest": [
              {
                "confidence": 0.5896488,
                "lexical": "yes",
                "itn": "yes",
                "maskedITN": "Yes",
                "display": "Yes.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT8.4S",
            "duration": "PT0.76S",
            "offsetInTicks": 84000000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.75485533,
                "lexical": "oh hi emily",
                "itn": "oh hi emily",
                "maskedITN": "Oh hi Emily",
                "display": "Oh, hi, Emily.",
                "sentiment": {
                  "positive": 0.18,
                  "neutral": 0.76,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT8.4S",
            "duration": "PT0.76S",
            "offsetInTicks": 84000000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.75485533,
                "lexical": "oh hi emily",
                "itn": "oh hi emily",
                "maskedITN": "Oh hi Emily",
                "display": "Oh, hi, Emily.",
                "sentiment": {
                  "positive": 0.18,
                  "neutral": 0.76,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT9.16S",
            "duration": "PT1.4S",
            "offsetInTicks": 91600000.0,
            "durationInTicks": 14000000.0,
            "nBest": [
              {
                "confidence": 0.66658294,
                "lexical": "i'm glad i got a hold of you",
                "itn": "i'm glad i got a hold of you",
                "maskedITN": "I'm glad I got a hold of you",
                "display": "I'm glad I got a hold of you.",
                "sentiment": {
                  "positive": 0.93,
                  "neutral": 0.06,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT9.16S",
            "duration": "PT1.4S",
            "offsetInTicks": 91600000.0,
            "durationInTicks": 14000000.0,
            "nBest": [
              {
                "confidence": 0.66658294,
                "lexical": "i'm glad i got a hold of you",
                "itn": "i'm glad i got a hold of you",
                "maskedITN": "I'm glad I got a hold of you",
                "display": "I'm glad I got a hold of you.",
                "sentiment": {
                  "positive": 0.93,
                  "neutral": 0.06,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT10.56S",
            "duration": "PT1S",
            "offsetInTicks": 105600000.0,
            "durationInTicks": 10000000.0,
            "nBest": [
              {
                "confidence": 0.8738227,
                "lexical": "it's been really hard to reach you",
                "itn": "it's been really hard to reach you",
                "maskedITN": "It's been really hard to reach you",
                "display": "It's been really hard to reach you.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.03,
                  "negative": 0.96
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT10.56S",
            "duration": "PT1S",
            "offsetInTicks": 105600000.0,
            "durationInTicks": 10000000.0,
            "nBest": [
              {
                "confidence": 0.8738227,
                "lexical": "it's been really hard to reach you",
                "itn": "it's been really hard to reach you",
                "maskedITN": "It's been really hard to reach you",
                "display": "It's been really hard to reach you.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.03,
                  "negative": 0.96
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT11.56S",
            "duration": "PT1.48S",
            "offsetInTicks": 115600000.0,
            "durationInTicks": 14800000.0,
            "nBest": [
              {
                "confidence": 0.93927175,
                "lexical": "i've been trying to call you for a while",
                "itn": "i've been trying to call you for a while",
                "maskedITN": "I've been trying to call you for a while",
                "display": "I've been trying to call you for a while.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.91,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT11.56S",
            "duration": "PT1.48S",
            "offsetInTicks": 115600000.0,
            "durationInTicks": 14800000.0,
            "nBest": [
              {
                "confidence": 0.93927175,
                "lexical": "i've been trying to call you for a while",
                "itn": "i've been trying to call you for a while",
                "maskedITN": "I've been trying to call you for a while",
                "display": "I've been trying to call you for a while.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.91,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT13.48S",
            "duration": "PT0.52S",
            "offsetInTicks": 134800000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.7048717,
                "lexical": "oh has it",
                "itn": "oh has it",
                "maskedITN": "Oh has it",
                "display": "Oh, has it?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT13.48S",
            "duration": "PT0.52S",
            "offsetInTicks": 134800000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.7048717,
                "lexical": "oh has it",
                "itn": "oh has it",
                "maskedITN": "Oh has it",
                "display": "Oh, has it?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT14.68S",
            "duration": "PT0.8S",
            "offsetInTicks": 146800000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.96455467,
                "lexical": "yeah it has",
                "itn": "yeah it has",
                "maskedITN": "Yeah it has",
                "display": "Yeah, it has.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.89,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT14.68S",
            "duration": "PT0.8S",
            "offsetInTicks": 146800000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.96455467,
                "lexical": "yeah it has",
                "itn": "yeah it has",
                "maskedITN": "Yeah it has",
                "display": "Yeah, it has.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.89,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT15.48S",
            "duration": "PT1.88S",
            "offsetInTicks": 154800000.0,
            "durationInTicks": 18800000.0,
            "nBest": [
              {
                "confidence": 0.93661267,
                "lexical": "but i guess you're really busy",
                "itn": "but i guess you're really busy",
                "maskedITN": "But I guess you're really busy",
                "display": "But I guess you're really busy.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.8,
                  "negative": 0.16
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT15.48S",
            "duration": "PT1.88S",
            "offsetInTicks": 154800000.0,
            "durationInTicks": 18800000.0,
            "nBest": [
              {
                "confidence": 0.93661267,
                "lexical": "but i guess you're really busy",
                "itn": "but i guess you're really busy",
                "maskedITN": "But I guess you're really busy",
                "display": "But I guess you're really busy.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.8,
                  "negative": 0.16
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT17.4S",
            "duration": "PT1.68S",
            "offsetInTicks": 174000000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.9108302,
                "lexical": "so i'm glad that i got a hold of you",
                "itn": "so i'm glad that i got a hold of you",
                "maskedITN": "So I'm glad that I got a hold of you",
                "display": "So I'm glad that I got a hold of you.",
                "sentiment": {
                  "positive": 0.94,
                  "neutral": 0.05,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT17.4S",
            "duration": "PT1.68S",
            "offsetInTicks": 174000000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.9108302,
                "lexical": "so i'm glad that i got a hold of you",
                "itn": "so i'm glad that i got a hold of you",
                "maskedITN": "So I'm glad that I got a hold of you",
                "display": "So I'm glad that I got a hold of you.",
                "sentiment": {
                  "positive": 0.94,
                  "neutral": 0.05,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT19.52S",
            "duration": "PT4.48S",
            "offsetInTicks": 195200000.0,
            "durationInTicks": 44800000.0,
            "nBest": [
              {
                "confidence": 0.88205296,
                "lexical": "and i wanted to talk to you about your treatment and your injury claim",
                "itn": "and i wanted to talk to you about your treatment and your injury claim",
                "maskedITN": "And I wanted to talk to you about your treatment and your injury claim",
                "display": "And I wanted to talk to you about your treatment and your injury claim.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.79,
                  "negative": 0.18
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT19.52S",
            "duration": "PT4.48S",
            "offsetInTicks": 195200000.0,
            "durationInTicks": 44800000.0,
            "nBest": [
              {
                "confidence": 0.88205296,
                "lexical": "and i wanted to talk to you about your treatment and your injury claim",
                "itn": "and i wanted to talk to you about your treatment and your injury claim",
                "maskedITN": "And I wanted to talk to you about your treatment and your injury claim",
                "display": "And I wanted to talk to you about your treatment and your injury claim.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.79,
                  "negative": 0.18
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT24.56S",
            "duration": "PT0.56S",
            "offsetInTicks": 245600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.61391276,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT24.56S",
            "duration": "PT0.56S",
            "offsetInTicks": 245600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.61391276,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT25.56S",
            "duration": "PT2S",
            "offsetInTicks": 255600000.0,
            "durationInTicks": 20000000.0,
            "nBest": [
              {
                "confidence": 0.80560035,
                "lexical": "what did you want to talk about specifically",
                "itn": "what did you want to talk about specifically",
                "maskedITN": "What did you want to talk about specifically",
                "display": "What did you want to talk about specifically?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT25.56S",
            "duration": "PT2S",
            "offsetInTicks": 255600000.0,
            "durationInTicks": 20000000.0,
            "nBest": [
              {
                "confidence": 0.80560035,
                "lexical": "what did you want to talk about specifically",
                "itn": "what did you want to talk about specifically",
                "maskedITN": "What did you want to talk about specifically",
                "display": "What did you want to talk about specifically?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT28.68S",
            "duration": "PT2.44S",
            "offsetInTicks": 286800000.0,
            "durationInTicks": 24400000.0,
            "nBest": [
              {
                "confidence": 0.8774591,
                "lexical": "well i want to talk to you about how your treatment is going",
                "itn": "well i want to talk to you about how your treatment is going",
                "maskedITN": "Well I want to talk to you about how your treatment is going",
                "display": "Well, I want to talk to you about how your treatment is going.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.9,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT28.68S",
            "duration": "PT2.44S",
            "offsetInTicks": 286800000.0,
            "durationInTicks": 24400000.0,
            "nBest": [
              {
                "confidence": 0.8774591,
                "lexical": "well i want to talk to you about how your treatment is going",
                "itn": "well i want to talk to you about how your treatment is going",
                "maskedITN": "Well I want to talk to you about how your treatment is going",
                "display": "Well, I want to talk to you about how your treatment is going.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.9,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT31.16S",
            "duration": "PT11.16S",
            "offsetInTicks": 311600000.0,
            "durationInTicks": 111600000.0,
            "nBest": [
              {
                "confidence": 0.900839,
                "lexical": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
                "itn": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
                "maskedITN": "So I've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
                "display": "So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT31.16S",
            "duration": "PT11.16S",
            "offsetInTicks": 311600000.0,
            "durationInTicks": 111600000.0,
            "nBest": [
              {
                "confidence": 0.900839,
                "lexical": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
                "itn": "so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
                "maskedITN": "So I've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist",
                "display": "So I've noticed that you've been going for to your RMT to massage for a while, and last time we talked, we talked about also going to your physiotherapist.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT42.32S",
            "duration": "PT6.36S",
            "offsetInTicks": 423200000.0,
            "durationInTicks": 63600000.0,
            "nBest": [
              {
                "confidence": 0.8943061,
                "lexical": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
                "itn": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
                "maskedITN": "I see that your doctor had recommended it too before and I want to follow up to see if you've been doing that or if you've talked to them",
                "display": "I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.89,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT42.32S",
            "duration": "PT6.36S",
            "offsetInTicks": 423200000.0,
            "durationInTicks": 63600000.0,
            "nBest": [
              {
                "confidence": 0.8943061,
                "lexical": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
                "itn": "i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them",
                "maskedITN": "I see that your doctor had recommended it too before and I want to follow up to see if you've been doing that or if you've talked to them",
                "display": "I see that your doctor had recommended it too before, and I want to follow up to see if you've been doing that or if you've talked to them.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.89,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT50S",
            "duration": "PT4.44S",
            "offsetInTicks": 500000000.0,
            "durationInTicks": 44400000.0,
            "nBest": [
              {
                "confidence": 0.89600575,
                "lexical": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
                "itn": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
                "maskedITN": "Yeah it's been kind of easier just to go to my massage therapist 'cause I can get appointments",
                "display": "Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments.",
                "sentiment": {
                  "positive": 0.35,
                  "neutral": 0.63,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT50S",
            "duration": "PT4.44S",
            "offsetInTicks": 500000000.0,
            "durationInTicks": 44400000.0,
            "nBest": [
              {
                "confidence": 0.89600575,
                "lexical": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
                "itn": "yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments",
                "maskedITN": "Yeah it's been kind of easier just to go to my massage therapist 'cause I can get appointments",
                "display": "Yeah, it's been kind of easier just to go to my massage therapist, 'cause I can get appointments.",
                "sentiment": {
                  "positive": 0.35,
                  "neutral": 0.63,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT55.56S",
            "duration": "PT3.84S",
            "offsetInTicks": 555600000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.9595821,
                "lexical": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
                "itn": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
                "maskedITN": "I was hoping I could find a physiotherapist in the same clinic but I couldn't",
                "display": "I was hoping I could find a physiotherapist in the same clinic, but I couldn't.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.11,
                  "negative": 0.88
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT55.56S",
            "duration": "PT3.84S",
            "offsetInTicks": 555600000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.9595821,
                "lexical": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
                "itn": "i was hoping i could find a physiotherapist in the same clinic but i couldn't",
                "maskedITN": "I was hoping I could find a physiotherapist in the same clinic but I couldn't",
                "display": "I was hoping I could find a physiotherapist in the same clinic, but I couldn't.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.11,
                  "negative": 0.88
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT59.4S",
            "duration": "PT2.96S",
            "offsetInTicks": 594000000.0,
            "durationInTicks": 29600000.0,
            "nBest": [
              {
                "confidence": 0.96160287,
                "lexical": "so i thought it was just easier to keep going to my massage therapist",
                "itn": "so i thought it was just easier to keep going to my massage therapist",
                "maskedITN": "So I thought it was just easier to keep going to my massage therapist",
                "display": "So I thought it was just easier to keep going to my massage therapist.",
                "sentiment": {
                  "positive": 0.32,
                  "neutral": 0.64,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT59.4S",
            "duration": "PT2.96S",
            "offsetInTicks": 594000000.0,
            "durationInTicks": 29600000.0,
            "nBest": [
              {
                "confidence": 0.96160287,
                "lexical": "so i thought it was just easier to keep going to my massage therapist",
                "itn": "so i thought it was just easier to keep going to my massage therapist",
                "maskedITN": "So I thought it was just easier to keep going to my massage therapist",
                "display": "So I thought it was just easier to keep going to my massage therapist.",
                "sentiment": {
                  "positive": 0.32,
                  "neutral": 0.64,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M3.16S",
            "duration": "PT11.4S",
            "offsetInTicks": 631600000.0,
            "durationInTicks": 114000000.0,
            "nBest": [
              {
                "confidence": 0.92028487,
                "lexical": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
                "itn": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
                "maskedITN": "OK well I want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
                "display": "OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.51,
                  "negative": 0.39
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M3.16S",
            "duration": "PT11.4S",
            "offsetInTicks": 631600000.0,
            "durationInTicks": 114000000.0,
            "nBest": [
              {
                "confidence": 0.92028487,
                "lexical": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
                "itn": "OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
                "maskedITN": "OK well I want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time",
                "display": "OK, well, I want you to know that it's been about a month now, and you're not going to notice the difference, and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.51,
                  "negative": 0.39
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M15.96S",
            "duration": "PT5.64S",
            "offsetInTicks": 759600000.0,
            "durationInTicks": 56400000.0,
            "nBest": [
              {
                "confidence": 0.9017721,
                "lexical": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
                "itn": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
                "maskedITN": "Oh OK Well my massage therapist kept booking me in so I thought I was just good to keep going there",
                "display": "Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there.",
                "sentiment": {
                  "positive": 0.61,
                  "neutral": 0.32,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M15.96S",
            "duration": "PT5.64S",
            "offsetInTicks": 759600000.0,
            "durationInTicks": 56400000.0,
            "nBest": [
              {
                "confidence": 0.9017721,
                "lexical": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
                "itn": "oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there",
                "maskedITN": "Oh OK Well my massage therapist kept booking me in so I thought I was just good to keep going there",
                "display": "Oh, OK, Well, my massage therapist kept booking me in, so I thought I was just good to keep going there.",
                "sentiment": {
                  "positive": 0.61,
                  "neutral": 0.32,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M22.24S",
            "duration": "PT1.04S",
            "offsetInTicks": 822400000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.97718424,
                "lexical": "yeah i can see that",
                "itn": "yeah i can see that",
                "maskedITN": "Yeah I can see that",
                "display": "Yeah, I can see that.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.88,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M22.24S",
            "duration": "PT1.04S",
            "offsetInTicks": 822400000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.97718424,
                "lexical": "yeah i can see that",
                "itn": "yeah i can see that",
                "maskedITN": "Yeah I can see that",
                "display": "Yeah, I can see that.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.88,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M23.28S",
            "duration": "PT4.92S",
            "offsetInTicks": 832800000.0,
            "durationInTicks": 49200000.0,
            "nBest": [
              {
                "confidence": 0.8318471,
                "lexical": "and we approved the last treatment request that your massage therapist sent in",
                "itn": "and we approved the last treatment request that your massage therapist sent in",
                "maskedITN": "And we approved the last treatment request that your massage therapist sent in",
                "display": "And we approved the last treatment request that your massage therapist sent in.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M23.28S",
            "duration": "PT4.92S",
            "offsetInTicks": 832800000.0,
            "durationInTicks": 49200000.0,
            "nBest": [
              {
                "confidence": 0.8318471,
                "lexical": "and we approved the last treatment request that your massage therapist sent in",
                "itn": "and we approved the last treatment request that your massage therapist sent in",
                "maskedITN": "And we approved the last treatment request that your massage therapist sent in",
                "display": "And we approved the last treatment request that your massage therapist sent in.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M28.36S",
            "duration": "PT2.12S",
            "offsetInTicks": 883600000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.8500976,
                "lexical": "but to be honest with you i'm not going to prove the next one",
                "itn": "but to be honest with you i'm not going to prove the next one",
                "maskedITN": "But to be honest with you I'm not going to prove the next one",
                "display": "But to be honest with you, I'm not going to prove the next one.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.65,
                  "negative": 0.29
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M28.36S",
            "duration": "PT2.12S",
            "offsetInTicks": 883600000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.8500976,
                "lexical": "but to be honest with you i'm not going to prove the next one",
                "itn": "but to be honest with you i'm not going to prove the next one",
                "maskedITN": "But to be honest with you I'm not going to prove the next one",
                "display": "But to be honest with you, I'm not going to prove the next one.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.65,
                  "negative": 0.29
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M30.88S",
            "duration": "PT3.24S",
            "offsetInTicks": 908800000.0,
            "durationInTicks": 32400000.0,
            "nBest": [
              {
                "confidence": 0.82520103,
                "lexical": "i did talk to you about talking to your physiotherapist and making that call",
                "itn": "i did talk to you about talking to your physiotherapist and making that call",
                "maskedITN": "I did talk to you about talking to your physiotherapist and making that call",
                "display": "I did talk to you about talking to your physiotherapist and making that call.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M30.88S",
            "duration": "PT3.24S",
            "offsetInTicks": 908800000.0,
            "durationInTicks": 32400000.0,
            "nBest": [
              {
                "confidence": 0.82520103,
                "lexical": "i did talk to you about talking to your physiotherapist and making that call",
                "itn": "i did talk to you about talking to your physiotherapist and making that call",
                "maskedITN": "I did talk to you about talking to your physiotherapist and making that call",
                "display": "I did talk to you about talking to your physiotherapist and making that call.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M34.28S",
            "duration": "PT4.72S",
            "offsetInTicks": 942800000.0,
            "durationInTicks": 47200000.0,
            "nBest": [
              {
                "confidence": 0.8628821,
                "lexical": "so you're going to need to do that if you want to keep having treatment provided under your claim",
                "itn": "so you're going to need to do that if you want to keep having treatment provided under your claim",
                "maskedITN": "So you're going to need to do that if you want to keep having treatment provided under your claim",
                "display": "So you're going to need to do that if you want to keep having treatment provided under your claim.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M34.28S",
            "duration": "PT4.72S",
            "offsetInTicks": 942800000.0,
            "durationInTicks": 47200000.0,
            "nBest": [
              {
                "confidence": 0.8628821,
                "lexical": "so you're going to need to do that if you want to keep having treatment provided under your claim",
                "itn": "so you're going to need to do that if you want to keep having treatment provided under your claim",
                "maskedITN": "So you're going to need to do that if you want to keep having treatment provided under your claim",
                "display": "So you're going to need to do that if you want to keep having treatment provided under your claim.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M39.36S",
            "duration": "PT1.12S",
            "offsetInTicks": 993600000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.8337438,
                "lexical": "OK that makes sense",
                "itn": "OK that makes sense",
                "maskedITN": "OK that makes sense",
                "display": "OK, that makes sense.",
                "sentiment": {
                  "positive": 0.32,
                  "neutral": 0.66,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M39.36S",
            "duration": "PT1.12S",
            "offsetInTicks": 993600000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.8337438,
                "lexical": "OK that makes sense",
                "itn": "OK that makes sense",
                "maskedITN": "OK that makes sense",
                "display": "OK, that makes sense.",
                "sentiment": {
                  "positive": 0.32,
                  "neutral": 0.66,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M40.76S",
            "duration": "PT0.56S",
            "offsetInTicks": 1007600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.975323,
                "lexical": "i can do that",
                "itn": "i can do that",
                "maskedITN": "I can do that",
                "display": "I can do that.",
                "sentiment": {
                  "positive": 0.14,
                  "neutral": 0.83,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M40.76S",
            "duration": "PT0.56S",
            "offsetInTicks": 1007600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.975323,
                "lexical": "i can do that",
                "itn": "i can do that",
                "maskedITN": "I can do that",
                "display": "I can do that.",
                "sentiment": {
                  "positive": 0.14,
                  "neutral": 0.83,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M41.36S",
            "duration": "PT0.4S",
            "offsetInTicks": 1013600000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.9654927,
                "lexical": "you know what",
                "itn": "you know what",
                "maskedITN": "You know what",
                "display": "You know what?",
                "sentiment": {
                  "positive": 0.1,
                  "neutral": 0.8,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M41.36S",
            "duration": "PT0.4S",
            "offsetInTicks": 1013600000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.9654927,
                "lexical": "you know what",
                "itn": "you know what",
                "maskedITN": "You know what",
                "display": "You know what?",
                "sentiment": {
                  "positive": 0.1,
                  "neutral": 0.8,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M41.76S",
            "duration": "PT4.76S",
            "offsetInTicks": 1017600000.0,
            "durationInTicks": 47600000.0,
            "nBest": [
              {
                "confidence": 0.9135152,
                "lexical": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
                "itn": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
                "maskedITN": "I'm feeling pretty good anyways so I don't even know if I'm going to need any more treatment",
                "display": "I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment.",
                "sentiment": {
                  "positive": 0.65,
                  "neutral": 0.23,
                  "negative": 0.12
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M41.76S",
            "duration": "PT4.76S",
            "offsetInTicks": 1017600000.0,
            "durationInTicks": 47600000.0,
            "nBest": [
              {
                "confidence": 0.9135152,
                "lexical": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
                "itn": "i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment",
                "maskedITN": "I'm feeling pretty good anyways so I don't even know if I'm going to need any more treatment",
                "display": "I'm feeling pretty good anyways, so I don't even know if I'm going to need any more treatment.",
                "sentiment": {
                  "positive": 0.65,
                  "neutral": 0.23,
                  "negative": 0.12
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M49.48S",
            "duration": "PT5.44S",
            "offsetInTicks": 1094800000.0,
            "durationInTicks": 54400000.0,
            "nBest": [
              {
                "confidence": 0.87481225,
                "lexical": "well you mentioned that you're still having problems with your knee and you're fine now",
                "itn": "well you mentioned that you're still having problems with your knee and you're fine now",
                "maskedITN": "Well you mentioned that you're still having problems with your knee and you're fine now",
                "display": "Well, you mentioned that you're still having problems with your knee and you're fine now.",
                "sentiment": {
                  "positive": 0.17,
                  "neutral": 0.44,
                  "negative": 0.39
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M49.48S",
            "duration": "PT5.44S",
            "offsetInTicks": 1094800000.0,
            "durationInTicks": 54400000.0,
            "nBest": [
              {
                "confidence": 0.87481225,
                "lexical": "well you mentioned that you're still having problems with your knee and you're fine now",
                "itn": "well you mentioned that you're still having problems with your knee and you're fine now",
                "maskedITN": "Well you mentioned that you're still having problems with your knee and you're fine now",
                "display": "Well, you mentioned that you're still having problems with your knee and you're fine now.",
                "sentiment": {
                  "positive": 0.17,
                  "neutral": 0.44,
                  "negative": 0.39
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M54.92S",
            "duration": "PT0.84S",
            "offsetInTicks": 1149200000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.9174827,
                "lexical": "is that what you're saying",
                "itn": "is that what you're saying",
                "maskedITN": "Is that what you're saying",
                "display": "Is that what you're saying?",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.9,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M54.92S",
            "duration": "PT0.84S",
            "offsetInTicks": 1149200000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.9174827,
                "lexical": "is that what you're saying",
                "itn": "is that what you're saying",
                "maskedITN": "Is that what you're saying",
                "display": "Is that what you're saying?",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.9,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M56.36S",
            "duration": "PT0.28S",
            "offsetInTicks": 1163600000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.9681455,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M56.36S",
            "duration": "PT0.28S",
            "offsetInTicks": 1163600000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.9681455,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M56.64S",
            "duration": "PT3.92S",
            "offsetInTicks": 1166400000.0,
            "durationInTicks": 39200000.0,
            "nBest": [
              {
                "confidence": 0.9308511,
                "lexical": "i mean it still hurts but i think you know it could be worse",
                "itn": "i mean it still hurts but i think you know it could be worse",
                "maskedITN": "I mean it still hurts but I think you know it could be worse",
                "display": "I mean, it still hurts, but I think, you know, it could be worse.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.15,
                  "negative": 0.84
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M56.64S",
            "duration": "PT3.92S",
            "offsetInTicks": 1166400000.0,
            "durationInTicks": 39200000.0,
            "nBest": [
              {
                "confidence": 0.9308511,
                "lexical": "i mean it still hurts but i think you know it could be worse",
                "itn": "i mean it still hurts but i think you know it could be worse",
                "maskedITN": "I mean it still hurts but I think you know it could be worse",
                "display": "I mean, it still hurts, but I think, you know, it could be worse.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.15,
                  "negative": 0.84
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M0.76S",
            "duration": "PT9.2S",
            "offsetInTicks": 1207600000.0,
            "durationInTicks": 92000000.0,
            "nBest": [
              {
                "confidence": 0.8537005,
                "lexical": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
                "itn": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
                "maskedITN": "So well I like I told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
                "display": "So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.24,
                  "negative": 0.66
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M0.76S",
            "duration": "PT9.2S",
            "offsetInTicks": 1207600000.0,
            "durationInTicks": 92000000.0,
            "nBest": [
              {
                "confidence": 0.8537005,
                "lexical": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
                "itn": "so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
                "maskedITN": "So well I like I told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards",
                "display": "So well, I like I told you before, if you don't follow the advice you were given, it likely could get worse and then you're not going to be able to get any treatment afterwards.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.24,
                  "negative": 0.66
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M9.96S",
            "duration": "PT5.28S",
            "offsetInTicks": 1299600000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.8918789,
                "lexical": "so when we talked and i gave you the information i you are expected to follow it",
                "itn": "so when we talked and i gave you the information i you are expected to follow it",
                "maskedITN": "So when we talked and I gave you the information I you are expected to follow it",
                "display": "So when we talked and I gave you the information, I you are expected to follow it.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M9.96S",
            "duration": "PT5.28S",
            "offsetInTicks": 1299600000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.8918789,
                "lexical": "so when we talked and i gave you the information i you are expected to follow it",
                "itn": "so when we talked and i gave you the information i you are expected to follow it",
                "maskedITN": "So when we talked and I gave you the information I you are expected to follow it",
                "display": "So when we talked and I gave you the information, I you are expected to follow it.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M15.24S",
            "duration": "PT7.88S",
            "offsetInTicks": 1352400000.0,
            "durationInTicks": 78800000.0,
            "nBest": [
              {
                "confidence": 0.8945967,
                "lexical": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
                "itn": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
                "maskedITN": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
                "display": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better.",
                "sentiment": {
                  "positive": 0.29,
                  "neutral": 0.68,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M15.24S",
            "duration": "PT7.88S",
            "offsetInTicks": 1352400000.0,
            "durationInTicks": 78800000.0,
            "nBest": [
              {
                "confidence": 0.8945967,
                "lexical": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
                "itn": "you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
                "maskedITN": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better",
                "display": "You do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better.",
                "sentiment": {
                  "positive": 0.29,
                  "neutral": 0.68,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M23.72S",
            "duration": "PT8.68S",
            "offsetInTicks": 1437200000.0,
            "durationInTicks": 86800000.0,
            "nBest": [
              {
                "confidence": 0.9103605,
                "lexical": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
                "itn": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
                "maskedITN": "OK well I guess I could always talk to my massage therapist and then yeah I could try calling around some physiotherapy clinics but if I don't it's OK too",
                "display": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too.",
                "sentiment": {
                  "positive": 0.17,
                  "neutral": 0.75,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M23.72S",
            "duration": "PT8.68S",
            "offsetInTicks": 1437200000.0,
            "durationInTicks": 86800000.0,
            "nBest": [
              {
                "confidence": 0.9103605,
                "lexical": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
                "itn": "OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too",
                "maskedITN": "OK well I guess I could always talk to my massage therapist and then yeah I could try calling around some physiotherapy clinics but if I don't it's OK too",
                "display": "OK, well, I guess I could always talk to my massage therapist and then, yeah, I could try calling around some physiotherapy clinics, but if I don't, it's OK too.",
                "sentiment": {
                  "positive": 0.17,
                  "neutral": 0.75,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M32.4S",
            "duration": "PT5.36S",
            "offsetInTicks": 1524000000.0,
            "durationInTicks": 53600000.0,
            "nBest": [
              {
                "confidence": 0.8952053,
                "lexical": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
                "itn": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
                "maskedITN": "If I don't get any more treatment well I really want you to reach out and call your physiotherapist",
                "display": "If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.64,
                  "negative": 0.28
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M32.4S",
            "duration": "PT5.36S",
            "offsetInTicks": 1524000000.0,
            "durationInTicks": 53600000.0,
            "nBest": [
              {
                "confidence": 0.8952053,
                "lexical": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
                "itn": "if i don't get any more treatment well i really want you to reach out and call your physiotherapist",
                "maskedITN": "If I don't get any more treatment well I really want you to reach out and call your physiotherapist",
                "display": "If I don't get any more treatment, well, I really want you to reach out and call your physiotherapist.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.64,
                  "negative": 0.28
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M37.76S",
            "duration": "PT5.76S",
            "offsetInTicks": 1577600000.0,
            "durationInTicks": 57600000.0,
            "nBest": [
              {
                "confidence": 0.89760923,
                "lexical": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
                "itn": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
                "maskedITN": "And since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
                "display": "And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.8,
                  "negative": 0.11
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M37.76S",
            "duration": "PT5.76S",
            "offsetInTicks": 1577600000.0,
            "durationInTicks": 57600000.0,
            "nBest": [
              {
                "confidence": 0.89760923,
                "lexical": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
                "itn": "and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
                "maskedITN": "And since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week",
                "display": "And since you haven't done it yet, and this is the third time we've talked about it, if you could please give me a call back next week.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.8,
                  "negative": 0.11
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M43.68S",
            "duration": "PT2.4S",
            "offsetInTicks": 1636800000.0,
            "durationInTicks": 24000000.0,
            "nBest": [
              {
                "confidence": 0.8954488,
                "lexical": "let's try to do that so that you're talking to them by then",
                "itn": "let's try to do that so that you're talking to them by then",
                "maskedITN": "Let's try to do that so that you're talking to them by then",
                "display": "Let's try to do that so that you're talking to them by then.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M43.68S",
            "duration": "PT2.4S",
            "offsetInTicks": 1636800000.0,
            "durationInTicks": 24000000.0,
            "nBest": [
              {
                "confidence": 0.8954488,
                "lexical": "let's try to do that so that you're talking to them by then",
                "itn": "let's try to do that so that you're talking to them by then",
                "maskedITN": "Let's try to do that so that you're talking to them by then",
                "display": "Let's try to do that so that you're talking to them by then.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M46.08S",
            "duration": "PT1.44S",
            "offsetInTicks": 1660800000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.97443545,
                "lexical": "and i would like to get an update from you",
                "itn": "and i would like to get an update from you",
                "maskedITN": "And I would like to get an update from you",
                "display": "And I would like to get an update from you.",
                "sentiment": {
                  "positive": 0.73,
                  "neutral": 0.24,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M46.08S",
            "duration": "PT1.44S",
            "offsetInTicks": 1660800000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.97443545,
                "lexical": "and i would like to get an update from you",
                "itn": "and i would like to get an update from you",
                "maskedITN": "And I would like to get an update from you",
                "display": "And I would like to get an update from you.",
                "sentiment": {
                  "positive": 0.73,
                  "neutral": 0.24,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M47.88S",
            "duration": "PT5S",
            "offsetInTicks": 1678800000.0,
            "durationInTicks": 50000000.0,
            "nBest": [
              {
                "confidence": 0.9526655,
                "lexical": "if i don't then i don't think i'll be able to approve any more of the massage either",
                "itn": "if i don't then i don't think i'll be able to approve any more of the massage either",
                "maskedITN": "If I don't then I don't think I'll be able to approve any more of the massage either",
                "display": "If I don't, then I don't think I'll be able to approve any more of the massage either.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.48,
                  "negative": 0.5
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M47.88S",
            "duration": "PT5S",
            "offsetInTicks": 1678800000.0,
            "durationInTicks": 50000000.0,
            "nBest": [
              {
                "confidence": 0.9526655,
                "lexical": "if i don't then i don't think i'll be able to approve any more of the massage either",
                "itn": "if i don't then i don't think i'll be able to approve any more of the massage either",
                "maskedITN": "If I don't then I don't think I'll be able to approve any more of the massage either",
                "display": "If I don't, then I don't think I'll be able to approve any more of the massage either.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.48,
                  "negative": 0.5
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M53.44S",
            "duration": "PT0.44S",
            "offsetInTicks": 1734400000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.7420973,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M53.44S",
            "duration": "PT0.44S",
            "offsetInTicks": 1734400000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.7420973,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M53.88S",
            "duration": "PT7.92S",
            "offsetInTicks": 1738800000.0,
            "durationInTicks": 79200000.0,
            "nBest": [
              {
                "confidence": 0.9224396,
                "lexical": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
                "itn": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
                "maskedITN": "So what happens if I need more treatment though or if I feel like I'm still in pain or I'm not able to do all of my regular stuff",
                "display": "So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.64,
                  "negative": 0.35
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M53.88S",
            "duration": "PT7.92S",
            "offsetInTicks": 1738800000.0,
            "durationInTicks": 79200000.0,
            "nBest": [
              {
                "confidence": 0.9224396,
                "lexical": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
                "itn": "so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff",
                "maskedITN": "So what happens if I need more treatment though or if I feel like I'm still in pain or I'm not able to do all of my regular stuff",
                "display": "So what happens if I need more treatment though, or if I feel like I'm still in pain or I'm not able to do all of my regular stuff?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.64,
                  "negative": 0.35
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M2.2S",
            "duration": "PT7.16S",
            "offsetInTicks": 1822000000.0,
            "durationInTicks": 71600000.0,
            "nBest": [
              {
                "confidence": 0.8876678,
                "lexical": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
                "itn": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
                "maskedITN": "Well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
                "display": "Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back.",
                "sentiment": {
                  "positive": 0.38,
                  "neutral": 0.56,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M2.2S",
            "duration": "PT7.16S",
            "offsetInTicks": 1822000000.0,
            "durationInTicks": 71600000.0,
            "nBest": [
              {
                "confidence": 0.8876678,
                "lexical": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
                "itn": "well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
                "maskedITN": "Well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back",
                "display": "Well, if you had been going for the treatment that was recommended in the beginning, then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back.",
                "sentiment": {
                  "positive": 0.38,
                  "neutral": 0.56,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M9.36S",
            "duration": "PT5.72S",
            "offsetInTicks": 1893600000.0,
            "durationInTicks": 57200000.0,
            "nBest": [
              {
                "confidence": 0.7993024,
                "lexical": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
                "itn": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
                "maskedITN": "But if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
                "display": "But if you're going to pause and stop treatment, it's gonna be really difficult for us to approve any more for you.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.17,
                  "negative": 0.81
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M9.36S",
            "duration": "PT5.72S",
            "offsetInTicks": 1893600000.0,
            "durationInTicks": 57200000.0,
            "nBest": [
              {
                "confidence": 0.7993024,
                "lexical": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
                "itn": "but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
                "maskedITN": "But if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you",
                "display": "But if you're going to pause and stop treatment, it's gonna be really difficult for us to approve any more for you.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.17,
                  "negative": 0.81
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M16.16S",
            "duration": "PT0.36S",
            "offsetInTicks": 1961600000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.9715944,
                "lexical": "really",
                "itn": "really",
                "maskedITN": "Really",
                "display": "Really.",
                "sentiment": {
                  "positive": 0.28,
                  "neutral": 0.63,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M16.16S",
            "duration": "PT0.36S",
            "offsetInTicks": 1961600000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.9715944,
                "lexical": "really",
                "itn": "really",
                "maskedITN": "Really",
                "display": "Really.",
                "sentiment": {
                  "positive": 0.28,
                  "neutral": 0.63,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M16.52S",
            "duration": "PT5.4S",
            "offsetInTicks": 1965200000.0,
            "durationInTicks": 54000000.0,
            "nBest": [
              {
                "confidence": 0.854016,
                "lexical": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
                "itn": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
                "maskedITN": "I think I've talked to you before and I put the notes in your file here that you're not following the advice that you were given",
                "display": "I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.62,
                  "negative": 0.37
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M16.52S",
            "duration": "PT5.4S",
            "offsetInTicks": 1965200000.0,
            "durationInTicks": 54000000.0,
            "nBest": [
              {
                "confidence": 0.854016,
                "lexical": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
                "itn": "i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given",
                "maskedITN": "I think I've talked to you before and I put the notes in your file here that you're not following the advice that you were given",
                "display": "I think I've talked to you before, and I put the notes in your file here that you're not following the advice that you were given.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.62,
                  "negative": 0.37
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M23.04S",
            "duration": "PT0.76S",
            "offsetInTicks": 2030400000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.8150648,
                "lexical": "oh OK",
                "itn": "oh OK",
                "maskedITN": "Oh OK",
                "display": "Oh, OK.",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.79,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M23.04S",
            "duration": "PT0.76S",
            "offsetInTicks": 2030400000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.8150648,
                "lexical": "oh OK",
                "itn": "oh OK",
                "maskedITN": "Oh OK",
                "display": "Oh, OK.",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.79,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M24S",
            "duration": "PT1.44S",
            "offsetInTicks": 2040000000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.9317466,
                "lexical": "well i'm really sorry",
                "itn": "well i'm really sorry",
                "maskedITN": "Well I'm really sorry",
                "display": "Well, I'm really sorry.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.15,
                  "negative": 0.82
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M24S",
            "duration": "PT1.44S",
            "offsetInTicks": 2040000000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.9317466,
                "lexical": "well i'm really sorry",
                "itn": "well i'm really sorry",
                "maskedITN": "Well I'm really sorry",
                "display": "Well, I'm really sorry.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.15,
                  "negative": 0.82
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M25.44S",
            "duration": "PT5.72S",
            "offsetInTicks": 2054400000.0,
            "durationInTicks": 57200000.0,
            "nBest": [
              {
                "confidence": 0.9236885,
                "lexical": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
                "itn": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
                "maskedITN": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me",
                "display": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me.",
                "sentiment": {
                  "positive": 0.24,
                  "neutral": 0.54,
                  "negative": 0.21
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M25.44S",
            "duration": "PT5.72S",
            "offsetInTicks": 2054400000.0,
            "durationInTicks": 57200000.0,
            "nBest": [
              {
                "confidence": 0.9236885,
                "lexical": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
                "itn": "i didn't mean to not follow the advice like i i typically do like to follow what you tell me",
                "maskedITN": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me",
                "display": "I didn't mean to not follow the advice like I I typically do like to follow what you tell me.",
                "sentiment": {
                  "positive": 0.24,
                  "neutral": 0.54,
                  "negative": 0.21
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M31.16S",
            "duration": "PT4.96S",
            "offsetInTicks": 2111600000.0,
            "durationInTicks": 49600000.0,
            "nBest": [
              {
                "confidence": 0.89022607,
                "lexical": "i just must have forgot but yeah OK i can do what you told me and i'll",
                "itn": "i just must have forgot but yeah OK i can do what you told me and i'll",
                "maskedITN": "I just must have forgot but yeah OK I can do what you told me and I'll",
                "display": "I just must have forgot, but yeah, OK, I can do what you told me and I'll.",
                "sentiment": {
                  "positive": 0.28,
                  "neutral": 0.51,
                  "negative": 0.21
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M31.16S",
            "duration": "PT4.96S",
            "offsetInTicks": 2111600000.0,
            "durationInTicks": 49600000.0,
            "nBest": [
              {
                "confidence": 0.89022607,
                "lexical": "i just must have forgot but yeah OK i can do what you told me and i'll",
                "itn": "i just must have forgot but yeah OK i can do what you told me and i'll",
                "maskedITN": "I just must have forgot but yeah OK I can do what you told me and I'll",
                "display": "I just must have forgot, but yeah, OK, I can do what you told me and I'll.",
                "sentiment": {
                  "positive": 0.28,
                  "neutral": 0.51,
                  "negative": 0.21
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M36.12S",
            "duration": "PT4.12S",
            "offsetInTicks": 2161200000.0,
            "durationInTicks": 41200000.0,
            "nBest": [
              {
                "confidence": 0.932642,
                "lexical": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
                "itn": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
                "maskedITN": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there",
                "display": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M36.12S",
            "duration": "PT4.12S",
            "offsetInTicks": 2161200000.0,
            "durationInTicks": 41200000.0,
            "nBest": [
              {
                "confidence": 0.932642,
                "lexical": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
                "itn": "i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there",
                "maskedITN": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there",
                "display": "I'll try and talk to a physiotherapist and see if I can get in and get some more treatment there.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M40.24S",
            "duration": "PT4.2S",
            "offsetInTicks": 2202400000.0,
            "durationInTicks": 42000000.0,
            "nBest": [
              {
                "confidence": 0.92678094,
                "lexical": "but if not i guess i just won't bother you anymore",
                "itn": "but if not i guess i just won't bother you anymore",
                "maskedITN": "But if not I guess I just won't bother you anymore",
                "display": "But if not, I guess I just won't bother you anymore.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.61,
                  "negative": 0.29
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M40.24S",
            "duration": "PT4.2S",
            "offsetInTicks": 2202400000.0,
            "durationInTicks": 42000000.0,
            "nBest": [
              {
                "confidence": 0.92678094,
                "lexical": "but if not i guess i just won't bother you anymore",
                "itn": "but if not i guess i just won't bother you anymore",
                "maskedITN": "But if not I guess I just won't bother you anymore",
                "display": "But if not, I guess I just won't bother you anymore.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.61,
                  "negative": 0.29
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M45.28S",
            "duration": "PT4.36S",
            "offsetInTicks": 2252800000.0,
            "durationInTicks": 43600000.0,
            "nBest": [
              {
                "confidence": 0.93374914,
                "lexical": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
                "itn": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
                "maskedITN": "Well I've noted that down your file and you've been given all the information so you know what needs to happen next",
                "display": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.91,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M45.28S",
            "duration": "PT4.36S",
            "offsetInTicks": 2252800000.0,
            "durationInTicks": 43600000.0,
            "nBest": [
              {
                "confidence": 0.93374914,
                "lexical": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
                "itn": "well i've noted that down your file and you've been given all the information so you know what needs to happen next",
                "maskedITN": "Well I've noted that down your file and you've been given all the information so you know what needs to happen next",
                "display": "Well, I've noted that down your file and you've been given all the information, so you know what needs to happen next.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.91,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M49.88S",
            "duration": "PT4.52S",
            "offsetInTicks": 2298800000.0,
            "durationInTicks": 45200000.0,
            "nBest": [
              {
                "confidence": 0.8420017,
                "lexical": "again if i don't hear back from by next week then we won't be approving any more treatment",
                "itn": "again if i don't hear back from by next week then we won't be approving any more treatment",
                "maskedITN": "Again if I don't hear back from by next week then we won't be approving any more treatment",
                "display": "Again, if I don't hear back from by next week, then we won't be approving any more treatment.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.18,
                  "negative": 0.8
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M49.88S",
            "duration": "PT4.52S",
            "offsetInTicks": 2298800000.0,
            "durationInTicks": 45200000.0,
            "nBest": [
              {
                "confidence": 0.8420017,
                "lexical": "again if i don't hear back from by next week then we won't be approving any more treatment",
                "itn": "again if i don't hear back from by next week then we won't be approving any more treatment",
                "maskedITN": "Again if I don't hear back from by next week then we won't be approving any more treatment",
                "display": "Again, if I don't hear back from by next week, then we won't be approving any more treatment.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.18,
                  "negative": 0.8
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M55.64S",
            "duration": "PT0.44S",
            "offsetInTicks": 2356400000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.9127285,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M55.64S",
            "duration": "PT0.44S",
            "offsetInTicks": 2356400000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.9127285,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M56.24S",
            "duration": "PT4.08S",
            "offsetInTicks": 2362400000.0,
            "durationInTicks": 40800000.0,
            "nBest": [
              {
                "confidence": 0.91390073,
                "lexical": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
                "itn": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
                "maskedITN": "OK well I'll try to follow up then with a physiotherapist and I'll try to get back to you next week",
                "display": "OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week.",
                "sentiment": {
                  "positive": 0.36,
                  "neutral": 0.57,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M56.24S",
            "duration": "PT4.08S",
            "offsetInTicks": 2362400000.0,
            "durationInTicks": 40800000.0,
            "nBest": [
              {
                "confidence": 0.91390073,
                "lexical": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
                "itn": "OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week",
                "maskedITN": "OK well I'll try to follow up then with a physiotherapist and I'll try to get back to you next week",
                "display": "OK, well, I'll try to follow up then with a physiotherapist and I'll try to get back to you next week.",
                "sentiment": {
                  "positive": 0.36,
                  "neutral": 0.57,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M0.32S",
            "duration": "PT1.56S",
            "offsetInTicks": 2403200000.0,
            "durationInTicks": 15600000.0,
            "nBest": [
              {
                "confidence": 0.9654271,
                "lexical": "is there anything else that i should be doing",
                "itn": "is there anything else that i should be doing",
                "maskedITN": "Is there anything else that I should be doing",
                "display": "Is there anything else that I should be doing?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M0.32S",
            "duration": "PT1.56S",
            "offsetInTicks": 2403200000.0,
            "durationInTicks": 15600000.0,
            "nBest": [
              {
                "confidence": 0.9654271,
                "lexical": "is there anything else that i should be doing",
                "itn": "is there anything else that i should be doing",
                "maskedITN": "Is there anything else that I should be doing",
                "display": "Is there anything else that I should be doing?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M2.28S",
            "duration": "PT0.2S",
            "offsetInTicks": 2422800000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.86801356,
                "lexical": "no",
                "itn": "no",
                "maskedITN": "No",
                "display": "No.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.75,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M2.28S",
            "duration": "PT0.2S",
            "offsetInTicks": 2422800000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.86801356,
                "lexical": "no",
                "itn": "no",
                "maskedITN": "No",
                "display": "No.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.75,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M2.48S",
            "duration": "PT0.68S",
            "offsetInTicks": 2424800000.0,
            "durationInTicks": 6800000.0,
            "nBest": [
              {
                "confidence": 0.9362608,
                "lexical": "you have my number",
                "itn": "you have my number",
                "maskedITN": "You have my number",
                "display": "You have my number.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M2.48S",
            "duration": "PT0.68S",
            "offsetInTicks": 2424800000.0,
            "durationInTicks": 6800000.0,
            "nBest": [
              {
                "confidence": 0.9362608,
                "lexical": "you have my number",
                "itn": "you have my number",
                "maskedITN": "You have my number",
                "display": "You have my number.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M3.16S",
            "duration": "PT4.48S",
            "offsetInTicks": 2431600000.0,
            "durationInTicks": 44800000.0,
            "nBest": [
              {
                "confidence": 0.8232506,
                "lexical": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
                "itn": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
                "maskedITN": "And like I mentioned I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
                "display": "And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.12,
                  "negative": 0.87
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M3.16S",
            "duration": "PT4.48S",
            "offsetInTicks": 2431600000.0,
            "durationInTicks": 44800000.0,
            "nBest": [
              {
                "confidence": 0.8232506,
                "lexical": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
                "itn": "and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
                "maskedITN": "And like I mentioned I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you",
                "display": "And like I mentioned, I tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.12,
                  "negative": 0.87
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M7.64S",
            "duration": "PT1.96S",
            "offsetInTicks": 2476400000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.95009106,
                "lexical": "so you know what time i work",
                "itn": "so you know what time i work",
                "maskedITN": "So you know what time I work",
                "display": "So you know what time I work.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M7.64S",
            "duration": "PT1.96S",
            "offsetInTicks": 2476400000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.95009106,
                "lexical": "so you know what time i work",
                "itn": "so you know what time i work",
                "maskedITN": "So you know what time I work",
                "display": "So you know what time I work.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M9.6S",
            "duration": "PT0.88S",
            "offsetInTicks": 2496000000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.96111125,
                "lexical": "so please give me a call",
                "itn": "so please give me a call",
                "maskedITN": "So please give me a call",
                "display": "So please give me a call.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.91,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M9.6S",
            "duration": "PT0.88S",
            "offsetInTicks": 2496000000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.96111125,
                "lexical": "so please give me a call",
                "itn": "so please give me a call",
                "maskedITN": "So please give me a call",
                "display": "So please give me a call.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.91,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M10.64S",
            "duration": "PT0.4S",
            "offsetInTicks": 2506400000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.7671407,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M10.64S",
            "duration": "PT0.4S",
            "offsetInTicks": 2506400000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.7671407,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M11.04S",
            "duration": "PT1.04S",
            "offsetInTicks": 2510400000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.9680886,
                "lexical": "i'm really sorry about that",
                "itn": "i'm really sorry about that",
                "maskedITN": "I'm really sorry about that",
                "display": "I'm really sorry about that.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.04,
                  "negative": 0.95
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M11.04S",
            "duration": "PT1.04S",
            "offsetInTicks": 2510400000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.9680886,
                "lexical": "i'm really sorry about that",
                "itn": "i'm really sorry about that",
                "maskedITN": "I'm really sorry about that",
                "display": "I'm really sorry about that.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.04,
                  "negative": 0.95
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M12.4S",
            "duration": "PT1.28S",
            "offsetInTicks": 2524000000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.9235704,
                "lexical": "thanks so much for calling me today",
                "itn": "thanks so much for calling me today",
                "maskedITN": "Thanks so much for calling me today",
                "display": "Thanks so much for calling me today.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M12.4S",
            "duration": "PT1.28S",
            "offsetInTicks": 2524000000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.9235704,
                "lexical": "thanks so much for calling me today",
                "itn": "thanks so much for calling me today",
                "maskedITN": "Thanks so much for calling me today",
                "display": "Thanks so much for calling me today.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M14S",
            "duration": "PT0.4S",
            "offsetInTicks": 2540000000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.8961135,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M14S",
            "duration": "PT0.4S",
            "offsetInTicks": 2540000000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.8961135,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M14.48S",
            "duration": "PT0.2S",
            "offsetInTicks": 2544800000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.95479965,
                "lexical": "bye",
                "itn": "bye",
                "maskedITN": "Bye",
                "display": "Bye.",
                "sentiment": {
                  "positive": 0.25,
                  "neutral": 0.7,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M14.48S",
            "duration": "PT0.2S",
            "offsetInTicks": 2544800000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.95479965,
                "lexical": "bye",
                "itn": "bye",
                "maskedITN": "Bye",
                "display": "Bye.",
                "sentiment": {
                  "positive": 0.25,
                  "neutral": 0.7,
                  "negative": 0.05
                }
              }
            ]
          }
        ]
      }
    }
},
{
    "short": {
      "audioFile": "/call3.wav",
      "representativeName": "Eddie",
      "customerName": "Emily",
      "date": "04/15/2024",
      "callLength": 4,
      "summary": "Eddie discusses Emily's recovery progress and informs her that further physiotherapy treatment may not be approved. Instead, they suggest transitioning to more active programs like kinesiology or self-guided gym training. Emily expresses interest and plans to explore these options, including reaching out to a teammate who is a kinesiologist. They agree to follow up next Thursday and conclude with positive remarks about Emily's recovery journey.",
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
      "transcription": {
        "source": "https://github.com/ofek-zilber-icbc/ICBCHackathon2024/raw/main/backend/azure_related/call3.wav",
        "timestamp": "2024-04-25T06:07:49Z",
        "durationInTicks": 2938500000,
        "duration": "PT4M53.85S",
        "combinedRecognizedPhrases": [
          {
            "channel": 0,
            "lexical": "hi there i'm calling from ICBC my name is eddie i'm looking for emily please hey emily hey emily how are you i'm OK how are you i'm doing pretty good how how was the oven repair that you had the other day did that work out OK oh actually they weren't able to fix it and i have to have them come back another day next week oh no i hope hope that goes well and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery and we did get a chance to review your treatment plan how's that sound good thanks yeah this is a good time OK great this will probably last maybe five minutes or so maybe even less but you know throughout this conversation just don't hesitate to ask any questions and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through and as you know we've had a couple steps leading up to today and that involved for example our medical assessment we've had a chance to speak with your care team as well really just to take a look at how your recovery is going so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that before i go into that did you have any questions about what we've been doing so far no that makes sense i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment i'm really happy to go over it and really want to give you as much details as possible on this and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan we took took a look at some of the progress we took a look at some of the limitations that you've had i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here you're also able to get back to most of your daily activities so i think you mentioned something along the lines of playing soccer you're back to playing about ninety percent of those games and while there is a little bit of pain you're you're able to go through all of it so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here how does that sound OK what do you mean something more active have you have you had a chance to try kinesiology or any self self guided training gym programs any of those before no i think i've seen a sign for it at the clinic i go to but no i haven't oh fair enough and happy to go over some of those details with you i think there's a couple of things we can definitely do with you and we want to find something that works for you as well do you have any actually because they're part of the soccer team do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active oh actually you know what i think someone on my team might be a kinesiologist themselves yeah maybe i'll reach out to them i think that's a great idea that's a great start kind of see what works for them and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery and once you're done that part then we can probably look at discharging the claim how does that sound did you want to go check in with your teammate and then we can have a conversation about let's say next thursday maybe i'll call you around the same time and then we can look at some of those options together yep that sounds good next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well so before i wrap up here though since you've got me any other questions like anything else i can help you out with no i think that's it for now i'll talk to them and then i'll try to think of any questions before we speak next thursday absolutely fantastic i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job and i think we'll get you to that last step and we'll move forward together on that OK so we'll chat next week then OK thank you bye for now",
            "itn": "hi there i'm calling from ICBC my name is eddie i'm looking for emily please hey emily hey emily how are you i'm OK how are you i'm doing pretty good how how was the oven repair that you had the other day did that work out OK oh actually they weren't able to fix it and i have to have them come back another day next week oh no i hope hope that goes well and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery and we did get a chance to review your treatment plan how's that sound good thanks yeah this is a good time OK great this will probably last maybe 5 minutes or so maybe even less but you know throughout this conversation just don't hesitate to ask any questions and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through and as you know we've had a couple steps leading up to today and that involved for example our medical assessment we've had a chance to speak with your care team as well really just to take a look at how your recovery is going so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that before i go into that did you have any questions about what we've been doing so far no that makes sense i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment i'm really happy to go over it and really want to give you as much details as possible on this and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan we took took a look at some of the progress we took a look at some of the limitations that you've had i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here you're also able to get back to most of your daily activities so i think you mentioned something along the lines of playing soccer you're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here how does that sound OK what do you mean something more active have you have you had a chance to try kinesiology or any self self guided training gym programs any of those before no i think i've seen a sign for it at the clinic i go to but no i haven't oh fair enough and happy to go over some of those details with you i think there's a couple of things we can definitely do with you and we want to find something that works for you as well do you have any actually because they're part of the soccer team do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active oh actually you know what i think someone on my team might be a kinesiologist themselves yeah maybe i'll reach out to them i think that's a great idea that's a great start kind of see what works for them and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery and once you're done that part then we can probably look at discharging the claim how does that sound did you want to go check in with your teammate and then we can have a conversation about let's say next thursday maybe i'll call you around the same time and then we can look at some of those options together yep that sounds good next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well so before i wrap up here though since you've got me any other questions like anything else i can help you out with no i think that's it for now i'll talk to them and then i'll try to think of any questions before we speak next thursday absolutely fantastic i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job and i think we'll get you to that last step and we'll move forward together on that OK so we'll chat next week then OK thank you bye for now",
            "maskedITN": "Hi there I'm calling from ICBC My name is Eddie I'm looking for Emily please Hey Emily Hey Emily How are you I'm OK How are you I'm doing pretty good How How was the oven repair that you had the other day Did that work out OK Oh actually they weren't able to fix it And I have to have them come back another day next week Oh no I hope Hope that goes well And yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery And we did get a chance to review your treatment plan How's that sound Good Thanks Yeah this is a good time OK great This will probably last maybe 5 minutes or so maybe even less But you know throughout this conversation just don't hesitate to ask any questions And like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through And as you know we've had a couple steps leading up to today and that involved for example our medical assessment We've had a chance to speak with your care team as well really just to take a look at how your recovery is going So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that Before I go into that did you have any questions about what we've been doing so far No that makes sense I'm I'm curious to know what the next steps are and and you know what the decision is regarding the treatment I'm really happy to go over it and really want to give you as much details as possible on this And basically after our review cycle that we've had we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan We took took a look at some of the progress We took a look at some of the limitations that you've had I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here You're also able to get back to most of your daily activities So I think you mentioned something along the lines of playing soccer You're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here How does that sound OK what do you mean something more active Have you have you had a chance to try kinesiology or any self self-guided training gym programs Any of those before No I think I've seen a sign for it at the clinic I go to but no I haven't Oh fair enough And happy to go over some of those details with you I think there's a couple of things we can definitely do with you and we want to find something that works for you as well Do you have any actually because they're part of the soccer team Do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active Oh actually you know what I think someone on my team might be a kinesiologist themselves Yeah maybe I'll reach out to them I think that's a great idea That's a great start Kind of see what works for them And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery And once you're done that part then we can probably look at discharging the claim How does that sound Did you want to go check in with your teammate And then we can have a conversation about let's say next Thursday Maybe I'll call you around the same time and then we can look at some of those options together Yep that sounds good Next Thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well So before I wrap up here though since you've got me any other questions like anything else I can help you out with No I think that's it for now I'll talk to them and then I'll try to think of any questions before we speak next Thursday Absolutely Fantastic I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job And I think we'll get you to that last step and we'll move forward together on that OK So we'll chat next week then OK Thank you Bye for now",
            "display": "Hi there. I'm calling from ICBC. My name is Eddie. I'm looking for Emily, please. Hey, Emily. Hey, Emily. How are you? I'm OK. How are you? I'm doing pretty good. How How was the oven repair that you had the other day? Did that work out OK? Oh, actually, they weren't able to fix it. And I have to have them come back another day next week. Oh, no. I hope. Hope that goes well. And yeah, well, you know, hopefully it doesn't cost too much or anything, but yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery. And we did get a chance to review your treatment plan. How's that sound? Good. Thanks. Yeah, this is a good time. OK, great. This will probably last maybe 5 minutes or so, maybe even less. But you know, throughout this conversation, just don't hesitate to ask any questions. And like we usually do, but got some interesting news here because we have had a chance to review the treatment that you're going through. And as you know, we've had a couple steps leading up to today and that involved, for example, our medical assessment. We've had a chance to speak with your care team as well, really just to take a look at how your recovery is going. So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that. Before I go into that, did you have any questions about what we've been doing so far? No, that makes sense. I'm, I'm curious to know what the next steps are and and you know what the decision is regarding the treatment. I'm really happy to go over it and really want to give you as much details as possible on this. And basically after our review cycle that we've had, we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan. We took took a look at some of the progress. We took a look at some of the limitations that you've had. I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs, you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here. You're also able to get back to most of your daily activities. So I think you mentioned something along the lines of playing soccer. You're back to playing about 90% of those games and while there is a little bit of pain, you're you're able to go through all of it. So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy. What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you, move you past the passive treatments here. How does that sound OK, what do you mean something more active? Have you, have you had a chance to try kinesiology or any self self-guided training gym programs? Any of those before? No. I think I've seen a sign for it at the clinic I go to, but no, I haven't. Oh, fair enough. And happy to go over some of those details with you. I think there's a couple of things we can definitely do with you and we want to find something that works for you as well. Do you have any actually, because they're part of the soccer team. Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active? Oh, actually, you know what? I think someone on my team might be a kinesiologist themselves. Yeah, maybe I'll reach out to them. I think that's a great idea. That's a great start. Kind of see what works for them. And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step, your recovery. And once you're done that part, then we can probably look at discharging the claim. How does that sound? Did you want to go check in with your teammate? And then we can have a conversation about, let's say, next Thursday. Maybe I'll call you around the same time and then we can look at some of those options together. Yep, that sounds good. Next Thursday works for me, so we can chat, then maybe we'll get some updates and some good news on repairing your oven as well. So before I wrap up here though, since you've got me any other questions like anything else I can help you out with? No, I think that's it for now. I'll talk to them and then I'll try to think of any questions before we speak next Thursday. Absolutely Fantastic. I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job. And I think we'll get you to that last step and we'll move forward together on that. OK. So we'll chat next week then. OK. Thank you. Bye for now."
          },
          {
            "channel": 1,
            "lexical": "hi there i'm calling from ICBC my name is eddie i'm looking for emily please hey emily hey emily how are you i'm OK how are you i'm doing pretty good how how was the oven repair that you had the other day did that work out OK oh actually they weren't able to fix it and i have to have them come back another day next week oh no i hope hope that goes well and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery and we did get a chance to review your treatment plan how's that sound good thanks yeah this is a good time OK great this will probably last maybe five minutes or so maybe even less but you know throughout this conversation just don't hesitate to ask any questions and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through and as you know we've had a couple steps leading up to today and that involved for example our medical assessment we've had a chance to speak with your care team as well really just to take a look at how your recovery is going so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that before i go into that did you have any questions about what we've been doing so far no that makes sense i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment i'm really happy to go over it and really want to give you as much details as possible on this and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan we took took a look at some of the progress we took a look at some of the limitations that you've had i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here you're also able to get back to most of your daily activities so i think you mentioned something along the lines of playing soccer you're back to playing about ninety percent of those games and while there is a little bit of pain you're you're able to go through all of it so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here how does that sound OK what do you mean something more active have you have you had a chance to try kinesiology or any self self guided training gym programs any of those before no i think i've seen a sign for it at the clinic i go to but no i haven't oh fair enough and happy to go over some of those details with you i think there's a couple of things we can definitely do with you and we want to find something that works for you as well do you have any actually because they're part of the soccer team do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active oh actually you know what i think someone on my team might be a kinesiologist themselves yeah maybe i'll reach out to them i think that's a great idea that's a great start kind of see what works for them and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery and once you're done that part then we can probably look at discharging the claim how does that sound did you want to go check in with your teammate and then we can have a conversation about let's say next thursday maybe i'll call you around the same time and then we can look at some of those options together yep that sounds good next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well so before i wrap up here though since you've got me any other questions like anything else i can help you out with no i think that's it for now i'll talk to them and then i'll try to think of any questions before we speak next thursday absolutely fantastic i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job and i think we'll get you to that last step and we'll move forward together on that OK so we'll chat next week then OK thank you bye for now",
            "itn": "hi there i'm calling from ICBC my name is eddie i'm looking for emily please hey emily hey emily how are you i'm OK how are you i'm doing pretty good how how was the oven repair that you had the other day did that work out OK oh actually they weren't able to fix it and i have to have them come back another day next week oh no i hope hope that goes well and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery and we did get a chance to review your treatment plan how's that sound good thanks yeah this is a good time OK great this will probably last maybe 5 minutes or so maybe even less but you know throughout this conversation just don't hesitate to ask any questions and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through and as you know we've had a couple steps leading up to today and that involved for example our medical assessment we've had a chance to speak with your care team as well really just to take a look at how your recovery is going so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that before i go into that did you have any questions about what we've been doing so far no that makes sense i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment i'm really happy to go over it and really want to give you as much details as possible on this and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan we took took a look at some of the progress we took a look at some of the limitations that you've had i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here you're also able to get back to most of your daily activities so i think you mentioned something along the lines of playing soccer you're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here how does that sound OK what do you mean something more active have you have you had a chance to try kinesiology or any self self guided training gym programs any of those before no i think i've seen a sign for it at the clinic i go to but no i haven't oh fair enough and happy to go over some of those details with you i think there's a couple of things we can definitely do with you and we want to find something that works for you as well do you have any actually because they're part of the soccer team do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active oh actually you know what i think someone on my team might be a kinesiologist themselves yeah maybe i'll reach out to them i think that's a great idea that's a great start kind of see what works for them and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery and once you're done that part then we can probably look at discharging the claim how does that sound did you want to go check in with your teammate and then we can have a conversation about let's say next thursday maybe i'll call you around the same time and then we can look at some of those options together yep that sounds good next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well so before i wrap up here though since you've got me any other questions like anything else i can help you out with no i think that's it for now i'll talk to them and then i'll try to think of any questions before we speak next thursday absolutely fantastic i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job and i think we'll get you to that last step and we'll move forward together on that OK so we'll chat next week then OK thank you bye for now",
            "maskedITN": "Hi there I'm calling from ICBC My name is Eddie I'm looking for Emily please Hey Emily Hey Emily How are you I'm OK How are you I'm doing pretty good How How was the oven repair that you had the other day Did that work out OK Oh actually they weren't able to fix it And I have to have them come back another day next week Oh no I hope Hope that goes well And yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery And we did get a chance to review your treatment plan How's that sound Good Thanks Yeah this is a good time OK great This will probably last maybe 5 minutes or so maybe even less But you know throughout this conversation just don't hesitate to ask any questions And like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through And as you know we've had a couple steps leading up to today and that involved for example our medical assessment We've had a chance to speak with your care team as well really just to take a look at how your recovery is going So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that Before I go into that did you have any questions about what we've been doing so far No that makes sense I'm I'm curious to know what the next steps are and and you know what the decision is regarding the treatment I'm really happy to go over it and really want to give you as much details as possible on this And basically after our review cycle that we've had we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan We took took a look at some of the progress We took a look at some of the limitations that you've had I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here You're also able to get back to most of your daily activities So I think you mentioned something along the lines of playing soccer You're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here How does that sound OK what do you mean something more active Have you have you had a chance to try kinesiology or any self self-guided training gym programs Any of those before No I think I've seen a sign for it at the clinic I go to but no I haven't Oh fair enough And happy to go over some of those details with you I think there's a couple of things we can definitely do with you and we want to find something that works for you as well Do you have any actually because they're part of the soccer team Do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active Oh actually you know what I think someone on my team might be a kinesiologist themselves Yeah maybe I'll reach out to them I think that's a great idea That's a great start Kind of see what works for them And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery And once you're done that part then we can probably look at discharging the claim How does that sound Did you want to go check in with your teammate And then we can have a conversation about let's say next Thursday Maybe I'll call you around the same time and then we can look at some of those options together Yep that sounds good Next Thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well So before I wrap up here though since you've got me any other questions like anything else I can help you out with No I think that's it for now I'll talk to them and then I'll try to think of any questions before we speak next Thursday Absolutely Fantastic I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job And I think we'll get you to that last step and we'll move forward together on that OK So we'll chat next week then OK Thank you Bye for now",
            "display": "Hi there. I'm calling from ICBC. My name is Eddie. I'm looking for Emily, please. Hey, Emily. Hey, Emily. How are you? I'm OK. How are you? I'm doing pretty good. How How was the oven repair that you had the other day? Did that work out OK? Oh, actually, they weren't able to fix it. And I have to have them come back another day next week. Oh, no. I hope. Hope that goes well. And yeah, well, you know, hopefully it doesn't cost too much or anything, but yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery. And we did get a chance to review your treatment plan. How's that sound? Good. Thanks. Yeah, this is a good time. OK, great. This will probably last maybe 5 minutes or so, maybe even less. But you know, throughout this conversation, just don't hesitate to ask any questions. And like we usually do, but got some interesting news here because we have had a chance to review the treatment that you're going through. And as you know, we've had a couple steps leading up to today and that involved, for example, our medical assessment. We've had a chance to speak with your care team as well, really just to take a look at how your recovery is going. So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that. Before I go into that, did you have any questions about what we've been doing so far? No, that makes sense. I'm, I'm curious to know what the next steps are and and you know what the decision is regarding the treatment. I'm really happy to go over it and really want to give you as much details as possible on this. And basically after our review cycle that we've had, we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan. We took took a look at some of the progress. We took a look at some of the limitations that you've had. I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs, you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here. You're also able to get back to most of your daily activities. So I think you mentioned something along the lines of playing soccer. You're back to playing about 90% of those games and while there is a little bit of pain, you're you're able to go through all of it. So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy. What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you, move you past the passive treatments here. How does that sound OK, what do you mean something more active? Have you, have you had a chance to try kinesiology or any self self-guided training gym programs? Any of those before? No. I think I've seen a sign for it at the clinic I go to, but no, I haven't. Oh, fair enough. And happy to go over some of those details with you. I think there's a couple of things we can definitely do with you and we want to find something that works for you as well. Do you have any actually, because they're part of the soccer team. Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active? Oh, actually, you know what? I think someone on my team might be a kinesiologist themselves. Yeah, maybe I'll reach out to them. I think that's a great idea. That's a great start. Kind of see what works for them. And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step, your recovery. And once you're done that part, then we can probably look at discharging the claim. How does that sound? Did you want to go check in with your teammate? And then we can have a conversation about, let's say, next Thursday. Maybe I'll call you around the same time and then we can look at some of those options together. Yep, that sounds good. Next Thursday works for me, so we can chat, then maybe we'll get some updates and some good news on repairing your oven as well. So before I wrap up here though, since you've got me any other questions like anything else I can help you out with? No, I think that's it for now. I'll talk to them and then I'll try to think of any questions before we speak next Thursday. Absolutely Fantastic. I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job. And I think we'll get you to that last step and we'll move forward together on that. OK. So we'll chat next week then. OK. Thank you. Bye for now."
          }
        ],
        "recognizedPhrases": [
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3.32S",
            "duration": "PT0.44S",
            "offsetInTicks": 33200000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.81349355,
                "lexical": "hi there",
                "itn": "hi there",
                "maskedITN": "Hi there",
                "display": "Hi there.",
                "sentiment": {
                  "positive": 0.28,
                  "neutral": 0.69,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3.32S",
            "duration": "PT0.44S",
            "offsetInTicks": 33200000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.8230108,
                "lexical": "hi there",
                "itn": "hi there",
                "maskedITN": "Hi there",
                "display": "Hi there.",
                "sentiment": {
                  "positive": 0.28,
                  "neutral": 0.69,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4.16S",
            "duration": "PT1.28S",
            "offsetInTicks": 41600000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.92106175,
                "lexical": "i'm calling from ICBC",
                "itn": "i'm calling from ICBC",
                "maskedITN": "I'm calling from ICBC",
                "display": "I'm calling from ICBC.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4.16S",
            "duration": "PT1.28S",
            "offsetInTicks": 41600000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.92038536,
                "lexical": "i'm calling from ICBC",
                "itn": "i'm calling from ICBC",
                "maskedITN": "I'm calling from ICBC",
                "display": "I'm calling from ICBC.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5.44S",
            "duration": "PT1.16S",
            "offsetInTicks": 54400000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.89736295,
                "lexical": "my name is eddie",
                "itn": "my name is eddie",
                "maskedITN": "My name is Eddie",
                "display": "My name is Eddie.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.99,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5.44S",
            "duration": "PT1.16S",
            "offsetInTicks": 54400000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.8916938,
                "lexical": "my name is eddie",
                "itn": "my name is eddie",
                "maskedITN": "My name is Eddie",
                "display": "My name is Eddie.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.99,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT6.6S",
            "duration": "PT1.68S",
            "offsetInTicks": 66000000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.94199723,
                "lexical": "i'm looking for emily please",
                "itn": "i'm looking for emily please",
                "maskedITN": "I'm looking for Emily please",
                "display": "I'm looking for Emily, please.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.82,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT6.6S",
            "duration": "PT1.68S",
            "offsetInTicks": 66000000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.9471818,
                "lexical": "i'm looking for emily please",
                "itn": "i'm looking for emily please",
                "maskedITN": "I'm looking for Emily please",
                "display": "I'm looking for Emily, please.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.82,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT8.28S",
            "duration": "PT0.96S",
            "offsetInTicks": 82800000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.44572142,
                "lexical": "hey emily",
                "itn": "hey emily",
                "maskedITN": "Hey Emily",
                "display": "Hey, Emily.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.71,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT8.28S",
            "duration": "PT0.96S",
            "offsetInTicks": 82800000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.44201618,
                "lexical": "hey emily",
                "itn": "hey emily",
                "maskedITN": "Hey Emily",
                "display": "Hey, Emily.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.71,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT9.92S",
            "duration": "PT0.48S",
            "offsetInTicks": 99200000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.83228254,
                "lexical": "hey emily",
                "itn": "hey emily",
                "maskedITN": "Hey Emily",
                "display": "Hey, Emily.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.71,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT9.92S",
            "duration": "PT0.48S",
            "offsetInTicks": 99200000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.8158349,
                "lexical": "hey emily",
                "itn": "hey emily",
                "maskedITN": "Hey Emily",
                "display": "Hey, Emily.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.71,
                  "negative": 0.07
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT10.4S",
            "duration": "PT0.44S",
            "offsetInTicks": 104000000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.8978739,
                "lexical": "how are you",
                "itn": "how are you",
                "maskedITN": "How are you",
                "display": "How are you?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.87,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT10.4S",
            "duration": "PT0.44S",
            "offsetInTicks": 104000000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.89300895,
                "lexical": "how are you",
                "itn": "how are you",
                "maskedITN": "How are you",
                "display": "How are you?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.87,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT10.84S",
            "duration": "PT1.12S",
            "offsetInTicks": 108400000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.8949623,
                "lexical": "i'm OK",
                "itn": "i'm OK",
                "maskedITN": "I'm OK",
                "display": "I'm OK.",
                "sentiment": {
                  "positive": 0.2,
                  "neutral": 0.71,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT10.84S",
            "duration": "PT1.12S",
            "offsetInTicks": 108400000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.89185834,
                "lexical": "i'm OK",
                "itn": "i'm OK",
                "maskedITN": "I'm OK",
                "display": "I'm OK.",
                "sentiment": {
                  "positive": 0.2,
                  "neutral": 0.71,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT11.96S",
            "duration": "PT0.36S",
            "offsetInTicks": 119600000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.96575654,
                "lexical": "how are you",
                "itn": "how are you",
                "maskedITN": "How are you",
                "display": "How are you?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.87,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT11.96S",
            "duration": "PT0.36S",
            "offsetInTicks": 119600000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.96596444,
                "lexical": "how are you",
                "itn": "how are you",
                "maskedITN": "How are you",
                "display": "How are you?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.87,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT12.68S",
            "duration": "PT1.04S",
            "offsetInTicks": 126800000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.97041637,
                "lexical": "i'm doing pretty good",
                "itn": "i'm doing pretty good",
                "maskedITN": "I'm doing pretty good",
                "display": "I'm doing pretty good.",
                "sentiment": {
                  "positive": 0.88,
                  "neutral": 0.08,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT12.68S",
            "duration": "PT1.04S",
            "offsetInTicks": 126800000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.97162366,
                "lexical": "i'm doing pretty good",
                "itn": "i'm doing pretty good",
                "maskedITN": "I'm doing pretty good",
                "display": "I'm doing pretty good.",
                "sentiment": {
                  "positive": 0.88,
                  "neutral": 0.08,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT13.72S",
            "duration": "PT3.52S",
            "offsetInTicks": 137200000.0,
            "durationInTicks": 35200000.0,
            "nBest": [
              {
                "confidence": 0.7490126,
                "lexical": "how how was the oven repair that you had the other day",
                "itn": "how how was the oven repair that you had the other day",
                "maskedITN": "How How was the oven repair that you had the other day",
                "display": "How How was the oven repair that you had the other day?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT13.72S",
            "duration": "PT3.52S",
            "offsetInTicks": 137200000.0,
            "durationInTicks": 35200000.0,
            "nBest": [
              {
                "confidence": 0.74584126,
                "lexical": "how how was the oven repair that you had the other day",
                "itn": "how how was the oven repair that you had the other day",
                "maskedITN": "How How was the oven repair that you had the other day",
                "display": "How How was the oven repair that you had the other day?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT17.24S",
            "duration": "PT1.36S",
            "offsetInTicks": 172400000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.9091786,
                "lexical": "did that work out OK",
                "itn": "did that work out OK",
                "maskedITN": "Did that work out OK",
                "display": "Did that work out OK?",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.88,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT17.24S",
            "duration": "PT1.36S",
            "offsetInTicks": 172400000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.90873194,
                "lexical": "did that work out OK",
                "itn": "did that work out OK",
                "maskedITN": "Did that work out OK",
                "display": "Did that work out OK?",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.88,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT18.8S",
            "duration": "PT3.2S",
            "offsetInTicks": 188000000.0,
            "durationInTicks": 32000000.0,
            "nBest": [
              {
                "confidence": 0.91132194,
                "lexical": "oh actually they weren't able to fix it",
                "itn": "oh actually they weren't able to fix it",
                "maskedITN": "Oh actually they weren't able to fix it",
                "display": "Oh, actually, they weren't able to fix it.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.32,
                  "negative": 0.65
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT18.8S",
            "duration": "PT3.2S",
            "offsetInTicks": 188000000.0,
            "durationInTicks": 32000000.0,
            "nBest": [
              {
                "confidence": 0.91272604,
                "lexical": "oh actually they weren't able to fix it",
                "itn": "oh actually they weren't able to fix it",
                "maskedITN": "Oh actually they weren't able to fix it",
                "display": "Oh, actually, they weren't able to fix it.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.32,
                  "negative": 0.65
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT22S",
            "duration": "PT2.2S",
            "offsetInTicks": 220000000.0,
            "durationInTicks": 22000000.0,
            "nBest": [
              {
                "confidence": 0.93837845,
                "lexical": "and i have to have them come back another day next week",
                "itn": "and i have to have them come back another day next week",
                "maskedITN": "And I have to have them come back another day next week",
                "display": "And I have to have them come back another day next week.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT22S",
            "duration": "PT2.2S",
            "offsetInTicks": 220000000.0,
            "durationInTicks": 22000000.0,
            "nBest": [
              {
                "confidence": 0.9373839,
                "lexical": "and i have to have them come back another day next week",
                "itn": "and i have to have them come back another day next week",
                "maskedITN": "And I have to have them come back another day next week",
                "display": "And I have to have them come back another day next week.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT24.48S",
            "duration": "PT0.48S",
            "offsetInTicks": 244800000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.8015369,
                "lexical": "oh no",
                "itn": "oh no",
                "maskedITN": "Oh no",
                "display": "Oh, no.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.39,
                  "negative": 0.52
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT24.48S",
            "duration": "PT0.48S",
            "offsetInTicks": 244800000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.7938294,
                "lexical": "oh no",
                "itn": "oh no",
                "maskedITN": "Oh no",
                "display": "Oh, no.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.39,
                  "negative": 0.52
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT24.96S",
            "duration": "PT0.24S",
            "offsetInTicks": 249600000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.8572207,
                "lexical": "i hope",
                "itn": "i hope",
                "maskedITN": "I hope",
                "display": "I hope.",
                "sentiment": {
                  "positive": 0.81,
                  "neutral": 0.17,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT24.96S",
            "duration": "PT0.24S",
            "offsetInTicks": 249600000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.85957783,
                "lexical": "i hope",
                "itn": "i hope",
                "maskedITN": "I hope",
                "display": "I hope.",
                "sentiment": {
                  "positive": 0.81,
                  "neutral": 0.17,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT25.32S",
            "duration": "PT0.96S",
            "offsetInTicks": 253200000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.8843232,
                "lexical": "hope that goes well",
                "itn": "hope that goes well",
                "maskedITN": "Hope that goes well",
                "display": "Hope that goes well.",
                "sentiment": {
                  "positive": 0.92,
                  "neutral": 0.07,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT25.32S",
            "duration": "PT0.96S",
            "offsetInTicks": 253200000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.88074994,
                "lexical": "hope that goes well",
                "itn": "hope that goes well",
                "maskedITN": "Hope that goes well",
                "display": "Hope that goes well.",
                "sentiment": {
                  "positive": 0.92,
                  "neutral": 0.07,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT26.28S",
            "duration": "PT8.64S",
            "offsetInTicks": 262800000.0,
            "durationInTicks": 86400000.0,
            "nBest": [
              {
                "confidence": 0.90997005,
                "lexical": "and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery",
                "itn": "and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery",
                "maskedITN": "And yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery",
                "display": "And yeah, well, you know, hopefully it doesn't cost too much or anything, but yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery.",
                "sentiment": {
                  "positive": 0.32,
                  "neutral": 0.6,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT26.28S",
            "duration": "PT8.64S",
            "offsetInTicks": 262800000.0,
            "durationInTicks": 86400000.0,
            "nBest": [
              {
                "confidence": 0.9099816,
                "lexical": "and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery",
                "itn": "and yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery",
                "maskedITN": "And yeah well you know hopefully it doesn't cost too much or anything but yeah hopefully you have a couple of minutes and let's just chat about part of your recovery",
                "display": "And yeah, well, you know, hopefully it doesn't cost too much or anything, but yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery.",
                "sentiment": {
                  "positive": 0.32,
                  "neutral": 0.6,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT34.92S",
            "duration": "PT1.96S",
            "offsetInTicks": 349200000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.96519625,
                "lexical": "and we did get a chance to review your treatment plan",
                "itn": "and we did get a chance to review your treatment plan",
                "maskedITN": "And we did get a chance to review your treatment plan",
                "display": "And we did get a chance to review your treatment plan.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT34.92S",
            "duration": "PT1.96S",
            "offsetInTicks": 349200000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.96519625,
                "lexical": "and we did get a chance to review your treatment plan",
                "itn": "and we did get a chance to review your treatment plan",
                "maskedITN": "And we did get a chance to review your treatment plan",
                "display": "And we did get a chance to review your treatment plan.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT36.88S",
            "duration": "PT0.6S",
            "offsetInTicks": 368800000.0,
            "durationInTicks": 6000000.0,
            "nBest": [
              {
                "confidence": 0.70561373,
                "lexical": "how's that sound",
                "itn": "how's that sound",
                "maskedITN": "How's that sound",
                "display": "How's that sound?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.93,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT36.88S",
            "duration": "PT0.6S",
            "offsetInTicks": 368800000.0,
            "durationInTicks": 6000000.0,
            "nBest": [
              {
                "confidence": 0.70561373,
                "lexical": "how's that sound",
                "itn": "how's that sound",
                "maskedITN": "How's that sound",
                "display": "How's that sound?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.93,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT37.48S",
            "duration": "PT0.12S",
            "offsetInTicks": 374800000.0,
            "durationInTicks": 1200000.0,
            "nBest": [
              {
                "confidence": 0.19165847,
                "lexical": "good",
                "itn": "good",
                "maskedITN": "Good",
                "display": "Good.",
                "sentiment": {
                  "positive": 0.89,
                  "neutral": 0.09,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT37.48S",
            "duration": "PT0.12S",
            "offsetInTicks": 374800000.0,
            "durationInTicks": 1200000.0,
            "nBest": [
              {
                "confidence": 0.19165847,
                "lexical": "good",
                "itn": "good",
                "maskedITN": "Good",
                "display": "Good.",
                "sentiment": {
                  "positive": 0.89,
                  "neutral": 0.09,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT38.44S",
            "duration": "PT0.24S",
            "offsetInTicks": 384400000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.9337251,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT38.44S",
            "duration": "PT0.24S",
            "offsetInTicks": 384400000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.9337251,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT39.04S",
            "duration": "PT1S",
            "offsetInTicks": 390400000.0,
            "durationInTicks": 10000000.0,
            "nBest": [
              {
                "confidence": 0.81188375,
                "lexical": "yeah this is a good time",
                "itn": "yeah this is a good time",
                "maskedITN": "Yeah this is a good time",
                "display": "Yeah, this is a good time.",
                "sentiment": {
                  "positive": 0.74,
                  "neutral": 0.22,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT39.04S",
            "duration": "PT1S",
            "offsetInTicks": 390400000.0,
            "durationInTicks": 10000000.0,
            "nBest": [
              {
                "confidence": 0.81188375,
                "lexical": "yeah this is a good time",
                "itn": "yeah this is a good time",
                "maskedITN": "Yeah this is a good time",
                "display": "Yeah, this is a good time.",
                "sentiment": {
                  "positive": 0.74,
                  "neutral": 0.22,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT40.12S",
            "duration": "PT0.64S",
            "offsetInTicks": 401200000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.95147717,
                "lexical": "OK great",
                "itn": "OK great",
                "maskedITN": "OK great",
                "display": "OK, great.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT40.12S",
            "duration": "PT0.64S",
            "offsetInTicks": 401200000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.95147717,
                "lexical": "OK great",
                "itn": "OK great",
                "maskedITN": "OK great",
                "display": "OK, great.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT40.76S",
            "duration": "PT4.12S",
            "offsetInTicks": 407600000.0,
            "durationInTicks": 41200000.0,
            "nBest": [
              {
                "confidence": 0.906721,
                "lexical": "this will probably last maybe five minutes or so maybe even less",
                "itn": "this will probably last maybe 5 minutes or so maybe even less",
                "maskedITN": "This will probably last maybe 5 minutes or so maybe even less",
                "display": "This will probably last maybe 5 minutes or so, maybe even less.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT40.76S",
            "duration": "PT4.12S",
            "offsetInTicks": 407600000.0,
            "durationInTicks": 41200000.0,
            "nBest": [
              {
                "confidence": 0.906721,
                "lexical": "this will probably last maybe five minutes or so maybe even less",
                "itn": "this will probably last maybe 5 minutes or so maybe even less",
                "maskedITN": "This will probably last maybe 5 minutes or so maybe even less",
                "display": "This will probably last maybe 5 minutes or so, maybe even less.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT44.88S",
            "duration": "PT3.84S",
            "offsetInTicks": 448800000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.96632344,
                "lexical": "but you know throughout this conversation just don't hesitate to ask any questions",
                "itn": "but you know throughout this conversation just don't hesitate to ask any questions",
                "maskedITN": "But you know throughout this conversation just don't hesitate to ask any questions",
                "display": "But you know, throughout this conversation, just don't hesitate to ask any questions.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.87,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT44.88S",
            "duration": "PT3.84S",
            "offsetInTicks": 448800000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.96632344,
                "lexical": "but you know throughout this conversation just don't hesitate to ask any questions",
                "itn": "but you know throughout this conversation just don't hesitate to ask any questions",
                "maskedITN": "But you know throughout this conversation just don't hesitate to ask any questions",
                "display": "But you know, throughout this conversation, just don't hesitate to ask any questions.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.87,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT48.72S",
            "duration": "PT8.04S",
            "offsetInTicks": 487200000.0,
            "durationInTicks": 80400000.0,
            "nBest": [
              {
                "confidence": 0.9381969,
                "lexical": "and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through",
                "itn": "and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through",
                "maskedITN": "And like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through",
                "display": "And like we usually do, but got some interesting news here because we have had a chance to review the treatment that you're going through.",
                "sentiment": {
                  "positive": 0.78,
                  "neutral": 0.18,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT48.72S",
            "duration": "PT8.04S",
            "offsetInTicks": 487200000.0,
            "durationInTicks": 80400000.0,
            "nBest": [
              {
                "confidence": 0.9381969,
                "lexical": "and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through",
                "itn": "and like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through",
                "maskedITN": "And like we usually do but got some interesting news here because we have had a chance to review the treatment that you're going through",
                "display": "And like we usually do, but got some interesting news here because we have had a chance to review the treatment that you're going through.",
                "sentiment": {
                  "positive": 0.78,
                  "neutral": 0.18,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT56.76S",
            "duration": "PT7.36S",
            "offsetInTicks": 567600000.0,
            "durationInTicks": 73600000.0,
            "nBest": [
              {
                "confidence": 0.9289378,
                "lexical": "and as you know we've had a couple steps leading up to today and that involved for example our medical assessment",
                "itn": "and as you know we've had a couple steps leading up to today and that involved for example our medical assessment",
                "maskedITN": "And as you know we've had a couple steps leading up to today and that involved for example our medical assessment",
                "display": "And as you know, we've had a couple steps leading up to today and that involved, for example, our medical assessment.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT56.76S",
            "duration": "PT7.36S",
            "offsetInTicks": 567600000.0,
            "durationInTicks": 73600000.0,
            "nBest": [
              {
                "confidence": 0.9289378,
                "lexical": "and as you know we've had a couple steps leading up to today and that involved for example our medical assessment",
                "itn": "and as you know we've had a couple steps leading up to today and that involved for example our medical assessment",
                "maskedITN": "And as you know we've had a couple steps leading up to today and that involved for example our medical assessment",
                "display": "And as you know, we've had a couple steps leading up to today and that involved, for example, our medical assessment.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M4.6S",
            "duration": "PT5.88S",
            "offsetInTicks": 646000000.0,
            "durationInTicks": 58800000.0,
            "nBest": [
              {
                "confidence": 0.8743496,
                "lexical": "we've had a chance to speak with your care team as well really just to take a look at how your recovery is going",
                "itn": "we've had a chance to speak with your care team as well really just to take a look at how your recovery is going",
                "maskedITN": "We've had a chance to speak with your care team as well really just to take a look at how your recovery is going",
                "display": "We've had a chance to speak with your care team as well, really just to take a look at how your recovery is going.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.75,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M4.6S",
            "duration": "PT5.88S",
            "offsetInTicks": 646000000.0,
            "durationInTicks": 58800000.0,
            "nBest": [
              {
                "confidence": 0.8743496,
                "lexical": "we've had a chance to speak with your care team as well really just to take a look at how your recovery is going",
                "itn": "we've had a chance to speak with your care team as well really just to take a look at how your recovery is going",
                "maskedITN": "We've had a chance to speak with your care team as well really just to take a look at how your recovery is going",
                "display": "We've had a chance to speak with your care team as well, really just to take a look at how your recovery is going.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.75,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M10.48S",
            "duration": "PT8.92S",
            "offsetInTicks": 704800000.0,
            "durationInTicks": 89200000.0,
            "nBest": [
              {
                "confidence": 0.92158234,
                "lexical": "so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that",
                "itn": "so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that",
                "maskedITN": "So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that",
                "display": "So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that.",
                "sentiment": {
                  "positive": 0.12,
                  "neutral": 0.87,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M10.48S",
            "duration": "PT8.92S",
            "offsetInTicks": 704800000.0,
            "durationInTicks": 89200000.0,
            "nBest": [
              {
                "confidence": 0.92158234,
                "lexical": "so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that",
                "itn": "so just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that",
                "maskedITN": "So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that",
                "display": "So just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that.",
                "sentiment": {
                  "positive": 0.12,
                  "neutral": 0.87,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M19.88S",
            "duration": "PT3.44S",
            "offsetInTicks": 798800000.0,
            "durationInTicks": 34400000.0,
            "nBest": [
              {
                "confidence": 0.9409067,
                "lexical": "before i go into that did you have any questions about what we've been doing so far",
                "itn": "before i go into that did you have any questions about what we've been doing so far",
                "maskedITN": "Before I go into that did you have any questions about what we've been doing so far",
                "display": "Before I go into that, did you have any questions about what we've been doing so far?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M19.88S",
            "duration": "PT3.44S",
            "offsetInTicks": 798800000.0,
            "durationInTicks": 34400000.0,
            "nBest": [
              {
                "confidence": 0.9409067,
                "lexical": "before i go into that did you have any questions about what we've been doing so far",
                "itn": "before i go into that did you have any questions about what we've been doing so far",
                "maskedITN": "Before I go into that did you have any questions about what we've been doing so far",
                "display": "Before I go into that, did you have any questions about what we've been doing so far?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M24.76S",
            "duration": "PT0.92S",
            "offsetInTicks": 847600000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.9332143,
                "lexical": "no that makes sense",
                "itn": "no that makes sense",
                "maskedITN": "No that makes sense",
                "display": "No, that makes sense.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.73,
                  "negative": 0.14
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M24.76S",
            "duration": "PT0.92S",
            "offsetInTicks": 847600000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.9332143,
                "lexical": "no that makes sense",
                "itn": "no that makes sense",
                "maskedITN": "No that makes sense",
                "display": "No, that makes sense.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.73,
                  "negative": 0.14
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M25.68S",
            "duration": "PT5.76S",
            "offsetInTicks": 856800000.0,
            "durationInTicks": 57600000.0,
            "nBest": [
              {
                "confidence": 0.8617998,
                "lexical": "i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment",
                "itn": "i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment",
                "maskedITN": "I'm I'm curious to know what the next steps are and and you know what the decision is regarding the treatment",
                "display": "I'm, I'm curious to know what the next steps are and and you know what the decision is regarding the treatment.",
                "sentiment": {
                  "positive": 0.29,
                  "neutral": 0.66,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M25.68S",
            "duration": "PT5.76S",
            "offsetInTicks": 856800000.0,
            "durationInTicks": 57600000.0,
            "nBest": [
              {
                "confidence": 0.8617998,
                "lexical": "i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment",
                "itn": "i'm i'm curious to know what the next steps are and and you know what the decision is regarding the treatment",
                "maskedITN": "I'm I'm curious to know what the next steps are and and you know what the decision is regarding the treatment",
                "display": "I'm, I'm curious to know what the next steps are and and you know what the decision is regarding the treatment.",
                "sentiment": {
                  "positive": 0.29,
                  "neutral": 0.66,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M32.68S",
            "duration": "PT4.8S",
            "offsetInTicks": 926800000.0,
            "durationInTicks": 48000000.0,
            "nBest": [
              {
                "confidence": 0.8115089,
                "lexical": "i'm really happy to go over it and really want to give you as much details as possible on this",
                "itn": "i'm really happy to go over it and really want to give you as much details as possible on this",
                "maskedITN": "I'm really happy to go over it and really want to give you as much details as possible on this",
                "display": "I'm really happy to go over it and really want to give you as much details as possible on this.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M32.68S",
            "duration": "PT4.8S",
            "offsetInTicks": 926800000.0,
            "durationInTicks": 48000000.0,
            "nBest": [
              {
                "confidence": 0.8115089,
                "lexical": "i'm really happy to go over it and really want to give you as much details as possible on this",
                "itn": "i'm really happy to go over it and really want to give you as much details as possible on this",
                "maskedITN": "I'm really happy to go over it and really want to give you as much details as possible on this",
                "display": "I'm really happy to go over it and really want to give you as much details as possible on this.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M37.48S",
            "duration": "PT13.4S",
            "offsetInTicks": 974800000.0,
            "durationInTicks": 134000000.0,
            "nBest": [
              {
                "confidence": 0.8444158,
                "lexical": "and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan",
                "itn": "and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan",
                "maskedITN": "And basically after our review cycle that we've had we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan",
                "display": "And basically after our review cycle that we've had, we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M37.48S",
            "duration": "PT13.4S",
            "offsetInTicks": 974800000.0,
            "durationInTicks": 134000000.0,
            "nBest": [
              {
                "confidence": 0.8444158,
                "lexical": "and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan",
                "itn": "and basically after our review cycle that we've had we've had the medical assessments like i mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan",
                "maskedITN": "And basically after our review cycle that we've had we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan",
                "display": "And basically after our review cycle that we've had, we've had the medical assessments like I mentioned and then talked with the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M51.16S",
            "duration": "PT2.16S",
            "offsetInTicks": 1111600000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.93368095,
                "lexical": "we took took a look at some of the progress",
                "itn": "we took took a look at some of the progress",
                "maskedITN": "We took took a look at some of the progress",
                "display": "We took took a look at some of the progress.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M51.16S",
            "duration": "PT2.16S",
            "offsetInTicks": 1111600000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.93368095,
                "lexical": "we took took a look at some of the progress",
                "itn": "we took took a look at some of the progress",
                "maskedITN": "We took took a look at some of the progress",
                "display": "We took took a look at some of the progress.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M53.8S",
            "duration": "PT3.12S",
            "offsetInTicks": 1138000000.0,
            "durationInTicks": 31200000.0,
            "nBest": [
              {
                "confidence": 0.92751527,
                "lexical": "we took a look at some of the limitations that you've had",
                "itn": "we took a look at some of the limitations that you've had",
                "maskedITN": "We took a look at some of the limitations that you've had",
                "display": "We took a look at some of the limitations that you've had.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M53.8S",
            "duration": "PT3.12S",
            "offsetInTicks": 1138000000.0,
            "durationInTicks": 31200000.0,
            "nBest": [
              {
                "confidence": 0.92751527,
                "lexical": "we took a look at some of the limitations that you've had",
                "itn": "we took a look at some of the limitations that you've had",
                "maskedITN": "We took a look at some of the limitations that you've had",
                "display": "We took a look at some of the limitations that you've had.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M57.16S",
            "duration": "PT15.24S",
            "offsetInTicks": 1171600000.0,
            "durationInTicks": 152400000.0,
            "nBest": [
              {
                "confidence": 0.89816296,
                "lexical": "i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here",
                "itn": "i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here",
                "maskedITN": "I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here",
                "display": "I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs, you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.65,
                  "negative": 0.31
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M57.16S",
            "duration": "PT15.24S",
            "offsetInTicks": 1171600000.0,
            "durationInTicks": 152400000.0,
            "nBest": [
              {
                "confidence": 0.89816296,
                "lexical": "i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here",
                "itn": "i think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here",
                "maskedITN": "I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here",
                "display": "I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs, you also had some challenges with raising your arm up above your shoulder and a lot of that has resolved based on what we can see here.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.65,
                  "negative": 0.31
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M13.04S",
            "duration": "PT3.04S",
            "offsetInTicks": 1330400000.0,
            "durationInTicks": 30400000.0,
            "nBest": [
              {
                "confidence": 0.92403567,
                "lexical": "you're also able to get back to most of your daily activities",
                "itn": "you're also able to get back to most of your daily activities",
                "maskedITN": "You're also able to get back to most of your daily activities",
                "display": "You're also able to get back to most of your daily activities.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M13.04S",
            "duration": "PT3.04S",
            "offsetInTicks": 1330400000.0,
            "durationInTicks": 30400000.0,
            "nBest": [
              {
                "confidence": 0.92403567,
                "lexical": "you're also able to get back to most of your daily activities",
                "itn": "you're also able to get back to most of your daily activities",
                "maskedITN": "You're also able to get back to most of your daily activities",
                "display": "You're also able to get back to most of your daily activities.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M16.08S",
            "duration": "PT3.76S",
            "offsetInTicks": 1360800000.0,
            "durationInTicks": 37600000.0,
            "nBest": [
              {
                "confidence": 0.9552022,
                "lexical": "so i think you mentioned something along the lines of playing soccer",
                "itn": "so i think you mentioned something along the lines of playing soccer",
                "maskedITN": "So I think you mentioned something along the lines of playing soccer",
                "display": "So I think you mentioned something along the lines of playing soccer.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M16.08S",
            "duration": "PT3.76S",
            "offsetInTicks": 1360800000.0,
            "durationInTicks": 37600000.0,
            "nBest": [
              {
                "confidence": 0.9552022,
                "lexical": "so i think you mentioned something along the lines of playing soccer",
                "itn": "so i think you mentioned something along the lines of playing soccer",
                "maskedITN": "So I think you mentioned something along the lines of playing soccer",
                "display": "So I think you mentioned something along the lines of playing soccer.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M20.08S",
            "duration": "PT8.12S",
            "offsetInTicks": 1400800000.0,
            "durationInTicks": 81200000.0,
            "nBest": [
              {
                "confidence": 0.8933797,
                "lexical": "you're back to playing about ninety percent of those games and while there is a little bit of pain you're you're able to go through all of it",
                "itn": "you're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it",
                "maskedITN": "You're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it",
                "display": "You're back to playing about 90% of those games and while there is a little bit of pain, you're you're able to go through all of it.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.59,
                  "negative": 0.34
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M20.08S",
            "duration": "PT8.12S",
            "offsetInTicks": 1400800000.0,
            "durationInTicks": 81200000.0,
            "nBest": [
              {
                "confidence": 0.8933797,
                "lexical": "you're back to playing about ninety percent of those games and while there is a little bit of pain you're you're able to go through all of it",
                "itn": "you're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it",
                "maskedITN": "You're back to playing about 90% of those games and while there is a little bit of pain you're you're able to go through all of it",
                "display": "You're back to playing about 90% of those games and while there is a little bit of pain, you're you're able to go through all of it.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.59,
                  "negative": 0.34
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M28.2S",
            "duration": "PT7.64S",
            "offsetInTicks": 1482000000.0,
            "durationInTicks": 76400000.0,
            "nBest": [
              {
                "confidence": 0.8891242,
                "lexical": "so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy",
                "itn": "so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy",
                "maskedITN": "So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy",
                "display": "So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.81,
                  "negative": 0.18
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M28.2S",
            "duration": "PT7.64S",
            "offsetInTicks": 1482000000.0,
            "durationInTicks": 76400000.0,
            "nBest": [
              {
                "confidence": 0.8891242,
                "lexical": "so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy",
                "itn": "so reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy",
                "maskedITN": "So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy",
                "display": "So reviewing all the information there at this point it doesn't look like we can approve further treatment for your physiotherapy.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.81,
                  "negative": 0.18
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M36.64S",
            "duration": "PT11.88S",
            "offsetInTicks": 1566400000.0,
            "durationInTicks": 118800000.0,
            "nBest": [
              {
                "confidence": 0.9004195,
                "lexical": "what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here",
                "itn": "what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here",
                "maskedITN": "What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here",
                "display": "What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you, move you past the passive treatments here.",
                "sentiment": {
                  "positive": 0.45,
                  "neutral": 0.53,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M36.64S",
            "duration": "PT11.88S",
            "offsetInTicks": 1566400000.0,
            "durationInTicks": 118800000.0,
            "nBest": [
              {
                "confidence": 0.9004195,
                "lexical": "what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here",
                "itn": "what we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here",
                "maskedITN": "What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you move you past the passive treatments here",
                "display": "What we can do and and offer is to help get you into something more active just to really help you get to that next level of your recovery and move you, move you past the passive treatments here.",
                "sentiment": {
                  "positive": 0.45,
                  "neutral": 0.53,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M48.52S",
            "duration": "PT3.2S",
            "offsetInTicks": 1685200000.0,
            "durationInTicks": 32000000.0,
            "nBest": [
              {
                "confidence": 0.951758,
                "lexical": "how does that sound OK what do you mean something more active",
                "itn": "how does that sound OK what do you mean something more active",
                "maskedITN": "How does that sound OK what do you mean something more active",
                "display": "How does that sound OK, what do you mean something more active?",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M48.52S",
            "duration": "PT3.2S",
            "offsetInTicks": 1685200000.0,
            "durationInTicks": 32000000.0,
            "nBest": [
              {
                "confidence": 0.951758,
                "lexical": "how does that sound OK what do you mean something more active",
                "itn": "how does that sound OK what do you mean something more active",
                "maskedITN": "How does that sound OK what do you mean something more active",
                "display": "How does that sound OK, what do you mean something more active?",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M53S",
            "duration": "PT8.88S",
            "offsetInTicks": 1730000000.0,
            "durationInTicks": 88800000.0,
            "nBest": [
              {
                "confidence": 0.90184844,
                "lexical": "have you have you had a chance to try kinesiology or any self self guided training gym programs",
                "itn": "have you have you had a chance to try kinesiology or any self self guided training gym programs",
                "maskedITN": "Have you have you had a chance to try kinesiology or any self self-guided training gym programs",
                "display": "Have you, have you had a chance to try kinesiology or any self self-guided training gym programs?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M53S",
            "duration": "PT8.88S",
            "offsetInTicks": 1730000000.0,
            "durationInTicks": 88800000.0,
            "nBest": [
              {
                "confidence": 0.90184844,
                "lexical": "have you have you had a chance to try kinesiology or any self self guided training gym programs",
                "itn": "have you have you had a chance to try kinesiology or any self self guided training gym programs",
                "maskedITN": "Have you have you had a chance to try kinesiology or any self self-guided training gym programs",
                "display": "Have you, have you had a chance to try kinesiology or any self self-guided training gym programs?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M1.88S",
            "duration": "PT0.92S",
            "offsetInTicks": 1818800000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.96467376,
                "lexical": "any of those before",
                "itn": "any of those before",
                "maskedITN": "Any of those before",
                "display": "Any of those before?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M1.88S",
            "duration": "PT0.92S",
            "offsetInTicks": 1818800000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.96467376,
                "lexical": "any of those before",
                "itn": "any of those before",
                "maskedITN": "Any of those before",
                "display": "Any of those before?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M3.76S",
            "duration": "PT0.32S",
            "offsetInTicks": 1837600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.62570566,
                "lexical": "no",
                "itn": "no",
                "maskedITN": "No",
                "display": "No.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.75,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M3.76S",
            "duration": "PT0.32S",
            "offsetInTicks": 1837600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.62570566,
                "lexical": "no",
                "itn": "no",
                "maskedITN": "No",
                "display": "No.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.75,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M4.08S",
            "duration": "PT3.96S",
            "offsetInTicks": 1840800000.0,
            "durationInTicks": 39600000.0,
            "nBest": [
              {
                "confidence": 0.9545978,
                "lexical": "i think i've seen a sign for it at the clinic i go to but no i haven't",
                "itn": "i think i've seen a sign for it at the clinic i go to but no i haven't",
                "maskedITN": "I think I've seen a sign for it at the clinic I go to but no I haven't",
                "display": "I think I've seen a sign for it at the clinic I go to, but no, I haven't.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.9,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M4.08S",
            "duration": "PT3.96S",
            "offsetInTicks": 1840800000.0,
            "durationInTicks": 39600000.0,
            "nBest": [
              {
                "confidence": 0.9545978,
                "lexical": "i think i've seen a sign for it at the clinic i go to but no i haven't",
                "itn": "i think i've seen a sign for it at the clinic i go to but no i haven't",
                "maskedITN": "I think I've seen a sign for it at the clinic I go to but no I haven't",
                "display": "I think I've seen a sign for it at the clinic I go to, but no, I haven't.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.9,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M9.96S",
            "duration": "PT0.56S",
            "offsetInTicks": 1899600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.6687399,
                "lexical": "oh fair enough",
                "itn": "oh fair enough",
                "maskedITN": "Oh fair enough",
                "display": "Oh, fair enough.",
                "sentiment": {
                  "positive": 0.47,
                  "neutral": 0.43,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M9.96S",
            "duration": "PT0.56S",
            "offsetInTicks": 1899600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.6687399,
                "lexical": "oh fair enough",
                "itn": "oh fair enough",
                "maskedITN": "Oh fair enough",
                "display": "Oh, fair enough.",
                "sentiment": {
                  "positive": 0.47,
                  "neutral": 0.43,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M10.52S",
            "duration": "PT2.16S",
            "offsetInTicks": 1905200000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.8952531,
                "lexical": "and happy to go over some of those details with you",
                "itn": "and happy to go over some of those details with you",
                "maskedITN": "And happy to go over some of those details with you",
                "display": "And happy to go over some of those details with you.",
                "sentiment": {
                  "positive": 0.89,
                  "neutral": 0.1,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M10.52S",
            "duration": "PT2.16S",
            "offsetInTicks": 1905200000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.8952531,
                "lexical": "and happy to go over some of those details with you",
                "itn": "and happy to go over some of those details with you",
                "maskedITN": "And happy to go over some of those details with you",
                "display": "And happy to go over some of those details with you.",
                "sentiment": {
                  "positive": 0.89,
                  "neutral": 0.1,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M12.68S",
            "duration": "PT4.76S",
            "offsetInTicks": 1926800000.0,
            "durationInTicks": 47600000.0,
            "nBest": [
              {
                "confidence": 0.8641874,
                "lexical": "i think there's a couple of things we can definitely do with you and we want to find something that works for you as well",
                "itn": "i think there's a couple of things we can definitely do with you and we want to find something that works for you as well",
                "maskedITN": "I think there's a couple of things we can definitely do with you and we want to find something that works for you as well",
                "display": "I think there's a couple of things we can definitely do with you and we want to find something that works for you as well.",
                "sentiment": {
                  "positive": 0.33,
                  "neutral": 0.63,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M12.68S",
            "duration": "PT4.76S",
            "offsetInTicks": 1926800000.0,
            "durationInTicks": 47600000.0,
            "nBest": [
              {
                "confidence": 0.8641874,
                "lexical": "i think there's a couple of things we can definitely do with you and we want to find something that works for you as well",
                "itn": "i think there's a couple of things we can definitely do with you and we want to find something that works for you as well",
                "maskedITN": "I think there's a couple of things we can definitely do with you and we want to find something that works for you as well",
                "display": "I think there's a couple of things we can definitely do with you and we want to find something that works for you as well.",
                "sentiment": {
                  "positive": 0.33,
                  "neutral": 0.63,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M18.6S",
            "duration": "PT2.72S",
            "offsetInTicks": 1986000000.0,
            "durationInTicks": 27200000.0,
            "nBest": [
              {
                "confidence": 0.90156263,
                "lexical": "do you have any actually because they're part of the soccer team",
                "itn": "do you have any actually because they're part of the soccer team",
                "maskedITN": "Do you have any actually because they're part of the soccer team",
                "display": "Do you have any actually, because they're part of the soccer team.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M18.6S",
            "duration": "PT2.72S",
            "offsetInTicks": 1986000000.0,
            "durationInTicks": 27200000.0,
            "nBest": [
              {
                "confidence": 0.90156263,
                "lexical": "do you have any actually because they're part of the soccer team",
                "itn": "do you have any actually because they're part of the soccer team",
                "maskedITN": "Do you have any actually because they're part of the soccer team",
                "display": "Do you have any actually, because they're part of the soccer team.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M21.68S",
            "duration": "PT7.84S",
            "offsetInTicks": 2016800000.0,
            "durationInTicks": 78400000.0,
            "nBest": [
              {
                "confidence": 0.92210555,
                "lexical": "do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active",
                "itn": "do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active",
                "maskedITN": "Do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active",
                "display": "Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M21.68S",
            "duration": "PT7.84S",
            "offsetInTicks": 2016800000.0,
            "durationInTicks": 78400000.0,
            "nBest": [
              {
                "confidence": 0.92210555,
                "lexical": "do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active",
                "itn": "do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active",
                "maskedITN": "Do you know anyone on your team that you might want to ask about what might work for you in terms of you know transitioning from physiotherapy to something more active",
                "display": "Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M30.12S",
            "duration": "PT0.92S",
            "offsetInTicks": 2101200000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.8516543,
                "lexical": "oh actually you know what",
                "itn": "oh actually you know what",
                "maskedITN": "Oh actually you know what",
                "display": "Oh, actually, you know what?",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.75,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M30.12S",
            "duration": "PT0.88S",
            "offsetInTicks": 2101200000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.829182,
                "lexical": "oh actually you know what",
                "itn": "oh actually you know what",
                "maskedITN": "Oh actually you know what",
                "display": "Oh, actually, you know what?",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.75,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M31S",
            "duration": "PT3.96S",
            "offsetInTicks": 2110000000.0,
            "durationInTicks": 39600000.0,
            "nBest": [
              {
                "confidence": 0.89706814,
                "lexical": "i think someone on my team might be a kinesiologist themselves",
                "itn": "i think someone on my team might be a kinesiologist themselves",
                "maskedITN": "I think someone on my team might be a kinesiologist themselves",
                "display": "I think someone on my team might be a kinesiologist themselves.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M31.04S",
            "duration": "PT3.92S",
            "offsetInTicks": 2110400000.0,
            "durationInTicks": 39200000.0,
            "nBest": [
              {
                "confidence": 0.88216424,
                "lexical": "i think someone on my team might be a kinesiologist themselves",
                "itn": "i think someone on my team might be a kinesiologist themselves",
                "maskedITN": "I think someone on my team might be a kinesiologist themselves",
                "display": "I think someone on my team might be a kinesiologist themselves.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M34.96S",
            "duration": "PT1.36S",
            "offsetInTicks": 2149600000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.9697123,
                "lexical": "yeah maybe i'll reach out to them",
                "itn": "yeah maybe i'll reach out to them",
                "maskedITN": "Yeah maybe I'll reach out to them",
                "display": "Yeah, maybe I'll reach out to them.",
                "sentiment": {
                  "positive": 0.27,
                  "neutral": 0.7,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M34.96S",
            "duration": "PT1.36S",
            "offsetInTicks": 2149600000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.96814376,
                "lexical": "yeah maybe i'll reach out to them",
                "itn": "yeah maybe i'll reach out to them",
                "maskedITN": "Yeah maybe I'll reach out to them",
                "display": "Yeah, maybe I'll reach out to them.",
                "sentiment": {
                  "positive": 0.27,
                  "neutral": 0.7,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M36.32S",
            "duration": "PT1.68S",
            "offsetInTicks": 2163200000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.8456946,
                "lexical": "i think that's a great idea",
                "itn": "i think that's a great idea",
                "maskedITN": "I think that's a great idea",
                "display": "I think that's a great idea.",
                "sentiment": {
                  "positive": 0.92,
                  "neutral": 0.07,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M36.32S",
            "duration": "PT1.68S",
            "offsetInTicks": 2163200000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.8238768,
                "lexical": "i think that's a great idea",
                "itn": "i think that's a great idea",
                "maskedITN": "I think that's a great idea",
                "display": "I think that's a great idea.",
                "sentiment": {
                  "positive": 0.92,
                  "neutral": 0.07,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M38S",
            "duration": "PT0.84S",
            "offsetInTicks": 2180000000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.8716016,
                "lexical": "that's a great start",
                "itn": "that's a great start",
                "maskedITN": "That's a great start",
                "display": "That's a great start.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.03,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M38S",
            "duration": "PT0.84S",
            "offsetInTicks": 2180000000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.8724174,
                "lexical": "that's a great start",
                "itn": "that's a great start",
                "maskedITN": "That's a great start",
                "display": "That's a great start.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.03,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M38.84S",
            "duration": "PT1.32S",
            "offsetInTicks": 2188400000.0,
            "durationInTicks": 13200000.0,
            "nBest": [
              {
                "confidence": 0.8903066,
                "lexical": "kind of see what works for them",
                "itn": "kind of see what works for them",
                "maskedITN": "Kind of see what works for them",
                "display": "Kind of see what works for them.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.91,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M38.84S",
            "duration": "PT1.32S",
            "offsetInTicks": 2188400000.0,
            "durationInTicks": 13200000.0,
            "nBest": [
              {
                "confidence": 0.8902451,
                "lexical": "kind of see what works for them",
                "itn": "kind of see what works for them",
                "maskedITN": "Kind of see what works for them",
                "display": "Kind of see what works for them.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.91,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M40.8S",
            "duration": "PT8.92S",
            "offsetInTicks": 2208000000.0,
            "durationInTicks": 89200000.0,
            "nBest": [
              {
                "confidence": 0.92405975,
                "lexical": "and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery",
                "itn": "and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery",
                "maskedITN": "And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery",
                "display": "And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step, your recovery.",
                "sentiment": {
                  "positive": 0.5,
                  "neutral": 0.47,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M40.8S",
            "duration": "PT8.88S",
            "offsetInTicks": 2208000000.0,
            "durationInTicks": 88800000.0,
            "nBest": [
              {
                "confidence": 0.9279842,
                "lexical": "and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery",
                "itn": "and then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery",
                "maskedITN": "And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step your recovery",
                "display": "And then you can let me know if there's also any equipment or anything that might help you become more independent in your training just to really get you to that final step, your recovery.",
                "sentiment": {
                  "positive": 0.5,
                  "neutral": 0.47,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M49.68S",
            "duration": "PT4.72S",
            "offsetInTicks": 2296800000.0,
            "durationInTicks": 47200000.0,
            "nBest": [
              {
                "confidence": 0.9398946,
                "lexical": "and once you're done that part then we can probably look at discharging the claim",
                "itn": "and once you're done that part then we can probably look at discharging the claim",
                "maskedITN": "And once you're done that part then we can probably look at discharging the claim",
                "display": "And once you're done that part, then we can probably look at discharging the claim.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M49.72S",
            "duration": "PT4.68S",
            "offsetInTicks": 2297200000.0,
            "durationInTicks": 46800000.0,
            "nBest": [
              {
                "confidence": 0.9377822,
                "lexical": "and once you're done that part then we can probably look at discharging the claim",
                "itn": "and once you're done that part then we can probably look at discharging the claim",
                "maskedITN": "And once you're done that part then we can probably look at discharging the claim",
                "display": "And once you're done that part, then we can probably look at discharging the claim.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M55.48S",
            "duration": "PT0.72S",
            "offsetInTicks": 2354800000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.9167174,
                "lexical": "how does that sound",
                "itn": "how does that sound",
                "maskedITN": "How does that sound",
                "display": "How does that sound?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M55.48S",
            "duration": "PT0.72S",
            "offsetInTicks": 2354800000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.9121312,
                "lexical": "how does that sound",
                "itn": "how does that sound",
                "maskedITN": "How does that sound",
                "display": "How does that sound?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M56.2S",
            "duration": "PT3.36S",
            "offsetInTicks": 2362000000.0,
            "durationInTicks": 33600000.0,
            "nBest": [
              {
                "confidence": 0.92056465,
                "lexical": "did you want to go check in with your teammate",
                "itn": "did you want to go check in with your teammate",
                "maskedITN": "Did you want to go check in with your teammate",
                "display": "Did you want to go check in with your teammate?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M56.2S",
            "duration": "PT3.36S",
            "offsetInTicks": 2362000000.0,
            "durationInTicks": 33600000.0,
            "nBest": [
              {
                "confidence": 0.91966385,
                "lexical": "did you want to go check in with your teammate",
                "itn": "did you want to go check in with your teammate",
                "maskedITN": "Did you want to go check in with your teammate",
                "display": "Did you want to go check in with your teammate?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M0.12S",
            "duration": "PT4.08S",
            "offsetInTicks": 2401200000.0,
            "durationInTicks": 40800000.0,
            "nBest": [
              {
                "confidence": 0.9403753,
                "lexical": "and then we can have a conversation about let's say next thursday",
                "itn": "and then we can have a conversation about let's say next thursday",
                "maskedITN": "And then we can have a conversation about let's say next Thursday",
                "display": "And then we can have a conversation about, let's say, next Thursday.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.92,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M0.12S",
            "duration": "PT4.08S",
            "offsetInTicks": 2401200000.0,
            "durationInTicks": 40800000.0,
            "nBest": [
              {
                "confidence": 0.9403753,
                "lexical": "and then we can have a conversation about let's say next thursday",
                "itn": "and then we can have a conversation about let's say next thursday",
                "maskedITN": "And then we can have a conversation about let's say next Thursday",
                "display": "And then we can have a conversation about, let's say, next Thursday.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.92,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M4.4S",
            "duration": "PT3.88S",
            "offsetInTicks": 2444000000.0,
            "durationInTicks": 38800000.0,
            "nBest": [
              {
                "confidence": 0.8497524,
                "lexical": "maybe i'll call you around the same time and then we can look at some of those options together",
                "itn": "maybe i'll call you around the same time and then we can look at some of those options together",
                "maskedITN": "Maybe I'll call you around the same time and then we can look at some of those options together",
                "display": "Maybe I'll call you around the same time and then we can look at some of those options together.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M4.4S",
            "duration": "PT3.88S",
            "offsetInTicks": 2444000000.0,
            "durationInTicks": 38800000.0,
            "nBest": [
              {
                "confidence": 0.8497524,
                "lexical": "maybe i'll call you around the same time and then we can look at some of those options together",
                "itn": "maybe i'll call you around the same time and then we can look at some of those options together",
                "maskedITN": "Maybe I'll call you around the same time and then we can look at some of those options together",
                "display": "Maybe I'll call you around the same time and then we can look at some of those options together.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M8.28S",
            "duration": "PT1.36S",
            "offsetInTicks": 2482800000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.6617513,
                "lexical": "yep that sounds good",
                "itn": "yep that sounds good",
                "maskedITN": "Yep that sounds good",
                "display": "Yep, that sounds good.",
                "sentiment": {
                  "positive": 0.78,
                  "neutral": 0.2,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M8.28S",
            "duration": "PT1.36S",
            "offsetInTicks": 2482800000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.6617513,
                "lexical": "yep that sounds good",
                "itn": "yep that sounds good",
                "maskedITN": "Yep that sounds good",
                "display": "Yep, that sounds good.",
                "sentiment": {
                  "positive": 0.78,
                  "neutral": 0.2,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M9.64S",
            "duration": "PT7.36S",
            "offsetInTicks": 2496400000.0,
            "durationInTicks": 73600000.0,
            "nBest": [
              {
                "confidence": 0.9196054,
                "lexical": "next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well",
                "itn": "next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well",
                "maskedITN": "Next Thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well",
                "display": "Next Thursday works for me, so we can chat, then maybe we'll get some updates and some good news on repairing your oven as well.",
                "sentiment": {
                  "positive": 0.58,
                  "neutral": 0.4,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M9.64S",
            "duration": "PT7.36S",
            "offsetInTicks": 2496400000.0,
            "durationInTicks": 73600000.0,
            "nBest": [
              {
                "confidence": 0.9196054,
                "lexical": "next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well",
                "itn": "next thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well",
                "maskedITN": "Next Thursday works for me so we can chat then maybe we'll get some updates and some good news on repairing your oven as well",
                "display": "Next Thursday works for me, so we can chat, then maybe we'll get some updates and some good news on repairing your oven as well.",
                "sentiment": {
                  "positive": 0.58,
                  "neutral": 0.4,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M17S",
            "duration": "PT5.28S",
            "offsetInTicks": 2570000000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.91297513,
                "lexical": "so before i wrap up here though since you've got me any other questions like anything else i can help you out with",
                "itn": "so before i wrap up here though since you've got me any other questions like anything else i can help you out with",
                "maskedITN": "So before I wrap up here though since you've got me any other questions like anything else I can help you out with",
                "display": "So before I wrap up here though, since you've got me any other questions like anything else I can help you out with?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.89,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M17S",
            "duration": "PT5.28S",
            "offsetInTicks": 2570000000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.91297513,
                "lexical": "so before i wrap up here though since you've got me any other questions like anything else i can help you out with",
                "itn": "so before i wrap up here though since you've got me any other questions like anything else i can help you out with",
                "maskedITN": "So before I wrap up here though since you've got me any other questions like anything else I can help you out with",
                "display": "So before I wrap up here though, since you've got me any other questions like anything else I can help you out with?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.89,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M23.8S",
            "duration": "PT1.56S",
            "offsetInTicks": 2638000000.0,
            "durationInTicks": 15600000.0,
            "nBest": [
              {
                "confidence": 0.93997073,
                "lexical": "no i think that's it for now",
                "itn": "no i think that's it for now",
                "maskedITN": "No I think that's it for now",
                "display": "No, I think that's it for now.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.9,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M23.8S",
            "duration": "PT1.56S",
            "offsetInTicks": 2638000000.0,
            "durationInTicks": 15600000.0,
            "nBest": [
              {
                "confidence": 0.93997073,
                "lexical": "no i think that's it for now",
                "itn": "no i think that's it for now",
                "maskedITN": "No I think that's it for now",
                "display": "No, I think that's it for now.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.9,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M25.36S",
            "duration": "PT4.2S",
            "offsetInTicks": 2653600000.0,
            "durationInTicks": 42000000.0,
            "nBest": [
              {
                "confidence": 0.9671998,
                "lexical": "i'll talk to them and then i'll try to think of any questions before we speak next thursday",
                "itn": "i'll talk to them and then i'll try to think of any questions before we speak next thursday",
                "maskedITN": "I'll talk to them and then I'll try to think of any questions before we speak next Thursday",
                "display": "I'll talk to them and then I'll try to think of any questions before we speak next Thursday.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M25.36S",
            "duration": "PT4.2S",
            "offsetInTicks": 2653600000.0,
            "durationInTicks": 42000000.0,
            "nBest": [
              {
                "confidence": 0.9671998,
                "lexical": "i'll talk to them and then i'll try to think of any questions before we speak next thursday",
                "itn": "i'll talk to them and then i'll try to think of any questions before we speak next thursday",
                "maskedITN": "I'll talk to them and then I'll try to think of any questions before we speak next Thursday",
                "display": "I'll talk to them and then I'll try to think of any questions before we speak next Thursday.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M30.4S",
            "duration": "PT0.92S",
            "offsetInTicks": 2704000000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.8038792,
                "lexical": "absolutely fantastic",
                "itn": "absolutely fantastic",
                "maskedITN": "Absolutely Fantastic",
                "display": "Absolutely Fantastic.",
                "sentiment": {
                  "positive": 0.99,
                  "neutral": 0.01,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M30.4S",
            "duration": "PT0.92S",
            "offsetInTicks": 2704000000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.8038792,
                "lexical": "absolutely fantastic",
                "itn": "absolutely fantastic",
                "maskedITN": "Absolutely Fantastic",
                "display": "Absolutely Fantastic.",
                "sentiment": {
                  "positive": 0.99,
                  "neutral": 0.01,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M31.32S",
            "duration": "PT10.84S",
            "offsetInTicks": 2713200000.0,
            "durationInTicks": 108400000.0,
            "nBest": [
              {
                "confidence": 0.92024535,
                "lexical": "i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job",
                "itn": "i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job",
                "maskedITN": "I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job",
                "display": "I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M31.32S",
            "duration": "PT10.84S",
            "offsetInTicks": 2713200000.0,
            "durationInTicks": 108400000.0,
            "nBest": [
              {
                "confidence": 0.92024535,
                "lexical": "i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job",
                "itn": "i just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job",
                "maskedITN": "I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in it's a lot about your own journey to recovery and you've done a really great job",
                "display": "I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M42.16S",
            "duration": "PT3.8S",
            "offsetInTicks": 2821600000.0,
            "durationInTicks": 38000000.0,
            "nBest": [
              {
                "confidence": 0.89355826,
                "lexical": "and i think we'll get you to that last step and we'll move forward together on that",
                "itn": "and i think we'll get you to that last step and we'll move forward together on that",
                "maskedITN": "And I think we'll get you to that last step and we'll move forward together on that",
                "display": "And I think we'll get you to that last step and we'll move forward together on that.",
                "sentiment": {
                  "positive": 0.14,
                  "neutral": 0.85,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M42.16S",
            "duration": "PT3.8S",
            "offsetInTicks": 2821600000.0,
            "durationInTicks": 38000000.0,
            "nBest": [
              {
                "confidence": 0.89355826,
                "lexical": "and i think we'll get you to that last step and we'll move forward together on that",
                "itn": "and i think we'll get you to that last step and we'll move forward together on that",
                "maskedITN": "And I think we'll get you to that last step and we'll move forward together on that",
                "display": "And I think we'll get you to that last step and we'll move forward together on that.",
                "sentiment": {
                  "positive": 0.14,
                  "neutral": 0.85,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M45.96S",
            "duration": "PT0.32S",
            "offsetInTicks": 2859600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.8829274,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M45.96S",
            "duration": "PT0.32S",
            "offsetInTicks": 2859600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.8829274,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M46.6S",
            "duration": "PT1.76S",
            "offsetInTicks": 2866000000.0,
            "durationInTicks": 17600000.0,
            "nBest": [
              {
                "confidence": 0.94125926,
                "lexical": "so we'll chat next week then",
                "itn": "so we'll chat next week then",
                "maskedITN": "So we'll chat next week then",
                "display": "So we'll chat next week then.",
                "sentiment": {
                  "positive": 0.18,
                  "neutral": 0.8,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M46.6S",
            "duration": "PT1.76S",
            "offsetInTicks": 2866000000.0,
            "durationInTicks": 17600000.0,
            "nBest": [
              {
                "confidence": 0.94125926,
                "lexical": "so we'll chat next week then",
                "itn": "so we'll chat next week then",
                "maskedITN": "So we'll chat next week then",
                "display": "So we'll chat next week then.",
                "sentiment": {
                  "positive": 0.18,
                  "neutral": 0.8,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M48.68S",
            "duration": "PT0.24S",
            "offsetInTicks": 2886800000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.73593664,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M48.68S",
            "duration": "PT0.24S",
            "offsetInTicks": 2886800000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.73593664,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M49.72S",
            "duration": "PT0.52S",
            "offsetInTicks": 2897200000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.2834987,
                "lexical": "thank you",
                "itn": "thank you",
                "maskedITN": "Thank you",
                "display": "Thank you.",
                "sentiment": {
                  "positive": 0.93,
                  "neutral": 0.06,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M49.72S",
            "duration": "PT0.52S",
            "offsetInTicks": 2897200000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.2834987,
                "lexical": "thank you",
                "itn": "thank you",
                "maskedITN": "Thank you",
                "display": "Thank you.",
                "sentiment": {
                  "positive": 0.93,
                  "neutral": 0.06,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M50.64S",
            "duration": "PT0.52S",
            "offsetInTicks": 2906400000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.71995986,
                "lexical": "bye for now",
                "itn": "bye for now",
                "maskedITN": "Bye for now",
                "display": "Bye for now.",
                "sentiment": {
                  "positive": 0.2,
                  "neutral": 0.75,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M50.64S",
            "duration": "PT0.52S",
            "offsetInTicks": 2906400000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.71995986,
                "lexical": "bye for now",
                "itn": "bye for now",
                "maskedITN": "Bye for now",
                "display": "Bye for now.",
                "sentiment": {
                  "positive": 0.2,
                  "neutral": 0.75,
                  "negative": 0.04
                }
              }
            ]
          }
        ]
      }
    }
},
{
    "short": {
      "audioFile": "/call4.wav",
      "representativeName": "Eddie",
      "customerName": "Bobby",
      "date": "04/22/2024",
      "callLength": 5,
      "summary": "Eddie discusses Bobby's recovery progress, treatment plan, and benefits. They talk about equipment usage, progress with physiotherapy, and Bobby's overall recovery. Eddie informs Bobby that they are ready for discharge from physiotherapy services and outlines the next steps. They agree on follow-up communication via email and phone, ensuring Bobby has all the necessary information for a smooth transition from treatment.",
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
      "transcription": {
        "source": "https://github.com/ofek-zilber-icbc/ICBCHackathon2024/raw/main/backend/azure_related/call4.wav",
        "timestamp": "2024-04-25T06:10:52Z",
        "durationInTicks": 3374700000,
        "duration": "PT5M37.47S",
        "combinedRecognizedPhrases": [
          {
            "channel": 0,
            "lexical": "hey there i'm calling from ICBC my name is eddie looking to speak with bobby please bobby speaking hey there bobby just calling for let's say ten to fifteen minutes just to give you a bit of an update is this a good time sure absolutely fantastic thank you so much yeah we'll make sure we go over my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better and part of that involves your treatment and the treatment plans that we receive so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well yeah OK sure jump into that do you have any questions i can help you out with no not really nope anything about your mileage expenses or anything about your equipment that you've recently purchased how's that been going no not really what do you mean by equipment i'm glad you asked some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes i think there was the foam roller and the therapans how how how's that exercise been going oh fine anything else you'd like to share about working with that physiotherapist that we should know about though no it's been good the the equipment 's working it's good that's great to hear thanks so much for sharing and and for yourself how are you finding the progress are you getting back to where you were before the crash i i guess i guess it's been OK yeah how i guess can you share how close are you getting to that in terms of your recovery i guess i'm doing fine the physiotherapist seems to think it's going OK so i good i guess i think you're doing really i think you're really doing really good i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist i think you're doing really great actually so you might be selling yourself a little bit short here but i think we're seeing some great progress oh OK good good to know thanks great so just working with you on some of your other benefits as well i just want to make sure i touch on your mileage how's the submission been like have you had all your reimbursements received properly i think so when do i have to have them in by anytime works whichever is convenient for you we have technically up to a hundred and eighty days from the date that you incur them OK fine that that's OK thanks OK great now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered and at this point you're ready for discharge from the physiotherapy services so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there how's that sound that's good that's good to know is there anything i else that you need from me anything else i need to do at this point i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash i guess i'm OK i think it's going fine mine is also good so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me i'll be available for you on monday to friday and eight to four so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations sounds good i think i've lost your email address can you email that to me again yeah not a problem not a problem and what i'll do is i will send you an email i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery and then also i'll be checking in with you in two weeks would you prefer that i email you would you prefer that i call you or you just give me a call when you're ready what's easier for you anything works for me really it's it's fine whichever one you want to do sure if that's the case then why don't we do this i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it but if you do have anything that comes up in the meantime then just give me a call how about that yeah and that that sounds good thanks OK absolutely fantastic it's always a pleasure talking to you really enjoy sharing this update with you and working with you on this so anything else just give me a call OK thanks eddie great thank you",
            "itn": "hey there i'm calling from ICBC my name is eddie looking to speak with bobby please bobby speaking hey there bobby just calling for let's say 10 to 15 minutes just to give you a bit of an update is this a good time sure absolutely fantastic thank you so much yeah we'll make sure we go over my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better and part of that involves your treatment and the treatment plans that we receive so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well yeah OK sure jump into that do you have any questions i can help you out with no not really nope anything about your mileage expenses or anything about your equipment that you've recently purchased how's that been going no not really what do you mean by equipment i'm glad you asked some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes i think there was the foam roller and the therapans how how how's that exercise been going oh fine anything else you'd like to share about working with that physiotherapist that we should know about though no it's been good the the equipment's working it's good that's great to hear thanks so much for sharing and and for yourself how are you finding the progress are you getting back to where you were before the crash i i guess i guess it's been OK yeah how i guess can you share how close are you getting to that in terms of your recovery i guess i'm doing fine the physiotherapist seems to think it's going OK so i good i guess i think you're doing really i think you're really doing really good i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist i think you're doing really great actually so you might be selling yourself a little bit short here but i think we're seeing some great progress oh OK good good to know thanks great so just working with you on some of your other benefits as well i just want to make sure i touch on your mileage how's the submission been like have you had all your reimbursements received properly i think so when do i have to have them in by anytime works whichever is convenient for you we have technically up to 180 days from the date that you incur them OK fine that that's OK thanks OK great now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered and at this point you're ready for discharge from the physiotherapy services so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there how's that sound that's good that's good to know is there anything i else that you need from me anything else i need to do at this point i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash i guess i'm OK i think it's going fine mine is also good so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me i'll be available for you on monday to friday and 8:00 to 4:00 so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations sounds good i think i've lost your email address can you email that to me again yeah not a problem not a problem and what i'll do is i will send you an email i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery and then also i'll be checking in with you in two weeks would you prefer that i email you would you prefer that i call you or you just give me a call when you're ready what's easier for you anything works for me really it's it's fine whichever one you want to do sure if that's the case then why don't we do this i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it but if you do have anything that comes up in the meantime then just give me a call how about that yeah and that that sounds good thanks OK absolutely fantastic it's always a pleasure talking to you really enjoy sharing this update with you and working with you on this so anything else just give me a call OK thanks eddie great thank you",
            "maskedITN": "Hey there I'm calling from ICBC My name is Eddie Looking to speak with Bobby please Bobby speaking Hey there Bobby Just calling for let's say 10 to 15 minutes just to give you a bit of an update Is this a good time Sure Absolutely Fantastic Thank you so much Yeah we'll make sure we go over My role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better And part of that involves your treatment and the treatment plans that we receive So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well Yeah OK sure jump into that Do you have any questions I can help you out with No not really Nope Anything about your mileage expenses or anything about your equipment that you've recently purchased How's that been going No not really What do you mean by equipment I'm glad you asked Some of the equipment that your physiotherapist recommended do you remember about I think there was the I'm just taking a look at my notes I think there was the foam roller and the therapans How how how's that exercise been going Oh fine Anything else you'd like to share about working with that physiotherapist that we should know about though No it's been good The the equipment's working It's good That's great to hear Thanks so much for sharing and and for yourself How are you finding the progress Are you getting back to where you were before the crash I I guess I guess it's been OK Yeah How I guess can you share how close are you getting to that in terms of your recovery I guess I'm doing fine The physiotherapist seems to think it's going OK So I good I guess I think you're doing really I think you're really doing really good I mean looking at the progress that you're making I'm looking at the treatment plans I'm looking at our consultation that we had with your physiotherapist I think you're doing really great actually So you might be selling yourself a little bit short here but I think we're seeing some great progress Oh OK good Good to know Thanks Great So just working with you on some of your other benefits as well I just want to make sure I touch on your mileage How's the submission been Like have you had all your reimbursements received properly I think so when do I have to have them in by anytime works whichever is convenient for you We have technically up to 180 days from the date that you incur them OK fine That that's OK Thanks OK great Now before I go into the treatment plan in itself and I'll share a little bit about the details here I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered And at this point you're ready for discharge from the physiotherapy services So with this treatment plan I think you do have two more treatments left and you'll be able to finish those last two and go from there How's that sound That's good That's good to know Is there anything I else that you need from me Anything else I need to do at this point I think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash I guess I'm OK I think it's going fine Mine is also good So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions I just want to really encourage you to give me a call e-mail me I'll be available for you on Monday to Friday and 8:00 to 4:00 So as you know just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations Sounds good I think I've lost your e-mail address Can you e-mail that to me again Yeah not a problem not a problem And what I'll do is I will send you an e-mail I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery And then also I'll be checking in with you in two weeks Would you prefer that I e-mail you Would you prefer that I call you or you just give me a call when you're ready What's easier for you Anything works for me really It's it's fine Whichever one you want to do sure If that's the case then why don't we do this I'll just mark this file to to close the file in three weeks and if I don't hear back from you then we'll close it But if you do have anything that comes up in the meantime then just give me a call How about that Yeah And that that sounds good Thanks OK Absolutely fantastic It's always a pleasure talking to you Really enjoy sharing this update with you and working with you on this So anything else just give me a call OK Thanks Eddie Great Thank you",
            "display": "Hey there. I'm calling from ICBC. My name is Eddie. Looking to speak with Bobby, please, Bobby speaking. Hey there, Bobby. Just calling for, let's say, 10 to 15 minutes just to give you a bit of an update. Is this a good time? Sure. Absolutely. Fantastic. Thank you so much. Yeah, we'll make sure we go over. My role, of course, is, as you know, is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better. And part of that involves your treatment and the treatment plans that we receive. So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well. Yeah, OK, sure, jump into that. Do you have any questions I can help you out with? No, not really. Nope. Anything about your mileage, expenses, or anything about your equipment that you've recently purchased. How's that been going? No, not really. What do you mean by equipment? I'm glad you asked. Some of the equipment that your physiotherapist recommended, do you remember about, I think there was the, I'm just taking a look at my notes. I think there was the foam roller and the therapans. How, how, how's that exercise been going? Oh, fine. Anything else you'd like to share about working with that physiotherapist that we should know about though? No, it's been good. The the equipment's working. It's good. That's great to hear. Thanks so much for sharing and and for yourself. How are you finding the progress? Are you getting back to where you were before the crash? I I guess. I guess it's been OK. Yeah. How I guess can you share how close are you getting to that in terms of your recovery? I guess I'm doing fine. The physiotherapist seems to think it's going OK. So I good. I guess I think you're doing really, I think you're really doing really good. I mean looking at the progress that you're making, I'm looking at the treatment plans, I'm looking at our consultation that we had with your physiotherapist. I think you're doing really great actually. So you might be selling yourself a little bit short here, but I think we're seeing some great progress. Oh, OK, good. Good to know. Thanks. Great. So just working with you on some of your other benefits as well. I just want to make sure I touch on your mileage. How's the submission been? Like have you had all your reimbursements received properly? I think so when do I have to have them in by anytime works, whichever is convenient for you. We have technically up to 180 days from the date that you incur them. OK, fine. That, that's OK. Thanks. OK, great. Now before I go into the treatment plan in itself, and I'll share a little bit about the details here, I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered. And at this point, you're ready for discharge from the physiotherapy services. So with this treatment plan, I think you do have two more treatments left and you'll be able to finish those last two and go from there. How's that sound? That's good. That's good to know. Is there anything I else that you need from me, Anything else I need to do at this point? I think it really comes down to for yourself, like anything that you feel like you need before you so that you can get back to where you were before the crash. I guess I'm OK. I think it's going fine. Mine is also good. So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions, I just want to really encourage you to give me a call, e-mail me. I'll be available for you on Monday to Friday and 8:00 to 4:00. So as you know, just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations. Sounds good. I think I've lost your e-mail address. Can you e-mail that to me again? Yeah, not a problem, not a problem. And what I'll do is I will send you an e-mail. I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery. And then also, I'll be checking in with you in two weeks. Would you prefer that I e-mail you? Would you prefer that I call you or you just give me a call when you're ready? What's easier for you? Anything works for me, really. It's it's fine. Whichever one you want to do, sure. If that's the case then why don't we do this? I'll just mark this file to to close the file in three weeks and if I don't hear back from you, then we'll close it. But if you do have anything that comes up in the meantime, then just give me a call. How about that? Yeah. And that that sounds good. Thanks. OK. Absolutely fantastic. It's always a pleasure talking to you. Really enjoy sharing this update with you and working with you on this. So anything else, just give me a call. OK. Thanks, Eddie. Great. Thank you."
          },
          {
            "channel": 1,
            "lexical": "hey there i'm calling from ICBC my name is eddie looking to speak with bobby please bobby speaking hey there bobby just calling for let's say ten to fifteen minutes just to give you a bit of an update is this a good time sure absolutely fantastic thank you so much yeah we'll make sure we go over my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better and part of that involves your treatment and the treatment plans that we receive so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well yeah OK sure jump into that do you have any questions i can help you out with no not really nope anything about your mileage expenses or anything about your equipment that you've recently purchased how's that been going no not really what do you mean by equipment i'm glad you asked some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes i think there was the foam roller and the therapans how how how's that exercise been going oh fine anything else you'd like to share about working with that physiotherapist that we should know about though no it's been good the the equipment 's working it's good that's great to hear thanks so much for sharing and and for yourself how are you finding the progress are you getting back to where you were before the crash i i guess i guess it's been OK yeah how i guess can you share how close are you getting to that in terms of your recovery i guess i'm doing fine the physiotherapist seems to think it's going OK so i good i guess i think you're doing really i think you're really doing really good i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist i think you're doing really great actually so you might be selling yourself a little bit short here but i think we're seeing some great progress oh OK good good to know thanks great so just working with you on some of your other benefits as well i just want to make sure i touch on your mileage how's the submission been like have you had all your reimbursements received properly i think so when do i have to have them in by anytime works whichever is convenient for you we have technically up to a hundred and eighty days from the date that you incur them OK fine that that's OK thanks OK great now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered and at this point you're ready for discharge from the physiotherapy services so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there how's that sound that's good that's good to know is there anything i else that you need from me anything else i need to do at this point i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash i guess i'm OK i think it's going fine mine is also good so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me i'll be available for you on monday to friday and eight to four so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations sounds good i think i've lost your email address can you email that to me again yeah not a problem not a problem and what i'll do is i will send you an email i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery and then also i'll be checking in with you in two weeks would you prefer that i email you would you prefer that i call you or you just give me a call when you're ready what's easier for you anything works for me really it's it's fine whichever one you want to do sure if that's the case then why don't we do this i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it but if you do have anything that comes up in the meantime then just give me a call how about that yeah and that that sounds good thanks OK absolutely fantastic it's always a pleasure talking to you really enjoy sharing this update with you and working with you on this so anything else just give me a call OK thanks eddie great thank you",
            "itn": "hey there i'm calling from ICBC my name is eddie looking to speak with bobby please bobby speaking hey there bobby just calling for let's say 10 to 15 minutes just to give you a bit of an update is this a good time sure absolutely fantastic thank you so much yeah we'll make sure we go over my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better and part of that involves your treatment and the treatment plans that we receive so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well yeah OK sure jump into that do you have any questions i can help you out with no not really nope anything about your mileage expenses or anything about your equipment that you've recently purchased how's that been going no not really what do you mean by equipment i'm glad you asked some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes i think there was the foam roller and the therapans how how how's that exercise been going oh fine anything else you'd like to share about working with that physiotherapist that we should know about though no it's been good the the equipment's working it's good that's great to hear thanks so much for sharing and and for yourself how are you finding the progress are you getting back to where you were before the crash i i guess i guess it's been OK yeah how i guess can you share how close are you getting to that in terms of your recovery i guess i'm doing fine the physiotherapist seems to think it's going OK so i good i guess i think you're doing really i think you're really doing really good i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist i think you're doing really great actually so you might be selling yourself a little bit short here but i think we're seeing some great progress oh OK good good to know thanks great so just working with you on some of your other benefits as well i just want to make sure i touch on your mileage how's the submission been like have you had all your reimbursements received properly i think so when do i have to have them in by anytime works whichever is convenient for you we have technically up to 180 days from the date that you incur them OK fine that that's OK thanks OK great now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered and at this point you're ready for discharge from the physiotherapy services so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there how's that sound that's good that's good to know is there anything i else that you need from me anything else i need to do at this point i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash i guess i'm OK i think it's going fine mine is also good so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me i'll be available for you on monday to friday and 8:00 to 4:00 so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations sounds good i think i've lost your email address can you email that to me again yeah not a problem not a problem and what i'll do is i will send you an email i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery and then also i'll be checking in with you in two weeks would you prefer that i email you would you prefer that i call you or you just give me a call when you're ready what's easier for you anything works for me really it's it's fine whichever one you want to do sure if that's the case then why don't we do this i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it but if you do have anything that comes up in the meantime then just give me a call how about that yeah and that that sounds good thanks OK absolutely fantastic it's always a pleasure talking to you really enjoy sharing this update with you and working with you on this so anything else just give me a call OK thanks eddie great thank you",
            "maskedITN": "Hey there I'm calling from ICBC My name is Eddie Looking to speak with Bobby please Bobby speaking Hey there Bobby Just calling for let's say 10 to 15 minutes just to give you a bit of an update Is this a good time Sure Absolutely Fantastic Thank you so much Yeah we'll make sure we go over My role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better And part of that involves your treatment and the treatment plans that we receive So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well Yeah OK sure jump into that Do you have any questions I can help you out with No not really Nope Anything about your mileage expenses or anything about your equipment that you've recently purchased How's that been going No not really What do you mean by equipment I'm glad you asked Some of the equipment that your physiotherapist recommended do you remember about I think there was the I'm just taking a look at my notes I think there was the foam roller and the therapans How how how's that exercise been going Oh fine Anything else you'd like to share about working with that physiotherapist that we should know about though No it's been good The the equipment's working It's good That's great to hear Thanks so much for sharing and and for yourself How are you finding the progress Are you getting back to where you were before the crash I I guess I guess it's been OK Yeah How I guess can you share how close are you getting to that in terms of your recovery I guess I'm doing fine The physiotherapist seems to think it's going OK So I good I guess I think you're doing really I think you're really doing really good I mean looking at the progress that you're making I'm looking at the treatment plans I'm looking at our consultation that we had with your physiotherapist I think you're doing really great actually So you might be selling yourself a little bit short here but I think we're seeing some great progress Oh OK good Good to know Thanks Great So just working with you on some of your other benefits as well I just want to make sure I touch on your mileage How's the submission been Like have you had all your reimbursements received properly I think so when do I have to have them in by anytime works whichever is convenient for you We have technically up to 180 days from the date that you incur them OK fine That that's OK Thanks OK great Now before I go into the treatment plan in itself and I'll share a little bit about the details here I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered And at this point you're ready for discharge from the physiotherapy services So with this treatment plan I think you do have two more treatments left and you'll be able to finish those last two and go from there How's that sound That's good That's good to know Is there anything I else that you need from me Anything else I need to do at this point I think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash I guess I'm OK I think it's going fine Mine is also good So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions I just want to really encourage you to give me a call e-mail me I'll be available for you on Monday to Friday and 8:00 to 4:00 So as you know just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations Sounds good I think I've lost your e-mail address Can you e-mail that to me again Yeah not a problem not a problem And what I'll do is I will send you an e-mail I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery And then also I'll be checking in with you in two weeks Would you prefer that I e-mail you Would you prefer that I call you or you just give me a call when you're ready What's easier for you Anything works for me really It's it's fine Whichever one you want to do sure If that's the case then why don't we do this I'll just mark this file to to close the file in three weeks and if I don't hear back from you then we'll close it But if you do have anything that comes up in the meantime then just give me a call How about that Yeah And that that sounds good Thanks OK Absolutely fantastic It's always a pleasure talking to you Really enjoy sharing this update with you and working with you on this So anything else just give me a call OK Thanks Eddie Great Thank you",
            "display": "Hey there. I'm calling from ICBC. My name is Eddie. Looking to speak with Bobby, please, Bobby speaking. Hey there, Bobby. Just calling for, let's say, 10 to 15 minutes just to give you a bit of an update. Is this a good time? Sure. Absolutely. Fantastic. Thank you so much. Yeah, we'll make sure we go over. My role, of course, is, as you know, is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better. And part of that involves your treatment and the treatment plans that we receive. So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well. Yeah, OK, sure, jump into that. Do you have any questions I can help you out with? No, not really. Nope. Anything about your mileage, expenses, or anything about your equipment that you've recently purchased. How's that been going? No, not really. What do you mean by equipment? I'm glad you asked. Some of the equipment that your physiotherapist recommended, do you remember about, I think there was the, I'm just taking a look at my notes. I think there was the foam roller and the therapans. How, how, how's that exercise been going? Oh, fine. Anything else you'd like to share about working with that physiotherapist that we should know about though? No, it's been good. The the equipment's working. It's good. That's great to hear. Thanks so much for sharing and and for yourself. How are you finding the progress? Are you getting back to where you were before the crash? I I guess. I guess it's been OK. Yeah. How I guess can you share how close are you getting to that in terms of your recovery? I guess I'm doing fine. The physiotherapist seems to think it's going OK. So I good. I guess I think you're doing really, I think you're really doing really good. I mean looking at the progress that you're making, I'm looking at the treatment plans, I'm looking at our consultation that we had with your physiotherapist. I think you're doing really great actually. So you might be selling yourself a little bit short here, but I think we're seeing some great progress. Oh, OK, good. Good to know. Thanks. Great. So just working with you on some of your other benefits as well. I just want to make sure I touch on your mileage. How's the submission been? Like have you had all your reimbursements received properly? I think so when do I have to have them in by anytime works, whichever is convenient for you. We have technically up to 180 days from the date that you incur them. OK, fine. That, that's OK. Thanks. OK, great. Now before I go into the treatment plan in itself, and I'll share a little bit about the details here, I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered. And at this point, you're ready for discharge from the physiotherapy services. So with this treatment plan, I think you do have two more treatments left and you'll be able to finish those last two and go from there. How's that sound? That's good. That's good to know. Is there anything I else that you need from me, Anything else I need to do at this point? I think it really comes down to for yourself, like anything that you feel like you need before you so that you can get back to where you were before the crash. I guess I'm OK. I think it's going fine. Mine is also good. So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions, I just want to really encourage you to give me a call, e-mail me. I'll be available for you on Monday to Friday and 8:00 to 4:00. So as you know, just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations. Sounds good. I think I've lost your e-mail address. Can you e-mail that to me again? Yeah, not a problem, not a problem. And what I'll do is I will send you an e-mail. I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery. And then also, I'll be checking in with you in two weeks. Would you prefer that I e-mail you? Would you prefer that I call you or you just give me a call when you're ready? What's easier for you? Anything works for me, really. It's it's fine. Whichever one you want to do, sure. If that's the case then why don't we do this? I'll just mark this file to to close the file in three weeks and if I don't hear back from you, then we'll close it. But if you do have anything that comes up in the meantime, then just give me a call. How about that? Yeah. And that that sounds good. Thanks. OK. Absolutely fantastic. It's always a pleasure talking to you. Really enjoy sharing this update with you and working with you on this. So anything else, just give me a call. OK. Thanks, Eddie. Great. Thank you."
          }
        ],
        "recognizedPhrases": [
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3.24S",
            "duration": "PT0.2S",
            "offsetInTicks": 32400000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.2039333,
                "lexical": "hey there",
                "itn": "hey there",
                "maskedITN": "Hey there",
                "display": "Hey there.",
                "sentiment": {
                  "positive": 0.33,
                  "neutral": 0.63,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3.24S",
            "duration": "PT0.2S",
            "offsetInTicks": 32400000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.2039333,
                "lexical": "hey there",
                "itn": "hey there",
                "maskedITN": "Hey there",
                "display": "Hey there.",
                "sentiment": {
                  "positive": 0.33,
                  "neutral": 0.63,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3.44S",
            "duration": "PT1.08S",
            "offsetInTicks": 34400000.0,
            "durationInTicks": 10800000.0,
            "nBest": [
              {
                "confidence": 0.81686556,
                "lexical": "i'm calling from ICBC",
                "itn": "i'm calling from ICBC",
                "maskedITN": "I'm calling from ICBC",
                "display": "I'm calling from ICBC.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3.44S",
            "duration": "PT1.08S",
            "offsetInTicks": 34400000.0,
            "durationInTicks": 10800000.0,
            "nBest": [
              {
                "confidence": 0.81686556,
                "lexical": "i'm calling from ICBC",
                "itn": "i'm calling from ICBC",
                "maskedITN": "I'm calling from ICBC",
                "display": "I'm calling from ICBC.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4.52S",
            "duration": "PT1.12S",
            "offsetInTicks": 45200000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.88487744,
                "lexical": "my name is eddie",
                "itn": "my name is eddie",
                "maskedITN": "My name is Eddie",
                "display": "My name is Eddie.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.99,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4.52S",
            "duration": "PT1.12S",
            "offsetInTicks": 45200000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.88487744,
                "lexical": "my name is eddie",
                "itn": "my name is eddie",
                "maskedITN": "My name is Eddie",
                "display": "My name is Eddie.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.99,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5.64S",
            "duration": "PT3.48S",
            "offsetInTicks": 56400000.0,
            "durationInTicks": 34800000.0,
            "nBest": [
              {
                "confidence": 0.88177663,
                "lexical": "looking to speak with bobby please bobby speaking",
                "itn": "looking to speak with bobby please bobby speaking",
                "maskedITN": "Looking to speak with Bobby please Bobby speaking",
                "display": "Looking to speak with Bobby, please, Bobby speaking.",
                "sentiment": {
                  "positive": 0.12,
                  "neutral": 0.87,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5.64S",
            "duration": "PT3.48S",
            "offsetInTicks": 56400000.0,
            "durationInTicks": 34800000.0,
            "nBest": [
              {
                "confidence": 0.88177663,
                "lexical": "looking to speak with bobby please bobby speaking",
                "itn": "looking to speak with bobby please bobby speaking",
                "maskedITN": "Looking to speak with Bobby please Bobby speaking",
                "display": "Looking to speak with Bobby, please, Bobby speaking.",
                "sentiment": {
                  "positive": 0.12,
                  "neutral": 0.87,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT10.08S",
            "duration": "PT0.8S",
            "offsetInTicks": 100800000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.8898164,
                "lexical": "hey there bobby",
                "itn": "hey there bobby",
                "maskedITN": "Hey there Bobby",
                "display": "Hey there, Bobby.",
                "sentiment": {
                  "positive": 0.23,
                  "neutral": 0.72,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT10.08S",
            "duration": "PT0.8S",
            "offsetInTicks": 100800000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.8898164,
                "lexical": "hey there bobby",
                "itn": "hey there bobby",
                "maskedITN": "Hey there Bobby",
                "display": "Hey there, Bobby.",
                "sentiment": {
                  "positive": 0.23,
                  "neutral": 0.72,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT11.04S",
            "duration": "PT5.16S",
            "offsetInTicks": 110400000.0,
            "durationInTicks": 51600000.0,
            "nBest": [
              {
                "confidence": 0.95516926,
                "lexical": "just calling for let's say ten to fifteen minutes just to give you a bit of an update",
                "itn": "just calling for let's say 10 to 15 minutes just to give you a bit of an update",
                "maskedITN": "Just calling for let's say 10 to 15 minutes just to give you a bit of an update",
                "display": "Just calling for, let's say, 10 to 15 minutes just to give you a bit of an update.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT11.04S",
            "duration": "PT5.16S",
            "offsetInTicks": 110400000.0,
            "durationInTicks": 51600000.0,
            "nBest": [
              {
                "confidence": 0.95516926,
                "lexical": "just calling for let's say ten to fifteen minutes just to give you a bit of an update",
                "itn": "just calling for let's say 10 to 15 minutes just to give you a bit of an update",
                "maskedITN": "Just calling for let's say 10 to 15 minutes just to give you a bit of an update",
                "display": "Just calling for, let's say, 10 to 15 minutes just to give you a bit of an update.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT16.2S",
            "duration": "PT1.04S",
            "offsetInTicks": 162000000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.9629723,
                "lexical": "is this a good time",
                "itn": "is this a good time",
                "maskedITN": "Is this a good time",
                "display": "Is this a good time?",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.82,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT16.2S",
            "duration": "PT1.04S",
            "offsetInTicks": 162000000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.9629723,
                "lexical": "is this a good time",
                "itn": "is this a good time",
                "maskedITN": "Is this a good time",
                "display": "Is this a good time?",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.82,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT18.2S",
            "duration": "PT0.12S",
            "offsetInTicks": 182000000.0,
            "durationInTicks": 1200000.0,
            "nBest": [
              {
                "confidence": 0.44883198,
                "lexical": "sure",
                "itn": "sure",
                "maskedITN": "Sure",
                "display": "Sure.",
                "sentiment": {
                  "positive": 0.14,
                  "neutral": 0.83,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT18.2S",
            "duration": "PT0.12S",
            "offsetInTicks": 182000000.0,
            "durationInTicks": 1200000.0,
            "nBest": [
              {
                "confidence": 0.44883198,
                "lexical": "sure",
                "itn": "sure",
                "maskedITN": "Sure",
                "display": "Sure.",
                "sentiment": {
                  "positive": 0.14,
                  "neutral": 0.83,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT19.12S",
            "duration": "PT0.44S",
            "offsetInTicks": 191200000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.6912203,
                "lexical": "absolutely",
                "itn": "absolutely",
                "maskedITN": "Absolutely",
                "display": "Absolutely.",
                "sentiment": {
                  "positive": 0.27,
                  "neutral": 0.7,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT19.12S",
            "duration": "PT0.44S",
            "offsetInTicks": 191200000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.6912203,
                "lexical": "absolutely",
                "itn": "absolutely",
                "maskedITN": "Absolutely",
                "display": "Absolutely.",
                "sentiment": {
                  "positive": 0.27,
                  "neutral": 0.7,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT19.56S",
            "duration": "PT0.64S",
            "offsetInTicks": 195600000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.9735406,
                "lexical": "fantastic",
                "itn": "fantastic",
                "maskedITN": "Fantastic",
                "display": "Fantastic.",
                "sentiment": {
                  "positive": 0.96,
                  "neutral": 0.03,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT19.56S",
            "duration": "PT0.64S",
            "offsetInTicks": 195600000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.9735406,
                "lexical": "fantastic",
                "itn": "fantastic",
                "maskedITN": "Fantastic",
                "display": "Fantastic.",
                "sentiment": {
                  "positive": 0.96,
                  "neutral": 0.03,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT20.2S",
            "duration": "PT0.88S",
            "offsetInTicks": 202000000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.8881118,
                "lexical": "thank you so much",
                "itn": "thank you so much",
                "maskedITN": "Thank you so much",
                "display": "Thank you so much.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.03,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT20.2S",
            "duration": "PT0.88S",
            "offsetInTicks": 202000000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.8881118,
                "lexical": "thank you so much",
                "itn": "thank you so much",
                "maskedITN": "Thank you so much",
                "display": "Thank you so much.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.03,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT21.72S",
            "duration": "PT2.4S",
            "offsetInTicks": 217200000.0,
            "durationInTicks": 24000000.0,
            "nBest": [
              {
                "confidence": 0.9373468,
                "lexical": "yeah we'll make sure we go over",
                "itn": "yeah we'll make sure we go over",
                "maskedITN": "Yeah we'll make sure we go over",
                "display": "Yeah, we'll make sure we go over.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.85,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT21.72S",
            "duration": "PT2.4S",
            "offsetInTicks": 217200000.0,
            "durationInTicks": 24000000.0,
            "nBest": [
              {
                "confidence": 0.9373468,
                "lexical": "yeah we'll make sure we go over",
                "itn": "yeah we'll make sure we go over",
                "maskedITN": "Yeah we'll make sure we go over",
                "display": "Yeah, we'll make sure we go over.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.85,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT24.84S",
            "duration": "PT9.8S",
            "offsetInTicks": 248400000.0,
            "durationInTicks": 98000000.0,
            "nBest": [
              {
                "confidence": 0.9420383,
                "lexical": "my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better",
                "itn": "my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better",
                "maskedITN": "My role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better",
                "display": "My role, of course, is, as you know, is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better.",
                "sentiment": {
                  "positive": 0.56,
                  "neutral": 0.4,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT24.84S",
            "duration": "PT9.8S",
            "offsetInTicks": 248400000.0,
            "durationInTicks": 98000000.0,
            "nBest": [
              {
                "confidence": 0.9420383,
                "lexical": "my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better",
                "itn": "my role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better",
                "maskedITN": "My role of course is as you know is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better",
                "display": "My role, of course, is, as you know, is to really help you with understanding your recovery and setting up your claim and give you all the benefits that you need to get you better.",
                "sentiment": {
                  "positive": 0.56,
                  "neutral": 0.4,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT34.64S",
            "duration": "PT5.28S",
            "offsetInTicks": 346400000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.9115934,
                "lexical": "and part of that involves your treatment and the treatment plans that we receive",
                "itn": "and part of that involves your treatment and the treatment plans that we receive",
                "maskedITN": "And part of that involves your treatment and the treatment plans that we receive",
                "display": "And part of that involves your treatment and the treatment plans that we receive.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT34.64S",
            "duration": "PT5.28S",
            "offsetInTicks": 346400000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.9115934,
                "lexical": "and part of that involves your treatment and the treatment plans that we receive",
                "itn": "and part of that involves your treatment and the treatment plans that we receive",
                "maskedITN": "And part of that involves your treatment and the treatment plans that we receive",
                "display": "And part of that involves your treatment and the treatment plans that we receive.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT41.04S",
            "duration": "PT7.44S",
            "offsetInTicks": 410400000.0,
            "durationInTicks": 74400000.0,
            "nBest": [
              {
                "confidence": 0.9176343,
                "lexical": "so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well",
                "itn": "so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well",
                "maskedITN": "So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well",
                "display": "So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT41.04S",
            "duration": "PT7.44S",
            "offsetInTicks": 410400000.0,
            "durationInTicks": 74400000.0,
            "nBest": [
              {
                "confidence": 0.9176343,
                "lexical": "so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well",
                "itn": "so we'll go over some of the decisions we've made and but want to make sure that you really understand that as well",
                "maskedITN": "So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well",
                "display": "So we'll go over some of the decisions we've made and but want to make sure that you really understand that as well.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT49.48S",
            "duration": "PT2.64S",
            "offsetInTicks": 494800000.0,
            "durationInTicks": 26400000.0,
            "nBest": [
              {
                "confidence": 0.8828686,
                "lexical": "yeah OK sure jump into that",
                "itn": "yeah OK sure jump into that",
                "maskedITN": "Yeah OK sure jump into that",
                "display": "Yeah, OK, sure, jump into that.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT49.48S",
            "duration": "PT2.64S",
            "offsetInTicks": 494800000.0,
            "durationInTicks": 26400000.0,
            "nBest": [
              {
                "confidence": 0.8828686,
                "lexical": "yeah OK sure jump into that",
                "itn": "yeah OK sure jump into that",
                "maskedITN": "Yeah OK sure jump into that",
                "display": "Yeah, OK, sure, jump into that.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT52.12S",
            "duration": "PT2.24S",
            "offsetInTicks": 521200000.0,
            "durationInTicks": 22400000.0,
            "nBest": [
              {
                "confidence": 0.9589779,
                "lexical": "do you have any questions i can help you out with",
                "itn": "do you have any questions i can help you out with",
                "maskedITN": "Do you have any questions I can help you out with",
                "display": "Do you have any questions I can help you out with?",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.81,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT52.12S",
            "duration": "PT2.24S",
            "offsetInTicks": 521200000.0,
            "durationInTicks": 22400000.0,
            "nBest": [
              {
                "confidence": 0.9589779,
                "lexical": "do you have any questions i can help you out with",
                "itn": "do you have any questions i can help you out with",
                "maskedITN": "Do you have any questions I can help you out with",
                "display": "Do you have any questions I can help you out with?",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.81,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT55.48S",
            "duration": "PT0.72S",
            "offsetInTicks": 554800000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.97311145,
                "lexical": "no not really",
                "itn": "no not really",
                "maskedITN": "No not really",
                "display": "No, not really.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.72,
                  "negative": 0.24
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT55.48S",
            "duration": "PT0.72S",
            "offsetInTicks": 554800000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.97311145,
                "lexical": "no not really",
                "itn": "no not really",
                "maskedITN": "No not really",
                "display": "No, not really.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.72,
                  "negative": 0.24
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT56.64S",
            "duration": "PT0.36S",
            "offsetInTicks": 566400000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.20052318,
                "lexical": "nope",
                "itn": "nope",
                "maskedITN": "Nope",
                "display": "Nope.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.84,
                  "negative": 0.13
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT56.64S",
            "duration": "PT0.36S",
            "offsetInTicks": 566400000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.20052318,
                "lexical": "nope",
                "itn": "nope",
                "maskedITN": "Nope",
                "display": "Nope.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.84,
                  "negative": 0.13
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT57.36S",
            "duration": "PT7.92S",
            "offsetInTicks": 573600000.0,
            "durationInTicks": 79200000.0,
            "nBest": [
              {
                "confidence": 0.9318237,
                "lexical": "anything about your mileage expenses or anything about your equipment that you've recently purchased",
                "itn": "anything about your mileage expenses or anything about your equipment that you've recently purchased",
                "maskedITN": "Anything about your mileage expenses or anything about your equipment that you've recently purchased",
                "display": "Anything about your mileage, expenses, or anything about your equipment that you've recently purchased.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.99,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT57.36S",
            "duration": "PT7.92S",
            "offsetInTicks": 573600000.0,
            "durationInTicks": 79200000.0,
            "nBest": [
              {
                "confidence": 0.9318237,
                "lexical": "anything about your mileage expenses or anything about your equipment that you've recently purchased",
                "itn": "anything about your mileage expenses or anything about your equipment that you've recently purchased",
                "maskedITN": "Anything about your mileage expenses or anything about your equipment that you've recently purchased",
                "display": "Anything about your mileage, expenses, or anything about your equipment that you've recently purchased.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.99,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M5.28S",
            "duration": "PT0.88S",
            "offsetInTicks": 652800000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.9100634,
                "lexical": "how's that been going",
                "itn": "how's that been going",
                "maskedITN": "How's that been going",
                "display": "How's that been going?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.92,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M5.28S",
            "duration": "PT0.88S",
            "offsetInTicks": 652800000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.9100634,
                "lexical": "how's that been going",
                "itn": "how's that been going",
                "maskedITN": "How's that been going",
                "display": "How's that been going?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.92,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M7.8S",
            "duration": "PT1.12S",
            "offsetInTicks": 678000000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.91203463,
                "lexical": "no not really",
                "itn": "no not really",
                "maskedITN": "No not really",
                "display": "No, not really.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.72,
                  "negative": 0.24
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M7.8S",
            "duration": "PT1.12S",
            "offsetInTicks": 678000000.0,
            "durationInTicks": 11200000.0,
            "nBest": [
              {
                "confidence": 0.91203463,
                "lexical": "no not really",
                "itn": "no not really",
                "maskedITN": "No not really",
                "display": "No, not really.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.72,
                  "negative": 0.24
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M9.44S",
            "duration": "PT1.16S",
            "offsetInTicks": 694400000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.9160474,
                "lexical": "what do you mean by equipment",
                "itn": "what do you mean by equipment",
                "maskedITN": "What do you mean by equipment",
                "display": "What do you mean by equipment?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M9.44S",
            "duration": "PT1.16S",
            "offsetInTicks": 694400000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.9160474,
                "lexical": "what do you mean by equipment",
                "itn": "what do you mean by equipment",
                "maskedITN": "What do you mean by equipment",
                "display": "What do you mean by equipment?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M11.84S",
            "duration": "PT0.96S",
            "offsetInTicks": 718400000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.7080048,
                "lexical": "i'm glad you asked",
                "itn": "i'm glad you asked",
                "maskedITN": "I'm glad you asked",
                "display": "I'm glad you asked.",
                "sentiment": {
                  "positive": 0.94,
                  "neutral": 0.05,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M11.84S",
            "duration": "PT0.96S",
            "offsetInTicks": 718400000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.7080048,
                "lexical": "i'm glad you asked",
                "itn": "i'm glad you asked",
                "maskedITN": "I'm glad you asked",
                "display": "I'm glad you asked.",
                "sentiment": {
                  "positive": 0.94,
                  "neutral": 0.05,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M13.36S",
            "duration": "PT8.28S",
            "offsetInTicks": 733600000.0,
            "durationInTicks": 82800000.0,
            "nBest": [
              {
                "confidence": 0.89790535,
                "lexical": "some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes",
                "itn": "some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes",
                "maskedITN": "Some of the equipment that your physiotherapist recommended do you remember about I think there was the I'm just taking a look at my notes",
                "display": "Some of the equipment that your physiotherapist recommended, do you remember about, I think there was the, I'm just taking a look at my notes.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M13.36S",
            "duration": "PT8.28S",
            "offsetInTicks": 733600000.0,
            "durationInTicks": 82800000.0,
            "nBest": [
              {
                "confidence": 0.8937066,
                "lexical": "some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes",
                "itn": "some of the equipment that your physiotherapist recommended do you remember about i think there was the i'm just taking a look at my notes",
                "maskedITN": "Some of the equipment that your physiotherapist recommended do you remember about I think there was the I'm just taking a look at my notes",
                "display": "Some of the equipment that your physiotherapist recommended, do you remember about, I think there was the, I'm just taking a look at my notes.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M21.64S",
            "duration": "PT5.2S",
            "offsetInTicks": 816400000.0,
            "durationInTicks": 52000000.0,
            "nBest": [
              {
                "confidence": 0.91804343,
                "lexical": "i think there was the foam roller and the therapans",
                "itn": "i think there was the foam roller and the therapans",
                "maskedITN": "I think there was the foam roller and the therapans",
                "display": "I think there was the foam roller and the therapans.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.98,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M21.64S",
            "duration": "PT5.2S",
            "offsetInTicks": 816400000.0,
            "durationInTicks": 52000000.0,
            "nBest": [
              {
                "confidence": 0.9146794,
                "lexical": "i think there was the foam roller and the therapans",
                "itn": "i think there was the foam roller and the therapans",
                "maskedITN": "I think there was the foam roller and the therapans",
                "display": "I think there was the foam roller and the therapans.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.98,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M26.84S",
            "duration": "PT1.92S",
            "offsetInTicks": 868400000.0,
            "durationInTicks": 19200000.0,
            "nBest": [
              {
                "confidence": 0.73549825,
                "lexical": "how how how's that exercise been going",
                "itn": "how how how's that exercise been going",
                "maskedITN": "How how how's that exercise been going",
                "display": "How, how, how's that exercise been going?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M26.84S",
            "duration": "PT1.92S",
            "offsetInTicks": 868400000.0,
            "durationInTicks": 19200000.0,
            "nBest": [
              {
                "confidence": 0.7258056,
                "lexical": "how how how's that exercise been going",
                "itn": "how how how's that exercise been going",
                "maskedITN": "How how how's that exercise been going",
                "display": "How, how, how's that exercise been going?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M30.32S",
            "duration": "PT0.64S",
            "offsetInTicks": 903200000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.84904647,
                "lexical": "oh fine",
                "itn": "oh fine",
                "maskedITN": "Oh fine",
                "display": "Oh, fine.",
                "sentiment": {
                  "positive": 0.38,
                  "neutral": 0.57,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M30.32S",
            "duration": "PT0.64S",
            "offsetInTicks": 903200000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.8466611,
                "lexical": "oh fine",
                "itn": "oh fine",
                "maskedITN": "Oh fine",
                "display": "Oh, fine.",
                "sentiment": {
                  "positive": 0.38,
                  "neutral": 0.57,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M32.96S",
            "duration": "PT4.72S",
            "offsetInTicks": 929600000.0,
            "durationInTicks": 47200000.0,
            "nBest": [
              {
                "confidence": 0.95345217,
                "lexical": "anything else you'd like to share about working with that physiotherapist that we should know about though",
                "itn": "anything else you'd like to share about working with that physiotherapist that we should know about though",
                "maskedITN": "Anything else you'd like to share about working with that physiotherapist that we should know about though",
                "display": "Anything else you'd like to share about working with that physiotherapist that we should know about though?",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.82,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M32.96S",
            "duration": "PT4.68S",
            "offsetInTicks": 929600000.0,
            "durationInTicks": 46800000.0,
            "nBest": [
              {
                "confidence": 0.9552083,
                "lexical": "anything else you'd like to share about working with that physiotherapist that we should know about though",
                "itn": "anything else you'd like to share about working with that physiotherapist that we should know about though",
                "maskedITN": "Anything else you'd like to share about working with that physiotherapist that we should know about though",
                "display": "Anything else you'd like to share about working with that physiotherapist that we should know about though?",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.82,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M38.24S",
            "duration": "PT0.8S",
            "offsetInTicks": 982400000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.8275925,
                "lexical": "no it's been good",
                "itn": "no it's been good",
                "maskedITN": "No it's been good",
                "display": "No, it's been good.",
                "sentiment": {
                  "positive": 0.56,
                  "neutral": 0.33,
                  "negative": 0.11
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M38.24S",
            "duration": "PT0.8S",
            "offsetInTicks": 982400000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.8243575,
                "lexical": "no it's been good",
                "itn": "no it's been good",
                "maskedITN": "No it's been good",
                "display": "No, it's been good.",
                "sentiment": {
                  "positive": 0.56,
                  "neutral": 0.33,
                  "negative": 0.11
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M39.12S",
            "duration": "PT1.8S",
            "offsetInTicks": 991200000.0,
            "durationInTicks": 18000000.0,
            "nBest": [
              {
                "confidence": 0.743519,
                "lexical": "the the equipment 's working",
                "itn": "the the equipment's working",
                "maskedITN": "The the equipment's working",
                "display": "The the equipment's working.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.86,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M39.12S",
            "duration": "PT1.76S",
            "offsetInTicks": 991200000.0,
            "durationInTicks": 17600000.0,
            "nBest": [
              {
                "confidence": 0.74721324,
                "lexical": "the the equipment 's working",
                "itn": "the the equipment's working",
                "maskedITN": "The the equipment's working",
                "display": "The the equipment's working.",
                "sentiment": {
                  "positive": 0.13,
                  "neutral": 0.86,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M40.88S",
            "duration": "PT0.4S",
            "offsetInTicks": 1008800000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.9060857,
                "lexical": "it's good",
                "itn": "it's good",
                "maskedITN": "It's good",
                "display": "It's good.",
                "sentiment": {
                  "positive": 0.9,
                  "neutral": 0.08,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M40.92S",
            "duration": "PT0.36S",
            "offsetInTicks": 1009200000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.90608394,
                "lexical": "it's good",
                "itn": "it's good",
                "maskedITN": "It's good",
                "display": "It's good.",
                "sentiment": {
                  "positive": 0.9,
                  "neutral": 0.08,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M42.6S",
            "duration": "PT0.72S",
            "offsetInTicks": 1026000000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.9147107,
                "lexical": "that's great to hear",
                "itn": "that's great to hear",
                "maskedITN": "That's great to hear",
                "display": "That's great to hear.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M42.6S",
            "duration": "PT0.76S",
            "offsetInTicks": 1026000000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.910288,
                "lexical": "that's great to hear",
                "itn": "that's great to hear",
                "maskedITN": "That's great to hear",
                "display": "That's great to hear.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M43.92S",
            "duration": "PT2.56S",
            "offsetInTicks": 1039200000.0,
            "durationInTicks": 25600000.0,
            "nBest": [
              {
                "confidence": 0.905424,
                "lexical": "thanks so much for sharing and and for yourself",
                "itn": "thanks so much for sharing and and for yourself",
                "maskedITN": "Thanks so much for sharing and and for yourself",
                "display": "Thanks so much for sharing and and for yourself.",
                "sentiment": {
                  "positive": 0.98,
                  "neutral": 0.02,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M43.92S",
            "duration": "PT2.56S",
            "offsetInTicks": 1039200000.0,
            "durationInTicks": 25600000.0,
            "nBest": [
              {
                "confidence": 0.9029247,
                "lexical": "thanks so much for sharing and and for yourself",
                "itn": "thanks so much for sharing and and for yourself",
                "maskedITN": "Thanks so much for sharing and and for yourself",
                "display": "Thanks so much for sharing and and for yourself.",
                "sentiment": {
                  "positive": 0.98,
                  "neutral": 0.02,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M46.48S",
            "duration": "PT1.8S",
            "offsetInTicks": 1064800000.0,
            "durationInTicks": 18000000.0,
            "nBest": [
              {
                "confidence": 0.93397796,
                "lexical": "how are you finding the progress",
                "itn": "how are you finding the progress",
                "maskedITN": "How are you finding the progress",
                "display": "How are you finding the progress?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M46.48S",
            "duration": "PT1.8S",
            "offsetInTicks": 1064800000.0,
            "durationInTicks": 18000000.0,
            "nBest": [
              {
                "confidence": 0.93592834,
                "lexical": "how are you finding the progress",
                "itn": "how are you finding the progress",
                "maskedITN": "How are you finding the progress",
                "display": "How are you finding the progress?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M48.28S",
            "duration": "PT3.16S",
            "offsetInTicks": 1082800000.0,
            "durationInTicks": 31600000.0,
            "nBest": [
              {
                "confidence": 0.92635024,
                "lexical": "are you getting back to where you were before the crash",
                "itn": "are you getting back to where you were before the crash",
                "maskedITN": "Are you getting back to where you were before the crash",
                "display": "Are you getting back to where you were before the crash?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.78,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M48.28S",
            "duration": "PT3.16S",
            "offsetInTicks": 1082800000.0,
            "durationInTicks": 31600000.0,
            "nBest": [
              {
                "confidence": 0.9268655,
                "lexical": "are you getting back to where you were before the crash",
                "itn": "are you getting back to where you were before the crash",
                "maskedITN": "Are you getting back to where you were before the crash",
                "display": "Are you getting back to where you were before the crash?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.78,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M51.88S",
            "duration": "PT0.76S",
            "offsetInTicks": 1118800000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.7584607,
                "lexical": "i i guess",
                "itn": "i i guess",
                "maskedITN": "I I guess",
                "display": "I I guess.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.95,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M51.88S",
            "duration": "PT0.76S",
            "offsetInTicks": 1118800000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.7530465,
                "lexical": "i i guess",
                "itn": "i i guess",
                "maskedITN": "I I guess",
                "display": "I I guess.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.95,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M52.64S",
            "duration": "PT0.92S",
            "offsetInTicks": 1126400000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.9375593,
                "lexical": "i guess it's been OK",
                "itn": "i guess it's been OK",
                "maskedITN": "I guess it's been OK",
                "display": "I guess it's been OK.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.85,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M52.64S",
            "duration": "PT0.92S",
            "offsetInTicks": 1126400000.0,
            "durationInTicks": 9200000.0,
            "nBest": [
              {
                "confidence": 0.9334035,
                "lexical": "i guess it's been OK",
                "itn": "i guess it's been OK",
                "maskedITN": "I guess it's been OK",
                "display": "I guess it's been OK.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.85,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M53.68S",
            "duration": "PT0.32S",
            "offsetInTicks": 1136800000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.9718131,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M53.68S",
            "duration": "PT0.32S",
            "offsetInTicks": 1136800000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.9678534,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M55.64S",
            "duration": "PT6.44S",
            "offsetInTicks": 1156400000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.8809996,
                "lexical": "how i guess can you share how close are you getting to that in terms of your recovery",
                "itn": "how i guess can you share how close are you getting to that in terms of your recovery",
                "maskedITN": "How I guess can you share how close are you getting to that in terms of your recovery",
                "display": "How I guess can you share how close are you getting to that in terms of your recovery?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M55.64S",
            "duration": "PT6.48S",
            "offsetInTicks": 1156400000.0,
            "durationInTicks": 64800000.0,
            "nBest": [
              {
                "confidence": 0.88247955,
                "lexical": "how i guess can you share how close are you getting to that in terms of your recovery",
                "itn": "how i guess can you share how close are you getting to that in terms of your recovery",
                "maskedITN": "How I guess can you share how close are you getting to that in terms of your recovery",
                "display": "How I guess can you share how close are you getting to that in terms of your recovery?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M3.2S",
            "duration": "PT1.84S",
            "offsetInTicks": 1232000000.0,
            "durationInTicks": 18400000.0,
            "nBest": [
              {
                "confidence": 0.97262293,
                "lexical": "i guess i'm doing fine",
                "itn": "i guess i'm doing fine",
                "maskedITN": "I guess I'm doing fine",
                "display": "I guess I'm doing fine.",
                "sentiment": {
                  "positive": 0.37,
                  "neutral": 0.55,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M3.2S",
            "duration": "PT1.84S",
            "offsetInTicks": 1232000000.0,
            "durationInTicks": 18400000.0,
            "nBest": [
              {
                "confidence": 0.96988547,
                "lexical": "i guess i'm doing fine",
                "itn": "i guess i'm doing fine",
                "maskedITN": "I guess I'm doing fine",
                "display": "I guess I'm doing fine.",
                "sentiment": {
                  "positive": 0.37,
                  "neutral": 0.55,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M5.24S",
            "duration": "PT2.6S",
            "offsetInTicks": 1252400000.0,
            "durationInTicks": 26000000.0,
            "nBest": [
              {
                "confidence": 0.85684645,
                "lexical": "the physiotherapist seems to think it's going OK",
                "itn": "the physiotherapist seems to think it's going OK",
                "maskedITN": "The physiotherapist seems to think it's going OK",
                "display": "The physiotherapist seems to think it's going OK.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M5.24S",
            "duration": "PT2.6S",
            "offsetInTicks": 1252400000.0,
            "durationInTicks": 26000000.0,
            "nBest": [
              {
                "confidence": 0.8643191,
                "lexical": "the physiotherapist seems to think it's going OK",
                "itn": "the physiotherapist seems to think it's going OK",
                "maskedITN": "The physiotherapist seems to think it's going OK",
                "display": "The physiotherapist seems to think it's going OK.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M7.84S",
            "duration": "PT1.4S",
            "offsetInTicks": 1278400000.0,
            "durationInTicks": 14000000.0,
            "nBest": [
              {
                "confidence": 0.8284218,
                "lexical": "so i good",
                "itn": "so i good",
                "maskedITN": "So I good",
                "display": "So I good.",
                "sentiment": {
                  "positive": 0.51,
                  "neutral": 0.45,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M7.84S",
            "duration": "PT1.4S",
            "offsetInTicks": 1278400000.0,
            "durationInTicks": 14000000.0,
            "nBest": [
              {
                "confidence": 0.82896006,
                "lexical": "so i good",
                "itn": "so i good",
                "maskedITN": "So I good",
                "display": "So I good.",
                "sentiment": {
                  "positive": 0.51,
                  "neutral": 0.45,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M9.24S",
            "duration": "PT5.12S",
            "offsetInTicks": 1292400000.0,
            "durationInTicks": 51200000.0,
            "nBest": [
              {
                "confidence": 0.83659995,
                "lexical": "i guess i think you're doing really i think you're really doing really good",
                "itn": "i guess i think you're doing really i think you're really doing really good",
                "maskedITN": "I guess I think you're doing really I think you're really doing really good",
                "display": "I guess I think you're doing really, I think you're really doing really good.",
                "sentiment": {
                  "positive": 0.73,
                  "neutral": 0.22,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M9.24S",
            "duration": "PT5.12S",
            "offsetInTicks": 1292400000.0,
            "durationInTicks": 51200000.0,
            "nBest": [
              {
                "confidence": 0.8367478,
                "lexical": "i guess i think you're doing really i think you're really doing really good",
                "itn": "i guess i think you're doing really i think you're really doing really good",
                "maskedITN": "I guess I think you're doing really I think you're really doing really good",
                "display": "I guess I think you're doing really, I think you're really doing really good.",
                "sentiment": {
                  "positive": 0.73,
                  "neutral": 0.22,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M14.36S",
            "duration": "PT8.8S",
            "offsetInTicks": 1343600000.0,
            "durationInTicks": 88000000.0,
            "nBest": [
              {
                "confidence": 0.93779117,
                "lexical": "i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist",
                "itn": "i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist",
                "maskedITN": "I mean looking at the progress that you're making I'm looking at the treatment plans I'm looking at our consultation that we had with your physiotherapist",
                "display": "I mean looking at the progress that you're making, I'm looking at the treatment plans, I'm looking at our consultation that we had with your physiotherapist.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.96,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M14.36S",
            "duration": "PT8.8S",
            "offsetInTicks": 1343600000.0,
            "durationInTicks": 88000000.0,
            "nBest": [
              {
                "confidence": 0.93779117,
                "lexical": "i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist",
                "itn": "i mean looking at the progress that you're making i'm looking at the treatment plans i'm looking at our consultation that we had with your physiotherapist",
                "maskedITN": "I mean looking at the progress that you're making I'm looking at the treatment plans I'm looking at our consultation that we had with your physiotherapist",
                "display": "I mean looking at the progress that you're making, I'm looking at the treatment plans, I'm looking at our consultation that we had with your physiotherapist.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.96,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M23.16S",
            "duration": "PT1.68S",
            "offsetInTicks": 1431600000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.9650272,
                "lexical": "i think you're doing really great actually",
                "itn": "i think you're doing really great actually",
                "maskedITN": "I think you're doing really great actually",
                "display": "I think you're doing really great actually.",
                "sentiment": {
                  "positive": 0.87,
                  "neutral": 0.11,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M23.16S",
            "duration": "PT1.68S",
            "offsetInTicks": 1431600000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.9650272,
                "lexical": "i think you're doing really great actually",
                "itn": "i think you're doing really great actually",
                "maskedITN": "I think you're doing really great actually",
                "display": "I think you're doing really great actually.",
                "sentiment": {
                  "positive": 0.87,
                  "neutral": 0.11,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M24.84S",
            "duration": "PT6S",
            "offsetInTicks": 1448400000.0,
            "durationInTicks": 60000000.0,
            "nBest": [
              {
                "confidence": 0.96725637,
                "lexical": "so you might be selling yourself a little bit short here but i think we're seeing some great progress",
                "itn": "so you might be selling yourself a little bit short here but i think we're seeing some great progress",
                "maskedITN": "So you might be selling yourself a little bit short here but I think we're seeing some great progress",
                "display": "So you might be selling yourself a little bit short here, but I think we're seeing some great progress.",
                "sentiment": {
                  "positive": 0.72,
                  "neutral": 0.23,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M24.84S",
            "duration": "PT6S",
            "offsetInTicks": 1448400000.0,
            "durationInTicks": 60000000.0,
            "nBest": [
              {
                "confidence": 0.96725637,
                "lexical": "so you might be selling yourself a little bit short here but i think we're seeing some great progress",
                "itn": "so you might be selling yourself a little bit short here but i think we're seeing some great progress",
                "maskedITN": "So you might be selling yourself a little bit short here but I think we're seeing some great progress",
                "display": "So you might be selling yourself a little bit short here, but I think we're seeing some great progress.",
                "sentiment": {
                  "positive": 0.72,
                  "neutral": 0.23,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M31.52S",
            "duration": "PT1.04S",
            "offsetInTicks": 1515200000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.68114245,
                "lexical": "oh OK good",
                "itn": "oh OK good",
                "maskedITN": "Oh OK good",
                "display": "Oh, OK, good.",
                "sentiment": {
                  "positive": 0.68,
                  "neutral": 0.28,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M31.52S",
            "duration": "PT1.04S",
            "offsetInTicks": 1515200000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.68114245,
                "lexical": "oh OK good",
                "itn": "oh OK good",
                "maskedITN": "Oh OK good",
                "display": "Oh, OK, good.",
                "sentiment": {
                  "positive": 0.68,
                  "neutral": 0.28,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M32.68S",
            "duration": "PT0.48S",
            "offsetInTicks": 1526800000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.9601352,
                "lexical": "good to know",
                "itn": "good to know",
                "maskedITN": "Good to know",
                "display": "Good to know.",
                "sentiment": {
                  "positive": 0.83,
                  "neutral": 0.15,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M32.68S",
            "duration": "PT0.48S",
            "offsetInTicks": 1526800000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.9601352,
                "lexical": "good to know",
                "itn": "good to know",
                "maskedITN": "Good to know",
                "display": "Good to know.",
                "sentiment": {
                  "positive": 0.83,
                  "neutral": 0.15,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M33.4S",
            "duration": "PT0.28S",
            "offsetInTicks": 1534000000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.9672841,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M33.4S",
            "duration": "PT0.28S",
            "offsetInTicks": 1534000000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.9672841,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M35.16S",
            "duration": "PT0.48S",
            "offsetInTicks": 1551600000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.83485484,
                "lexical": "great",
                "itn": "great",
                "maskedITN": "Great",
                "display": "Great.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.02,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M35.16S",
            "duration": "PT0.48S",
            "offsetInTicks": 1551600000.0,
            "durationInTicks": 4800000.0,
            "nBest": [
              {
                "confidence": 0.83485484,
                "lexical": "great",
                "itn": "great",
                "maskedITN": "Great",
                "display": "Great.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.02,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M35.84S",
            "duration": "PT3.24S",
            "offsetInTicks": 1558400000.0,
            "durationInTicks": 32400000.0,
            "nBest": [
              {
                "confidence": 0.91331434,
                "lexical": "so just working with you on some of your other benefits as well",
                "itn": "so just working with you on some of your other benefits as well",
                "maskedITN": "So just working with you on some of your other benefits as well",
                "display": "So just working with you on some of your other benefits as well.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M35.84S",
            "duration": "PT3.24S",
            "offsetInTicks": 1558400000.0,
            "durationInTicks": 32400000.0,
            "nBest": [
              {
                "confidence": 0.91331434,
                "lexical": "so just working with you on some of your other benefits as well",
                "itn": "so just working with you on some of your other benefits as well",
                "maskedITN": "So just working with you on some of your other benefits as well",
                "display": "So just working with you on some of your other benefits as well.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M39.08S",
            "duration": "PT3.16S",
            "offsetInTicks": 1590800000.0,
            "durationInTicks": 31600000.0,
            "nBest": [
              {
                "confidence": 0.91164535,
                "lexical": "i just want to make sure i touch on your mileage",
                "itn": "i just want to make sure i touch on your mileage",
                "maskedITN": "I just want to make sure I touch on your mileage",
                "display": "I just want to make sure I touch on your mileage.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.96,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M39.08S",
            "duration": "PT3.16S",
            "offsetInTicks": 1590800000.0,
            "durationInTicks": 31600000.0,
            "nBest": [
              {
                "confidence": 0.91164535,
                "lexical": "i just want to make sure i touch on your mileage",
                "itn": "i just want to make sure i touch on your mileage",
                "maskedITN": "I just want to make sure I touch on your mileage",
                "display": "I just want to make sure I touch on your mileage.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.96,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M43.4S",
            "duration": "PT2.2S",
            "offsetInTicks": 1634000000.0,
            "durationInTicks": 22000000.0,
            "nBest": [
              {
                "confidence": 0.8745789,
                "lexical": "how's the submission been",
                "itn": "how's the submission been",
                "maskedITN": "How's the submission been",
                "display": "How's the submission been?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M43.4S",
            "duration": "PT2.2S",
            "offsetInTicks": 1634000000.0,
            "durationInTicks": 22000000.0,
            "nBest": [
              {
                "confidence": 0.8745789,
                "lexical": "how's the submission been",
                "itn": "how's the submission been",
                "maskedITN": "How's the submission been",
                "display": "How's the submission been?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M45.6S",
            "duration": "PT2.92S",
            "offsetInTicks": 1656000000.0,
            "durationInTicks": 29200000.0,
            "nBest": [
              {
                "confidence": 0.9183584,
                "lexical": "like have you had all your reimbursements received properly",
                "itn": "like have you had all your reimbursements received properly",
                "maskedITN": "Like have you had all your reimbursements received properly",
                "display": "Like have you had all your reimbursements received properly?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M45.6S",
            "duration": "PT2.92S",
            "offsetInTicks": 1656000000.0,
            "durationInTicks": 29200000.0,
            "nBest": [
              {
                "confidence": 0.9183584,
                "lexical": "like have you had all your reimbursements received properly",
                "itn": "like have you had all your reimbursements received properly",
                "maskedITN": "Like have you had all your reimbursements received properly",
                "display": "Like have you had all your reimbursements received properly?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M49.76S",
            "duration": "PT7.44S",
            "offsetInTicks": 1697600000.0,
            "durationInTicks": 74400000.0,
            "nBest": [
              {
                "confidence": 0.754047,
                "lexical": "i think so when do i have to have them in by anytime works whichever is convenient for you",
                "itn": "i think so when do i have to have them in by anytime works whichever is convenient for you",
                "maskedITN": "I think so when do I have to have them in by anytime works whichever is convenient for you",
                "display": "I think so when do I have to have them in by anytime works, whichever is convenient for you.",
                "sentiment": {
                  "positive": 0.33,
                  "neutral": 0.64,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M49.76S",
            "duration": "PT7.44S",
            "offsetInTicks": 1697600000.0,
            "durationInTicks": 74400000.0,
            "nBest": [
              {
                "confidence": 0.754047,
                "lexical": "i think so when do i have to have them in by anytime works whichever is convenient for you",
                "itn": "i think so when do i have to have them in by anytime works whichever is convenient for you",
                "maskedITN": "I think so when do I have to have them in by anytime works whichever is convenient for you",
                "display": "I think so when do I have to have them in by anytime works, whichever is convenient for you.",
                "sentiment": {
                  "positive": 0.33,
                  "neutral": 0.64,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M57.2S",
            "duration": "PT5.04S",
            "offsetInTicks": 1772000000.0,
            "durationInTicks": 50400000.0,
            "nBest": [
              {
                "confidence": 0.8917405,
                "lexical": "we have technically up to a hundred and eighty days from the date that you incur them",
                "itn": "we have technically up to 180 days from the date that you incur them",
                "maskedITN": "We have technically up to 180 days from the date that you incur them",
                "display": "We have technically up to 180 days from the date that you incur them.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M57.2S",
            "duration": "PT5.04S",
            "offsetInTicks": 1772000000.0,
            "durationInTicks": 50400000.0,
            "nBest": [
              {
                "confidence": 0.8917405,
                "lexical": "we have technically up to a hundred and eighty days from the date that you incur them",
                "itn": "we have technically up to 180 days from the date that you incur them",
                "maskedITN": "We have technically up to 180 days from the date that you incur them",
                "display": "We have technically up to 180 days from the date that you incur them.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M2.24S",
            "duration": "PT1.72S",
            "offsetInTicks": 1822400000.0,
            "durationInTicks": 17200000.0,
            "nBest": [
              {
                "confidence": 0.20779154,
                "lexical": "OK fine",
                "itn": "OK fine",
                "maskedITN": "OK fine",
                "display": "OK, fine.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.74,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M2.24S",
            "duration": "PT1.72S",
            "offsetInTicks": 1822400000.0,
            "durationInTicks": 17200000.0,
            "nBest": [
              {
                "confidence": 0.20779154,
                "lexical": "OK fine",
                "itn": "OK fine",
                "maskedITN": "OK fine",
                "display": "OK, fine.",
                "sentiment": {
                  "positive": 0.22,
                  "neutral": 0.74,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M4S",
            "duration": "PT0.64S",
            "offsetInTicks": 1840000000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.7393612,
                "lexical": "that that's OK",
                "itn": "that that's OK",
                "maskedITN": "That that's OK",
                "display": "That, that's OK.",
                "sentiment": {
                  "positive": 0.31,
                  "neutral": 0.65,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M4S",
            "duration": "PT0.64S",
            "offsetInTicks": 1840000000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.7393612,
                "lexical": "that that's OK",
                "itn": "that that's OK",
                "maskedITN": "That that's OK",
                "display": "That, that's OK.",
                "sentiment": {
                  "positive": 0.31,
                  "neutral": 0.65,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M4.64S",
            "duration": "PT0.36S",
            "offsetInTicks": 1846400000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.94788235,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M4.64S",
            "duration": "PT0.36S",
            "offsetInTicks": 1846400000.0,
            "durationInTicks": 3600000.0,
            "nBest": [
              {
                "confidence": 0.94788235,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M5S",
            "duration": "PT1.44S",
            "offsetInTicks": 1850000000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.4246265,
                "lexical": "OK great",
                "itn": "OK great",
                "maskedITN": "OK great",
                "display": "OK, great.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M5S",
            "duration": "PT1.44S",
            "offsetInTicks": 1850000000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.4246265,
                "lexical": "OK great",
                "itn": "OK great",
                "maskedITN": "OK great",
                "display": "OK, great.",
                "sentiment": {
                  "positive": 0.95,
                  "neutral": 0.04,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M7.96S",
            "duration": "PT16.52S",
            "offsetInTicks": 1879600000.0,
            "durationInTicks": 165200000.0,
            "nBest": [
              {
                "confidence": 0.94621843,
                "lexical": "now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered",
                "itn": "now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered",
                "maskedITN": "Now before I go into the treatment plan in itself and I'll share a little bit about the details here I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered",
                "display": "Now before I go into the treatment plan in itself, and I'll share a little bit about the details here, I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered.",
                "sentiment": {
                  "positive": 0.54,
                  "neutral": 0.42,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M7.96S",
            "duration": "PT16.52S",
            "offsetInTicks": 1879600000.0,
            "durationInTicks": 165200000.0,
            "nBest": [
              {
                "confidence": 0.94621843,
                "lexical": "now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered",
                "itn": "now before i go into the treatment plan in itself and i'll share a little bit about the details here i do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered",
                "maskedITN": "Now before I go into the treatment plan in itself and I'll share a little bit about the details here I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered",
                "display": "Now before I go into the treatment plan in itself, and I'll share a little bit about the details here, I do want to share that the physiotherapist has indicated that you've made some really great progress and you're largely recovered.",
                "sentiment": {
                  "positive": 0.54,
                  "neutral": 0.42,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M24.68S",
            "duration": "PT5.56S",
            "offsetInTicks": 2046800000.0,
            "durationInTicks": 55600000.0,
            "nBest": [
              {
                "confidence": 0.9390254,
                "lexical": "and at this point you're ready for discharge from the physiotherapy services",
                "itn": "and at this point you're ready for discharge from the physiotherapy services",
                "maskedITN": "And at this point you're ready for discharge from the physiotherapy services",
                "display": "And at this point, you're ready for discharge from the physiotherapy services.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M24.68S",
            "duration": "PT5.56S",
            "offsetInTicks": 2046800000.0,
            "durationInTicks": 55600000.0,
            "nBest": [
              {
                "confidence": 0.9390254,
                "lexical": "and at this point you're ready for discharge from the physiotherapy services",
                "itn": "and at this point you're ready for discharge from the physiotherapy services",
                "maskedITN": "And at this point you're ready for discharge from the physiotherapy services",
                "display": "And at this point, you're ready for discharge from the physiotherapy services.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M30.52S",
            "duration": "PT8.4S",
            "offsetInTicks": 2105200000.0,
            "durationInTicks": 84000000.0,
            "nBest": [
              {
                "confidence": 0.9220267,
                "lexical": "so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there",
                "itn": "so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there",
                "maskedITN": "So with this treatment plan I think you do have two more treatments left and you'll be able to finish those last two and go from there",
                "display": "So with this treatment plan, I think you do have two more treatments left and you'll be able to finish those last two and go from there.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M30.52S",
            "duration": "PT8.4S",
            "offsetInTicks": 2105200000.0,
            "durationInTicks": 84000000.0,
            "nBest": [
              {
                "confidence": 0.9220267,
                "lexical": "so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there",
                "itn": "so with this treatment plan i think you do have two more treatments left and you'll be able to finish those last two and go from there",
                "maskedITN": "So with this treatment plan I think you do have two more treatments left and you'll be able to finish those last two and go from there",
                "display": "So with this treatment plan, I think you do have two more treatments left and you'll be able to finish those last two and go from there.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M38.92S",
            "duration": "PT0.68S",
            "offsetInTicks": 2189200000.0,
            "durationInTicks": 6800000.0,
            "nBest": [
              {
                "confidence": 0.76153046,
                "lexical": "how's that sound",
                "itn": "how's that sound",
                "maskedITN": "How's that sound",
                "display": "How's that sound?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.93,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M38.92S",
            "duration": "PT0.68S",
            "offsetInTicks": 2189200000.0,
            "durationInTicks": 6800000.0,
            "nBest": [
              {
                "confidence": 0.76153046,
                "lexical": "how's that sound",
                "itn": "how's that sound",
                "maskedITN": "How's that sound",
                "display": "How's that sound?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.93,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M40.44S",
            "duration": "PT0.56S",
            "offsetInTicks": 2204400000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.9134377,
                "lexical": "that's good",
                "itn": "that's good",
                "maskedITN": "That's good",
                "display": "That's good.",
                "sentiment": {
                  "positive": 0.9,
                  "neutral": 0.09,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M40.44S",
            "duration": "PT0.56S",
            "offsetInTicks": 2204400000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.9134377,
                "lexical": "that's good",
                "itn": "that's good",
                "maskedITN": "That's good",
                "display": "That's good.",
                "sentiment": {
                  "positive": 0.9,
                  "neutral": 0.09,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M41S",
            "duration": "PT0.84S",
            "offsetInTicks": 2210000000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.97506356,
                "lexical": "that's good to know",
                "itn": "that's good to know",
                "maskedITN": "That's good to know",
                "display": "That's good to know.",
                "sentiment": {
                  "positive": 0.78,
                  "neutral": 0.19,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M41S",
            "duration": "PT0.84S",
            "offsetInTicks": 2210000000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.97506356,
                "lexical": "that's good to know",
                "itn": "that's good to know",
                "maskedITN": "That's good to know",
                "display": "That's good to know.",
                "sentiment": {
                  "positive": 0.78,
                  "neutral": 0.19,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M42.36S",
            "duration": "PT5.96S",
            "offsetInTicks": 2223600000.0,
            "durationInTicks": 59600000.0,
            "nBest": [
              {
                "confidence": 0.8914289,
                "lexical": "is there anything i else that you need from me anything else i need to do at this point",
                "itn": "is there anything i else that you need from me anything else i need to do at this point",
                "maskedITN": "Is there anything I else that you need from me Anything else I need to do at this point",
                "display": "Is there anything I else that you need from me, Anything else I need to do at this point?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M42.36S",
            "duration": "PT5.96S",
            "offsetInTicks": 2223600000.0,
            "durationInTicks": 59600000.0,
            "nBest": [
              {
                "confidence": 0.8914289,
                "lexical": "is there anything i else that you need from me anything else i need to do at this point",
                "itn": "is there anything i else that you need from me anything else i need to do at this point",
                "maskedITN": "Is there anything I else that you need from me Anything else I need to do at this point",
                "display": "Is there anything I else that you need from me, Anything else I need to do at this point?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.95,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M48.32S",
            "duration": "PT7S",
            "offsetInTicks": 2283200000.0,
            "durationInTicks": 70000000.0,
            "nBest": [
              {
                "confidence": 0.9604731,
                "lexical": "i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash",
                "itn": "i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash",
                "maskedITN": "I think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash",
                "display": "I think it really comes down to for yourself, like anything that you feel like you need before you so that you can get back to where you were before the crash.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.81,
                  "negative": 0.17
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M48.32S",
            "duration": "PT7S",
            "offsetInTicks": 2283200000.0,
            "durationInTicks": 70000000.0,
            "nBest": [
              {
                "confidence": 0.9604731,
                "lexical": "i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash",
                "itn": "i think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash",
                "maskedITN": "I think it really comes down to for yourself like anything that you feel like you need before you so that you can get back to where you were before the crash",
                "display": "I think it really comes down to for yourself, like anything that you feel like you need before you so that you can get back to where you were before the crash.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.81,
                  "negative": 0.17
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M56.24S",
            "duration": "PT0.8S",
            "offsetInTicks": 2362400000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.9382775,
                "lexical": "i guess i'm OK",
                "itn": "i guess i'm OK",
                "maskedITN": "I guess I'm OK",
                "display": "I guess I'm OK.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M56.24S",
            "duration": "PT0.8S",
            "offsetInTicks": 2362400000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.9382775,
                "lexical": "i guess i'm OK",
                "itn": "i guess i'm OK",
                "maskedITN": "I guess I'm OK",
                "display": "I guess I'm OK.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M57.04S",
            "duration": "PT1.68S",
            "offsetInTicks": 2370400000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.8822394,
                "lexical": "i think it's going fine",
                "itn": "i think it's going fine",
                "maskedITN": "I think it's going fine",
                "display": "I think it's going fine.",
                "sentiment": {
                  "positive": 0.36,
                  "neutral": 0.59,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M57.04S",
            "duration": "PT1.68S",
            "offsetInTicks": 2370400000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.8822394,
                "lexical": "i think it's going fine",
                "itn": "i think it's going fine",
                "maskedITN": "I think it's going fine",
                "display": "I think it's going fine.",
                "sentiment": {
                  "positive": 0.36,
                  "neutral": 0.59,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M1.12S",
            "duration": "PT0.88S",
            "offsetInTicks": 2411200000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.852337,
                "lexical": "mine is also good",
                "itn": "mine is also good",
                "maskedITN": "Mine is also good",
                "display": "Mine is also good.",
                "sentiment": {
                  "positive": 0.61,
                  "neutral": 0.35,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M1.12S",
            "duration": "PT0.88S",
            "offsetInTicks": 2411200000.0,
            "durationInTicks": 8800000.0,
            "nBest": [
              {
                "confidence": 0.852337,
                "lexical": "mine is also good",
                "itn": "mine is also good",
                "maskedITN": "Mine is also good",
                "display": "Mine is also good.",
                "sentiment": {
                  "positive": 0.61,
                  "neutral": 0.35,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M2.16S",
            "duration": "PT13.36S",
            "offsetInTicks": 2421600000.0,
            "durationInTicks": 133600000.0,
            "nBest": [
              {
                "confidence": 0.9275488,
                "lexical": "so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me",
                "itn": "so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me",
                "maskedITN": "So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions I just want to really encourage you to give me a call e-mail me",
                "display": "So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions, I just want to really encourage you to give me a call, e-mail me.",
                "sentiment": {
                  "positive": 0.25,
                  "neutral": 0.73,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M2.16S",
            "duration": "PT13.36S",
            "offsetInTicks": 2421600000.0,
            "durationInTicks": 133600000.0,
            "nBest": [
              {
                "confidence": 0.9275488,
                "lexical": "so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me",
                "itn": "so what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions i just want to really encourage you to give me a call email me",
                "maskedITN": "So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions I just want to really encourage you to give me a call e-mail me",
                "display": "So what we'll do is if there's any more recommendations from your physiotherapist as you wrap up the last two sessions, I just want to really encourage you to give me a call, e-mail me.",
                "sentiment": {
                  "positive": 0.25,
                  "neutral": 0.73,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M16.12S",
            "duration": "PT3.92S",
            "offsetInTicks": 2561200000.0,
            "durationInTicks": 39200000.0,
            "nBest": [
              {
                "confidence": 0.94388366,
                "lexical": "i'll be available for you on monday to friday and eight to four",
                "itn": "i'll be available for you on monday to friday and 8:00 to 4:00",
                "maskedITN": "I'll be available for you on Monday to Friday and 8:00 to 4:00",
                "display": "I'll be available for you on Monday to Friday and 8:00 to 4:00.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M16.12S",
            "duration": "PT3.92S",
            "offsetInTicks": 2561200000.0,
            "durationInTicks": 39200000.0,
            "nBest": [
              {
                "confidence": 0.94388366,
                "lexical": "i'll be available for you on monday to friday and eight to four",
                "itn": "i'll be available for you on monday to friday and 8:00 to 4:00",
                "maskedITN": "I'll be available for you on Monday to Friday and 8:00 to 4:00",
                "display": "I'll be available for you on Monday to Friday and 8:00 to 4:00.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M20.24S",
            "duration": "PT6.44S",
            "offsetInTicks": 2602400000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.9084115,
                "lexical": "so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations",
                "itn": "so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations",
                "maskedITN": "So as you know just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations",
                "display": "So as you know, just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations.",
                "sentiment": {
                  "positive": 0.66,
                  "neutral": 0.3,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M20.24S",
            "duration": "PT6.44S",
            "offsetInTicks": 2602400000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.9084115,
                "lexical": "so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations",
                "itn": "so as you know just give me a shout and then i'm happy to walk through those options with you if they have any further recommendations",
                "maskedITN": "So as you know just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations",
                "display": "So as you know, just give me a shout and then I'm happy to walk through those options with you if they have any further recommendations.",
                "sentiment": {
                  "positive": 0.66,
                  "neutral": 0.3,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M27.12S",
            "duration": "PT0.52S",
            "offsetInTicks": 2671200000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.92404014,
                "lexical": "sounds good",
                "itn": "sounds good",
                "maskedITN": "Sounds good",
                "display": "Sounds good.",
                "sentiment": {
                  "positive": 0.94,
                  "neutral": 0.05,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M27.12S",
            "duration": "PT0.52S",
            "offsetInTicks": 2671200000.0,
            "durationInTicks": 5200000.0,
            "nBest": [
              {
                "confidence": 0.92404014,
                "lexical": "sounds good",
                "itn": "sounds good",
                "maskedITN": "Sounds good",
                "display": "Sounds good.",
                "sentiment": {
                  "positive": 0.94,
                  "neutral": 0.05,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M28.16S",
            "duration": "PT1.44S",
            "offsetInTicks": 2681600000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.8525362,
                "lexical": "i think i've lost your email address",
                "itn": "i think i've lost your email address",
                "maskedITN": "I think I've lost your e-mail address",
                "display": "I think I've lost your e-mail address.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.07,
                  "negative": 0.93
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M28.16S",
            "duration": "PT1.44S",
            "offsetInTicks": 2681600000.0,
            "durationInTicks": 14400000.0,
            "nBest": [
              {
                "confidence": 0.8525362,
                "lexical": "i think i've lost your email address",
                "itn": "i think i've lost your email address",
                "maskedITN": "I think I've lost your e-mail address",
                "display": "I think I've lost your e-mail address.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.07,
                  "negative": 0.93
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M29.6S",
            "duration": "PT2.12S",
            "offsetInTicks": 2696000000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.9625716,
                "lexical": "can you email that to me again",
                "itn": "can you email that to me again",
                "maskedITN": "Can you e-mail that to me again",
                "display": "Can you e-mail that to me again?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M29.6S",
            "duration": "PT2.12S",
            "offsetInTicks": 2696000000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.9625716,
                "lexical": "can you email that to me again",
                "itn": "can you email that to me again",
                "maskedITN": "Can you e-mail that to me again",
                "display": "Can you e-mail that to me again?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.93,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M31.72S",
            "duration": "PT3.84S",
            "offsetInTicks": 2717200000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.85329276,
                "lexical": "yeah not a problem not a problem",
                "itn": "yeah not a problem not a problem",
                "maskedITN": "Yeah not a problem not a problem",
                "display": "Yeah, not a problem, not a problem.",
                "sentiment": {
                  "positive": 0.72,
                  "neutral": 0.22,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M31.72S",
            "duration": "PT3.84S",
            "offsetInTicks": 2717200000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.85329276,
                "lexical": "yeah not a problem not a problem",
                "itn": "yeah not a problem not a problem",
                "maskedITN": "Yeah not a problem not a problem",
                "display": "Yeah, not a problem, not a problem.",
                "sentiment": {
                  "positive": 0.72,
                  "neutral": 0.22,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M35.56S",
            "duration": "PT3.68S",
            "offsetInTicks": 2755600000.0,
            "durationInTicks": 36800000.0,
            "nBest": [
              {
                "confidence": 0.9589455,
                "lexical": "and what i'll do is i will send you an email",
                "itn": "and what i'll do is i will send you an email",
                "maskedITN": "And what I'll do is I will send you an e-mail",
                "display": "And what I'll do is I will send you an e-mail.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M35.56S",
            "duration": "PT3.68S",
            "offsetInTicks": 2755600000.0,
            "durationInTicks": 36800000.0,
            "nBest": [
              {
                "confidence": 0.9589455,
                "lexical": "and what i'll do is i will send you an email",
                "itn": "and what i'll do is i will send you an email",
                "maskedITN": "And what I'll do is I will send you an e-mail",
                "display": "And what I'll do is I will send you an e-mail.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M39.24S",
            "duration": "PT6.44S",
            "offsetInTicks": 2792400000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.9293121,
                "lexical": "i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery",
                "itn": "i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery",
                "maskedITN": "I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery",
                "display": "I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery.",
                "sentiment": {
                  "positive": 0.84,
                  "neutral": 0.14,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M39.24S",
            "duration": "PT6.44S",
            "offsetInTicks": 2792400000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.9293121,
                "lexical": "i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery",
                "itn": "i'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery",
                "maskedITN": "I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery",
                "display": "I'll actually summarize what we talked about today for you and really just celebrate what a great job you've done in your recovery.",
                "sentiment": {
                  "positive": 0.84,
                  "neutral": 0.14,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M45.92S",
            "duration": "PT4.44S",
            "offsetInTicks": 2859200000.0,
            "durationInTicks": 44400000.0,
            "nBest": [
              {
                "confidence": 0.96712214,
                "lexical": "and then also i'll be checking in with you in two weeks",
                "itn": "and then also i'll be checking in with you in two weeks",
                "maskedITN": "And then also I'll be checking in with you in two weeks",
                "display": "And then also, I'll be checking in with you in two weeks.",
                "sentiment": {
                  "positive": 0.1,
                  "neutral": 0.88,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M45.92S",
            "duration": "PT4.44S",
            "offsetInTicks": 2859200000.0,
            "durationInTicks": 44400000.0,
            "nBest": [
              {
                "confidence": 0.96712214,
                "lexical": "and then also i'll be checking in with you in two weeks",
                "itn": "and then also i'll be checking in with you in two weeks",
                "maskedITN": "And then also I'll be checking in with you in two weeks",
                "display": "And then also, I'll be checking in with you in two weeks.",
                "sentiment": {
                  "positive": 0.1,
                  "neutral": 0.88,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M50.76S",
            "duration": "PT2.12S",
            "offsetInTicks": 2907600000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.91986024,
                "lexical": "would you prefer that i email you",
                "itn": "would you prefer that i email you",
                "maskedITN": "Would you prefer that I e-mail you",
                "display": "Would you prefer that I e-mail you?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M50.76S",
            "duration": "PT2.12S",
            "offsetInTicks": 2907600000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.91986024,
                "lexical": "would you prefer that i email you",
                "itn": "would you prefer that i email you",
                "maskedITN": "Would you prefer that I e-mail you",
                "display": "Would you prefer that I e-mail you?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M52.88S",
            "duration": "PT3.84S",
            "offsetInTicks": 2928800000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.9447231,
                "lexical": "would you prefer that i call you or you just give me a call when you're ready",
                "itn": "would you prefer that i call you or you just give me a call when you're ready",
                "maskedITN": "Would you prefer that I call you or you just give me a call when you're ready",
                "display": "Would you prefer that I call you or you just give me a call when you're ready?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M52.88S",
            "duration": "PT3.84S",
            "offsetInTicks": 2928800000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.9447231,
                "lexical": "would you prefer that i call you or you just give me a call when you're ready",
                "itn": "would you prefer that i call you or you just give me a call when you're ready",
                "maskedITN": "Would you prefer that I call you or you just give me a call when you're ready",
                "display": "Would you prefer that I call you or you just give me a call when you're ready?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M56.72S",
            "duration": "PT0.96S",
            "offsetInTicks": 2967200000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.9542066,
                "lexical": "what's easier for you",
                "itn": "what's easier for you",
                "maskedITN": "What's easier for you",
                "display": "What's easier for you?",
                "sentiment": {
                  "positive": 0.19,
                  "neutral": 0.73,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M56.72S",
            "duration": "PT0.96S",
            "offsetInTicks": 2967200000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.9542066,
                "lexical": "what's easier for you",
                "itn": "what's easier for you",
                "maskedITN": "What's easier for you",
                "display": "What's easier for you?",
                "sentiment": {
                  "positive": 0.19,
                  "neutral": 0.73,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4M58.88S",
            "duration": "PT1.28S",
            "offsetInTicks": 2988800000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.8618949,
                "lexical": "anything works for me really",
                "itn": "anything works for me really",
                "maskedITN": "Anything works for me really",
                "display": "Anything works for me, really.",
                "sentiment": {
                  "positive": 0.53,
                  "neutral": 0.43,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4M58.88S",
            "duration": "PT1.28S",
            "offsetInTicks": 2988800000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.8618949,
                "lexical": "anything works for me really",
                "itn": "anything works for me really",
                "maskedITN": "Anything works for me really",
                "display": "Anything works for me, really.",
                "sentiment": {
                  "positive": 0.53,
                  "neutral": 0.43,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M0.16S",
            "duration": "PT0.64S",
            "offsetInTicks": 3001600000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.57188267,
                "lexical": "it's it's fine",
                "itn": "it's it's fine",
                "maskedITN": "It's it's fine",
                "display": "It's it's fine.",
                "sentiment": {
                  "positive": 0.35,
                  "neutral": 0.43,
                  "negative": 0.22
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M0.16S",
            "duration": "PT0.64S",
            "offsetInTicks": 3001600000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.57188267,
                "lexical": "it's it's fine",
                "itn": "it's it's fine",
                "maskedITN": "It's it's fine",
                "display": "It's it's fine.",
                "sentiment": {
                  "positive": 0.35,
                  "neutral": 0.43,
                  "negative": 0.22
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M0.8S",
            "duration": "PT2.88S",
            "offsetInTicks": 3008000000.0,
            "durationInTicks": 28800000.0,
            "nBest": [
              {
                "confidence": 0.61702377,
                "lexical": "whichever one you want to do sure",
                "itn": "whichever one you want to do sure",
                "maskedITN": "Whichever one you want to do sure",
                "display": "Whichever one you want to do, sure.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.92,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M0.8S",
            "duration": "PT2.88S",
            "offsetInTicks": 3008000000.0,
            "durationInTicks": 28800000.0,
            "nBest": [
              {
                "confidence": 0.61702377,
                "lexical": "whichever one you want to do sure",
                "itn": "whichever one you want to do sure",
                "maskedITN": "Whichever one you want to do sure",
                "display": "Whichever one you want to do, sure.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.92,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M3.68S",
            "duration": "PT2.16S",
            "offsetInTicks": 3036800000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.8646442,
                "lexical": "if that's the case then why don't we do this",
                "itn": "if that's the case then why don't we do this",
                "maskedITN": "If that's the case then why don't we do this",
                "display": "If that's the case then why don't we do this?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.8,
                  "negative": 0.17
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M3.68S",
            "duration": "PT2.16S",
            "offsetInTicks": 3036800000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.8646442,
                "lexical": "if that's the case then why don't we do this",
                "itn": "if that's the case then why don't we do this",
                "maskedITN": "If that's the case then why don't we do this",
                "display": "If that's the case then why don't we do this?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.8,
                  "negative": 0.17
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M6.72S",
            "duration": "PT9.76S",
            "offsetInTicks": 3067200000.0,
            "durationInTicks": 97600000.0,
            "nBest": [
              {
                "confidence": 0.9393919,
                "lexical": "i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it",
                "itn": "i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it",
                "maskedITN": "I'll just mark this file to to close the file in three weeks and if I don't hear back from you then we'll close it",
                "display": "I'll just mark this file to to close the file in three weeks and if I don't hear back from you, then we'll close it.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.66,
                  "negative": 0.33
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M6.72S",
            "duration": "PT9.76S",
            "offsetInTicks": 3067200000.0,
            "durationInTicks": 97600000.0,
            "nBest": [
              {
                "confidence": 0.9393919,
                "lexical": "i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it",
                "itn": "i'll just mark this file to to close the file in three weeks and if i don't hear back from you then we'll close it",
                "maskedITN": "I'll just mark this file to to close the file in three weeks and if I don't hear back from you then we'll close it",
                "display": "I'll just mark this file to to close the file in three weeks and if I don't hear back from you, then we'll close it.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.66,
                  "negative": 0.33
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M16.48S",
            "duration": "PT3.64S",
            "offsetInTicks": 3164800000.0,
            "durationInTicks": 36400000.0,
            "nBest": [
              {
                "confidence": 0.9599862,
                "lexical": "but if you do have anything that comes up in the meantime then just give me a call",
                "itn": "but if you do have anything that comes up in the meantime then just give me a call",
                "maskedITN": "But if you do have anything that comes up in the meantime then just give me a call",
                "display": "But if you do have anything that comes up in the meantime, then just give me a call.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M16.48S",
            "duration": "PT3.64S",
            "offsetInTicks": 3164800000.0,
            "durationInTicks": 36400000.0,
            "nBest": [
              {
                "confidence": 0.9599862,
                "lexical": "but if you do have anything that comes up in the meantime then just give me a call",
                "itn": "but if you do have anything that comes up in the meantime then just give me a call",
                "maskedITN": "But if you do have anything that comes up in the meantime then just give me a call",
                "display": "But if you do have anything that comes up in the meantime, then just give me a call.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.97,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M20.16S",
            "duration": "PT0.64S",
            "offsetInTicks": 3201600000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.87814784,
                "lexical": "how about that",
                "itn": "how about that",
                "maskedITN": "How about that",
                "display": "How about that?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.92,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M20.16S",
            "duration": "PT0.64S",
            "offsetInTicks": 3201600000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.87814784,
                "lexical": "how about that",
                "itn": "how about that",
                "maskedITN": "How about that",
                "display": "How about that?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.92,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M21.36S",
            "duration": "PT0.24S",
            "offsetInTicks": 3213600000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.9704338,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M21.36S",
            "duration": "PT0.24S",
            "offsetInTicks": 3213600000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.9704338,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M21.6S",
            "duration": "PT1.16S",
            "offsetInTicks": 3216000000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.77812207,
                "lexical": "and that that sounds good",
                "itn": "and that that sounds good",
                "maskedITN": "And that that sounds good",
                "display": "And that that sounds good.",
                "sentiment": {
                  "positive": 0.75,
                  "neutral": 0.22,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M21.6S",
            "duration": "PT1.16S",
            "offsetInTicks": 3216000000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.77812207,
                "lexical": "and that that sounds good",
                "itn": "and that that sounds good",
                "maskedITN": "And that that sounds good",
                "display": "And that that sounds good.",
                "sentiment": {
                  "positive": 0.75,
                  "neutral": 0.22,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M22.8S",
            "duration": "PT0.44S",
            "offsetInTicks": 3228000000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.9645603,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M22.8S",
            "duration": "PT0.44S",
            "offsetInTicks": 3228000000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.9645603,
                "lexical": "thanks",
                "itn": "thanks",
                "maskedITN": "Thanks",
                "display": "Thanks.",
                "sentiment": {
                  "positive": 0.86,
                  "neutral": 0.13,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M23.96S",
            "duration": "PT0.32S",
            "offsetInTicks": 3239600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.6862024,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M23.96S",
            "duration": "PT0.32S",
            "offsetInTicks": 3239600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.6862024,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M24.32S",
            "duration": "PT0.96S",
            "offsetInTicks": 3243200000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.9489589,
                "lexical": "absolutely fantastic",
                "itn": "absolutely fantastic",
                "maskedITN": "Absolutely fantastic",
                "display": "Absolutely fantastic.",
                "sentiment": {
                  "positive": 0.99,
                  "neutral": 0.01,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M24.32S",
            "duration": "PT0.96S",
            "offsetInTicks": 3243200000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.9489589,
                "lexical": "absolutely fantastic",
                "itn": "absolutely fantastic",
                "maskedITN": "Absolutely fantastic",
                "display": "Absolutely fantastic.",
                "sentiment": {
                  "positive": 0.99,
                  "neutral": 0.01,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M25.28S",
            "duration": "PT2.16S",
            "offsetInTicks": 3252800000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.95437413,
                "lexical": "it's always a pleasure talking to you",
                "itn": "it's always a pleasure talking to you",
                "maskedITN": "It's always a pleasure talking to you",
                "display": "It's always a pleasure talking to you.",
                "sentiment": {
                  "positive": 0.9,
                  "neutral": 0.08,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M25.28S",
            "duration": "PT2.16S",
            "offsetInTicks": 3252800000.0,
            "durationInTicks": 21600000.0,
            "nBest": [
              {
                "confidence": 0.95437413,
                "lexical": "it's always a pleasure talking to you",
                "itn": "it's always a pleasure talking to you",
                "maskedITN": "It's always a pleasure talking to you",
                "display": "It's always a pleasure talking to you.",
                "sentiment": {
                  "positive": 0.9,
                  "neutral": 0.08,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M27.44S",
            "duration": "PT3.4S",
            "offsetInTicks": 3274400000.0,
            "durationInTicks": 34000000.0,
            "nBest": [
              {
                "confidence": 0.89825946,
                "lexical": "really enjoy sharing this update with you and working with you on this",
                "itn": "really enjoy sharing this update with you and working with you on this",
                "maskedITN": "Really enjoy sharing this update with you and working with you on this",
                "display": "Really enjoy sharing this update with you and working with you on this.",
                "sentiment": {
                  "positive": 0.99,
                  "neutral": 0.01,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M27.44S",
            "duration": "PT3.4S",
            "offsetInTicks": 3274400000.0,
            "durationInTicks": 34000000.0,
            "nBest": [
              {
                "confidence": 0.89825946,
                "lexical": "really enjoy sharing this update with you and working with you on this",
                "itn": "really enjoy sharing this update with you and working with you on this",
                "maskedITN": "Really enjoy sharing this update with you and working with you on this",
                "display": "Really enjoy sharing this update with you and working with you on this.",
                "sentiment": {
                  "positive": 0.99,
                  "neutral": 0.01,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M30.84S",
            "duration": "PT2.12S",
            "offsetInTicks": 3308400000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.925952,
                "lexical": "so anything else just give me a call",
                "itn": "so anything else just give me a call",
                "maskedITN": "So anything else just give me a call",
                "display": "So anything else, just give me a call.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M30.84S",
            "duration": "PT2.12S",
            "offsetInTicks": 3308400000.0,
            "durationInTicks": 21200000.0,
            "nBest": [
              {
                "confidence": 0.925952,
                "lexical": "so anything else just give me a call",
                "itn": "so anything else just give me a call",
                "maskedITN": "So anything else just give me a call",
                "display": "So anything else, just give me a call.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M33.28S",
            "duration": "PT0.16S",
            "offsetInTicks": 3332800000.0,
            "durationInTicks": 1600000.0,
            "nBest": [
              {
                "confidence": 0.9074128,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M33.28S",
            "duration": "PT0.16S",
            "offsetInTicks": 3332800000.0,
            "durationInTicks": 1600000.0,
            "nBest": [
              {
                "confidence": 0.9074128,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M33.48S",
            "duration": "PT0.6S",
            "offsetInTicks": 3334800000.0,
            "durationInTicks": 6000000.0,
            "nBest": [
              {
                "confidence": 0.78640854,
                "lexical": "thanks eddie",
                "itn": "thanks eddie",
                "maskedITN": "Thanks Eddie",
                "display": "Thanks, Eddie.",
                "sentiment": {
                  "positive": 0.68,
                  "neutral": 0.31,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M33.48S",
            "duration": "PT0.6S",
            "offsetInTicks": 3334800000.0,
            "durationInTicks": 6000000.0,
            "nBest": [
              {
                "confidence": 0.78640854,
                "lexical": "thanks eddie",
                "itn": "thanks eddie",
                "maskedITN": "Thanks Eddie",
                "display": "Thanks, Eddie.",
                "sentiment": {
                  "positive": 0.68,
                  "neutral": 0.31,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M34.52S",
            "duration": "PT0.2S",
            "offsetInTicks": 3345200000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.55597967,
                "lexical": "great",
                "itn": "great",
                "maskedITN": "Great",
                "display": "Great.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.02,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M34.52S",
            "duration": "PT0.2S",
            "offsetInTicks": 3345200000.0,
            "durationInTicks": 2000000.0,
            "nBest": [
              {
                "confidence": 0.55597967,
                "lexical": "great",
                "itn": "great",
                "maskedITN": "Great",
                "display": "Great.",
                "sentiment": {
                  "positive": 0.97,
                  "neutral": 0.02,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT5M34.8S",
            "duration": "PT0.4S",
            "offsetInTicks": 3348000000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.9654661,
                "lexical": "thank you",
                "itn": "thank you",
                "maskedITN": "Thank you",
                "display": "Thank you.",
                "sentiment": {
                  "positive": 0.93,
                  "neutral": 0.06,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT5M34.8S",
            "duration": "PT0.4S",
            "offsetInTicks": 3348000000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.9654661,
                "lexical": "thank you",
                "itn": "thank you",
                "maskedITN": "Thank you",
                "display": "Thank you.",
                "sentiment": {
                  "positive": 0.93,
                  "neutral": 0.06,
                  "negative": 0.01
                }
              }
            ]
          }
        ]
      }
    }
},
{
    "short": {
      "audioFile": "/PositiveSpecialistNegativeCustomer.wav",
      "representativeName": "Bobby",
      "customerName": "Emily",
      "date": "04/20/2024",
      "callLength": 4,
      "summary": "Emily is frustrated with the lack of progress in her treatment and the perceived interruption in her sessions. She's also disappointed to learn that ICBC doesn't offer compensation under the enhanced care system. Despite her frustration, Bobby from ICBC assures her that he will follow up with her physiotherapist to resolve the issues with her sessions. Emily ends the call expressing her dissatisfaction.",
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
      "transcription": {
        "source": "https://github.com/ofek-zilber-icbc/ICBCHackathon2024/raw/main/backend/azure_related/PositiveSpecialistNegativeCustomer.wav",
        "timestamp": "2024-04-25T06:13:26Z",
        "durationInTicks": 2427300000,
        "duration": "PT4M2.73S",
        "combinedRecognizedPhrases": [
          {
            "channel": 0,
            "lexical": "hi may i speak to emily please yep this is emily hi emily this is bobby calling from ICBC how are you doing i'm OK i'm kind of busy what do you need oh i'm sorry to hear that is there a better time to reach her do you have a few minutes now to talk about your claim yeah i guess we can talk now if we have to OK and how are things going with you right now not good like every morning i wake up i'm in so much pain i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment my doctor agrees i need treatment too what's going on i'm actually really sorry to hear that emily i can understand that you'd be frustrated if you haven't heard back can i ask when the last time was that you did hear an update i don't know it feels like a really long time like at least eight weeks or so OK yeah that that shouldn't happen and let's look into that right now so we can sort things out for you if you have a few minutes i'm just going to ask you from the last couple of physios that you did how you felt things were going i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do honestly it's been like a year and a half and i don't feel like i've made any progress at all like i you know it's so disruptive to my life i go to treatment three times a week now i've been paying for it out of pocket the last two months and i'm not feeling any better OK i'm i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening so let's take care of that for you i'll get that information from you in a second but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist i'm just wondering why you were thinking you weren't able to go for a reason yeah they told me that the treatment was cut off by ACDC and i had to pay sorry who who told you that the physiotherapist i'm really sorry to hear that OK we can clear that up with them but there there are some sessions left but you know what i don't want you to have to worry about this you leave that with me i will contact your physiotherapist and follow up with you i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery is there anything else that's going on right now that i can help with yeah i mean you know whatever if my treatment is going to be cut off like you know that's annoying it's unfair because i still need treatment but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that ICBC doesn't supply compensation for your claim since we started with enhanced care we talked about this in the beginning of your claim so i wanted to make sure that you understand and please ask me any questions about it but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment you mentioned that you've been going to physio for about a year and a half so that's part of the benefits that you get with your claim and i know that we followed up with your doctor as well to check on your recovery and how you're doing those are are the things that we want to do to support you there isn't any compensation amount what there's no more compensation so i've been struggling with this injury i have been wasting all my time going to treatment and i'm not even going to get any money for it we we don't have compensation anymore emily that is correct OK whatever bye",
            "itn": "hi may i speak to emily please yep this is emily hi emily this is bobby calling from ICBC how are you doing i'm OK i'm kind of busy what do you need oh i'm sorry to hear that is there a better time to reach her do you have a few minutes now to talk about your claim yeah i guess we can talk now if we have to OK and how are things going with you right now not good like every morning i wake up i'm in so much pain i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment my doctor agrees i need treatment too what's going on i'm actually really sorry to hear that emily i can understand that you'd be frustrated if you haven't heard back can i ask when the last time was that you did hear an update i don't know it feels like a really long time like at least eight weeks or so OK yeah that that shouldn't happen and let's look into that right now so we can sort things out for you if you have a few minutes i'm just going to ask you from the last couple of physios that you did how you felt things were going i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do honestly it's been like a year and a half and i don't feel like i've made any progress at all like i you know it's so disruptive to my life i go to treatment three times a week now i've been paying for it out of pocket the last two months and i'm not feeling any better OK i'm i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening so let's take care of that for you i'll get that information from you in a second but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist i'm just wondering why you were thinking you weren't able to go for a reason yeah they told me that the treatment was cut off by ACDC and i had to pay sorry who who told you that the physiotherapist i'm really sorry to hear that OK we can clear that up with them but there there are some sessions left but you know what i don't want you to have to worry about this you leave that with me i will contact your physiotherapist and follow up with you i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery is there anything else that's going on right now that i can help with yeah i mean you know whatever if my treatment is going to be cut off like you know that's annoying it's unfair because i still need treatment but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that ICBC doesn't supply compensation for your claim since we started with enhanced care we talked about this in the beginning of your claim so i wanted to make sure that you understand and please ask me any questions about it but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment you mentioned that you've been going to physio for about a year and a half so that's part of the benefits that you get with your claim and i know that we followed up with your doctor as well to check on your recovery and how you're doing those are are the things that we want to do to support you there isn't any compensation amount what there's no more compensation so i've been struggling with this injury i have been wasting all my time going to treatment and i'm not even going to get any money for it we we don't have compensation anymore emily that is correct OK whatever bye",
            "maskedITN": "Hi May I speak to Emily please Yep this is Emily Hi Emily This is Bobby calling from ICBC How are you doing I'm OK I'm kind of busy What do you need Oh I'm sorry to hear that Is there a better time to reach her Do you have a few minutes now to talk about your claim Yeah I guess we can talk now if we have to OK And how are things going with you right now Not good Like every morning I wake up I'm in so much pain I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment My doctor agrees I need treatment too What's going on I'm actually really sorry to hear that Emily I can understand that you'd be frustrated if you haven't heard back Can I ask when the last time was that you did hear an update I don't know It feels like a really long time like at least eight weeks or so OK Yeah that that shouldn't happen And let's look into that right now so we can sort things out for you if you have a few minutes I'm just going to ask you from the last couple of physios that you did how you felt things were going I'm just looking at your file here and it looks like you were finding that it was a little bit helpful but I just wanted to check now to see what your thoughts were and see what we can do Honestly it's been like a year and a half and I don't feel like I've made any progress at all Like I you know it's so disruptive to my life I go to treatment three times a week now I've been paying for it out of pocket the last two months and I'm not feeling any better OK I'm I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening So let's take care of that for you I'll get that information from you in a second But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist I'm just wondering why you were thinking you weren't able to go for a reason Yeah They told me that the treatment was cut off by ACDC and I had to pay Sorry Who Who told you that The physiotherapist I'm really sorry to hear that OK we can clear that up with them But there there are some sessions left But you know what I don't want you to have to worry about this You leave that with me I will contact your physiotherapist and follow up with you I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery Is there anything else that's going on right now that I can help with Yeah I mean you know whatever If my treatment is going to be cut off like you know that's annoying It's unfair because I still need treatment But I guess you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today You know Emily I just wanted to clarify I know we've talked about this before as well but I just wanted to make sure that you are clear that we actually don't do that ICBC doesn't supply compensation for your claim since we started with enhanced care We talked about this in the beginning of your claim So I wanted to make sure that you understand and please ask me any questions about it But overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment You mentioned that you've been going to physio for about a year and a half So that's part of the benefits that you get with your claim And I know that we followed up with your doctor as well to check on your recovery and how you're doing Those are are the things that we want to do to support you There isn't any compensation amount What there's no more compensation So I've been struggling with this injury I have been wasting all my time going to treatment and I'm not even going to get any money for it We we don't have compensation anymore Emily that is correct OK whatever Bye",
            "display": "Hi. May I speak to Emily, please? Yep, this is Emily. Hi, Emily. This is Bobby calling from ICBC. How are you doing? I'm OK. I'm kind of busy. What do you need? Oh, I'm sorry to hear that. Is there a better time to reach her? Do you have a few minutes now to talk about your claim? Yeah, I guess we can talk now if we have to. OK. And how are things going with you right now? Not good. Like every morning I wake up, I'm in so much pain. I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment. My doctor agrees I need treatment too. What's going on? I'm actually really sorry to hear that, Emily. I can understand that you'd be frustrated if you haven't heard back. Can I ask, when the last time was that you did hear an update? I don't know. It feels like a really long time, like at least eight weeks or so. OK, Yeah, that that shouldn't happen. And let's look into that right now so we can sort things out for you if you have a few minutes. I'm just going to ask you from the last couple of physios that you did, how you felt things were going. I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can do. Honestly, it's been like a year and a half and I don't feel like I've made any progress at all. Like I, you know, it's so disruptive to my life. I go to treatment three times a week now. I've been paying for it out of pocket the last two months and I'm not feeling any better. OK, I'm. I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening. So let's take care of that for you. I'll get that information from you in a second. But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go. I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist. I'm just wondering why you were thinking you weren't able to go for a reason. Yeah. They told me that the treatment was cut off by ACDC and I had to pay. Sorry. Who? Who told you that? The physiotherapist. I'm really sorry to hear that. OK, we can clear that up with them. But there there are some sessions left. But you know what? I don't want you to have to worry about this. You leave that with me. I will contact your physiotherapist and follow up with you. I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery. Is there anything else that's going on right now that I can help with? Yeah, I mean, you know, whatever. If my treatment is going to be cut off, like, you know, that's annoying. It's unfair because I still need treatment. But I guess, you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today? You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you are clear that we actually don't do that. ICBC doesn't supply compensation for your claim since we started with enhanced care. We talked about this in the beginning of your claim. So I wanted to make sure that you understand and please ask me any questions about it. But overall what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment. You mentioned that you've been going to physio for about a year and a half. So that's part of the benefits that you get with your claim. And I know that we followed up with your doctor as well to check on your recovery and how you're doing. Those are are the things that we want to do to support you. There isn't any compensation amount. What there's no more compensation. So I've been struggling with this injury. I have been wasting all my time going to treatment and I'm not even going to get any money for it. We we don't have compensation anymore. Emily, that is correct. OK, whatever. Bye."
          },
          {
            "channel": 1,
            "lexical": "hi may i speak to emily please yep this is emily hi emily this is bobby calling from ICBC how are you doing i'm OK i'm kind of busy what do you need oh i'm sorry to hear that is there a better time to reach her do you have a few minutes now to talk about your claim yeah i guess we can talk now if we have to OK and how are things going with you right now not good like every morning i wake up i'm in so much pain i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment my doctor agrees i need treatment too what's going on i'm actually really sorry to hear that emily i can understand that you'd be frustrated if you haven't heard back can i ask when the last time was that you did hear an update i don't know it feels like a really long time like at least eight weeks or so OK yeah that that shouldn't happen and let's look into that right now so we can sort things out for you if you have a few minutes i'm just going to ask you from the last couple of physios that you did how you felt things were going i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do honestly it's been like a year and a half and i don't feel like i've made any progress at all like i you know it's so disruptive to my life i go to treatment three times a week now i've been paying for it out of pocket the last two months and i'm not feeling any better OK i'm i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening so let's take care of that for you i'll get that information from you in a second but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist i'm just wondering why you were thinking you weren't able to go for a reason yeah they told me that the treatment was cut off by ACDC and i had to pay sorry who who told you that the physiotherapist i'm really sorry to hear that OK we can clear that up with them but there there are some sessions left but you know what i don't want you to have to worry about this you leave that with me i will contact your physiotherapist and follow up with you i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery is there anything else that's going on right now that i can help with yeah i mean you know whatever if my treatment is going to be cut off like you know that's annoying it's unfair because i still need treatment but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that ICBC doesn't supply compensation for your claim since we started with enhanced care we talked about this in the beginning of your claim so i wanted to make sure that you understand and please ask me any questions about it but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment you mentioned that you've been going to physio for about a year and a half so that's part of the benefits that you get with your claim and i know that we followed up with your doctor as well to check on your recovery and how you're doing those are are the things that we want to do to support you there isn't any compensation amount what there's no more compensation so i've been struggling with this injury i have been wasting all my time going to treatment and i'm not even going to get any money for it we we don't have compensation anymore emily that is correct OK whatever bye",
            "itn": "hi may i speak to emily please yep this is emily hi emily this is bobby calling from ICBC how are you doing i'm OK i'm kind of busy what do you need oh i'm sorry to hear that is there a better time to reach her do you have a few minutes now to talk about your claim yeah i guess we can talk now if we have to OK and how are things going with you right now not good like every morning i wake up i'm in so much pain i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment my doctor agrees i need treatment too what's going on i'm actually really sorry to hear that emily i can understand that you'd be frustrated if you haven't heard back can i ask when the last time was that you did hear an update i don't know it feels like a really long time like at least eight weeks or so OK yeah that that shouldn't happen and let's look into that right now so we can sort things out for you if you have a few minutes i'm just going to ask you from the last couple of physios that you did how you felt things were going i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do honestly it's been like a year and a half and i don't feel like i've made any progress at all like i you know it's so disruptive to my life i go to treatment three times a week now i've been paying for it out of pocket the last two months and i'm not feeling any better OK i'm i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening so let's take care of that for you i'll get that information from you in a second but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist i'm just wondering why you were thinking you weren't able to go for a reason yeah they told me that the treatment was cut off by ACDC and i had to pay sorry who who told you that the physiotherapist i'm really sorry to hear that OK we can clear that up with them but there there are some sessions left but you know what i don't want you to have to worry about this you leave that with me i will contact your physiotherapist and follow up with you i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery is there anything else that's going on right now that i can help with yeah i mean you know whatever if my treatment is going to be cut off like you know that's annoying it's unfair because i still need treatment but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that ICBC doesn't supply compensation for your claim since we started with enhanced care we talked about this in the beginning of your claim so i wanted to make sure that you understand and please ask me any questions about it but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment you mentioned that you've been going to physio for about a year and a half so that's part of the benefits that you get with your claim and i know that we followed up with your doctor as well to check on your recovery and how you're doing those are are the things that we want to do to support you there isn't any compensation amount what there's no more compensation so i've been struggling with this injury i have been wasting all my time going to treatment and i'm not even going to get any money for it we we don't have compensation anymore emily that is correct OK whatever bye",
            "maskedITN": "Hi May I speak to Emily please Yep this is Emily Hi Emily This is Bobby calling from ICBC How are you doing I'm OK I'm kind of busy What do you need Oh I'm sorry to hear that Is there a better time to reach her Do you have a few minutes now to talk about your claim Yeah I guess we can talk now if we have to OK And how are things going with you right now Not good Like every morning I wake up I'm in so much pain I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment My doctor agrees I need treatment too What's going on I'm actually really sorry to hear that Emily I can understand that you'd be frustrated if you haven't heard back Can I ask when the last time was that you did hear an update I don't know It feels like a really long time like at least eight weeks or so OK Yeah that that shouldn't happen And let's look into that right now so we can sort things out for you if you have a few minutes I'm just going to ask you from the last couple of physios that you did how you felt things were going I'm just looking at your file here and it looks like you were finding that it was a little bit helpful but I just wanted to check now to see what your thoughts were and see what we can do Honestly it's been like a year and a half and I don't feel like I've made any progress at all Like I you know it's so disruptive to my life I go to treatment three times a week now I've been paying for it out of pocket the last two months and I'm not feeling any better OK I'm I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening So let's take care of that for you I'll get that information from you in a second But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist I'm just wondering why you were thinking you weren't able to go for a reason Yeah They told me that the treatment was cut off by ACDC and I had to pay Sorry Who Who told you that The physiotherapist I'm really sorry to hear that OK we can clear that up with them But there there are some sessions left But you know what I don't want you to have to worry about this You leave that with me I will contact your physiotherapist and follow up with you I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery Is there anything else that's going on right now that I can help with Yeah I mean you know whatever If my treatment is going to be cut off like you know that's annoying It's unfair because I still need treatment But I guess you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today You know Emily I just wanted to clarify I know we've talked about this before as well but I just wanted to make sure that you are clear that we actually don't do that ICBC doesn't supply compensation for your claim since we started with enhanced care We talked about this in the beginning of your claim So I wanted to make sure that you understand and please ask me any questions about it But overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment You mentioned that you've been going to physio for about a year and a half So that's part of the benefits that you get with your claim And I know that we followed up with your doctor as well to check on your recovery and how you're doing Those are are the things that we want to do to support you There isn't any compensation amount What there's no more compensation So I've been struggling with this injury I have been wasting all my time going to treatment and I'm not even going to get any money for it We we don't have compensation anymore Emily that is correct OK whatever Bye",
            "display": "Hi. May I speak to Emily, please? Yep, this is Emily. Hi, Emily. This is Bobby calling from ICBC. How are you doing? I'm OK. I'm kind of busy. What do you need? Oh, I'm sorry to hear that. Is there a better time to reach her? Do you have a few minutes now to talk about your claim? Yeah, I guess we can talk now if we have to. OK. And how are things going with you right now? Not good. Like every morning I wake up, I'm in so much pain. I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment. My doctor agrees I need treatment too. What's going on? I'm actually really sorry to hear that, Emily. I can understand that you'd be frustrated if you haven't heard back. Can I ask, when the last time was that you did hear an update? I don't know. It feels like a really long time, like at least eight weeks or so. OK, Yeah, that that shouldn't happen. And let's look into that right now so we can sort things out for you if you have a few minutes. I'm just going to ask you from the last couple of physios that you did, how you felt things were going. I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can do. Honestly, it's been like a year and a half and I don't feel like I've made any progress at all. Like I, you know, it's so disruptive to my life. I go to treatment three times a week now. I've been paying for it out of pocket the last two months and I'm not feeling any better. OK, I'm. I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening. So let's take care of that for you. I'll get that information from you in a second. But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go. I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist. I'm just wondering why you were thinking you weren't able to go for a reason. Yeah. They told me that the treatment was cut off by ACDC and I had to pay. Sorry. Who? Who told you that? The physiotherapist. I'm really sorry to hear that. OK, we can clear that up with them. But there there are some sessions left. But you know what? I don't want you to have to worry about this. You leave that with me. I will contact your physiotherapist and follow up with you. I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery. Is there anything else that's going on right now that I can help with? Yeah, I mean, you know, whatever. If my treatment is going to be cut off, like, you know, that's annoying. It's unfair because I still need treatment. But I guess, you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today? You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you are clear that we actually don't do that. ICBC doesn't supply compensation for your claim since we started with enhanced care. We talked about this in the beginning of your claim. So I wanted to make sure that you understand and please ask me any questions about it. But overall what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment. You mentioned that you've been going to physio for about a year and a half. So that's part of the benefits that you get with your claim. And I know that we followed up with your doctor as well to check on your recovery and how you're doing. Those are are the things that we want to do to support you. There isn't any compensation amount. What there's no more compensation. So I've been struggling with this injury. I have been wasting all my time going to treatment and I'm not even going to get any money for it. We we don't have compensation anymore. Emily, that is correct. OK, whatever. Bye."
          }
        ],
        "recognizedPhrases": [
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2.88S",
            "duration": "PT0.28S",
            "offsetInTicks": 28800000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.9437071,
                "lexical": "hi",
                "itn": "hi",
                "maskedITN": "Hi",
                "display": "Hi.",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.8,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2.88S",
            "duration": "PT0.28S",
            "offsetInTicks": 28800000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.93053186,
                "lexical": "hi",
                "itn": "hi",
                "maskedITN": "Hi",
                "display": "Hi.",
                "sentiment": {
                  "positive": 0.16,
                  "neutral": 0.8,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3.16S",
            "duration": "PT1.36S",
            "offsetInTicks": 31600000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.86563975,
                "lexical": "may i speak to emily please",
                "itn": "may i speak to emily please",
                "maskedITN": "May I speak to Emily please",
                "display": "May I speak to Emily, please?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.86,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3.16S",
            "duration": "PT1.36S",
            "offsetInTicks": 31600000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.8899218,
                "lexical": "may i speak to emily please",
                "itn": "may i speak to emily please",
                "maskedITN": "May I speak to Emily please",
                "display": "May I speak to Emily, please?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.86,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT4.68S",
            "duration": "PT1.16S",
            "offsetInTicks": 46800000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.7512417,
                "lexical": "yep this is emily",
                "itn": "yep this is emily",
                "maskedITN": "Yep this is Emily",
                "display": "Yep, this is Emily.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT4.68S",
            "duration": "PT1.16S",
            "offsetInTicks": 46800000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.72893906,
                "lexical": "yep this is emily",
                "itn": "yep this is emily",
                "maskedITN": "Yep this is Emily",
                "display": "Yep, this is Emily.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT6.24S",
            "duration": "PT0.72S",
            "offsetInTicks": 62400000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.9092696,
                "lexical": "hi emily",
                "itn": "hi emily",
                "maskedITN": "Hi Emily",
                "display": "Hi, Emily.",
                "sentiment": {
                  "positive": 0.19,
                  "neutral": 0.76,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT6.24S",
            "duration": "PT0.72S",
            "offsetInTicks": 62400000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.927262,
                "lexical": "hi emily",
                "itn": "hi emily",
                "maskedITN": "Hi Emily",
                "display": "Hi, Emily.",
                "sentiment": {
                  "positive": 0.19,
                  "neutral": 0.76,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT6.96S",
            "duration": "PT1.72S",
            "offsetInTicks": 69600000.0,
            "durationInTicks": 17200000.0,
            "nBest": [
              {
                "confidence": 0.9051591,
                "lexical": "this is bobby calling from ICBC",
                "itn": "this is bobby calling from ICBC",
                "maskedITN": "This is Bobby calling from ICBC",
                "display": "This is Bobby calling from ICBC.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.99,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT6.96S",
            "duration": "PT1.72S",
            "offsetInTicks": 69600000.0,
            "durationInTicks": 17200000.0,
            "nBest": [
              {
                "confidence": 0.90150267,
                "lexical": "this is bobby calling from ICBC",
                "itn": "this is bobby calling from ICBC",
                "maskedITN": "This is Bobby calling from ICBC",
                "display": "This is Bobby calling from ICBC.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.99,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT8.68S",
            "duration": "PT0.76S",
            "offsetInTicks": 86800000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.97374713,
                "lexical": "how are you doing",
                "itn": "how are you doing",
                "maskedITN": "How are you doing",
                "display": "How are you doing?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.88,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT8.68S",
            "duration": "PT0.76S",
            "offsetInTicks": 86800000.0,
            "durationInTicks": 7600000.0,
            "nBest": [
              {
                "confidence": 0.9709842,
                "lexical": "how are you doing",
                "itn": "how are you doing",
                "maskedITN": "How are you doing",
                "display": "How are you doing?",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.88,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT10.92S",
            "duration": "PT0.44S",
            "offsetInTicks": 109200000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.94321966,
                "lexical": "i'm OK",
                "itn": "i'm OK",
                "maskedITN": "I'm OK",
                "display": "I'm OK.",
                "sentiment": {
                  "positive": 0.2,
                  "neutral": 0.71,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT10.96S",
            "duration": "PT0.4S",
            "offsetInTicks": 109600000.0,
            "durationInTicks": 4000000.0,
            "nBest": [
              {
                "confidence": 0.93666327,
                "lexical": "i'm OK",
                "itn": "i'm OK",
                "maskedITN": "I'm OK",
                "display": "I'm OK.",
                "sentiment": {
                  "positive": 0.2,
                  "neutral": 0.71,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT11.36S",
            "duration": "PT0.84S",
            "offsetInTicks": 113600000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.9090486,
                "lexical": "i'm kind of busy",
                "itn": "i'm kind of busy",
                "maskedITN": "I'm kind of busy",
                "display": "I'm kind of busy.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.72,
                  "negative": 0.23
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT11.36S",
            "duration": "PT0.84S",
            "offsetInTicks": 113600000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.90496814,
                "lexical": "i'm kind of busy",
                "itn": "i'm kind of busy",
                "maskedITN": "I'm kind of busy",
                "display": "I'm kind of busy.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.72,
                  "negative": 0.23
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT12.24S",
            "duration": "PT0.64S",
            "offsetInTicks": 122400000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.95850545,
                "lexical": "what do you need",
                "itn": "what do you need",
                "maskedITN": "What do you need",
                "display": "What do you need?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT12.24S",
            "duration": "PT0.64S",
            "offsetInTicks": 122400000.0,
            "durationInTicks": 6400000.0,
            "nBest": [
              {
                "confidence": 0.9622505,
                "lexical": "what do you need",
                "itn": "what do you need",
                "maskedITN": "What do you need",
                "display": "What do you need?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT13.64S",
            "duration": "PT1.28S",
            "offsetInTicks": 136400000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.7997146,
                "lexical": "oh i'm sorry to hear that",
                "itn": "oh i'm sorry to hear that",
                "maskedITN": "Oh I'm sorry to hear that",
                "display": "Oh, I'm sorry to hear that.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.05,
                  "negative": 0.92
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT13.64S",
            "duration": "PT1.28S",
            "offsetInTicks": 136400000.0,
            "durationInTicks": 12800000.0,
            "nBest": [
              {
                "confidence": 0.7997102,
                "lexical": "oh i'm sorry to hear that",
                "itn": "oh i'm sorry to hear that",
                "maskedITN": "Oh I'm sorry to hear that",
                "display": "Oh, I'm sorry to hear that.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.05,
                  "negative": 0.92
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT14.92S",
            "duration": "PT1.2S",
            "offsetInTicks": 149200000.0,
            "durationInTicks": 12000000.0,
            "nBest": [
              {
                "confidence": 0.87947285,
                "lexical": "is there a better time to reach her",
                "itn": "is there a better time to reach her",
                "maskedITN": "Is there a better time to reach her",
                "display": "Is there a better time to reach her?",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.91,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT14.92S",
            "duration": "PT1.2S",
            "offsetInTicks": 149200000.0,
            "durationInTicks": 12000000.0,
            "nBest": [
              {
                "confidence": 0.90727335,
                "lexical": "is there a better time to reach her",
                "itn": "is there a better time to reach her",
                "maskedITN": "Is there a better time to reach her",
                "display": "Is there a better time to reach her?",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.91,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT16.12S",
            "duration": "PT2.04S",
            "offsetInTicks": 161200000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.9318125,
                "lexical": "do you have a few minutes now to talk about your claim",
                "itn": "do you have a few minutes now to talk about your claim",
                "maskedITN": "Do you have a few minutes now to talk about your claim",
                "display": "Do you have a few minutes now to talk about your claim?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT16.12S",
            "duration": "PT2.04S",
            "offsetInTicks": 161200000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.93921983,
                "lexical": "do you have a few minutes now to talk about your claim",
                "itn": "do you have a few minutes now to talk about your claim",
                "maskedITN": "Do you have a few minutes now to talk about your claim",
                "display": "Do you have a few minutes now to talk about your claim?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT18.2S",
            "duration": "PT2.44S",
            "offsetInTicks": 182000000.0,
            "durationInTicks": 24400000.0,
            "nBest": [
              {
                "confidence": 0.9638122,
                "lexical": "yeah i guess we can talk now if we have to",
                "itn": "yeah i guess we can talk now if we have to",
                "maskedITN": "Yeah I guess we can talk now if we have to",
                "display": "Yeah, I guess we can talk now if we have to.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT18.2S",
            "duration": "PT2.44S",
            "offsetInTicks": 182000000.0,
            "durationInTicks": 24400000.0,
            "nBest": [
              {
                "confidence": 0.9651416,
                "lexical": "yeah i guess we can talk now if we have to",
                "itn": "yeah i guess we can talk now if we have to",
                "maskedITN": "Yeah I guess we can talk now if we have to",
                "display": "Yeah, I guess we can talk now if we have to.",
                "sentiment": {
                  "positive": 0.06,
                  "neutral": 0.93,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT21.96S",
            "duration": "PT0.56S",
            "offsetInTicks": 219600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.7774918,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT21.96S",
            "duration": "PT0.56S",
            "offsetInTicks": 219600000.0,
            "durationInTicks": 5600000.0,
            "nBest": [
              {
                "confidence": 0.79460377,
                "lexical": "OK",
                "itn": "OK",
                "maskedITN": "OK",
                "display": "OK.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.9,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT22.52S",
            "duration": "PT2.08S",
            "offsetInTicks": 225200000.0,
            "durationInTicks": 20800000.0,
            "nBest": [
              {
                "confidence": 0.9755057,
                "lexical": "and how are things going with you right now",
                "itn": "and how are things going with you right now",
                "maskedITN": "And how are things going with you right now",
                "display": "And how are things going with you right now?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT22.52S",
            "duration": "PT2.08S",
            "offsetInTicks": 225200000.0,
            "durationInTicks": 20800000.0,
            "nBest": [
              {
                "confidence": 0.9768235,
                "lexical": "and how are things going with you right now",
                "itn": "and how are things going with you right now",
                "maskedITN": "And how are things going with you right now",
                "display": "And how are things going with you right now?",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT24.8S",
            "duration": "PT0.8S",
            "offsetInTicks": 248000000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.9690535,
                "lexical": "not good",
                "itn": "not good",
                "maskedITN": "Not good",
                "display": "Not good.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.01,
                  "negative": 0.98
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT24.8S",
            "duration": "PT0.8S",
            "offsetInTicks": 248000000.0,
            "durationInTicks": 8000000.0,
            "nBest": [
              {
                "confidence": 0.970397,
                "lexical": "not good",
                "itn": "not good",
                "maskedITN": "Not good",
                "display": "Not good.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.01,
                  "negative": 0.98
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT25.6S",
            "duration": "PT3.12S",
            "offsetInTicks": 256000000.0,
            "durationInTicks": 31200000.0,
            "nBest": [
              {
                "confidence": 0.9681473,
                "lexical": "like every morning i wake up i'm in so much pain",
                "itn": "like every morning i wake up i'm in so much pain",
                "maskedITN": "Like every morning I wake up I'm in so much pain",
                "display": "Like every morning I wake up, I'm in so much pain.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.05,
                  "negative": 0.94
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT25.6S",
            "duration": "PT3.12S",
            "offsetInTicks": 256000000.0,
            "durationInTicks": 31200000.0,
            "nBest": [
              {
                "confidence": 0.97015387,
                "lexical": "like every morning i wake up i'm in so much pain",
                "itn": "like every morning i wake up i'm in so much pain",
                "maskedITN": "Like every morning I wake up I'm in so much pain",
                "display": "Like every morning I wake up, I'm in so much pain.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.05,
                  "negative": 0.94
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT29.08S",
            "duration": "PT7.12S",
            "offsetInTicks": 290800000.0,
            "durationInTicks": 71200000.0,
            "nBest": [
              {
                "confidence": 0.9306106,
                "lexical": "i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment",
                "itn": "i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment",
                "maskedITN": "I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment",
                "display": "I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.91,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT29.08S",
            "duration": "PT7.12S",
            "offsetInTicks": 290800000.0,
            "durationInTicks": 71200000.0,
            "nBest": [
              {
                "confidence": 0.9306106,
                "lexical": "i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment",
                "itn": "i know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like i need treatment",
                "maskedITN": "I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment",
                "display": "I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything like I need treatment.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.91,
                  "negative": 0.08
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT36.2S",
            "duration": "PT1.96S",
            "offsetInTicks": 362000000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.8742485,
                "lexical": "my doctor agrees i need treatment too",
                "itn": "my doctor agrees i need treatment too",
                "maskedITN": "My doctor agrees I need treatment too",
                "display": "My doctor agrees I need treatment too.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.8,
                  "negative": 0.17
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT36.2S",
            "duration": "PT1.96S",
            "offsetInTicks": 362000000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.8742485,
                "lexical": "my doctor agrees i need treatment too",
                "itn": "my doctor agrees i need treatment too",
                "maskedITN": "My doctor agrees I need treatment too",
                "display": "My doctor agrees I need treatment too.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.8,
                  "negative": 0.17
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT38.16S",
            "duration": "PT0.84S",
            "offsetInTicks": 381600000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.96910393,
                "lexical": "what's going on",
                "itn": "what's going on",
                "maskedITN": "What's going on",
                "display": "What's going on?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.76,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT38.16S",
            "duration": "PT0.84S",
            "offsetInTicks": 381600000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.96910393,
                "lexical": "what's going on",
                "itn": "what's going on",
                "maskedITN": "What's going on",
                "display": "What's going on?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.76,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT39.08S",
            "duration": "PT2.04S",
            "offsetInTicks": 390800000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.89951,
                "lexical": "i'm actually really sorry to hear that emily",
                "itn": "i'm actually really sorry to hear that emily",
                "maskedITN": "I'm actually really sorry to hear that Emily",
                "display": "I'm actually really sorry to hear that, Emily.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.06,
                  "negative": 0.92
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT39.08S",
            "duration": "PT2.04S",
            "offsetInTicks": 390800000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.89951,
                "lexical": "i'm actually really sorry to hear that emily",
                "itn": "i'm actually really sorry to hear that emily",
                "maskedITN": "I'm actually really sorry to hear that Emily",
                "display": "I'm actually really sorry to hear that, Emily.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.06,
                  "negative": 0.92
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT41.12S",
            "duration": "PT3.2S",
            "offsetInTicks": 411200000.0,
            "durationInTicks": 32000000.0,
            "nBest": [
              {
                "confidence": 0.88941836,
                "lexical": "i can understand that you'd be frustrated if you haven't heard back",
                "itn": "i can understand that you'd be frustrated if you haven't heard back",
                "maskedITN": "I can understand that you'd be frustrated if you haven't heard back",
                "display": "I can understand that you'd be frustrated if you haven't heard back.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.18,
                  "negative": 0.8
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT41.12S",
            "duration": "PT3.2S",
            "offsetInTicks": 411200000.0,
            "durationInTicks": 32000000.0,
            "nBest": [
              {
                "confidence": 0.88941836,
                "lexical": "i can understand that you'd be frustrated if you haven't heard back",
                "itn": "i can understand that you'd be frustrated if you haven't heard back",
                "maskedITN": "I can understand that you'd be frustrated if you haven't heard back",
                "display": "I can understand that you'd be frustrated if you haven't heard back.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.18,
                  "negative": 0.8
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT45.4S",
            "duration": "PT3.52S",
            "offsetInTicks": 454000000.0,
            "durationInTicks": 35200000.0,
            "nBest": [
              {
                "confidence": 0.9195928,
                "lexical": "can i ask when the last time was that you did hear an update",
                "itn": "can i ask when the last time was that you did hear an update",
                "maskedITN": "Can I ask when the last time was that you did hear an update",
                "display": "Can I ask, when the last time was that you did hear an update?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT45.4S",
            "duration": "PT3.52S",
            "offsetInTicks": 454000000.0,
            "durationInTicks": 35200000.0,
            "nBest": [
              {
                "confidence": 0.9195928,
                "lexical": "can i ask when the last time was that you did hear an update",
                "itn": "can i ask when the last time was that you did hear an update",
                "maskedITN": "Can I ask when the last time was that you did hear an update",
                "display": "Can I ask, when the last time was that you did hear an update?",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.97,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT50.6S",
            "duration": "PT0.44S",
            "offsetInTicks": 506000000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.9631167,
                "lexical": "i don't know",
                "itn": "i don't know",
                "maskedITN": "I don't know",
                "display": "I don't know.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.9,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT50.6S",
            "duration": "PT0.44S",
            "offsetInTicks": 506000000.0,
            "durationInTicks": 4400000.0,
            "nBest": [
              {
                "confidence": 0.9631167,
                "lexical": "i don't know",
                "itn": "i don't know",
                "maskedITN": "I don't know",
                "display": "I don't know.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.9,
                  "negative": 0.09
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT51.04S",
            "duration": "PT3.28S",
            "offsetInTicks": 510400000.0,
            "durationInTicks": 32800000.0,
            "nBest": [
              {
                "confidence": 0.936815,
                "lexical": "it feels like a really long time like at least eight weeks or so",
                "itn": "it feels like a really long time like at least eight weeks or so",
                "maskedITN": "It feels like a really long time like at least eight weeks or so",
                "display": "It feels like a really long time, like at least eight weeks or so.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.86,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT51.04S",
            "duration": "PT3.28S",
            "offsetInTicks": 510400000.0,
            "durationInTicks": 32800000.0,
            "nBest": [
              {
                "confidence": 0.936815,
                "lexical": "it feels like a really long time like at least eight weeks or so",
                "itn": "it feels like a really long time like at least eight weeks or so",
                "maskedITN": "It feels like a really long time like at least eight weeks or so",
                "display": "It feels like a really long time, like at least eight weeks or so.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.86,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT54.52S",
            "duration": "PT1.96S",
            "offsetInTicks": 545200000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.80114144,
                "lexical": "OK yeah that that shouldn't happen",
                "itn": "OK yeah that that shouldn't happen",
                "maskedITN": "OK Yeah that that shouldn't happen",
                "display": "OK, Yeah, that that shouldn't happen.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.68,
                  "negative": 0.21
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT54.52S",
            "duration": "PT1.96S",
            "offsetInTicks": 545200000.0,
            "durationInTicks": 19600000.0,
            "nBest": [
              {
                "confidence": 0.80114144,
                "lexical": "OK yeah that that shouldn't happen",
                "itn": "OK yeah that that shouldn't happen",
                "maskedITN": "OK Yeah that that shouldn't happen",
                "display": "OK, Yeah, that that shouldn't happen.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.68,
                  "negative": 0.21
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT56.48S",
            "duration": "PT4.6S",
            "offsetInTicks": 564800000.0,
            "durationInTicks": 46000000.0,
            "nBest": [
              {
                "confidence": 0.9124719,
                "lexical": "and let's look into that right now so we can sort things out for you if you have a few minutes",
                "itn": "and let's look into that right now so we can sort things out for you if you have a few minutes",
                "maskedITN": "And let's look into that right now so we can sort things out for you if you have a few minutes",
                "display": "And let's look into that right now so we can sort things out for you if you have a few minutes.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.9,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT56.48S",
            "duration": "PT4.6S",
            "offsetInTicks": 564800000.0,
            "durationInTicks": 46000000.0,
            "nBest": [
              {
                "confidence": 0.9124719,
                "lexical": "and let's look into that right now so we can sort things out for you if you have a few minutes",
                "itn": "and let's look into that right now so we can sort things out for you if you have a few minutes",
                "maskedITN": "And let's look into that right now so we can sort things out for you if you have a few minutes",
                "display": "And let's look into that right now so we can sort things out for you if you have a few minutes.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.9,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M1.52S",
            "duration": "PT6.44S",
            "offsetInTicks": 615200000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.9074248,
                "lexical": "i'm just going to ask you from the last couple of physios that you did how you felt things were going",
                "itn": "i'm just going to ask you from the last couple of physios that you did how you felt things were going",
                "maskedITN": "I'm just going to ask you from the last couple of physios that you did how you felt things were going",
                "display": "I'm just going to ask you from the last couple of physios that you did, how you felt things were going.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M1.52S",
            "duration": "PT6.44S",
            "offsetInTicks": 615200000.0,
            "durationInTicks": 64400000.0,
            "nBest": [
              {
                "confidence": 0.9074248,
                "lexical": "i'm just going to ask you from the last couple of physios that you did how you felt things were going",
                "itn": "i'm just going to ask you from the last couple of physios that you did how you felt things were going",
                "maskedITN": "I'm just going to ask you from the last couple of physios that you did how you felt things were going",
                "display": "I'm just going to ask you from the last couple of physios that you did, how you felt things were going.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M7.96S",
            "duration": "PT11.24S",
            "offsetInTicks": 679600000.0,
            "durationInTicks": 112400000.0,
            "nBest": [
              {
                "confidence": 0.9559715,
                "lexical": "i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do",
                "itn": "i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do",
                "maskedITN": "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful but I just wanted to check now to see what your thoughts were and see what we can do",
                "display": "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can do.",
                "sentiment": {
                  "positive": 0.29,
                  "neutral": 0.67,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M7.96S",
            "duration": "PT11.24S",
            "offsetInTicks": 679600000.0,
            "durationInTicks": 112400000.0,
            "nBest": [
              {
                "confidence": 0.9559715,
                "lexical": "i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do",
                "itn": "i'm just looking at your file here and it looks like you were finding that it was a little bit helpful but i just wanted to check now to see what your thoughts were and see what we can do",
                "maskedITN": "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful but I just wanted to check now to see what your thoughts were and see what we can do",
                "display": "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can do.",
                "sentiment": {
                  "positive": 0.29,
                  "neutral": 0.67,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M19.68S",
            "duration": "PT5.04S",
            "offsetInTicks": 796800000.0,
            "durationInTicks": 50400000.0,
            "nBest": [
              {
                "confidence": 0.97040397,
                "lexical": "honestly it's been like a year and a half and i don't feel like i've made any progress at all",
                "itn": "honestly it's been like a year and a half and i don't feel like i've made any progress at all",
                "maskedITN": "Honestly it's been like a year and a half and I don't feel like I've made any progress at all",
                "display": "Honestly, it's been like a year and a half and I don't feel like I've made any progress at all.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.41,
                  "negative": 0.58
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M19.68S",
            "duration": "PT5.04S",
            "offsetInTicks": 796800000.0,
            "durationInTicks": 50400000.0,
            "nBest": [
              {
                "confidence": 0.97040397,
                "lexical": "honestly it's been like a year and a half and i don't feel like i've made any progress at all",
                "itn": "honestly it's been like a year and a half and i don't feel like i've made any progress at all",
                "maskedITN": "Honestly it's been like a year and a half and I don't feel like I've made any progress at all",
                "display": "Honestly, it's been like a year and a half and I don't feel like I've made any progress at all.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.41,
                  "negative": 0.58
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M25.28S",
            "duration": "PT2.48S",
            "offsetInTicks": 852800000.0,
            "durationInTicks": 24800000.0,
            "nBest": [
              {
                "confidence": 0.8923666,
                "lexical": "like i you know it's so disruptive to my life",
                "itn": "like i you know it's so disruptive to my life",
                "maskedITN": "Like I you know it's so disruptive to my life",
                "display": "Like I, you know, it's so disruptive to my life.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.3,
                  "negative": 0.66
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M25.28S",
            "duration": "PT2.48S",
            "offsetInTicks": 852800000.0,
            "durationInTicks": 24800000.0,
            "nBest": [
              {
                "confidence": 0.8923666,
                "lexical": "like i you know it's so disruptive to my life",
                "itn": "like i you know it's so disruptive to my life",
                "maskedITN": "Like I you know it's so disruptive to my life",
                "display": "Like I, you know, it's so disruptive to my life.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.3,
                  "negative": 0.66
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M27.76S",
            "duration": "PT2.44S",
            "offsetInTicks": 877600000.0,
            "durationInTicks": 24400000.0,
            "nBest": [
              {
                "confidence": 0.97499484,
                "lexical": "i go to treatment three times a week now",
                "itn": "i go to treatment three times a week now",
                "maskedITN": "I go to treatment three times a week now",
                "display": "I go to treatment three times a week now.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M27.76S",
            "duration": "PT2.44S",
            "offsetInTicks": 877600000.0,
            "durationInTicks": 24400000.0,
            "nBest": [
              {
                "confidence": 0.97499484,
                "lexical": "i go to treatment three times a week now",
                "itn": "i go to treatment three times a week now",
                "maskedITN": "I go to treatment three times a week now",
                "display": "I go to treatment three times a week now.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M30.2S",
            "duration": "PT6.28S",
            "offsetInTicks": 902000000.0,
            "durationInTicks": 62800000.0,
            "nBest": [
              {
                "confidence": 0.96435344,
                "lexical": "i've been paying for it out of pocket the last two months and i'm not feeling any better",
                "itn": "i've been paying for it out of pocket the last two months and i'm not feeling any better",
                "maskedITN": "I've been paying for it out of pocket the last two months and I'm not feeling any better",
                "display": "I've been paying for it out of pocket the last two months and I'm not feeling any better.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.04,
                  "negative": 0.95
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M30.2S",
            "duration": "PT6.28S",
            "offsetInTicks": 902000000.0,
            "durationInTicks": 62800000.0,
            "nBest": [
              {
                "confidence": 0.96435344,
                "lexical": "i've been paying for it out of pocket the last two months and i'm not feeling any better",
                "itn": "i've been paying for it out of pocket the last two months and i'm not feeling any better",
                "maskedITN": "I've been paying for it out of pocket the last two months and I'm not feeling any better",
                "display": "I've been paying for it out of pocket the last two months and I'm not feeling any better.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.04,
                  "negative": 0.95
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M36.6S",
            "duration": "PT0.96S",
            "offsetInTicks": 966000000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.76494753,
                "lexical": "OK i'm",
                "itn": "OK i'm",
                "maskedITN": "OK I'm",
                "display": "OK, I'm.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M36.6S",
            "duration": "PT0.96S",
            "offsetInTicks": 966000000.0,
            "durationInTicks": 9600000.0,
            "nBest": [
              {
                "confidence": 0.76494753,
                "lexical": "OK i'm",
                "itn": "OK i'm",
                "maskedITN": "OK I'm",
                "display": "OK, I'm.",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.92,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M37.84S",
            "duration": "PT5.28S",
            "offsetInTicks": 978400000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.79559684,
                "lexical": "i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening",
                "itn": "i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening",
                "maskedITN": "I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening",
                "display": "I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.06,
                  "negative": 0.92
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M37.84S",
            "duration": "PT5.28S",
            "offsetInTicks": 978400000.0,
            "durationInTicks": 52800000.0,
            "nBest": [
              {
                "confidence": 0.79559684,
                "lexical": "i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening",
                "itn": "i'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening",
                "maskedITN": "I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening",
                "display": "I'm sorry again to hear about the your paying out of pocket that technically we that shouldn't be happening.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.06,
                  "negative": 0.92
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M43.12S",
            "duration": "PT1.36S",
            "offsetInTicks": 1031200000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.9669555,
                "lexical": "so let's take care of that for you",
                "itn": "so let's take care of that for you",
                "maskedITN": "So let's take care of that for you",
                "display": "So let's take care of that for you.",
                "sentiment": {
                  "positive": 0.26,
                  "neutral": 0.72,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M43.12S",
            "duration": "PT1.36S",
            "offsetInTicks": 1031200000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.9669555,
                "lexical": "so let's take care of that for you",
                "itn": "so let's take care of that for you",
                "maskedITN": "So let's take care of that for you",
                "display": "So let's take care of that for you.",
                "sentiment": {
                  "positive": 0.26,
                  "neutral": 0.72,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M44.48S",
            "duration": "PT2.68S",
            "offsetInTicks": 1044800000.0,
            "durationInTicks": 26800000.0,
            "nBest": [
              {
                "confidence": 0.96166503,
                "lexical": "i'll get that information from you in a second",
                "itn": "i'll get that information from you in a second",
                "maskedITN": "I'll get that information from you in a second",
                "display": "I'll get that information from you in a second.",
                "sentiment": {
                  "positive": 0.17,
                  "neutral": 0.81,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M44.48S",
            "duration": "PT2.68S",
            "offsetInTicks": 1044800000.0,
            "durationInTicks": 26800000.0,
            "nBest": [
              {
                "confidence": 0.96166503,
                "lexical": "i'll get that information from you in a second",
                "itn": "i'll get that information from you in a second",
                "maskedITN": "I'll get that information from you in a second",
                "display": "I'll get that information from you in a second.",
                "sentiment": {
                  "positive": 0.17,
                  "neutral": 0.81,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M47.16S",
            "duration": "PT5.32S",
            "offsetInTicks": 1071600000.0,
            "durationInTicks": 53200000.0,
            "nBest": [
              {
                "confidence": 0.94222295,
                "lexical": "but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go",
                "itn": "but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go",
                "maskedITN": "But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go",
                "display": "But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.34,
                  "negative": 0.64
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M47.16S",
            "duration": "PT5.32S",
            "offsetInTicks": 1071600000.0,
            "durationInTicks": 53200000.0,
            "nBest": [
              {
                "confidence": 0.94222295,
                "lexical": "but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go",
                "itn": "but also i'm i'm a little concerned for you about your treatment and that you haven't been able to go",
                "maskedITN": "But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go",
                "display": "But also I'm I'm a little concerned for you about your treatment and that you haven't been able to go.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.34,
                  "negative": 0.64
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT1M53.6S",
            "duration": "PT7.36S",
            "offsetInTicks": 1136000000.0,
            "durationInTicks": 73600000.0,
            "nBest": [
              {
                "confidence": 0.95112085,
                "lexical": "i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist",
                "itn": "i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist",
                "maskedITN": "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist",
                "display": "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT1M53.6S",
            "duration": "PT7.36S",
            "offsetInTicks": 1136000000.0,
            "durationInTicks": 73600000.0,
            "nBest": [
              {
                "confidence": 0.95112085,
                "lexical": "i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist",
                "itn": "i'm looking at the information i have here and it looks like you still have some sessions left with your physiotherapist",
                "maskedITN": "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist",
                "display": "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M1.24S",
            "duration": "PT5.84S",
            "offsetInTicks": 1212400000.0,
            "durationInTicks": 58400000.0,
            "nBest": [
              {
                "confidence": 0.8066553,
                "lexical": "i'm just wondering why you were thinking you weren't able to go for a reason",
                "itn": "i'm just wondering why you were thinking you weren't able to go for a reason",
                "maskedITN": "I'm just wondering why you were thinking you weren't able to go for a reason",
                "display": "I'm just wondering why you were thinking you weren't able to go for a reason.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.69,
                  "negative": 0.29
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M1.24S",
            "duration": "PT5.84S",
            "offsetInTicks": 1212400000.0,
            "durationInTicks": 58400000.0,
            "nBest": [
              {
                "confidence": 0.8066553,
                "lexical": "i'm just wondering why you were thinking you weren't able to go for a reason",
                "itn": "i'm just wondering why you were thinking you weren't able to go for a reason",
                "maskedITN": "I'm just wondering why you were thinking you weren't able to go for a reason",
                "display": "I'm just wondering why you were thinking you weren't able to go for a reason.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.69,
                  "negative": 0.29
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M7.28S",
            "duration": "PT0.28S",
            "offsetInTicks": 1272800000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.8655474,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M7.28S",
            "duration": "PT0.28S",
            "offsetInTicks": 1272800000.0,
            "durationInTicks": 2800000.0,
            "nBest": [
              {
                "confidence": 0.8655474,
                "lexical": "yeah",
                "itn": "yeah",
                "maskedITN": "Yeah",
                "display": "Yeah.",
                "sentiment": {
                  "positive": 0.15,
                  "neutral": 0.81,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M7.6S",
            "duration": "PT3.28S",
            "offsetInTicks": 1276000000.0,
            "durationInTicks": 32800000.0,
            "nBest": [
              {
                "confidence": 0.9107346,
                "lexical": "they told me that the treatment was cut off by ACDC and i had to pay",
                "itn": "they told me that the treatment was cut off by ACDC and i had to pay",
                "maskedITN": "They told me that the treatment was cut off by ACDC and I had to pay",
                "display": "They told me that the treatment was cut off by ACDC and I had to pay.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.52,
                  "negative": 0.47
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M7.6S",
            "duration": "PT3.28S",
            "offsetInTicks": 1276000000.0,
            "durationInTicks": 32800000.0,
            "nBest": [
              {
                "confidence": 0.9107346,
                "lexical": "they told me that the treatment was cut off by ACDC and i had to pay",
                "itn": "they told me that the treatment was cut off by ACDC and i had to pay",
                "maskedITN": "They told me that the treatment was cut off by ACDC and I had to pay",
                "display": "They told me that the treatment was cut off by ACDC and I had to pay.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.52,
                  "negative": 0.47
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M11.32S",
            "duration": "PT0.32S",
            "offsetInTicks": 1313200000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.8417847,
                "lexical": "sorry",
                "itn": "sorry",
                "maskedITN": "Sorry",
                "display": "Sorry.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.15,
                  "negative": 0.81
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M11.32S",
            "duration": "PT0.32S",
            "offsetInTicks": 1313200000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.8417847,
                "lexical": "sorry",
                "itn": "sorry",
                "maskedITN": "Sorry",
                "display": "Sorry.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.15,
                  "negative": 0.81
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M11.64S",
            "duration": "PT0.24S",
            "offsetInTicks": 1316400000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.6634989,
                "lexical": "who",
                "itn": "who",
                "maskedITN": "Who",
                "display": "Who?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.9,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M11.64S",
            "duration": "PT0.24S",
            "offsetInTicks": 1316400000.0,
            "durationInTicks": 2400000.0,
            "nBest": [
              {
                "confidence": 0.6634989,
                "lexical": "who",
                "itn": "who",
                "maskedITN": "Who",
                "display": "Who?",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.9,
                  "negative": 0.06
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M11.96S",
            "duration": "PT0.84S",
            "offsetInTicks": 1319600000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.84499705,
                "lexical": "who told you that",
                "itn": "who told you that",
                "maskedITN": "Who told you that",
                "display": "Who told you that?",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.83,
                  "negative": 0.12
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M11.96S",
            "duration": "PT0.84S",
            "offsetInTicks": 1319600000.0,
            "durationInTicks": 8400000.0,
            "nBest": [
              {
                "confidence": 0.84499705,
                "lexical": "who told you that",
                "itn": "who told you that",
                "maskedITN": "Who told you that",
                "display": "Who told you that?",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.83,
                  "negative": 0.12
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M12.92S",
            "duration": "PT1.16S",
            "offsetInTicks": 1329200000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.8164802,
                "lexical": "the physiotherapist",
                "itn": "the physiotherapist",
                "maskedITN": "The physiotherapist",
                "display": "The physiotherapist.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M12.92S",
            "duration": "PT1.16S",
            "offsetInTicks": 1329200000.0,
            "durationInTicks": 11600000.0,
            "nBest": [
              {
                "confidence": 0.8164802,
                "lexical": "the physiotherapist",
                "itn": "the physiotherapist",
                "maskedITN": "The physiotherapist",
                "display": "The physiotherapist.",
                "sentiment": {
                  "positive": 0.05,
                  "neutral": 0.94,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M14.4S",
            "duration": "PT1.36S",
            "offsetInTicks": 1344000000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.9121654,
                "lexical": "i'm really sorry to hear that",
                "itn": "i'm really sorry to hear that",
                "maskedITN": "I'm really sorry to hear that",
                "display": "I'm really sorry to hear that.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.04,
                  "negative": 0.95
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M14.4S",
            "duration": "PT1.36S",
            "offsetInTicks": 1344000000.0,
            "durationInTicks": 13600000.0,
            "nBest": [
              {
                "confidence": 0.9121654,
                "lexical": "i'm really sorry to hear that",
                "itn": "i'm really sorry to hear that",
                "maskedITN": "I'm really sorry to hear that",
                "display": "I'm really sorry to hear that.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.04,
                  "negative": 0.95
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M15.76S",
            "duration": "PT1.56S",
            "offsetInTicks": 1357600000.0,
            "durationInTicks": 15600000.0,
            "nBest": [
              {
                "confidence": 0.93043697,
                "lexical": "OK we can clear that up with them",
                "itn": "OK we can clear that up with them",
                "maskedITN": "OK we can clear that up with them",
                "display": "OK, we can clear that up with them.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.88,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M15.76S",
            "duration": "PT1.56S",
            "offsetInTicks": 1357600000.0,
            "durationInTicks": 15600000.0,
            "nBest": [
              {
                "confidence": 0.93043697,
                "lexical": "OK we can clear that up with them",
                "itn": "OK we can clear that up with them",
                "maskedITN": "OK we can clear that up with them",
                "display": "OK, we can clear that up with them.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.88,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M17.32S",
            "duration": "PT2.04S",
            "offsetInTicks": 1373200000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.80961156,
                "lexical": "but there there are some sessions left",
                "itn": "but there there are some sessions left",
                "maskedITN": "But there there are some sessions left",
                "display": "But there there are some sessions left.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.96,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M17.32S",
            "duration": "PT2.04S",
            "offsetInTicks": 1373200000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.80961156,
                "lexical": "but there there are some sessions left",
                "itn": "but there there are some sessions left",
                "maskedITN": "But there there are some sessions left",
                "display": "But there there are some sessions left.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.96,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M20.24S",
            "duration": "PT0.72S",
            "offsetInTicks": 1402400000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.91563475,
                "lexical": "but you know what",
                "itn": "but you know what",
                "maskedITN": "But you know what",
                "display": "But you know what?",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.8,
                  "negative": 0.13
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M20.24S",
            "duration": "PT0.72S",
            "offsetInTicks": 1402400000.0,
            "durationInTicks": 7200000.0,
            "nBest": [
              {
                "confidence": 0.91563475,
                "lexical": "but you know what",
                "itn": "but you know what",
                "maskedITN": "But you know what",
                "display": "But you know what?",
                "sentiment": {
                  "positive": 0.07,
                  "neutral": 0.8,
                  "negative": 0.13
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M20.96S",
            "duration": "PT2.2S",
            "offsetInTicks": 1409600000.0,
            "durationInTicks": 22000000.0,
            "nBest": [
              {
                "confidence": 0.9663841,
                "lexical": "i don't want you to have to worry about this",
                "itn": "i don't want you to have to worry about this",
                "maskedITN": "I don't want you to have to worry about this",
                "display": "I don't want you to have to worry about this.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.35,
                  "negative": 0.56
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M20.96S",
            "duration": "PT2.2S",
            "offsetInTicks": 1409600000.0,
            "durationInTicks": 22000000.0,
            "nBest": [
              {
                "confidence": 0.9663841,
                "lexical": "i don't want you to have to worry about this",
                "itn": "i don't want you to have to worry about this",
                "maskedITN": "I don't want you to have to worry about this",
                "display": "I don't want you to have to worry about this.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.35,
                  "negative": 0.56
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M23.16S",
            "duration": "PT1.04S",
            "offsetInTicks": 1431600000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.9751466,
                "lexical": "you leave that with me",
                "itn": "you leave that with me",
                "maskedITN": "You leave that with me",
                "display": "You leave that with me.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.77,
                  "negative": 0.12
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M23.16S",
            "duration": "PT1.04S",
            "offsetInTicks": 1431600000.0,
            "durationInTicks": 10400000.0,
            "nBest": [
              {
                "confidence": 0.9751466,
                "lexical": "you leave that with me",
                "itn": "you leave that with me",
                "maskedITN": "You leave that with me",
                "display": "You leave that with me.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.77,
                  "negative": 0.12
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M24.48S",
            "duration": "PT3.56S",
            "offsetInTicks": 1444800000.0,
            "durationInTicks": 35600000.0,
            "nBest": [
              {
                "confidence": 0.91179335,
                "lexical": "i will contact your physiotherapist and follow up with you",
                "itn": "i will contact your physiotherapist and follow up with you",
                "maskedITN": "I will contact your physiotherapist and follow up with you",
                "display": "I will contact your physiotherapist and follow up with you.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M24.48S",
            "duration": "PT3.56S",
            "offsetInTicks": 1444800000.0,
            "durationInTicks": 35600000.0,
            "nBest": [
              {
                "confidence": 0.91179335,
                "lexical": "i will contact your physiotherapist and follow up with you",
                "itn": "i will contact your physiotherapist and follow up with you",
                "maskedITN": "I will contact your physiotherapist and follow up with you",
                "display": "I will contact your physiotherapist and follow up with you.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.0
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M28.08S",
            "duration": "PT7.44S",
            "offsetInTicks": 1480800000.0,
            "durationInTicks": 74400000.0,
            "nBest": [
              {
                "confidence": 0.89397573,
                "lexical": "i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery",
                "itn": "i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery",
                "maskedITN": "I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery",
                "display": "I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery.",
                "sentiment": {
                  "positive": 0.21,
                  "neutral": 0.76,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M28.08S",
            "duration": "PT7.44S",
            "offsetInTicks": 1480800000.0,
            "durationInTicks": 74400000.0,
            "nBest": [
              {
                "confidence": 0.89397573,
                "lexical": "i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery",
                "itn": "i can do that today because i want to make sure that you're still able to go for treatment and this is not interrupting your recovery",
                "maskedITN": "I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery",
                "display": "I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery.",
                "sentiment": {
                  "positive": 0.21,
                  "neutral": 0.76,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M35.92S",
            "duration": "PT2.92S",
            "offsetInTicks": 1559200000.0,
            "durationInTicks": 29200000.0,
            "nBest": [
              {
                "confidence": 0.85698164,
                "lexical": "is there anything else that's going on right now that i can help with",
                "itn": "is there anything else that's going on right now that i can help with",
                "maskedITN": "Is there anything else that's going on right now that I can help with",
                "display": "Is there anything else that's going on right now that I can help with?",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.86,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M35.92S",
            "duration": "PT2.92S",
            "offsetInTicks": 1559200000.0,
            "durationInTicks": 29200000.0,
            "nBest": [
              {
                "confidence": 0.85698164,
                "lexical": "is there anything else that's going on right now that i can help with",
                "itn": "is there anything else that's going on right now that i can help with",
                "maskedITN": "Is there anything else that's going on right now that I can help with",
                "display": "Is there anything else that's going on right now that I can help with?",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.86,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M39S",
            "duration": "PT2S",
            "offsetInTicks": 1590000000.0,
            "durationInTicks": 20000000.0,
            "nBest": [
              {
                "confidence": 0.94199115,
                "lexical": "yeah i mean you know whatever",
                "itn": "yeah i mean you know whatever",
                "maskedITN": "Yeah I mean you know whatever",
                "display": "Yeah, I mean, you know, whatever.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M39S",
            "duration": "PT2S",
            "offsetInTicks": 1590000000.0,
            "durationInTicks": 20000000.0,
            "nBest": [
              {
                "confidence": 0.94199115,
                "lexical": "yeah i mean you know whatever",
                "itn": "yeah i mean you know whatever",
                "maskedITN": "Yeah I mean you know whatever",
                "display": "Yeah, I mean, you know, whatever.",
                "sentiment": {
                  "positive": 0.04,
                  "neutral": 0.94,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M41S",
            "duration": "PT4.72S",
            "offsetInTicks": 1610000000.0,
            "durationInTicks": 47200000.0,
            "nBest": [
              {
                "confidence": 0.9249219,
                "lexical": "if my treatment is going to be cut off like you know that's annoying",
                "itn": "if my treatment is going to be cut off like you know that's annoying",
                "maskedITN": "If my treatment is going to be cut off like you know that's annoying",
                "display": "If my treatment is going to be cut off, like, you know, that's annoying.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.03,
                  "negative": 0.97
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M41S",
            "duration": "PT4.72S",
            "offsetInTicks": 1610000000.0,
            "durationInTicks": 47200000.0,
            "nBest": [
              {
                "confidence": 0.9249219,
                "lexical": "if my treatment is going to be cut off like you know that's annoying",
                "itn": "if my treatment is going to be cut off like you know that's annoying",
                "maskedITN": "If my treatment is going to be cut off like you know that's annoying",
                "display": "If my treatment is going to be cut off, like, you know, that's annoying.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.03,
                  "negative": 0.97
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M45.72S",
            "duration": "PT1.84S",
            "offsetInTicks": 1657200000.0,
            "durationInTicks": 18400000.0,
            "nBest": [
              {
                "confidence": 0.9212968,
                "lexical": "it's unfair because i still need treatment",
                "itn": "it's unfair because i still need treatment",
                "maskedITN": "It's unfair because I still need treatment",
                "display": "It's unfair because I still need treatment.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.13,
                  "negative": 0.87
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M45.72S",
            "duration": "PT1.84S",
            "offsetInTicks": 1657200000.0,
            "durationInTicks": 18400000.0,
            "nBest": [
              {
                "confidence": 0.9212968,
                "lexical": "it's unfair because i still need treatment",
                "itn": "it's unfair because i still need treatment",
                "maskedITN": "It's unfair because I still need treatment",
                "display": "It's unfair because I still need treatment.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.13,
                  "negative": 0.87
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M48.16S",
            "duration": "PT6.68S",
            "offsetInTicks": 1681600000.0,
            "durationInTicks": 66800000.0,
            "nBest": [
              {
                "confidence": 0.9062713,
                "lexical": "but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today",
                "itn": "but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today",
                "maskedITN": "But I guess you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today",
                "display": "But I guess, you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M48.16S",
            "duration": "PT6.68S",
            "offsetInTicks": 1681600000.0,
            "durationInTicks": 66800000.0,
            "nBest": [
              {
                "confidence": 0.9062713,
                "lexical": "but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today",
                "itn": "but i guess you know we can also just settle the claim up and and i can have my compensation now what it what's your offer today",
                "maskedITN": "But I guess you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today",
                "display": "But I guess, you know we can also just settle the claim up and and I can have my compensation Now what it what's your offer today?",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.94,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT2M56.52S",
            "duration": "PT7.84S",
            "offsetInTicks": 1765200000.0,
            "durationInTicks": 78400000.0,
            "nBest": [
              {
                "confidence": 0.8967706,
                "lexical": "you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that",
                "itn": "you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that",
                "maskedITN": "You know Emily I just wanted to clarify I know we've talked about this before as well but I just wanted to make sure that you are clear that we actually don't do that",
                "display": "You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you are clear that we actually don't do that.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.81,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT2M56.52S",
            "duration": "PT7.84S",
            "offsetInTicks": 1765200000.0,
            "durationInTicks": 78400000.0,
            "nBest": [
              {
                "confidence": 0.8967706,
                "lexical": "you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that",
                "itn": "you know emily i just wanted to clarify i know we've talked about this before as well but i just wanted to make sure that you are clear that we actually don't do that",
                "maskedITN": "You know Emily I just wanted to clarify I know we've talked about this before as well but I just wanted to make sure that you are clear that we actually don't do that",
                "display": "You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you are clear that we actually don't do that.",
                "sentiment": {
                  "positive": 0.09,
                  "neutral": 0.81,
                  "negative": 0.1
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M4.36S",
            "duration": "PT7.16S",
            "offsetInTicks": 1843600000.0,
            "durationInTicks": 71600000.0,
            "nBest": [
              {
                "confidence": 0.9125328,
                "lexical": "ICBC doesn't supply compensation for your claim since we started with enhanced care",
                "itn": "ICBC doesn't supply compensation for your claim since we started with enhanced care",
                "maskedITN": "ICBC doesn't supply compensation for your claim since we started with enhanced care",
                "display": "ICBC doesn't supply compensation for your claim since we started with enhanced care.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.4,
                  "negative": 0.59
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M4.36S",
            "duration": "PT7.16S",
            "offsetInTicks": 1843600000.0,
            "durationInTicks": 71600000.0,
            "nBest": [
              {
                "confidence": 0.9125328,
                "lexical": "ICBC doesn't supply compensation for your claim since we started with enhanced care",
                "itn": "ICBC doesn't supply compensation for your claim since we started with enhanced care",
                "maskedITN": "ICBC doesn't supply compensation for your claim since we started with enhanced care",
                "display": "ICBC doesn't supply compensation for your claim since we started with enhanced care.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.4,
                  "negative": 0.59
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M12S",
            "duration": "PT1.68S",
            "offsetInTicks": 1920000000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.7001154,
                "lexical": "we talked about this in the beginning of your claim",
                "itn": "we talked about this in the beginning of your claim",
                "maskedITN": "We talked about this in the beginning of your claim",
                "display": "We talked about this in the beginning of your claim.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M12S",
            "duration": "PT1.68S",
            "offsetInTicks": 1920000000.0,
            "durationInTicks": 16800000.0,
            "nBest": [
              {
                "confidence": 0.7001154,
                "lexical": "we talked about this in the beginning of your claim",
                "itn": "we talked about this in the beginning of your claim",
                "maskedITN": "We talked about this in the beginning of your claim",
                "display": "We talked about this in the beginning of your claim.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.96,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M13.68S",
            "duration": "PT3.84S",
            "offsetInTicks": 1936800000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.9044693,
                "lexical": "so i wanted to make sure that you understand and please ask me any questions about it",
                "itn": "so i wanted to make sure that you understand and please ask me any questions about it",
                "maskedITN": "So I wanted to make sure that you understand and please ask me any questions about it",
                "display": "So I wanted to make sure that you understand and please ask me any questions about it.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.89,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M13.68S",
            "duration": "PT3.84S",
            "offsetInTicks": 1936800000.0,
            "durationInTicks": 38400000.0,
            "nBest": [
              {
                "confidence": 0.9044693,
                "lexical": "so i wanted to make sure that you understand and please ask me any questions about it",
                "itn": "so i wanted to make sure that you understand and please ask me any questions about it",
                "maskedITN": "So I wanted to make sure that you understand and please ask me any questions about it",
                "display": "So I wanted to make sure that you understand and please ask me any questions about it.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.89,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M17.52S",
            "duration": "PT8S",
            "offsetInTicks": 1975200000.0,
            "durationInTicks": 80000000.0,
            "nBest": [
              {
                "confidence": 0.92725337,
                "lexical": "but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment",
                "itn": "but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment",
                "maskedITN": "But overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment",
                "display": "But overall what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.69,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M17.52S",
            "duration": "PT8S",
            "offsetInTicks": 1975200000.0,
            "durationInTicks": 80000000.0,
            "nBest": [
              {
                "confidence": 0.92725337,
                "lexical": "but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment",
                "itn": "but overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment",
                "maskedITN": "But overall what it is is when you are in an accident we want to make sure that we're doing everything to help you recover and that's including the treatment",
                "display": "But overall what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment.",
                "sentiment": {
                  "positive": 0.11,
                  "neutral": 0.69,
                  "negative": 0.2
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M25.8S",
            "duration": "PT2.24S",
            "offsetInTicks": 2058000000.0,
            "durationInTicks": 22400000.0,
            "nBest": [
              {
                "confidence": 0.86521447,
                "lexical": "you mentioned that you've been going to physio for about a year and a half",
                "itn": "you mentioned that you've been going to physio for about a year and a half",
                "maskedITN": "You mentioned that you've been going to physio for about a year and a half",
                "display": "You mentioned that you've been going to physio for about a year and a half.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M25.8S",
            "duration": "PT2.24S",
            "offsetInTicks": 2058000000.0,
            "durationInTicks": 22400000.0,
            "nBest": [
              {
                "confidence": 0.86521447,
                "lexical": "you mentioned that you've been going to physio for about a year and a half",
                "itn": "you mentioned that you've been going to physio for about a year and a half",
                "maskedITN": "You mentioned that you've been going to physio for about a year and a half",
                "display": "You mentioned that you've been going to physio for about a year and a half.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.98,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M28.04S",
            "duration": "PT3.04S",
            "offsetInTicks": 2080400000.0,
            "durationInTicks": 30400000.0,
            "nBest": [
              {
                "confidence": 0.9046181,
                "lexical": "so that's part of the benefits that you get with your claim",
                "itn": "so that's part of the benefits that you get with your claim",
                "maskedITN": "So that's part of the benefits that you get with your claim",
                "display": "So that's part of the benefits that you get with your claim.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.91,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M28.04S",
            "duration": "PT3.04S",
            "offsetInTicks": 2080400000.0,
            "durationInTicks": 30400000.0,
            "nBest": [
              {
                "confidence": 0.9046181,
                "lexical": "so that's part of the benefits that you get with your claim",
                "itn": "so that's part of the benefits that you get with your claim",
                "maskedITN": "So that's part of the benefits that you get with your claim",
                "display": "So that's part of the benefits that you get with your claim.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.91,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M31.4S",
            "duration": "PT5.44S",
            "offsetInTicks": 2114000000.0,
            "durationInTicks": 54400000.0,
            "nBest": [
              {
                "confidence": 0.930166,
                "lexical": "and i know that we followed up with your doctor as well to check on your recovery and how you're doing",
                "itn": "and i know that we followed up with your doctor as well to check on your recovery and how you're doing",
                "maskedITN": "And I know that we followed up with your doctor as well to check on your recovery and how you're doing",
                "display": "And I know that we followed up with your doctor as well to check on your recovery and how you're doing.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M31.4S",
            "duration": "PT5.44S",
            "offsetInTicks": 2114000000.0,
            "durationInTicks": 54400000.0,
            "nBest": [
              {
                "confidence": 0.930166,
                "lexical": "and i know that we followed up with your doctor as well to check on your recovery and how you're doing",
                "itn": "and i know that we followed up with your doctor as well to check on your recovery and how you're doing",
                "maskedITN": "And I know that we followed up with your doctor as well to check on your recovery and how you're doing",
                "display": "And I know that we followed up with your doctor as well to check on your recovery and how you're doing.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.95,
                  "negative": 0.01
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M37.16S",
            "duration": "PT2.24S",
            "offsetInTicks": 2171600000.0,
            "durationInTicks": 22400000.0,
            "nBest": [
              {
                "confidence": 0.8560495,
                "lexical": "those are are the things that we want to do to support you",
                "itn": "those are are the things that we want to do to support you",
                "maskedITN": "Those are are the things that we want to do to support you",
                "display": "Those are are the things that we want to do to support you.",
                "sentiment": {
                  "positive": 0.49,
                  "neutral": 0.48,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M37.16S",
            "duration": "PT2.24S",
            "offsetInTicks": 2171600000.0,
            "durationInTicks": 22400000.0,
            "nBest": [
              {
                "confidence": 0.8560495,
                "lexical": "those are are the things that we want to do to support you",
                "itn": "those are are the things that we want to do to support you",
                "maskedITN": "Those are are the things that we want to do to support you",
                "display": "Those are are the things that we want to do to support you.",
                "sentiment": {
                  "positive": 0.49,
                  "neutral": 0.48,
                  "negative": 0.03
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M39.4S",
            "duration": "PT2.04S",
            "offsetInTicks": 2194000000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.9241029,
                "lexical": "there isn't any compensation amount",
                "itn": "there isn't any compensation amount",
                "maskedITN": "There isn't any compensation amount",
                "display": "There isn't any compensation amount.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.73,
                  "negative": 0.26
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M39.4S",
            "duration": "PT2.04S",
            "offsetInTicks": 2194000000.0,
            "durationInTicks": 20400000.0,
            "nBest": [
              {
                "confidence": 0.9241029,
                "lexical": "there isn't any compensation amount",
                "itn": "there isn't any compensation amount",
                "maskedITN": "There isn't any compensation amount",
                "display": "There isn't any compensation amount.",
                "sentiment": {
                  "positive": 0.01,
                  "neutral": 0.73,
                  "negative": 0.26
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M41.52S",
            "duration": "PT2.84S",
            "offsetInTicks": 2215200000.0,
            "durationInTicks": 28400000.0,
            "nBest": [
              {
                "confidence": 0.8655437,
                "lexical": "what there's no more compensation",
                "itn": "what there's no more compensation",
                "maskedITN": "What there's no more compensation",
                "display": "What there's no more compensation.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.63,
                  "negative": 0.35
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M41.52S",
            "duration": "PT2.84S",
            "offsetInTicks": 2215200000.0,
            "durationInTicks": 28400000.0,
            "nBest": [
              {
                "confidence": 0.8655437,
                "lexical": "what there's no more compensation",
                "itn": "what there's no more compensation",
                "maskedITN": "What there's no more compensation",
                "display": "What there's no more compensation.",
                "sentiment": {
                  "positive": 0.02,
                  "neutral": 0.63,
                  "negative": 0.35
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M44.8S",
            "duration": "PT3.24S",
            "offsetInTicks": 2248000000.0,
            "durationInTicks": 32400000.0,
            "nBest": [
              {
                "confidence": 0.82243294,
                "lexical": "so i've been struggling with this injury",
                "itn": "so i've been struggling with this injury",
                "maskedITN": "So I've been struggling with this injury",
                "display": "So I've been struggling with this injury.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.03,
                  "negative": 0.96
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M44.8S",
            "duration": "PT3.24S",
            "offsetInTicks": 2248000000.0,
            "durationInTicks": 32400000.0,
            "nBest": [
              {
                "confidence": 0.82243294,
                "lexical": "so i've been struggling with this injury",
                "itn": "so i've been struggling with this injury",
                "maskedITN": "So I've been struggling with this injury",
                "display": "So I've been struggling with this injury.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.03,
                  "negative": 0.96
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M48.04S",
            "duration": "PT4.84S",
            "offsetInTicks": 2280400000.0,
            "durationInTicks": 48400000.0,
            "nBest": [
              {
                "confidence": 0.91572714,
                "lexical": "i have been wasting all my time going to treatment and i'm not even going to get any money for it",
                "itn": "i have been wasting all my time going to treatment and i'm not even going to get any money for it",
                "maskedITN": "I have been wasting all my time going to treatment and I'm not even going to get any money for it",
                "display": "I have been wasting all my time going to treatment and I'm not even going to get any money for it.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.04,
                  "negative": 0.96
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M48.04S",
            "duration": "PT4.84S",
            "offsetInTicks": 2280400000.0,
            "durationInTicks": 48400000.0,
            "nBest": [
              {
                "confidence": 0.91572714,
                "lexical": "i have been wasting all my time going to treatment and i'm not even going to get any money for it",
                "itn": "i have been wasting all my time going to treatment and i'm not even going to get any money for it",
                "maskedITN": "I have been wasting all my time going to treatment and I'm not even going to get any money for it",
                "display": "I have been wasting all my time going to treatment and I'm not even going to get any money for it.",
                "sentiment": {
                  "positive": 0.0,
                  "neutral": 0.04,
                  "negative": 0.96
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M53.76S",
            "duration": "PT1.8S",
            "offsetInTicks": 2337600000.0,
            "durationInTicks": 18000000.0,
            "nBest": [
              {
                "confidence": 0.82976806,
                "lexical": "we we don't have compensation anymore",
                "itn": "we we don't have compensation anymore",
                "maskedITN": "We we don't have compensation anymore",
                "display": "We we don't have compensation anymore.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.65,
                  "negative": 0.32
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M53.76S",
            "duration": "PT1.8S",
            "offsetInTicks": 2337600000.0,
            "durationInTicks": 18000000.0,
            "nBest": [
              {
                "confidence": 0.82976806,
                "lexical": "we we don't have compensation anymore",
                "itn": "we we don't have compensation anymore",
                "maskedITN": "We we don't have compensation anymore",
                "display": "We we don't have compensation anymore.",
                "sentiment": {
                  "positive": 0.03,
                  "neutral": 0.65,
                  "negative": 0.32
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M55.56S",
            "duration": "PT1.24S",
            "offsetInTicks": 2355600000.0,
            "durationInTicks": 12400000.0,
            "nBest": [
              {
                "confidence": 0.90595454,
                "lexical": "emily that is correct",
                "itn": "emily that is correct",
                "maskedITN": "Emily that is correct",
                "display": "Emily, that is correct.",
                "sentiment": {
                  "positive": 0.49,
                  "neutral": 0.49,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M55.56S",
            "duration": "PT1.24S",
            "offsetInTicks": 2355600000.0,
            "durationInTicks": 12400000.0,
            "nBest": [
              {
                "confidence": 0.90595454,
                "lexical": "emily that is correct",
                "itn": "emily that is correct",
                "maskedITN": "Emily that is correct",
                "display": "Emily, that is correct.",
                "sentiment": {
                  "positive": 0.49,
                  "neutral": 0.49,
                  "negative": 0.02
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M57.92S",
            "duration": "PT1.2S",
            "offsetInTicks": 2379200000.0,
            "durationInTicks": 12000000.0,
            "nBest": [
              {
                "confidence": 0.8762555,
                "lexical": "OK whatever",
                "itn": "OK whatever",
                "maskedITN": "OK whatever",
                "display": "OK, whatever.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.89,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M57.92S",
            "duration": "PT1.2S",
            "offsetInTicks": 2379200000.0,
            "durationInTicks": 12000000.0,
            "nBest": [
              {
                "confidence": 0.8762555,
                "lexical": "OK whatever",
                "itn": "OK whatever",
                "maskedITN": "OK whatever",
                "display": "OK, whatever.",
                "sentiment": {
                  "positive": 0.08,
                  "neutral": 0.89,
                  "negative": 0.04
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 0,
            "offset": "PT3M59.36S",
            "duration": "PT0.32S",
            "offsetInTicks": 2393600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.7800385,
                "lexical": "bye",
                "itn": "bye",
                "maskedITN": "Bye",
                "display": "Bye.",
                "sentiment": {
                  "positive": 0.25,
                  "neutral": 0.7,
                  "negative": 0.05
                }
              }
            ]
          },
          {
            "recognitionStatus": "Success",
            "channel": 1,
            "offset": "PT3M59.36S",
            "duration": "PT0.32S",
            "offsetInTicks": 2393600000.0,
            "durationInTicks": 3200000.0,
            "nBest": [
              {
                "confidence": 0.7800385,
                "lexical": "bye",
                "itn": "bye",
                "maskedITN": "Bye",
                "display": "Bye.",
                "sentiment": {
                  "positive": 0.25,
                  "neutral": 0.7,
                  "negative": 0.05
                }
              }
            ]
          }
        ]
      }
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
