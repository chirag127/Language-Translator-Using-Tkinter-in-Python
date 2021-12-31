import pyttsx3

# required engine for text to speech

engine = pyttsx3.init("sapi5")

# sapi5 is the default voice engine of windows and it is installed by default in windows

# getproperties is used to get the properties of the engine like rate, volume, pitch, etc.

voices = engine.getProperty("voices")


# setproperties is used to set the properties of the engine like rate, volume, pitch, etc.


engine.setProperty("voice", voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# wish according to the time
def wish():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


wish()
# Translator function

# # end further execution if run as a standalone program
# exit()

from translate import Translator

def translate():
    translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)

from tkinter import *


# Tkinter chiragsinghalwindow Window with title
chiragsinghalwindow = Tk()
chiragsinghalwindow.title("Translator App by Chirag Singhal")

# Creating a Frame and Grid to hold the Content
mainframe = Frame(chiragsinghalwindow)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)

# variables for dropdown list
lan1 = StringVar(chiragsinghalwindow)
lan2 = StringVar(chiragsinghalwindow)


# supported languages are Afrikaans
# Albanian
# Amharic
# Arabic
# Armenian
# Azerbaijani
# Bajan
# Balkan Gipsy
# Basque
# Bemba
# Bengali
# Bielarus
# Bislama
# Bosnian
# Breton
# Bulgarian
# Burmese
# Catalan
# Cebuano
# Chamorro
# Chinese (Simplified)
# Chinese Traditional
# Comorian (Ngazidja)
# Coptic
# Creole English (Antigua and Barbuda)
# Creole English (Bahamas)
# Creole English (Grenadian)
# Creole English (Guyanese)
# Creole English (Jamaican)
# Creole English (Vincentian)
# Creole English (Virgin Islands)
# Creole French (Haitian)
# Creole French (Saint Lucian)
# Creole French (Seselwa)
# Creole Portuguese (Upper Guinea)
# Croatian
# Czech
# Danish
# Dutch
# Dzongkha
# English
# Esperanto
# Estonian
# Fanagalo
# Faroese
# Finnish
# French
# Galician
# Georgian
# German
# Greek
# Greek (Classical)
# Gujarati
# Hausa
# Hawaiian
# Hebrew
# Hindi
# Hungarian
# Icelandic
# Indonesian
# Inuktitut (Greenlandic)
# Irish Gaelic
# Italian
# Japanese
# Javanese
# Kabuverdianu
# Kabylian
# Kannada
# Kazakh
# Khmer
# Kinyarwanda
# Kirundi
# Korean
# Kurdish
# Kurdish Sorani
# Kyrgyz
# Lao
# Latin
# Latvian
# Lithuanian
# Luxembourgish
# Macedonian
# Malagasy
# Malay
# Maldivian
# Maltese
# Manx Gaelic
# Maori
# Marshallese
# Mende
# Mongolian
# Morisyen
# Nepali
# Niuean
# Norwegian
# Nyanja
# Pakistani
# Palauan
# Panjabi
# Papiamentu
# Pashto
# Persian
# Pijin
# Polish
# Portuguese
# Potawatomi
# Quechua
# Romanian
# Russian
# Samoan
# Sango
# Scots Gaelic
# Serbian
# Shona
# Sinhala
# Slovak
# Slovenian
# Somali
# Sotho, Southern
# Spanish
# Sranan Tongo
# Swahili
# Swedish
# Swiss German
# Syriac (Aramaic)
# Tagalog
# Tajik
# Tamashek (Tuareg)
# Tamil
# Telugu
# Tetum
# Thai
# Tibetan
# Tigrinya
# Tok Pisin
# Tokelauan
# Tongan
# Tswana
# Turkish
# Turkmen
# Tuvaluan
# Ukrainian
# Uma
# Uzbek
# Vietnamese
# Wallisian
# Welsh
# Wolof
# Xhosa
# Yiddish
# Zulu

