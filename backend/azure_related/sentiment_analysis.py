"""
FILE: sample_analyze_sentiment.py

DESCRIPTION:
    This sample demonstrates how to analyze sentiment in documents.
    An overall and per-sentence sentiment is returned.

    In this sample we will be a skydiving company going through reviews people have left for our company.
    We will extract the reviews that we are certain have a positive sentiment and post them onto our
    website to attract more divers.

USAGE:
    python sample_analyze_sentiment.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_LANGUAGE_ENDPOINT - the endpoint to your Language resource.
    2) AZURE_LANGUAGE_KEY - your Language subscription key
"""

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = os.environ["LANGUAGE_ENDPOINT"]
key = os.environ["LANGUAGE_KEY"]

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


def analyze_sentiment():
    # conversation = [{'speaker': 'Guest-1', 'text': "Hi there, I'm calling from ICBC. My name is Eddie. I'm looking for Emily please."}, {'speaker': 'Guest-1', 'text': 'This is Emily.'}, 
    #                 {'speaker': 'Guest-1', 'text': 'Hey Emily, how are?'}, 
    #                 {'speaker': 'Guest-2', 'text': "You. I'm OK. How are you?"}, 
    #                 {'speaker': 'Guest-1', 'text': "I'm doing pretty good. How? How was the oven repair that you had the other day? Did that work out?"}, 
    #                 {'speaker': 'Guest-2', 'text': "OK, Oh, actually they weren't able to fix it and I have to have them come."}, 
    #                 {'speaker': 'Guest-1', 'text': "Back another day next week. Oh, no, I hope that goes well. And yeah, but, you know, hopefully it doesn't cost too much or anything. But yeah, hopefully you have a couple of minutes and let's just chat about part of your recovery. And we did get a chance to review your treatment plan. How does that sound?"}, 
    #                 {'speaker': 'Guest-1', 'text': "Thanks. Now is a good time. OK, great. This will probably last maybe 5 minutes or so, maybe even less. But you know, throughout this conversation, just don't hesitate to ask any questions and like we usually do. But I've got some interesting news here because we have had a chance to review the treatment that you're going through. And as you know, we've had a couple steps leading up to today and that involves, for example, our medical assessment. We've had a chance to speak with your care team as well."}, 
    #                 {'speaker': 'Guest-1', 'text': "Really just to take a look at how your recovery is going. So I just wanted to share about the decision on some of the treatments and how we're going to make your recovery move forward on that. Before I go into that, did you have any questions about what we've been doing so far?"}, 
    #                 {'speaker': 'Guest-2', 'text': "No, that makes sense. I'm curious to know what the next steps are and and you know what the decision is regarding the treatment."}, 
    #                 {'speaker': 'Guest-1', 'text': 'Really happy to go over it and really want to give you as much details as possible on this and.'}, 
    #                 {'speaker': 'Guest-1', 'text': "Basically, after our review cycle that we've had, we've had the medical assessment like I mentioned and then talked to the healthcare providers and more recently talking to this healthcare provider that shared the treatment plan. We took took a look at some of the progress. We took a look at some of the limitations that you've had. I think some of the things you mentioned where you weren't able to work on the oven and do some of the repairs. You also have some challenges with raising your arm up above."}, 
    #                 {'speaker': 'Guest-1', 'text': "Your shoulder and a lot of that is resolved based on what we can see here. You're also able to get back to most of your daily activities. So I think you mentioned something along the lines of playing soccer. You're back to playing about 90% of those games and while there is a little bit of pain, you're able to go through all of it. So reviewing all the information there at this point, it doesn't look like we can approve further treatment for your physiotherapy. What we can do and and offer is."}, 
    #                 {'speaker': 'Guest-1', 'text': 'To help get you into something more active, just to really help you get to that next level of your recovery and move you move you past the passive treatments here. How does that sound?'}, 
    #                 {'speaker': 'Guest-2', 'text': 'OK, what do you mean something more active have?'}, 
    #                 {'speaker': 'Guest-1', 'text': 'You have you had a chance to try kinesiology or any self self-guided training gym programs? Any of those before?'}, 
    #                 {'speaker': 'Guest-2', 'text': "No, I think I've seen a sign for it at the clinic I go to, but no, I haven't."}, 
    #                 {'speaker': 'Guest-1', 'text': "Fair enough, and happy to go over some of those details with you. I think there's a couple of things we can definitely do with you and we want to find something that works for you as well. Umm, do you have any actually? Because they're probably the soccer team. Do you know anyone on your team that you might want to ask about what might work for you in terms of, you know, transitioning from physiotherapy to something more active?"}, 
    #                 {'speaker': 'Guest-2', 'text': "Oh, actually, you know what? I think someone on my team might be a kinesiologist themselves. Yeah, maybe I'll reach out to them."}, 
    #                 {'speaker': 'Guest-1', 'text': "I think that's a great idea. That's a great start, kind of see what works for them and then you can let me know if there's also any equipment or anything that might help you become more independent in your training."}, 
    #                 {'speaker': 'Guest-1', 'text': "Just to really get you to that final step, your recovery. And once you're done that part, then we can probably look at discharging the claim. How does that sound? Did you want to go check in with your teammate? And then we can have a conversation about, let's say next Thursday. May I call you around the same time and then we can look at some of those."}, 
    #                 {'speaker': 'Guest-2', 'text': 'Options together? Yeah, that sounds good. Next Thursday works for me so we can chat then.'}, 
    #                 {'speaker': 'Guest-1', 'text': "Maybe we'll get some updates and some good news on repairing your oven as well. So before I wrap up here though, since you've got me, any other questions, like anything else I can help you out with?"}, 
    #                 {'speaker': 'Guest-2', 'text': "No, I think that's it for now. I'll talk to them and then I'll try to think of any questions before we speak next Thursday."}, 
    #                 {'speaker': 'Guest-1', 'text': "Absolutely fantastic. I just want to commend you on how well you've done on your recovery and just seeing that everything that you've participated in, it's a lot about your own journey to recovery and you've done a really great job. And I think we'll get you to that last step and we'll move forward together on that. OK, So we'll chat next week then. OK, Fantastic. Bye for now."}, 
    #                 {'speaker': 'Unknown', 'text': ''}]
    conversation = [{'speaker': 'Guest-1', 'text': 'Hi, may I speak to Emily please?'}, 
                    {'speaker': 'Guest-1', 'text': 'Yep, this is Emily.'}, 
                    {'speaker': 'Guest-1', 'text': "I'm OK, I'm kind of busy. What do you?"}, 
                    {'speaker': 'Guest-1', 'text': "Need. Oh, I'm sorry to hear that. Is there a better time to reach her? Do you have a?"}, 
                    {'speaker': 'Guest-1', 'text': 'OK. And how are things going with you right now?'}, 
                    {'speaker': 'Guest-2', 'text': "Not good. Like every morning I wake up I'm in so much pain. I know that my physio and my massage therapist has put a new treatment plan in and haven't heard anything."}, 
                    {'speaker': 'Guest-2', 'text': "Like I need treatment. My doctor agrees I need treatment too. What's going on?"}, 
                    {'speaker': 'Guest-2', 'text': "I don't know, It feels like a really long time, like at least eight weeks or so."}, 
                    {'speaker': 'Guest-1', 'text': "OK, Yeah, that that shouldn't happen and let's look into that right now so we can sort things out for you. If you have a few minutes. I'm just going to ask you from the last couple of physios that you did, how you felt things were going."}, 
                    {'speaker': 'Guest-1', 'text': "I'm just looking at your file here and it looks like you were finding that it was a little bit helpful, but I just wanted to check now to see what your thoughts were and see what we can."}, 
                    {'speaker': 'Guest-2', 'text': "Do honestly, it's been like a year and a half and I don't feel like I've made any progress at all. Like I, you know, it's so disruptive to my life. I go to treatment three times a week now. I've been paying for it out of pocket the last two months and I'm not feeling any better."}, 
                    {'speaker': 'Guest-1', 'text': "OK, I'm, I'm sorry again to hear about the you're paying out of pocket."}, 
                    {'speaker': 'Guest-1', 'text': "That technically we that shouldn't be happening, so let's take care of that for you. I'll get that information from you."}, 
                    {'speaker': 'Guest-1', 'text': "In a second, but also I'm a little concerned for you about your treatment and that you haven't been able to go."}, 
                    {'speaker': 'Guest-1', 'text': "I'm looking at the information I have here and it looks like you still have some sessions left with your physiotherapist. I'm just wondering why?"}, 
                    {'speaker': 'Guest-1', 'text': "You were thinking you weren't able to go serve a reason, Yeah."}, 
                    {'speaker': 'Guest-2', 'text': 'They told me that the treatment was cut off by ACDC and I had to pay. Sorry, who? Who told you that? The physiotherapist.'}, 
                    {'speaker': 'Guest-1', 'text': "I'm really sorry to hear that. OK, we can clear that up with them. But there, there are some sessions left. But you know what? I don't want you to have to worry about this. You leave that with me."}, 
                    {'speaker': 'Guest-1', 'text': "I will contact your physiotherapist and follow up with you. I can do that today because I want to make sure that you're still able to go for treatment and this is not interrupting your recovery. Is there anything else that's going on right now that I."}, 
                    {'speaker': 'Guest-2', 'text': "Can help with yeah, I mean, you know, whatever, if my treatment is going to be cut off, like, you know, that's annoying. It's unfair because I still need treatment. But I guess, you know, we can also just settle the claim up and and I can have my compensation now."}, 
                    {'speaker': 'Guest-2', 'text': "What? What's your offer today?"}, 
                    {'speaker': 'Guest-1', 'text': "You know, Emily, I just wanted to clarify, I know we've talked about this before as well, but I just wanted to make sure that you were clear that we actually don't do that. ICBC doesn't supply compensation for your claim since we started with enhanced care. We talked about this in the beginning reclaim. So I wanted to make sure that you understand and please ask me any questions about it. But overall, what it is, is when you are in an accident, we want to make sure that we're doing everything to help you recover and that's including the treatment. You mentioned that you've been going to physio for about a year and a half. So that's part of the benefits that you get with your claim."}, 
                    {'speaker': 'Guest-1', 'text': "And I know that we followed up with your doctor as well to check on your recovery and how you're doing. Those are are the things that we want to do to support you. There isn't any compensation amount."}, 
                    {'speaker': 'Guest-2', 'text': "What, There's no more compensation? So I've been struggling with this injury. I have been wasting all my time going to treatment and I'm not even going to get any money for."}, 
                    {'speaker': 'Guest-1', 'text': "It we, we don't have compensation anymore, Emily, that is correct."}, 
                    {'speaker': 'Guest-2', 'text': 'OK, whatever. Bye.'}, 
                    {'speaker': 'Unknown', 'text': ''}]
    

    sentences = list(map(lambda c: c['text'], conversation))
    
    # print("sentences: " + str(sentences))
    i = 0
    negatives = []
    while i < len(sentences):
        sub = list((sentences[idx] for idx in range(i, min(i+10, len(sentences)))))
        # print("sub: " + str(sub))
        result = text_analytics_client.analyze_sentiment(sub, show_opinion_mining=True)
        for r in result:
            # print("result: {}".format(r))
            if not r.is_error and r.sentiment == 'negative':
                negatives.append(r)
                print("********************BEGIN SENTIMENT**********************")
                print("sentiment: " + r.sentiment)
                print("id: " + r.id)
                print("kind: " + r.kind)
                print("stats: {}".format(r.statistics))
                for s in r.sentences:
                    print("*********BEGIN SENTENCE***********")
                    print("sentiment: " + s.sentiment)
                    print("confidence: {}".format(s.confidence_scores))
                    print("text: " + s.text)
                    print("length: {}".format(s.length))
                    print("offset: {}".format(s.offset))
                    print("mined_opinions: {}".format(s.mined_opinions))
                    print("*********END SENTENCE***********")
                print("********************END SENTIMENT**********************")

        i += 10
    
    # print("negatives: {}".format(negatives))

    


