class Translation(object):
    START_TEXT = """Hi!
<b>Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org</b>\n
\n<b>please read the TnC before proceeding: https://t.me/Mo_Tech_YT/38\n
\n<b>Thank you for using me 😬</b>\n\n🖥️How To Use This Bot🖥️👉https://youtu.be/5eEsvLAKVc0\n\n👤Any Doubt @Mo_Tech_Group\n🤖Bot Update @Mo_Tech_YT</b>\n
/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """<b>I see!
now please send the Telegram code that you received from Telegram!
this code is only used for the purpose of getting the APP ID from my.telegram.org
if you do not trust this bot dev, please host this bot yourself
by opening https://github.com/MRK-Y/MT-MyTelegramOrg-Bot and clicking on the Pink Button</b
/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "<b>something wrongings. failed to get app id. \n\nSupport Group @Mo_Tech_YT</b>"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