# choices to show in dropdown menu
choices = {
    "Afrikaans",
    "Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Azerbaijani",
    "Bajan",
    "Balkan Gipsy",
    "Basque",
    "Bemba",
    "Bengali",
    "Bielarus",
    "Bislama",
    "Bosnian",
    "Breton",
    "Bulgarian",
    "Burmese",
    "Catalan",
    "Cebuano",
    "Chamorro",
    "Chinese",
    "Comorian",
    "Coptic",
    "Croatian",
    "Czech",
    "Danish",
    "Dutch",
    "Dzongkha",
    "English",
    "Esperanto",
    "Estonian",
    "Fanagalo",
    "Faroese",
    "Finnish",
    "French",
    "Galician",
    "Georgian",
    "German",
    "Greek",
    "Gujarati",
    "Hausa",
    "Hawaiian",
    "Hebrew",
    "Hindi",
    "Hungarian",
    "Icelandic",
    "Indonesian",
    "Irish Gaelic",
    "Italian",
    "Japanese",
    "Javanese",
    "Kabuverdianu",
    "Kabylian",
    "Kannada",
    "Kazakh",
    "Khmer",
    "Kinyarwanda",
    "Kirundi",
    "Korean",
    "Kurdish",
    "Kurdish Sorani",
    "Kyrgyz",
    "Lao",
    "Latin",
    "Latvian",
    "Lithuanian",
    "Luxembourgish",
    "Macedonian",
    "Malagasy",
    "Malay",
    "Maldivian",
    "Maltese",
    "Manx Gaelic",
    "Maori",
    "Marshallese",
    "Mende",
    "Mongolian",
    "Morisyen",
    "Nepali",
    "Niuean",
    "Norwegian",
    "Nyanja",
    "Pakistani",
    "Palauan",
    "Panjabi",
    "Papiamentu",
    "Pashto",
    "Persian",
    "Pijin",
    "Polish",
    "Portuguese",
    "Potawatomi",
    "Quechua",
    "Romanian",
    "Russian",
    "Samoan",
    "Sango",
    "Scots Gaelic",
    "Serbian",
    "Shona",
    "Sinhala",
    "Slovak",
    "Slovenian",
    "Somali",
    "Spanish",
    "Sranan Tongo",
    "Swahili",
    "Swedish",
    "Swiss German",
    "Tagalog",
    "Tajik",
    "Tamil",
    "Telugu",
    "Tetum",
    "Thai",
    "Tibetan",
    "Tigrinya",
    "Tok Pisin",
    "Tokelauan",
    "Tongan",
    "Tswana",
    "Turkish",
    "Turkmen",
    "Tuvaluan",
    "Ukrainian",
    "Uma",
    "Uzbek",
    "Vietnamese",
    "Wallisian",
    "Welsh",
    "Wolof",
    "Xhosa",
    "Yiddish",
    "Zulu",
}

# default selection for dropdownlists
lan1.set("English")
lan2.set("Hindi")

# creating dropdown and arranging in the grid
lan1menu = OptionMenu(mainframe, lan1, *choices)
Label(mainframe, text="From Language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)

lan2menu = OptionMenu(mainframe, lan2, *choices)
Label(mainframe, text="To Language").grid(row=0, column=2)
lan2menu.grid(row=1, column=2)

# Text Box to take user input
Label(mainframe, text="Enter text").grid(row=2, column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2, column=1)

# textbox to show output
# label can also be used
Label(mainframe, text="Output").grid(row=2, column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1).grid(row=2, column=3)

# creating a button to call Translator function
b = Button(mainframe, text="Translate", command=translate).grid(
    row=3, column=1, columnspan=3
)
speak("Welcome to the translator software")
speak("Enter the text you want to translate in the text box named Enter text")
speak("Enter the language you want to translate from in the drop down menu named From language")
speak("Enter the language you want to translate to in the drop down menu named To language")

chiragsinghalwindow.mainloop()


