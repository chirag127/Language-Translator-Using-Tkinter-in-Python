from tkinter import *
from translate import Translator

# Translator function


def translate():
    translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)


# Tkinter chiragsinghalwindow Window with title
chiragsinghalwindow = Tk()
chiragsinghalwindow.title("Translator App created by mayank kaushik and harsh rai")

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
Label(mainframe, text="Select a language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)

lan2menu = OptionMenu(mainframe, lan2, *choices)
Label(mainframe, text="Select a language").grid(row=0, column=2)
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

chiragsinghalwindow.mainloop()
