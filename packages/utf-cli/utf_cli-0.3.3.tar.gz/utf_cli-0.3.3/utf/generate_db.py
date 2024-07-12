# Inspired by https://github.com/sethmlarson/utf8.xyz/blob/main/build-db.py
from dataclasses import dataclass
import importlib.resources
import json
import sqlite3
import csv

import platformdirs


db_path = platformdirs.user_cache_path("utf", "treyhunner") / "utf8.db"


@dataclass(slots=True, frozen=True)
class Character:
    glyph: str
    name: str
    category: str

    @classmethod
    def from_csv_row(cls, row):
        ordinal, name, group = row[:3]
        ordinal = int(ordinal, 16)
        name = name.lower()
        if group == "Sc":
            category = "currency"
        elif "arrow" in name:
            category = "arrows"
        else:
            category = None
        return cls(chr(ordinal), name, category)

    @property
    def is_control(self):
        """Return True for control characters."""
        return "<" in self.name


def get_character_data():
    # File from https://www.unicode.org/Public/draft/UCD/ucd/UnicodeData.txt
    path = importlib.resources.files("utf") / "UnicodeData.txt"
    with path.open() as file:
        characters = [
            Character.from_csv_row(row)
            for row in csv.reader(file, delimiter=";")
        ]
        return {
            character.glyph: character
            for character in characters
        }


def get_keywords_data():
    # File from https://github.com/muan/emojilib/blob/main/dist/emoji-en-US.json
    path = importlib.resources.files("utf") / "emoji-en-US.json"
    keyword_data = json.loads(path.read_text())
    return [
        (keyword.replace("_", " "), glyph)
        for glyph, keywords in keyword_data.items()
        for keyword in keywords
    ]


def make_database():
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(db_path)
    db.execute(
        """
        CREATE TABLE symbols (
            glyph TEXT PRIMARY KEY,
            name TEXT,
            category TEXT DEFAULT '',
            priority INTEGER
        );
        """
    )
    db.execute(
        """
        CREATE TABLE copied (
            glyph TEXT PRIMARY KEY,
            copies INTEGER,
            last_copied DATETIME
        );
        """
    )
    db.execute(
        """
        CREATE TABLE keywords (
            keyword TEXT,
            glyph TEXT
        );
        """
    )
    db.execute("CREATE INDEX keyword_index ON keywords (keyword COLLATE NOCASE);")
    characters = get_character_data()
    keywords = get_keywords_data()
    for name, glyph in keywords:
        characters.setdefault(glyph, Character(glyph, name, "emoji"))
    # Turn keywords into a set to deduplicate
    keywords = set(keywords) | {
        (character.name, character.glyph)
        for character in characters.values()
        if not character.is_control
    }
    common = common_characters()
    populate_chars_table(db, characters.values(), common)
    populate_keywords_table(db, keywords)
    populate_copied_table(db)
    db.commit()
    db.close()


def populate_chars_table(db, characters, common):
    for char in characters:
        if char.is_control:
            continue
        db.execute(
            """
            INSERT INTO symbols (
                name, glyph, category, priority
            ) VALUES (
                ?, ?, ?, ?
            )
            """,
            (
                char.name,
                char.glyph,
                char.category,
                common.get(char.glyph, 0),
            )
        )


def populate_keywords_table(db, keywords):
    for keyword, glyph in keywords:
        db.execute(
            """
            INSERT INTO keywords (
                keyword, glyph
            ) VALUES (
                ?, ?
            )
            """,
            (keyword, glyph)
        )


def populate_copied_table(db):
    fake_copies = [
        "\N{face with tears of joy}",
        "\N{bullet}",
        "\N{sparkles}",
        "\N{em dash}",
        "\N{thumbs up sign}",
        "\N{horizontal ellipsis}",
        "\N{purple heart}",
        "\N{interrobang}",
        "\N{smiling face with smiling eyes}",
        "\N{zero width space}",
        "\N{party popper}",
        "\N{superscript two}",
        "\N{grinning face}",
        "\N{vulgar fraction one half}",
        "\N{unicorn face}",
        "\N{rightwards arrow}",
        "\N{snake}",
        "\N{left double quotation mark}",
        "\N{cookie}",
        "\N{right double quotation mark}",
        "\N{electric light bulb}",
        "\N{right single quotation mark}",
        "\N{sparkling heart}",
        "\N{place of interest sign}",
        "\N{person raising both hands in celebration}",
        "\N{not equal to}",
        "\N{rainbow}",
        "\N{inverted question mark}",
        "\N{shocked face with exploding head}",
        "\N{degree sign}",
        "\N{mushroom}",
        "\N{no-break space}",
        "\N{sunflower}",
        "\N{Grimacing Face}",
        "\N{Shrug}",
    ]
    for n, glyph in enumerate(fake_copies, start=1):
        db.execute(
            """
            INSERT INTO copied (
                glyph, copies, last_copied
            ) VALUES (
                ?, ?, datetime('now', '-{n} hour')
            )
            """,
            (glyph, 0)
        )



