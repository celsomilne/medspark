class Languages:

    # TODO : move this to a separate file
    _languages = {
        "af": "Afrikaans",
        "ak": "Akan",
        "sq": "Albanian",
        "ws": "Samoa",
        "am": "Amharic",
        "ar": "Arabic",
        "hy": "Armenian",
        "az": "Azerbaijani",
        "eu": "Basque",
        "be": "Belarusian",
        "bn": "Bengali",
        "bh": "Bihari",
        "bs": "Bosnian",
        "br": "Breton",
        "bg": "Bulgarian",
        "bt": "Bhutanese",
        "km": "Cambodian",
        "ca": "Catalan",
        "ny": "Chichewa",
        "co": "Corsican",
        "hr": "Croatian",
        "cs": "Czech",
        "da": "Danish",
        "nl": "Dutch",
        "en": "English",
        "eo": "Esperanto",
        "et": "Estonian",
        "ee": "Ewe",
        "fo": "Faroese",
        "tl": "Filipino",
        "fi": "Finnish",
        "fr": "French",
        "fy": "Frisian",
        "gl": "Galician",
        "ka": "Georgian",
        "de": "German",
        "el": "Greek",
        "kl": "Greenlandic",
        "gn": "Guarani",
        "gu": "Gujarati",
        "ht": "Haitian Creole",
        "ha": "Hausa",
        "iw": "Hebrew",
        "hi": "Hindi",
        "hu": "Hungarian",
        "is": "Icelandic",
        "ig": "Igbo",
        "id": "Indonesian",
        "ia": "Interlingua",
        "ga": "Irish",
        "it": "Italian",
        "ja": "Japanese",
        "jw": "Javanese",
        "kn": "Kannada",
        "kk": "Kazakh",
        "rw": "Kinyarwanda",
        "rn": "Kirundi",
        "kg": "Kongo",
        "ko": "Korean",
        "ku": "Kurdish",
        "ky": "Kyrgyz",
        "lo": "Laothian",
        "la": "Latin",
        "lv": "Latvian",
        "ln": "Lingala",
        "lt": "Lithuanian",
        "lg": "Luganda",
        "mk": "Macedonian",
        "mg": "Malagasy",
        "my": "Malay",
        "ml": "Malayalam",
        "mt": "Maltese",
        "mv": "Maldives",
        "mi": "Maori",
        "mr": "Marathi",
        "mo": "Moldavian",
        "mn": "Mongolian",
        "ne": "Nepali",
        "no": "Norwegian",
        "oc": "Occitan",
        "or": "Oriya",
        "om": "Oromo",
        "ps": "Pashto",
        "fa": "Persian",
        "pl": "Polish",
        "pt": "Portuguese",
        "pa": "Punjabi",
        "qu": "Quechua",
        "ro": "Romanian",
        "rm": "Romansh",
        "ru": "Russian",
        "gd": "Scots Gaelic",
        "sr": "Serbian",
        "st": "Sesotho",
        "tn": "Setswana",
        "sn": "Shona",
        "sd": "Sindhi",
        "si": "Sinhalese",
        "sk": "Slovak",
        "sl": "Slovenian",
        "so": "Somali",
        "es": "Spanish",
        "su": "Sundanese",
        "sw": "Swahili",
        "sv": "Swedish",
        "tg": "Tajik",
        "ta": "Tamil",
        "tt": "Tatar",
        "te": "Telugu",
        "th": "Thai",
        "ti": "Tigrinya",
        "to": "Tonga",
        "tr": "Turkish",
        "tk": "Turkmen",
        "tw": "Twi",
        "ug": "Uighur",
        "uk": "Ukrainian",
        "ur": "Urdu",
        "uz": "Uzbek",
        "vu": "Vanuatu",
        "vi": "Vietnamese",
        "cy": "Welsh",
        "wo": "Wolof",
        "xh": "Xhosa",
        "yi": "Yiddish",
        "yo": "Yoruba",
        "zu": "Zulu",
    }

    # Static method which returns the language code for a given language name
    @staticmethod
    def get_language_code(language_name):
        for code, name in Languages._languages.items():
            if name == language_name:
                return code

        # Raise an exception, as the language name was not found
        raise Exception("Language name not found")

    # Static method which returns the language name for a given language code
    @staticmethod
    def get_language_name(language_code):
        return Languages._languages[language_code]

    # Return the languages as a list of tuples
    @staticmethod
    def as_tuples():
        return [(code, name) for code, name in Languages._languages.items()]

    # Return whether the language code is valid
    @staticmethod
    def is_valid_language_code(language_code):
        return language_code in Languages.as_dict()

    @staticmethod
    def as_dict():
        return Languages._languages

    @staticmethod
    def as_list():
        return list(Languages._languages.keys())
