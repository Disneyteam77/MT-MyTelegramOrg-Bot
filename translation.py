class Translation(object):
    START_TEXT = """Hi!
<b>Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org</b>
\n<b>🖥️How To Use This Bot🖥️\nhttps://youtu.be/5eEsvLAKVc0</b>\n\n👤Any Doubt @Mo_Tech_Group\n🤖Bot Update @Mo_Tech_YT</b>
\n<b>please read the TnC before proceeding: https://t.me/Mo_Tech_YT/38</b>
\n<b>/start at any stage to re-enter your details<b>"""
    AFTER_RECVD_CODE_TEXT = """<b>I see!
now please send the Telegram code that you received from Telegram!
this code is only used for the purpose of getting the APP ID from my.telegram.org
\nif you do not trust this bot dev, please host this bot yourself
by opening https://github.com/MRK-Y/MT-MyTelegramOrg-Bot and clicking on the Pink Button</b>
\n<b>/start at any stage to re-enter your details</b>"""
    BEFORE_SUCC_LOGIN = "😔Wait....!Plz😁"
    ERRED_PAGE = "<b>something wrongings. failed to get app id. \n\nSupport Group @Mo_Tech_YT</b>"
    CANCELLED_MESG = "<b>😴Bye! Please re /start the bot conversation</b>"
    IN_VALID_CODE_PVDED = "<b>😔sorry, but the input does not seem to be a valid Telegram Web-Login code</b>"
    IN_VALID_PHNO_PVDED = "<b>😔sorry, but the input does not seem to be a valid phone number</b>"