def common_characters():
    common_emoji = "😂🤣👍😭🙏😘🥰😍😊🎉😁💕🥺😅🔥🤦🤷🙄😆🤗😉🎂🤔👏🙂😳🥳😎👌💜😔💪✨💖👀😋😏😢👉💗😩💯🌹💞🎈💙😃😡💐😜🙈🤞😄🤤🙌🤪😀💋💀👇💔😌💓🤩🙃😬😱😴🤭😐🌞😒😇🌸😈🎶🎊🥵😞💚🖤💰😚👑🎁💥🙋😑🥴👈💩✅👋🤮😤🤢🌟❗😥🌈💛😝 😫😲🖕🔴🌻🤯💃👊🤬🏃😕⚡☕🍀💦⭐🦋🤨🌺😹🤘🌷💝💤🤝🐰😓💘🍻😟😣🧐😠🤠😻🌙😛🤙🙊🧡🤡🤫🌼🥂😷🤓🥶😶😖🎵🚶😙🍆🤑💅😗🐶🍓✋👅👄🌿🚨📣🤟🍑🍃😮💎📢🌱🙁🍷😪🌚🏆🍒💉❌💢🛒😸🐾👎🚀🎯🍺📌📷🙇💨🍕🏠📸🐇🚩😰👶🌊🐕💫😵🎤🏡🥀🤧🍾🍰🍁🤲👆😯✊💌💸🧁⚽❓🕺😺💧💣🤐🍎🐷🐥💁📍🎀🙅🥇🌝🔫🐱🐣🎧💟👹💍🍼💡😽🍊😨🍫🧢🤕🚫🎼🐻📲👻👿🧚🌮🍭🐟🐸🐝🐈🔵🔪😧🌄😾🤸📱🍇🌴🐢🌃👽🍌📺👐⏰🔔🌅🦄⭕🎥🍋🥚💲📚🐔🎸🥃😿🚗🌎🔊🦅🚿🦆🍉🍬🧸🍨📝🤚📩💵👼💭🌍⚫👧🤜🍿🧿🏀🍏🌳🙉😦⚾🤰🍹🍦🛑🧘🍔🍂🐒🍪🙀🍗🌠🎬🌵🍄🐐🍩🦁🙆📞👸🍅🐍👦💬🥤😼🌾🧀🎮🧠☔🌏🛌🔝🌉🤛🤒👗⚪🌲🍜🐦🍯👮🏅🐼💄👺🔞🎆🎨🍞🎇🦜🐑🐙🦍🔗📖🔹🥓🥒🍸🥧💻🐖📈💊👩🌀💆🥩🎄🌽🤥🐎🆘💏🥕🔮🦀🐠🌛👠🐓🥊🛐🚬🔰🌜🍴🥔🎓👙🗿🥑👯🍍⛽🏁👂🦊👃🦖🐴🎃🦠🌕📦🌌⛳🍧🍟🎹🥞👣🥜🍡🦷🚴🍝🎻🐊🍖🐺🐽🚮🍵🌭🐄🥁🍳👫⌚🔆🐳🌯🦴🥪🦃🎣🔻🐀🐬🍚🤖🐧🦈🏄🏈🧬🌐🔍📴🥦🐯📮🥛🥭🖖🐛🦞🐤🧟🍤🦐🎭🐞🐵🍣🥗🆔🔑👴🤴👵🤳🧨⬛👤🎩🔙🥫🆕🥐👰💳🐚🌆⚓🆗🤱👭🦇👨🦗🦕🏹🐮🚲💑🚒🦎🦉🐂🍈🚭🐘🚙🔨⏩📄🥎🔒🎱🦵🏊🛵🔎👟🆒🔱🦌🥈🚚♈🐜🎲💠🥝🦶👾💮🦑🔺🐁🐌🔷👖💒🐉🎍👕🚽🍥🍐🏫🚂🔐⛄⏳⛅🔜🥣🎋🔶🔸⛔🦸📻👓🥉🐅📊🦝🚪🚘👱🧜🏥⛵🕋📰💇🥬🐨🧹👥⬜📆🥖🐩🤺🛁⌛🔽🍲🦘🥥🛀📅📿🕛🌑🚛🧺📡🐭🗽🆓🎾🏐🎒🆚🌋📉🏒🕐🦙🧙🦟🃏🚢🙍📕👬🐆🔛❕👒🐪🥟🧼🍶🎪👔📎🦚🍠🥨🍮🏩🐃🔅🏰📬➕📛🐏🎺🕌🐋🥋🐲❎🎫📨⛪🦒🎡🧱🎷🚑🚓🚃🏇🌇🙎🚌💶🚜🌰🍛💴👛🧓🥾🐫🥢🧤🚔🎰🧔🥯➖🐹🦂🔘🔄📥📹🛫📏🎠🆙💈🔖🍱🕜🍢🏢🔌🦔🛸🤵👞🔋◾👜🚧♋🏮🐡👘🛹♉🚦🧩🚺🥄🧛🗻♐🦹🏨🏉🦛💼🛴📘🧦🥘🤹♊🚁🔓🏴💿🦓📜👷🚣🧖👳🎎🚹⛺🎅🧂🚐🏏📀🎐🦢🌔🗼🌒🧞🕒🎳🎢🔟⏬🧵🚵🧒♌🧪🚕🧽⛲🏦👚📋♒🌘🐗📠🤼♏🧳🧶📧🏂👢🥅🍙♎🔯🤾♍📯🌓🧻🔁🎽🧣🧗🎴♓📗👪❔🔚📙🧕🏓🧲💹💷◽📃🏧🥙➰🌖🌗🌂🔉🎌📤🀄🔭🚰🧑📒🧧🦏♿🎿🍘🏯🔲🕑🥡💺🔈♑🧴🥮🔧🛬🎑🚤📐📓🎏⏪🏪🧝🚆💂🧥🛶🔕📼🔇🏸💽🦡🌁📔🚄📶🚼🔦🚅🉑🧾🧭🕓🚖🥽📑🕙🤽🔬🚸🎦🗾🔼🕘👡📁🚍🥠🚥🏬🥍🈵🕝🔢🧫🆖🧮🥼➿🤶🕕🏑🔃📵🈶🥏📳🆑📫🕖🚋🔩🕗📂🚇🥌🧰🕚🚏🧯🔏🧷🚷🚎🚉🆎👲🕔💾➗🏺🕎💱🚳🚻📟🉐🈹🥿🕥⏫🔳🕞🔂🚠🏣👝🚊🏭⛎🚈🔀🚾🚝🕍🈴🚟🈯🚯🔤🛂📪🚡🏤🚞🈺📭🕡🛄🕦🚱🕣🈚🈲🔠🛷📇🕤🕧🈸🈳🕢🕠🕟🛃🛅🔡🔣🦰🈁🦱🦲🦳"
    common_characters = "•\N{zero width space}␡¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿŁłŃńŅņŇňŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŴŵŶŷŸŹźŻżŽžſƆƎƜɐɑɒɔɘəɛɜɞɟɡɢɣɤɥɨɪɬɮɯɰɴɵɶɷɸɹʁʇʌʍʎʞΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψωАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяᴀᴁᴂᴃᴄᴅᴆᴇᴈᴉᴊᴋᴌᴍᴎᴏᴐᴑᴒᴓᴔᴕᴖᴗᴘᴙᴚᴛᴜᴝᴞᴟᴠᴡᴢᴣᴤᴥᴦᴧᴨᴩᴪẞỲỳỴỵỸỹ‐‑‒–—―‖‗‘’‚‛“”„‟†‡‣․‥…‧‰‱′″‴‵‶‷‸‹›※‼‽‾‿⁀⁁⁂⁃⁄⁅⁆⁇⁈⁉⁊⁋⁌⁍⁎⁏⁐⁑⁒⁓⁔⁕⁗⁰ⁱ⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹℀℁ℂ℃℄℅℆ℇ℈℉ℊℋℌℍℎℏℐℑℒℓ℔ℕ№℗℘ℙℚℛℜℝ℞℟℠℡™℣ℤ℥Ω℧ℨ℩KÅℬℭ℮ℯℰℱℲℳℴℵℶℷℸ⅁⅂⅃⅄ⅅⅆⅇⅈⅉ⅋ⅎ⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿↄ←↑→↓↔↕↖↗↘↙↚↛↜↝↞↟↠↡↢↣↤↥↦↧↨↩↪↫↬↭↮↯↰↱↲↳↴↵↶↷↸↹↺↻↼↽↾↿⇀⇁⇂⇃⇄⇅⇆⇇⇈⇉⇊⇋⇌⇍⇎⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇚⇛⇜⇝⇞⇟⇠⇡⇢⇣⇤⇥⇦⇧⇨⇩⇪⇫⇬⇭⇮⇯⇰⇱⇲⇳⇴⇵⇶⇷⇸⇹⇺⇻⇼⇽⇾⇿∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑−∓∔∕∖∗∘∙√∛∜∝∞∟∠∡∢∣∤∥∦∧∨∩∪∫∬∭∮∯∰∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⌀⌁⌂⌃⌄⌅⌆⌇⌈⌉⌊⌋⌐⌑⌒⌓⌔⌕⌖⌗⌘⌙⌠⌡⌢⌣⌤⌥⌦⌧⌨⌫⌬⎛⎜⎝⎞⎟⎠⎡⎢⎣⎤⎥⎦⎧⎨⎩⎪⎫⎬⎭⏎⏏⏚⏛⏱⏲␢␣─━│┃┄┅┆┇┈┉┊┋┌┍┎┏┐┑┒┓└┕┖┗┘┙┚┛├┝┞┟┠┡┢┣┤┥┦┧┨┩┪┫┬┭┮┯┰┱┲┳┴┵┶┷┸┹┺┻┼┽┾┿╀╁╂╃╄╅╆╇╈╉╊╋╌╍╎╏═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╭╮╯╰╱╲╳╴╵╶╷╸╹╺╻╼╽╾╿▀▁▂▃▄▅▆▇█▉▊▋▌▍▎▏▐░▒▓▔▕▖▗▘▙▚▛▜▝▞▟■□▢▣▤▥▦▧▨▩▪▫▬▭▮▯▰▱▲△▴▵▶▷▸▹►▻▼▽▾▿◀◁◂◃◄◅◆◇◈◉◊○◌◍◎●◐◑◒◓◔◕◖◗◘◙◚◛◜◝◞◟◠◡◢◣◤◥◦◧◨◩◪◫◬◭◮◯◰◱◲◳◴◵◶◷◸◹◺◻◼◿☀☁☂☃☄★☆☇☈☉☊☋☌☍☎☏☐☑☒☓☖☗☘☙☚☛☜☝☞☟☠☡☢☣☤☥☦☧☨☩☪☫☬☭☮☯☰☱☲☳☴☵☶☷☸☹☺☻☼☽☾☿♀♁♂♃♄♅♆♇♔♕♖♗♘♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♲♳♴♵♶♷♸♹♺♻♼♽♾⚀⚁⚂⚃⚄⚅⚐⚑⚒⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚞⚟⚠⚢⚣⚤⚥⚦⚧⚨⚩⚬⚭⚮⚯⚰⚱⚲⚳⚴⚵⚶⚷⚸⚹⚺⚻⚼⛀⛁⛂⛃⛢⛤⛥⛦⛧⛨⛩⛫⛬⛭⛮⛯⛰⛱⛴⛶⛷⛸⛹⛻⛼⛾⛿✁✂✃✄✆✇✈✉✌✍✎✏✐✑✒✓✔✕✖✗✘✙✚✛✜✝✞✟✠✡✢✣✤✥✦✧✩✪✫✬✭✮✯✰✱✲✳✴✵✶✷✸✹✺✻✼✽✾✿❀❁❂❃❄❅❆❇❈❉❊❋❍❏❐❑❒❖❘❙❚❛❜❝❞❟❠❡❢❣❤❥❦❧➔➘➙➚➛➜➝➞➟➠➡➢➣➤➥➦➧➨➩➪➫➬➭➮➯➱➲➳➴➵➶➷➸➹➺➻➼➽➾⟰⟱⟲⟳⟴⟵⟶⟷⟸⟹⟺⟻⟼⟽⟾⟿⤀⤁⤂⤃⤄⤅⤆⤇⤈⤉⤊⤋⤌⤍⤎⤏⤐⤑⤒⤓⤔⤕⤖⤗⤘⤙⤚⤛⤜⤝⤞⤟⤠⤡⤢⤣⤤⤥⤦⤧⤨⤩⤪⤫⤬⤭⤮⤯⤰⤱⤲⤳⤴⤵⤶⤷⤸⤹⤺⤻⤼⤽⤾⤿⥀⥁⥂⥃⥄⥅⥆⥇⥈⥉⥊⥋⥌⥍⥎⥏⥐⥑⬀⬁⬂⬃⬄⬅⬆⬇⬈⬉⬊⬋⬌⬍⬎⬏⬐⬑⬒⬓⬔⬕⬖⬗⬘⬙⬚ⱠⱡⱣⱥⱦⱭⱯⱰ⸢⸣⸤⸥⸮〃〄ﬀﬁﬂﬃﬄﬅﬆ﴾﴿﷼︐︑︒︓︔︕︖︗︘︙︰︱︲︳︴︵︶︷︸︹︺︻︼︽︾︿﹀﹁﹂﹃﹄﹅﹆﹉﹊﹋﹌﹍﹎﹏﹐﹑﹒﹔﹕﹖﹗﹘﹙﹚﹛﹜﹝﹞﹟﹠﹡﹢﹣﹤﹥﹦﹨ ﹩﹪﹫\ufeff！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～｟｠￠￡￢￣￤￥￦￼�"
    priorities = {}
    for i, character in enumerate(common_emoji):
        priorities[character] = 100-i//(len(common_emoji)/100)
    for i, character in enumerate(common_characters):
        priorities[character] = 100-i//(len(common_characters)/100)
    return priorities
