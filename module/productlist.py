from esapp.models import *
from django.conf import settings

import os
import json
import random
from random import shuffle

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
    ImageSendMessage, BubbleStyle, BlockStyle)
from esapp.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def productlist(event):
    items = []
    products = Product.objects.all()  # .distinct()
    # 隨機數量 # change 3 to how many random items you want
    # [<Product: 冰絲涼感袖套>, <Product: Fitbit Versa 2 健康運動智慧手錶>, <Product: 男挺版修身透氣高爾夫POLO衫 INESIS>]
    random_items = random.sample(list(products), len(products))
    random_items = random.sample(random_items, 25)
    # 隨機一個
    #random_object = Product.objects.order_by('?')[0]
    # 隨機一個 # if you want only a single random item
    #random_item = random.choice(products)
    cols = []

    for product in random_items:

        price = str(product.price)
        # print("https://escooter-esbot-bucket.s3.amazonaws.com/"+str(product.image))
        col = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "image",
                    "url": "https://escooter-esbot-bucket.s3.amazonaws.com/"+str(product.image),
                    "aspectRatio": "100:100",
                    "action": {
                        "type": "uri",
                        "label": "商品資訊",
                        "uri": "https://escooter-esbot.herokuapp.com/user-product-info/"+str(product.id),
                    },
                    "align": "start",
                    "gravity": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": product.name,
                            "color": "#111111",
                            "weight": "bold",
                            "size": "md",
                            "align": "start",
                            "gravity": "center",
                            "wrap": True,
                            "maxLines": 2
                        },
                        {
                            "type": "text",
                            "text": "$"+price,
                            "color": "#111111",
                            "weight": "bold",
                            "size": "md",
                            "align": "start",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": product.producer.producer_name,
                            "color": "#89b0ae",
                            "weight": "bold",
                            "size": "sm",
                            "align": "start",
                            "gravity": "center"
                        }
                    ],
                    "action": {
                        "type": "uri",
                        "label": "商品資訊",
                        "uri": "https://escooter-esbot.herokuapp.com/user-product-info/"+str(product.id),
                    },
                    "paddingAll": "5px"
                }
            ],
            "backgroundColor": "#dbf0f0",
            "cornerRadius": "5px",
            "borderWidth": "3px",
            "borderColor": "#ffffff"
        }
        cols.append(col)

    item1 = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": "#a8dadc",
            "contents": [
                {
                    "type": "text",
                    "text": "特賣商品",
                    "weight": "bold",
                    "size": "xl",
                    "gravity": "center",
                    "align": "center",
                    "color": "#FFFFFF"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": cols[0:5],
            "paddingAll": "5px"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "來去逛逛 >>",
                            "color": "#ffffff",
                            "size": "md",
                            "align": "center",
                            "flex": 1
                        }
                    ],
                    "margin": "xs"
                }
            ],
            "backgroundColor": "#a8dadc"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://escooter-esbot.herokuapp.com/user-products"
        },
        "styles": {
            "body": {
                "backgroundColor": "#FEFEFE"
            },
            "footer": {
                "separator": True
            }
        }
    }

    item2 = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": "#a8dadc",
            "contents": [
                {
                    "type": "text",
                    "text": "特賣商品",
                    "weight": "bold",
                    "size": "xl",
                    "gravity": "center",
                    "align": "center",
                    "color": "#FFFFFF"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": cols[5:10],
            "paddingAll": "5px"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "來去逛逛 >>",
                            "color": "#ffffff",
                            "size": "md",
                            "align": "center",
                            "flex": 1
                        }
                    ],
                    "margin": "xs"
                }
            ],
            "backgroundColor": "#a8dadc"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://escooter-esbot.herokuapp.com/user-products"
        },
        "styles": {
            "body": {
                "backgroundColor": "#FEFEFE"
            },
            "footer": {
                "separator": True
            }
        }
    }
    item3 = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": "#a8dadc",
            "contents": [
                {
                    "type": "text",
                    "text": "特賣商品",
                    "weight": "bold",
                    "size": "xl",
                    "gravity": "center",
                    "align": "center",
                    "color": "#FFFFFF"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": cols[10:15],
            "paddingAll": "5px"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "來去逛逛 >>",
                            "color": "#ffffff",
                            "size": "md",
                            "align": "center",
                            "flex": 1
                        }
                    ],
                    "margin": "xs"
                }
            ],
            "backgroundColor": "#a8dadc"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://escooter-esbot.herokuapp.com/user-products"
        },
        "styles": {
            "body": {
                "backgroundColor": "#FEFEFE"
            },
            "footer": {
                "separator": True
            }
        }
    }
    item4 = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": "#a8dadc",
            "contents": [
                {
                    "type": "text",
                    "text": "特賣商品",
                    "weight": "bold",
                    "size": "xl",
                    "gravity": "center",
                    "align": "center",
                    "color": "#FFFFFF"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": cols[15:20],
            "paddingAll": "5px"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "來去逛逛 >>",
                            "color": "#ffffff",
                            "size": "md",
                            "align": "center",
                            "flex": 1
                        }
                    ],
                    "margin": "xs"
                }
            ],
            "backgroundColor": "#a8dadc"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://escooter-esbot.herokuapp.com/user-products"
        },
        "styles": {
            "body": {
                "backgroundColor": "#FEFEFE"
            },
            "footer": {
                "separator": True
            }
        }
    }
    item5 = {
        "type": "bubble",
        "size": "mega",
        "header": {
            "type": "box",
            "layout": "horizontal",
            "backgroundColor": "#a8dadc",
            "contents": [
                {
                    "type": "text",
                    "text": "特賣商品",
                    "weight": "bold",
                    "size": "xl",
                    "gravity": "center",
                    "align": "center",
                    "color": "#FFFFFF"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": cols[20:25],
            "paddingAll": "5px"
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "來去逛逛 >>",
                            "color": "#ffffff",
                            "size": "md",
                            "align": "center",
                            "flex": 1
                        }
                    ],
                    "margin": "xs"
                }
            ],
            "backgroundColor": "#a8dadc"
        },
        "action": {
            "type": "uri",
            "label": "action",
            "uri": "https://escooter-esbot.herokuapp.com/user-products"
        },
        "styles": {
            "body": {
                "backgroundColor": "#FEFEFE"
            },
            "footer": {
                "separator": True
            }
        }
    }

    _list = {
        "type": "flex",
        "altText": "特賣商品",
        "contents": {
            "type": "carousel",
            "contents": [item1, item2, item3, item4, item5]
        }
    }
    change_text = """特賣商品
系統忙碌時，稍待幾分鐘再試"""
    change_msg = {
        "type": "flex",
        "altText": "特賣商品",
        "contents": {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "更多特賣產品",
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
    try:
        container_obj = FlexSendMessage.new_from_json_dict(_list)
        container_obj2 = FlexSendMessage.new_from_json_dict(change_msg)

        # line_bot_api.push_message
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj, container_obj2])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))
