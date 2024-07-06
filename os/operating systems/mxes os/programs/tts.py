while True:
    import pyttsx3 # type: ignore
    engine = pyttsx3.init()
    line=input("> input line to exit input $exit$.\n> ")
    if line=="$exit$":
        exit()
    engine.say(line)
    engine.runAndWait()