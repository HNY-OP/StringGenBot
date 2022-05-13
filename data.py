from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛꜱ", url="https://t.me/hnyrobo/9")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ꜰᴏʀ ᴍᴏʀᴇ ʙᴏᴛꜱ", url="https://t.me/hnyrobo")],
    ]

    START = """
ʜᴇʏ {}
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {}

ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜꜱᴛ ᴛʜɪꜱ ʙᴏᴛ, 
1) ꜱᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
2) ᴅᴇʟᴇᴛᴇ ᴛʜɪꜱ ᴄʜᴀᴛ

ꜱᴛɪʟʟ ʀᴇᴀᴅɪɴɢ?
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ (ᴇᴠᴇɴ ᴠᴇʀꜱɪᴏɴ 2) ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ. ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ !

ʙʏ @HNYROBO

    """

    HELP = """
**ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ**

/ᴀʙᴏᴜᴛ - ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ
/ʜᴇʟᴘ - ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ
/ꜱᴛᴀʀᴛ - ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/ɢᴇɴᴇʀᴀᴛᴇ - ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ
/ᴄᴀɴᴄᴇʟ - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ
/ʀᴇꜱᴛᴀʀᴛ - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴘʀᴏᴄᴇꜱꜱ

"""

    ABOUT = """**ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ** 

ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ʙʏ @HNYROBO

ꜰʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](ʜᴛᴛᴘꜱ://ᴅᴏᴄꜱ.ᴘʏʀᴏɢʀᴀᴍ.ᴏʀɢ)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](ʜᴛᴛᴘꜱ://ᴡᴡᴡ.ᴘʏᴛʜᴏɴ.ᴏʀɢ)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : @HNYOP
    """
