from esapp.models import *
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

import os
import json
import random

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


@csrf_exempt
def look4store(event):
    items = []
    producers = Producer.objects.exclude(producer_name=None).all()
    random_producers = random.sample(list(producers), len(producers))
    random_producers = random.sample(list(producers), 5)
    for producer in random_producers:
        if producer.producer_name is not None:
            item = {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://escooter-esbot-bucket.s3.amazonaws.com/"+str(producer.charge.profile_pic),
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "uri": "https://escooter-esbot.herokuapp.com/user-producer/?producer_name="+producer.producer_name,
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": producer.producer_name,
                            "weight": "bold",
                            "size": "xl",
                            "color": "#405958"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "margin": "lg",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "md",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/NciGxlS.png",
                                            "offsetTop": "3px"
                                        },
                                        {
                                            "type": "text",
                                            "text": producer.producer_time,
                                            "wrap": True,
                                            "color": "#405958",
                                            "size": "md",
                                            "flex": 5
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "md",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://i.imgur.com/cWLuQ6T.png"
                                        },
                                        {
                                            "type": "text",
                                            "text": producer.producer_ctiy +
                                            producer.producer_address,
                                            "wrap": True,
                                            "color": "#405958",
                                            "size": "md",
                                            "flex": 5,
                                            "action": {
                                                "type": "uri",
                                                "label": producer.producer_ctiy +
                                                producer.producer_address,
                                                "uri": "https://www.google.com.tw/maps/place/"+producer.producer_ctiy +
                                                producer.producer_address,
                                            }
                                        }
                                    ]
                                }

                            ]
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "color": "#89b0ae",
                            "action": {
                                "type": "uri",
                                "label": "撥打 "+producer.producer_phone,
                                "uri": "tel:"+producer.producer_phone
                            }
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "color": "#89b0ae",
                            "action": {
                                "type": "uri",
                                "label": "詳細資料",
                                "uri": "https://escooter-esbot.herokuapp.com/user-producer/?producer_name="+producer.producer_name,
                            }
                        },
                        {
                            "type": "spacer",
                            "size": "sm"
                        }
                    ],
                    "flex": 0,
                    "backgroundColor": "#dbf0f0"
                },
                "styles": {
                    "body": {
                        "backgroundColor": "#dbf0f0"
                    },
                    "footer": {
                        "backgroundColor": "#dbf0f0"
                    }
                }
            }
            items.append(item)

    item_end = {
        "type": "bubble",
        "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "color": "#405958",
                        "action": {
                            "type": "uri",
                            "label": "查看最近的優質店家 >>",
                            "uri": "https://escooter-esbot.herokuapp.com/user-producer"
                        },
                        "style": "link"
                    }
                ],
            "offsetTop": "150px",
            "spacing": "xxl"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                    {
                        "type": "spacer",
                        "size": "sm"
                    }
            ],
            "flex": 0
        }
    }
    items.append(item_end)

    change_text = """尋找店家
系統忙碌時，稍待幾分鐘再試"""
    change_msg = {
        "type": "flex",
        "altText": "尋找店家",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "更多店家資訊",
                        "color": "#ffffff",
                        "weight": "bold",
                        "align": "center",
                        "gravity": "center",
                        "size": "lg"
                    },
                    {
                        "type": "image",
                        "url": "https://i.imgur.com/925168D.png",
                        "size": "xxs",
                        "position": "absolute",
                        "offsetTop": "8px",
                        "offsetEnd": "20px"
                    }
                ],
                "backgroundColor": "#a8dadc",
                "action": {
                    "type": "message",
                    "label": "action",
                    "text": change_text
                }
            }
        }
    }

    _list = {
        "type": "flex",
        "altText": "尋找店家",
        "contents": {
            "type": "carousel",
            "contents": items[0:6]
        }
    }
    try:
        container_obj = FlexSendMessage.new_from_json_dict(_list)
        container_obj2 = FlexSendMessage.new_from_json_dict(change_msg)

        # line_bot_api.push_message
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj, container_obj2])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢"))
