import requests
from reds_simple_logger import Logger
logger = Logger()

cara_base_url = "https://cara.twinklerealm.net"

class CaraAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    class ChatFilterResponse:
        def __init__(self, response):
            chatfilter_response_int = response["item1"]
            if chatfilter_response_int != 0:
                if chatfilter_response_int == 1:
                    chatfilter_response_reason: str = "1: Bad Word"
                elif chatfilter_response_int == 2 or chatfilter_response_int == 3:
                    chatfilter_response_reason: str = "2: Hidden Badword"
                elif chatfilter_response_int == 4:
                    chatfilter_response_reason: str = "4: NSFW Content"
                elif chatfilter_response_int == 5:
                    chatfilter_response_reason: str = "5: Registered Spam Message"
                elif chatfilter_response_int == 6:
                    chatfilter_response_reason: str = "6: User was flagged for suspicious activity"
                elif chatfilter_response_int == 7:
                    chatfilter_response_reason: str = "7: Bot activity"
                #elif chatfilter_response_int == 8:
                #    chatfilter_response_reason: str = "8: Registered spammer"
                elif chatfilter_response_int == 9:
                    chatfilter_response_reason: str = "9: Forbidden Letter"

            self.result: int = response["item1"]
            self.reason: str = chatfilter_response_reason
            self.messageID: int = response["item2"]["messageID"]
            self.analysisSteps: str = response["item2"]["analysisSteps"]
            self.markedAsSpam: bool = response["item2"]["markedAsSpam"]
            self.levenshteinPair: str = response["item2"]["levenshteinPair"]
            self.json: str = response

    def chatfilter(self, message: str, levenshtein: int, FilteredWords, GuildID:int, ChannelID: int, AuthorID: int,
                   MessageID: int, GuildName: str, ChannelName: str, AuthorName: str, GoodWords = None, OnlyASCII:bool = None):
        logger.working("Sending request to API endpoint...")
        if OnlyASCII == True:
            OnlyASCII = "True"
        else:
            OnlyASCII = "False"
        logger.waiting("Waiting for response from endpoint...")
        response = requests.get(
                f'{cara_base_url}/api/ChatfilterAPI/msg',
                params={
                    "key": str(self.api_key),
                    "content": str(message).encode("utf-8"),
                    "levenshtein": str(levenshtein),
                    "FilteredWords": ";".join(FilteredWords),
                    "GoodWords": ";".join(GoodWords),
                    "GuildID": str(GuildID),
                    "ChannelID": str(ChannelID),
                    "AuthorID": str(AuthorID),
                    "MessageID": str(MessageID),
                    "GuildName": str(GuildName).encode("utf-8"),
                    "ChannelName": str(ChannelName).encode("utf-8"),
                    "AuthorName": str(AuthorName).encode("utf-8"),
                    "OnlyASCII": str(OnlyASCII)
                }
            )
        response_json = response.json()
        return self.ChatFilterResponse(response_json)
    
