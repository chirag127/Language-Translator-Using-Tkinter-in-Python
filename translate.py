import pyautogui
from time import sleep
import pytesseract
import keyboard
import googletrans
import pyttsx3


def sp(text):
    print(text)
    speak(text)


# make a program that will take a screenshot of the screen and save it to a file
# then it will read the text from the file and translate it to english
# then it will speak the text

# take a screenshot of area around the cursor


def screenshot():
    x = pyautogui.position()[0]
    y = pyautogui.position()[1]

    width = 100
    height = 30

    img = pyautogui.screenshot("screenshot.png", region=(x + 10, y, width, height))
    print("Screenshot taken")

    img.save("screenshot.png")

    # import mss
    # import mss.tools

    # with mss.mss() as sct:
    #     # The screen part to capture
    #     region = {'top': y, 'left': x, 'width': width, 'height': height}

    #     # Grab the data
    #     img = sct.grab(region)

    #     # Save to the picture file
    #     mss.tools.to_png(img.rgb, img.size, output='screenshot.png')

    return img


def ocr():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
    return pytesseract.image_to_string(screenshot(), lang="chi_tra_vert")


def translate():
    text = ocr()
    print(text)
    translator = googletrans.Translator()
    translation = translator.translate(text, dest="en")
    return translation.text


def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


def main():
    while True:
        if keyboard.is_pressed("q"):
            sp(translate())

        else:
            sleep(0.1)


if __name__ == "__main__":
    main()
