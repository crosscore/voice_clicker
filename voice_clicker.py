import speech_recognition as sr
import pyautogui


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("話してください...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ja-JP")
        print(f"認識された音声: {text}")
        return text
    except sr.UnknownValueError:
        print("音声を認識できませんでした")
    except sr.RequestError as e:
        print(f"音声認識サービスにエラーが発生しました: {e}")


def main():
    while True:
        text = recognize_speech()
        if text:
            if "左" in text:
                pyautogui.press("left")
                print("方向キーの←を入力しました")


if __name__ == "__main__":
    main()