def sample_analyze_sentiment() -> None:
    print(
        "In this sample we will be combing through reviews customers have left about their"
        "experience using our skydiving company, Contoso."
    )
    print(
        "We start out with a list of reviews. Let us extract the reviews we are sure are "
        "positive, so we can display them on our website and get even more customers!"
    )

    # [START analyze_sentiment]
    

    endpoint = os.environ["LANGUAGE_ENDPOINT"]
    key = os.environ["LANGUAGE_KEY"]

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    documents = [
        """I had the best day of my life. I decided to go sky-diving and it made me appreciate my whole life so much more.
        I developed a deep-connection with my instructor as well, and I feel as if I've made a life-long friend in her.""",
        """This was a waste of my time. All of the views on this drop are extremely boring, all I saw was grass. 0/10 would
        not recommend to any divers, even first timers.""",
        """This was pretty good! The sights were ok, and I had fun with my instructors! Can't complain too much about my experience""",
        """I only have one word for my experience: WOW!!! I can't believe I have had such a wonderful skydiving company right
        in my backyard this whole time! I will definitely be a repeat customer, and I want to take my grandmother skydiving too,
        I know she'll love it!"""
    ]


    result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
    docs = [doc for doc in result if not doc.is_error]

    print("Let's visualize the sentiment of each of these documents")
    for idx, doc in enumerate(docs):
        print(f"Document text: {documents[idx]}")
        print(f"Overall sentiment: {doc.sentiment}")
    # [END analyze_sentiment]

    print("Now, let us extract all of the positive reviews")
    positive_reviews = [doc for doc in docs if doc.sentiment == 'positive']

    print("We want to be very confident that our reviews are positive since we'll be posting them on our website.")
    print("We're going to confirm our chosen reviews are positive using two different tests")

    print(
        "First, we are going to check how confident the sentiment analysis model is that a document is positive. "
        "Let's go with a 90% confidence."
    )
    positive_reviews = [
        review for review in positive_reviews
        if review.confidence_scores.positive >= 0.9
    ]

    print(
        "Finally, we also want to make sure every sentence is positive so we only showcase our best selves!"
    )
    positive_reviews_final = []
    for idx, review in enumerate(positive_reviews):
        print(f"Looking at positive review #{idx + 1}")
        any_sentence_not_positive = False
        for sentence in review.sentences:
            print("...Sentence '{}' has sentiment '{}' with confidence scores '{}'".format(
                sentence.text,
                sentence.sentiment,
                sentence.confidence_scores
                )
            )
            if sentence.sentiment != 'positive':
                any_sentence_not_positive = True
        if not any_sentence_not_positive:
            positive_reviews_final.append(review)

    print("We now have the final list of positive reviews we are going to display on our website!")


if __name__ == '__main__':
    analyze_sentiment()