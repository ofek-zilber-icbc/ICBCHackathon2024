# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"

key = "a950fc49a1c048ce8c458048403b2704"
endpoint = "https://language-service-2.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Authenticate the client using your key and endpoint 
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for summarizing text
def sample_extractive_summarization(client):
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    ) 

    document = [
       "hi this is bobby calling from I C B C S assembly hi this is emily yes oh hi emily i'm glad i got a hold of you it's been really hard to reach you i've been trying to call you for a while oh has it yeah it has but i guess you're really busy so i'm glad that i got a hold of you and i wanted to talk to you about your treatment and your injury claim OK what did you want to talk about specifically well i want to talk to you about how your treatment is going so i've noticed that you've been going for to your RMT to massage for a while and last time we talked we talked about also going to your physiotherapist i see that your doctor had recommended it too before and i want to follow up to see if you've been doing that or if you've talked to them yeah it's been kind of easier just to go to my massage therapist 'cause i can get appointments i was hoping i could find a physiotherapist in the same clinic but i couldn't so i thought it was just easier to keep going to my massage therapist OK well i want you to know that it's been about a month now and you're not going to notice the difference and you're not going to notice much of improvement if you don't follow the instructions that we talked about last time oh OK well my massage therapist kept booking me in so i thought i was just good to keep going there yeah i can see that and we approved the last treatment request that your massage therapist sent in but to be honest with you i'm not going to prove the next one i did talk to you about talking to your physiotherapist and making that call so you're going to need to do that if you want to keep having treatment provided under your claim OK that makes sense i can do that you know what i'm feeling pretty good anyways so i don't even know if i'm going to need any more treatment well you mentioned that you're still having problems with your knee and you're fine now is that what you're saying yeah i mean it still hurts but i think you know it could be worse so well i like i told you before if you don't follow the advice you were given it likely could get worse and then you're not going to be able to get any treatment afterwards so when we talked and i gave you the information i you are expected to follow it you do have a duty to also go with the treatment and with what's what the guidance is so that you do recover and feel better OK well i guess i could always talk to my massage therapist and then yeah i could try calling around some physiotherapy clinics but if i don't it's OK too if i don't get any more treatment well i really want you to reach out and call your physiotherapist and since you haven't done it yet and this is the third time we've talked about it if you could please give me a call back next week let's try to do that so that you're talking to them by then and i would like to get an update from you if i don't then i don't think i'll be able to approve any more of the massage either OK so what happens if i need more treatment though or if i feel like i'm still in pain or i'm not able to do all of my regular stuff well if you had been going for the treatment that was recommended in the beginning then you probably would have noticed you're feeling better by now and you probably wouldn't need to come back but if you're going to pause and stop treatment it's gonna be really difficult for us to approve any more for you really i think i've talked to you before and i put the notes in your file here that you're not following the advice that you were given oh OK well i'm really sorry i didn't mean to not follow the advice like i i typically do like to follow what you tell me i just must have forgot but yeah OK i can do what you told me and i'll i'll try and talk to a physiotherapist and see if i can get in and get some more treatment there but if not i guess i just won't bother you anymore well i've noted that down your file and you've been given all the information so you know what needs to happen next again if i don't hear back from by next week then we won't be approving any more treatment OK OK well i'll try to follow up then with a physiotherapist and i'll try to get back to you next week is there anything else that i should be doing no you have my number and like i mentioned i tried to reach you multiple times over the last couple weeks and it's really hard to get a hold of you so you know what time i work so please give me a call OK i'm really sorry about that thanks so much for calling me today OK bye"
    ]

    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=4)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

sample_extractive_summarization(client)