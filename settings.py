class BaseSettings:
    # Заполнять ниже `BotSettings`

    USERS = ()
    PROXIES = ()
    CONF_CODE = ""
    SCOPE = 140489887
    APP_ID = 5982451
    CAPTCHA_KEY = "58d2050e8830e31f079c61c39bc5a1e2"
    CAPTCHA_SERVER = "rucaptcha"
    READ_OUT = False
    PLUGINS = ()

    DEBUG = False


# Importing all the plugins to allow including to PLUGINS
from plugins import *

# Edit this settings
class BotSettings(BaseSettings):
    USERS = (
	    ("user", "d18abc930f146b329cceed588f5588834ae73447e53076552845ce4c3622c63d331cc8e76dfe4cca7fafd",),
		("user", "b30872d5bd365fcb1626d3991a60508fb67a936a6977a0fdd41516716bbcbcad11e47d6fc54f6978e5ea4",)
    )

    PROXIES = (
        # ("ADDRESS", "LOGIN", "PASSWORD", "ENCODING),
    )

    # Code for Callback Api (if you use it)

    CONF_CODE = ""

    # VK information

    SCOPE = 140489887
    APP_ID = 5982451

    # Captcha solver's data

    CAPTCHA_KEY = ""
    CAPTCHA_SERVER = "rucaptcha"

    # Other

    READ_OUT = False

    # Plugins

    # Plugin's main class names must by unique!

    # You can import needed plugins in any way possible by Python
    # Exmaple: `from plugins.about import AboutPlugin`
    #
    # You can import any plugins inside `plugins` using special bot-specific package:
    # from plugin import AboutPlugin
    #
    # You can import all plugins at once using `from plugins import *` at module-level.

    prefixes = ("!", "бот ", "бот, ", "бот,", "jojo", "джоджо")
    admins = (291434783, 393951972, 404703521)

    hp = HelpPlugin("помощь", "команды", "?", short=False, prefixes=prefixes)

    PLUGINS = (
        # Leave only "PostgreSQL" or "MySQL", host is adress of your database, port is a number
        PeeweePlugin("ec2-54-163-246-193.compute-1.amazonaws.com", "ddaa2pvhv78uj0", "tgvapmlrtgeiyf", "ac4cf97cf7e0b621abfc17b197d5a85931e9fe3c120f56c479b6b3327a3b791d", 5432, "PostgreSQL"),
        # PeeweePlugin("host", "database's name", "user", "password", port, "PostgreSQL" or "MySQL"),
        AdminPlugin(prefixes=prefixes, admins=admins, setadmins=True),
        ChatMetaPlugin(),

        # Requires `PeeweePlugin`:
        # DuelerPlugin(prefixes=prefixes),
        # AzinoPlugin("азино", prefixes=prefixes),
        # RussianRoulettePlugin(prefixes=prefixes),
        # LockChatPlugin("сохранять", prefixes=prefixes),

        # Can use `PeeweePlugin`:
        RememberPlugin("напомни",prefixes=prefixes),   # use_db=True, if you can use PeeweePlugin

        # Plugins:
        LockChatPlugin("сохранять", prefixes=prefixes),
        AzinoPlugin("азино", prefixes=prefixes),
        RussianRoulettePlugin(prefixes=prefixes),
        LockChatPlugin("сохранять", prefixes=prefixes),
        DuelerPlugin(prefixes=prefixes),
        WeatherPlugin("погода", token="token for api", prefixes=prefixes),
        VoterPlugin(prefixes=prefixes),
        FacePlugin("сделай", prefixes=prefixes),
        SmileWritePlugin("смайлами", prefixes=prefixes),
        JokePlugin("а", "анекдот", prefixes=prefixes),
        GraffitiPlugin("граффити", prefixes=prefixes),
        QuotePlugin("цитатка"),
        WikiPlugin("что такое", prefixes=prefixes),
        AnagramsPlugin(["анаграмма", "анаграммы"], prefixes=prefixes),
        HangmanPlugin(["виселица"], prefixes=prefixes),
        MembersPlugin("кто тут", prefixes=prefixes),
        PairPlugin("кто кого", prefixes=prefixes),
        WhoIsPlugin("кто", prefixes=prefixes),
        AboutPlugin("о боте", "инфа", prefixes=prefixes),
        BirthdayPlugin("дни рождения", "др", prefixes=prefixes),
        ToptextbottomtextPlugin("мем", "свой текст", prefixes=prefixes),
        ChatKickerPlugin(["кик"], ["фри", "анкик"], prefixes=prefixes, admins=admins, admins_only=True),
        RandomPostPlugin({"random": "-111759315", "memes": "-77127883", "мемы": "-77127883"}, prefixes=prefixes),
        CalculatorPlugin("посчитай", "посч", prefixes=prefixes),
        Audio2TextPlugin(key="1c89f760-adb8-49a0-a06e-6ac5c560cfa2", prefixes=prefixes),
        DispatchPlugin("рассылка", prefixes=prefixes, admins=admins),
        hp,

        # Needs tokens (see plugin's codes, some have defaults):
        SayerPlugin(prefixes=prefixes),
        # WeatherPlugin("погода", token="token for api", prefixes=prefixes),
        # EmotionsDetectorPlugin("лицо", key="token for api", prefixes=prefixes),
        DialogflowPlugin(prefixes=prefixes),  # plugin for DialogflowPlugin (chatting, learning etc)

        # Plugins for bot's control
        AntifloodPlugin(),
        ResendCommanderPlugin(),
        ResendCheckerPlugin(),
    )

    hp.add_plugins(PLUGINS)
