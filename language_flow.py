def get_twiml_response(user_input):
    from twilio.twiml.voice_response import VoiceResponse

    response = VoiceResponse()

    if "hindi" in user_input:
        response.say("Namaste! BullWash Ghar aur Gaadi Safai mein aapka swagat hai. Kripya apna naam aur location batayein.", language="hi-IN")
    elif "marathi" in user_input:
        response.say("Namaskaar! BullWash madhe tumcha swagat aahe. Tumcha naav aani location sangaa.", language="mr-IN")
    elif "tamil" in user_input:
        response.say("Vanakkam! BullWash house cleaning service-il unga swagatam. Unga peyar sollunga.", language="ta-IN")
    elif "bengali" in user_input:
        response.say("Namaskar! BullWash service-e apnar swagat. Apnar naam aar thikana bolun.", language="bn-IN")
    else:
        response.say("Hello! Welcome to BullWash Auto and Home Cleaning Services. Please say your name and location.", language="en-IN")

    return str(response)
