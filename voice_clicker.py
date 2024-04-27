import speech_recognition as sr
import pyautogui


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-US")
        print(f"Recognized speech: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not recognize speech")
    except sr.RequestError as e:
        print(f"Error occurred in speech recognition service: {e}")


def main():
    while True:
        text = recognize_speech()
        if text:
            if (
                "left" in text.lower()
                or "port" in text.lower()
                or "nav left" in text.lower()
            ):
                pyautogui.press("left")
                print("Left arrow key pressed")
            elif (
                "right" in text.lower()
                or "starboard" in text.lower()
                or "nav right" in text.lower()
            ):
                pyautogui.press("right")
                print("Right arrow key pressed")


if __name__ == "__main__":
    main()
