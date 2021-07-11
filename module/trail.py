from esapp.models import *
from django.conf import settings

import os
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)
from esapp.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def trail(event):
    try:

        container_obj = FlexSendMessage.new_from_json_dict(_list)
        #container_obj2 = FlexSendMessage.new_from_json_dict(search_msg)
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj])

    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


def trail_search(event, mtext):
    try:
        keyword = mtext[5:]
        # print("https://www.forest.gov.tw/trail?q="+keyword)

        container_obj = FlexSendMessage.new_from_json_dict(_list)
        item1_search = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "「"+keyword+"」"+"搜尋結果",
                        "color": "#ffffff",
                        "size": "xl",
                        "align": "center"
                    }
                ]
            },
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/8zuiuQO.png",
                "aspectRatio": "341:148",
                "size": "full",
                "action": {
                    "type": "uri",
                    "label": "林務局全球資訊網 ",
                    "uri": "https://www.forest.gov.tw/trail?q="+keyword,
                },
                "height": "110px",
                "width": "280px",
                "align": "center"
            },
            "styles": {
                "header": {
                    "backgroundColor": "#a8dadc"
                }
            }
        }

        _list_search = {
            "type": "flex",
            "altText": "為您搜尋在林務局全球資訊網",
            "contents": {
                "type": "carousel",
                "contents": [item1_search]
            }
        }
        container_obj_search = FlexSendMessage.new_from_json_dict(_list_search)
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj_search])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


text_str = """直接前往以上網站，
或是輸入[登山步道 關鍵字]，
如:登山步道 八仙"""
search_msg = {
    "type": "flex",
    "altText": "登山步道",
    "contents": {
        "type": "bubble",
        "size": "mega",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": text_str,
                    "color": "#ffffff",
                    "weight": "bold",
                    "align": "start",
                    "size": "lg",
                    "wrap": True,
                    "margin": "none"
                }
            ],
            "backgroundColor": "#a8dadc",
            "action": {
                "type": "message",
                "label": "action",
                "text": "登山步道 八仙"
            }
        }
    }
}

item1 = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/8zuiuQO.png",
                        "aspectRatio": "341:148",
                        "size": "full"
                    }
                ],
                "action": {
                    "type": "uri",
                    "label": "林務局全球資訊網 ",
                    "uri": "https://www.forest.gov.tw"
                },
                "height": "110px",
                "width": "280px",
                "align": "center"
            }
        ],
        "borderWidth": "5px",
        "borderColor": "#ffffff",
        "cornerRadius": "10px",
        "paddingAll": "5px",
        "align": "center",
        "size": "xl"
    }
}
item2 = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://recreation.forest.gov.tw/images/layout/logo.png",
                        "aspectRatio": "341:148",
                        "size": "full"
                    }
                ],
                "action": {
                    "type": "uri",
                    "label": "台灣山林悠遊網",
                    "uri": "https://recreation.forest.gov.tw/"
                },
                "height": "110px",
                "width": "280px",
                "align": "center"
            }
        ],
        "borderWidth": "5px",
        "borderColor": "#000000",
        "cornerRadius": "10px",
        "paddingAll": "5px",
        "align": "center",
        "size": "xl"
    },
    "styles": {
        "body": {
            "backgroundColor": "#000000"
        }
    }
}
item3 = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/kjPUlOD.png",
                        "aspectRatio": "341:148",
                        "size": "full"
                    }
                ],
                "action": {
                    "type": "uri",
                    "label": "健行筆記",
                    "uri": "https://hiking.biji.co/"
                },
                "height": "110px",
                "width": "280px",
                "align": "center"
            }
        ],
        "borderWidth": "5px",
        "borderColor": "#ffffff",
        "cornerRadius": "10px",
        "paddingAll": "5px",
        "align": "center",
        "size": "xl"
    }
}
item4 = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/rTNiG9y.jpg",
                        "aspectRatio": "341:148",
                        "size": "full"
                    }
                ],
                "action": {
                    "type": "uri",
                    "label": "脊梁山脈旅遊年",
                    "uri": "https://i30.taiwan.net.tw/"
                },
                "height": "110px",
                "width": "280px",
                "align": "center"
            }
        ],
        "borderWidth": "5px",
        "borderColor": "#ffffff",
        "cornerRadius": "10px",
        "paddingAll": "5px",
        "align": "center",
        "size": "xl"
    }
}

_list = {
    "type": "flex",
    "altText": "登山步道資訊網站:林務局全球資訊網 / 台灣山林悠遊網 / 健行筆記 / 脊梁山脈旅遊年",
    "contents": {
        "type": "carousel",
        "contents": [item1, item2, item3, item4]
    }
}
