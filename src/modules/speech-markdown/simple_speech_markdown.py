class SimpleSpeechMarkdown:
    _emphasis_levels = {
        "strong": "++",
        "moderate": "+",
        "none": "~",
        "reduced": "-",
    }
    _rate_levels = [
        "x-slow",
        "slow",
        "medium",
        "fast",
        "x-fast"
    ]
    _pitch_levels = [
        "x-high",
        "high",
        "medium",
        "low",
        "x-low"
    ]
    _time_formats = [
        "hms12",
        "hms24"
    ]
    _units = [
        "foot",
        "ft"
    ]
    _volume_levels = [
        "silent",
        "x-soft",
        "soft",
        "medium",
        "loud",
        "x-loud"
    ]
    def __init__(self):
        pass
    def address(self, text: str) -> str:
        """
        Args:
            text (str): Address text
        Returns:
            str: Speech Markdown address (e.g. "(123 Main Street)[address]")
        See Also:
            https://www.speechmarkdown.org/syntax/address/
        """
        return f'({text})[address]'
    def audio(self, url, caption: str = "", standard: bool = True) -> str:
        """
        Args:
            url (str): Audio URL
            caption (str): Audio caption
            standard (bool): Standard or short format
        Returns:
            str: Speech Markdown audio (e.g. "!({caption})[\"{url}\"]")
        See Also:
            https://www.speechmarkdown.org/syntax/audio/
        """
        if(standard):
            return f'!({caption})[\"{url}\"]'
        else: # short format
            return f'![\"{url}\"]'
    def break_(self, time: int = 500, time_as: str = "ms", strength: str = None) -> str:
        """
        Args:
            time (int): Time
            time_as (str): Time unit
            strength (str): Strength
        Returns:
            str: Speech Markdown break (e.g. "[500ms]" or "[break:\"strong\"]")
        See Also:
            https://www.speechmarkdown.org/syntax/break/
        """
        if(strength):
            return f'[break:\"{strength}\"]'
        else:
            return f'[{time}{time_as}]'
    def cardinal(self, number: int) -> str:
        """
        Args:
            number (int): Cardinal number
        Returns:
            str: Speech Markdown cardinal (e.g. "(123)[cardinal]")
        See Also:
            https://www.speechmarkdown.org/syntax/cardinal/
        """
        return f'({number})[cardinal]'
    def characters(self, text: str) -> str:
        """
        Args:
            text (str): Characters
        Returns:
            str: Speech Markdown characters (e.g. "(abc)[characters]")
        See Also:
            https://www.speechmarkdown.org/syntax/characters/
        """
        return f'({text})[characters]'
    def date(self, text: str, format: str = "dmy") -> str:
        """
        Args:
            text (str): Date text
            format (str): Date format
        Returns:
            str: Speech Markdown date (e.g. "(01/01/2020)[date:dmy]")
        See Also:
            https://www.speechmarkdown.org/syntax/date/
        """
        # TODO date text verification (supports seperators: slash /, dash -, dot .)
        return f'({text})[date:{format}]'
    def emphasis(self, text: str, level: str, inline: bool = False) -> str:
        """
        Args:
            text (str): Emphasis text
            level (str): Emphasis level (must be one of "strong", "moderate", "none", "reduced")
            inline (bool): Inline or standard format
        Returns:
            str: Speech Markdown emphasis (e.g. "(text)[emphasis:\"strong\"] or "++text++" with inline=True)
        Raises:
            ValueError: Invalid emphasis level
        See Also:
            https://www.speechmarkdown.org/syntax/emphasis/
        """
        if(level not in self._emphasis_levels.keys()):
            raise ValueError(f'Invalid emphasis level: {level} (must be one of {self._emphasis_levels.keys()})')
        if(inline):
            return f'{_emphasis_levels[level]}{text}{_emphasis_levels[level]}'
        else:
            return f'({text})[emphasis:\"{level}\"]'
    def expletive(self, text: str) -> str:
        """
        Args:
            text (str): Expletive text
        Returns:
            str: Speech Markdown expletive (e.g. "(text)[expletive]")
        See Also:
            https://www.speechmarkdown.org/syntax/expletive/
        """
        return f'({text})[expletive]'
    def fraction(self, numerator, denominator) -> str:
        """
        Args:
            numerator: Numerator (must be int or str)
            denominator: Denominator (must be int or str)
        Returns:
            str: Speech Markdown fraction (e.g. "(1/2)[fraction]" or "(1+1/2)[fraction]")
        Raises:
            ValueError: Invalid numerator type (must be int or str)
            ValueError: Invalid denominator type (must be int or str)
        See Also:
            https://www.speechmarkdown.org/syntax/fraction/
        """
        # can be int (e.g. 4) or str (e.g. '1+1')
        if(type(numerator) is not int and type(numerator) is not str):
            raise ValueError(f'Invalid numerator type: {type(numerator)} (must be int or str)')
        if(type(denominator) is not int and type(denominator) is not str):
            raise ValueError(f'Invalid denominator type: {type(denominator)} (must be int or str)')
        return f'({numerator}/{denominator})[fraction]'
    def interjection(self, text: str) -> str:
        """
        Args:
            text (str): Interjection text
        Returns:
            str: Speech Markdown interjection (e.g. "(text)[interjection]")
        See Also:
            https://www.speechmarkdown.org/syntax/interjection/
        """
        return f'({text})[interjection]'
    def ipa(self, text: str, phonetic: str, short: bool = False) -> str:
        """
        Args:
            text (str): Text
            phonetic (str): Phonetic
            short (bool): Short or standard format
        Returns:
            str: Speech Markdown IPA (e.g. "(pecan)[ipa:\"pɪˈkɑːn\"]")
        See Also:
            https://www.speechmarkdown.org/syntax/ipa/
        """
        if(short):
            return f'({text})[/{phonetic}/]'
        else:
            return f'({text})[ipa:\"{phonetic}\"]'
    def lang(self, text: str, lang: str) -> str:
        """
        Args:
            text (str): Text
            lang (str): Language
        Returns:
            str: Speech Markdown lang (e.g. "(text)[lang:\"en-US\"]")
        See Also:
            https://www.speechmarkdown.org/syntax/lang/
        """
        # TODO Verify language code for lang()
        return f'({text})[lang:\"{lang}\"]'
    def number(self, number: int) -> str:
        """
        Args:
            number (int): Number
        Returns:
            str: Speech Markdown number (e.g. "(123)[number]")
        See Also:
            https://www.speechmarkdown.org/syntax/number/
        """
        # NOTE number is the same as cardinal
        return f'({number})[number]'
    def ordinal(self, number: int) -> str:
        """
        Args:
            number (int): Ordinal number
        Returns:
            str: Speech Markdown ordinal (e.g. "(1)[ordinal]")
        See Also:
            https://www.speechmarkdown.org/syntax/ordinal/
        """
        return f'({number})[ordinal]'
    def phone(self, text: str, country_code: str = "1") -> str:
        """
        Args:
            text (str): Text
            country_code (str): Country code
        Returns:
            str: Speech Markdown phone (e.g. "(555-555-5555)[phone]" or "(555-555-5555)[phone:\"1\"]")
        See Also:
            https://www.speechmarkdown.org/syntax/phone/
        """
        # TODO Verify phone number for phone()
        return f'({text})[phone:\"{number}\"]'
    def pitch(self, text: str, level: str = "medium") -> str:
        """
        Args:
            text (str): Pitch text
            level (str): Pitch level (must be one of: x-high, high, medium, low, x-low)
        Returns:
            str: Speech Markdown pitch (e.g. "(text)[pitch:\"x-high\"]")
        Raises:
            ValueError: Invalid pitch level (must be one of: x-high, high, medium, low, x-low)
        See Also:
            https://www.speechmarkdown.org/syntax/pitch/
        """
        if(level not in self._pitch_levels):
            raise ValueError(f'Invalid pitch level: {level} (must be one of: {", ".join(self._pitch_levels)})')
        return f'({text})[pitch:\"{level}\"]'
    def rate(self, text: str, speed: str = "medium") -> str:
        """
        Args:
            text (str): Rate text
            speed (str): Rate speed (must be one of: x-slow, slow, medium, fast, x-fast)
        Returns:
            str: Speech Markdown rate (e.g. "(text)[rate:\"x-slow\"]")
        Raises:
            ValueError: Invalid rate speed (must be one of: x-slow, slow, medium, fast, x-fast)
        See Also:
            https://www.speechmarkdown.org/syntax/rate/
        """
        if(speed not in self._rate_levels):
            raise ValueError(f'Invalid rate speed: {speed} (must be one of: {", ".join(self._rate_levels)})')
        return f'({text})[rate:\"{speed}\"]'
    def sub(self, abbreviation: str, text: str, short: bool = False) -> str:
        """
        Args:
            abbreviation (str): Abbreviation
            text (str): Text
        Returns:
            str: Speech Markdown sub (e.g. "(abbreviation)[sub:\"text\"]" or "(abbreviation)[\"text\"]" if short=True)
        See Also:
            https://www.speechmarkdown.org/syntax/sub/
        """
        if(short):
            return f'({abbreviation})[\"{text}\"]'
        else:
            return f'({text})[sub:\"{abbreviation}\"]'
    def time(self, time: str, format: str = "hms24") -> str:
        """
        Args:
            time (str): Time
            format (str): Time format (must be one of: hms12, hms24)
        Returns:
            str: Speech Markdown time (e.g. "(1:30pm)[time:\"hms12\"]" or "(13:00)[time:\"hms24\"]")
        Raises:
            ValueError: Invalid time format (must be one of: hms12, hms24)
        See Also:
            https://www.speechmarkdown.org/syntax/time/
        """
        # TODO Verify provided time for time()
        if(format not in self._time_formats):
            raise ValueError(f'Invalid time format: {format} (must be one of: {", ".join(self._time_formats)})')
        return f'({time})[time:\"{format}\"]'
    def unit(self, number: int, unit: str) -> str:
        """
        Args:
            number (int): Number
            unit (str): Unit (Not all unit types are supported yet, currently only supports: foot, ft)
        Returns:
            str: Speech Markdown unit (e.g. "(1 ft)[unit]" or "(1 foot)[unit]")
        Raises:
            ValueError: Invalid unit (must be one of: foot, ft)
        See Also:
            https://www.speechmarkdown.org/syntax/unit/
        """
        # TODO Add support for more unit types for unit()
        # TODO Convert metric units to SSML supported imperial units for unit()
        if(unit not in self._units):
            raise ValueError(f'Invalid unit: {unit} (must be one of: {", ".join(self._units)})'
        return f'({number} {unit})[unit]'
    def volume(self, text: str, level: str = "medium") -> str:
        """
        Args:
            text (str): Volume text
            level (str): Volume level (must be one of: silent, x-soft, soft, medium, loud, x-loud)
        Returns:
            str: Speech Markdown volume (e.g. "(text)[volume:\"silent\"]")
        Raises:
            ValueError: Invalid volume level (must be one of: silent, x-soft, soft, medium, loud, x-loud)
        See Also:
            https://www.speechmarkdown.org/syntax/volume/
        """
        if(level not in self._volume_levels):
            raise ValueError(f'Invalid volume level: {level} (must be one of: {", ".join(self._volume_levels)})')
        return f'({text})[volume:\"{level}\"]'
    def whisper(self, text: str) -> str:
        """
        Args:
            text (str): Whisper text
        Returns:
            str: Speech Markdown whisper (e.g. "(text)[whisper]")
        See Also:
            https://www.speechmarkdown.org/syntax/whisper/
        """
        return f'({text})[whisper]'