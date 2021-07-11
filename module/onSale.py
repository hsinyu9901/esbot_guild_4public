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


def onSale(event):
    try:
        _list = {
            "type": "template",
            "altText": "特賣商品",
            "template": {
                "type": "image_carousel",
                "columns": [
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "立即下訂>>",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/nYHNpV0.jpg",
                        "action": {
                            "type": "message",
                            "label": "更多詳情 >>",
                            "text": "yes"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/zUA9itR.jpg",
                        "action": {
                            "type": "uri",
                            "label": "View detail",
                            "uri": "http://example.com/page/222"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                    {
                        "imageUrl": "https://i.imgur.com/U3r1tiV.jpg",
                        "action": {
                            "type": "postback",
                            "label": "Buy",
                            "data": "action=buy&itemid=111"
                        }
                    },
                ]
            }
        }
        container_obj = TemplateSendMessage.new_from_json_dict(_list)
        line_bot_api.reply_message(event.reply_token, container_obj)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='發生錯誤！'))


""" 
image_carousel_template_message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackAction(
                    label='postback1',
                    display_text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackAction(
                    label='postback2',
                    display_text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
) """
