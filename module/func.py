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
    ImageSendMessage, ImagemapSendMessage, BaseSize, MessageImagemapAction, URIImagemapAction, ImagemapArea,   DatetimePickerTemplateAction)
from esapp.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def menu(event):
    try:
        _list = {
            "type": "flex",
            "altText": "電腦版選單",
            "contents": {
                "type": "bubble",
                "size": "giga",
                "header": {
                    "type": "box",
                    "layout": "horizontal",
                    "backgroundColor": "#a8dadc",
                    "contents": [
                        {
                            "type": "text",
                            "text": "【電腦版選單】",
                            "size": "xl",
                            "gravity": "center",
                            "align": "center",
                            "color": "#ffffff",
                            "weight": "bold"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "separator",
                            "color": "#FFFFFF",
                            "margin": "none"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "聯合特賣",
                                            "color": "#405958",
                                            "size": "xl",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": "特賣商品"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "尋找店家",
                                            "color": "#405958",
                                            "size": "xl",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": "尋找店家"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": "https://i.imgur.com/H8Vn9st.png",
                                            "size": "xxs"
                                        }
                                    ],
                                    "position": "absolute",
                                    "paddingAll": "0px",
                                    "offsetTop": "3px",
                                    "offsetStart": "3px"
                                }
                            ],
                            "paddingTop": "5px",
                            "paddingStart": "5px",
                            "paddingEnd": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "登山步道",
                                            "color": "#89b0ae",
                                            "size": "md",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": "登山步道"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "關於我們",
                                            "color": "#89b0ae",
                                            "size": "md",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": "關於我們"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "回報問題",
                                            "color": "#89b0ae",
                                            "size": "md",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": "填寫問卷: https://docs.google.com/forms/d/e/1FAIpQLSds3ZUM_v7r4W0By4He4VES3tv5lmwtTL9rda15zWhPCpEN6Q/viewform?usp=sf_link"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "使用說明",
                                            "color": "#89b0ae",
                                            "size": "md",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": "使用說明"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                }
                            ],
                            "paddingStart": "5px",
                            "paddingEnd": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "邀請好友",
                                            "color": "#89b0ae",
                                            "size": "xl",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "uri",
                                                "label": "邀請好友",
                                                "uri": "line://nv/recommendOA/@350oetzg"
                                            },
                                            "weight": "bold"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "公會專屬",
                                            "size": "xl",
                                            "align": "center",
                                            "wrap": True,
                                            "action": {
                                                "type": "uri",
                                                "label": "公會專屬",
                                                "uri": "https://liff.line.me/1654480216-m04VLLJg"
                                            },
                                            "weight": "bold",
                                            "color": "#89b0ae"
                                        }
                                    ],
                                    "backgroundColor": "#dbf0f0",
                                    "borderColor": "#a8dadc",
                                    "borderWidth": "5px",
                                    "cornerRadius": "10px",
                                    "paddingAll": "5px"
                                }
                            ],
                            "paddingBottom": "5px",
                            "paddingStart": "5px",
                            "paddingEnd": "5px"
                        }
                    ],
                    "paddingAll": "0px",
                    "backgroundColor": "#a8dadc"
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
        }

        container_obj = FlexSendMessage.new_from_json_dict(_list)
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj])

    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


def sendUse(event):  # 使用說明
    try:

        message = {
            "type": "flex",
            "altText": "使用說明",
            "contents": {
                "type": "bubble",
                "size": "giga",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "【使用說明】",
                            "size": "xl",
                            "color": "#ffffff",
                            "weight": "bold",
                            "align": "center"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "聯合特賣",
                                    "color": "#89b0ae",
                                    "size": "xl",
                                    "flex": 1,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "優質商品不嫌多~ 限定好康都在這 !",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "lg",
                                    "flex": 5,
                                    "gravity": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "width": "96%",
                            "offsetStart": "2%",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "尋找店家",
                                    "color": "#89b0ae",
                                    "size": "xl",
                                    "flex": 1,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "快來看看離你最近的優質店家是?",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "lg",
                                    "flex": 5,
                                    "gravity": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "width": "96%",
                            "offsetStart": "2%",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "登山步道",
                                    "color": "#89b0ae",
                                    "size": "xl",
                                    "flex": 1,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "輸入[登山步道 關鍵字]， 如:登山步道 八仙",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "lg",
                                    "flex": 5,
                                    "gravity": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "width": "96%",
                            "offsetStart": "2%",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "邀請好友",
                                    "color": "#89b0ae",
                                    "size": "xl",
                                    "flex": 1,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "這麼多好康，不能只有我知道，傳送本頻道資訊給好友!",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "lg",
                                    "flex": 5,
                                    "gravity": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "width": "96%",
                            "offsetStart": "2%",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "查看更多",
                                    "color": "#89b0ae",
                                    "size": "xl",
                                    "flex": 1,
                                    "wrap": True
                                },
                                {
                                    "type": "text",
                                    "text": "電腦版選單/使用說明/關於我們/回報問題",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "lg",
                                    "flex": 5,
                                    "gravity": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "width": "96%",
                            "offsetStart": "2%",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px"
                        }
                    ],
                    "paddingAll": "0px",
                    "backgroundColor": "#a8dadc"
                },
                "styles": {
                    "header": {
                        "backgroundColor": "#a8dadc"
                    }
                }
            }
        }

        container_obj = FlexSendMessage.new_from_json_dict(message)
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


def sendUseP(event):  # 使用說明
    try:
        text1 = '''
1. [公會專屬]輸入{通行碼}
2. 初次[登入]畫面，請勿更改預設帳號，輸入{預設密碼}
3. [設定]畫面，正確輸入{個人與廠商資料}，務必[儲存變更]
4. 選擇[變更密碼]，輸入上述第三項之[個人資料的信箱]提交
               '''
        message = TextSendMessage(
            text=text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))

# ImagemapSendMessage(組圖訊息)

# 登山步道


def imagemap_message():
    message = ImagemapSendMessage(
        base_url="https://i.imgur.com/3fEi67o.png",
        alt_text='登山步道資訊網站:林務局全球資訊網/台灣山林悠遊網/健行筆記/脊梁山脈旅遊年',
        base_size=BaseSize(height=1000, width=1000),
        actions=[
            URIImagemapAction(
                # 林務局全球資訊網
                link_uri="https://www.forest.gov.tw/",
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=250
                )
            ),
            URIImagemapAction(
                # 台灣山林悠遊網
                link_uri="https://recreation.forest.gov.tw/",
                area=ImagemapArea(
                    x=0, y=250, width=1000, height=250
                )
            ),
            URIImagemapAction(
                # 健行筆記
                link_uri="https://hiking.biji.co/",
                area=ImagemapArea(
                    x=0, y=500, width=1000, height=250
                )
            ),
            URIImagemapAction(
                # 脊梁山脈旅遊年
                link_uri="https://i30.taiwan.net.tw/",
                area=ImagemapArea(
                    x=0, y=750, width=1000, height=250
                )
            ),
        ]
    )
    return message



def sendAbout(event):  # 關於我們
    try:
        _list = {
            "type": "flex",
            "altText": "關於我們",
            "contents": {
                "type": "bubble",
                "size": "giga",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "【關於我們】",
                            "size": "xl",
                            "color": "#ffffff",
                            "weight": "bold",
                            "align": "center"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "中華民國體育用品經銷商協會",
                                    "color": "#89b0ae",
                                    "size": "lg",
                                    "flex": 1,
                                    "wrap": True,
                                    "align": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "backgroundColor": "#dbf0f0",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px",
                            "paddingAll": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "新北市體育用品同業公會",
                                    "color": "#89b0ae",
                                    "size": "lg",
                                    "flex": 1,
                                    "wrap": True,
                                    "align": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xl",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "世新大學資管系",
                                    "color": "#89b0ae",
                                    "size": "lg",
                                    "flex": 1,
                                    "wrap": True,
                                    "align": "center"
                                }
                            ],
                            "cornerRadius": "10px",
                            "paddingAll": "5px",
                            "backgroundColor": "#dbf0f0",
                            "borderColor": "#a8dadc",
                            "borderWidth": "5px",
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "http://im.wp.shu.edu.tw/"
                            }
                        }
                    ],
                    "backgroundColor": "#a8dadc"
                },
                "styles": {
                    "header": {
                        "backgroundColor": "#a8dadc"
                    }
                }
            }
        }
        container_obj = FlexSendMessage.new_from_json_dict(_list)
        line_bot_api.reply_message(
            event.reply_token, messages=[container_obj])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))



def pushMessage(event, mtext):  # 推播訊息給所有顧客
    try:
        msg = mtext[10:]  # 取得訊息
        friendall = Friend.objects.all()
        for friend in friendall:  # 逐一推播
            if friend.lineid is not None:
                message = TextSendMessage(
                    text=msg
                )
                line_bot_api.push_message(
                    friend.lineid, messages=[message])  # 推播訊息
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


def shopping(event):
    try:

        quick_list = {
            "type": "text",
            "text": "請選擇",
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/AFm8tnM.png",
                        "action": {
                            "type": "message",
                            "label": "使用說明",
                            "text": "使用說明"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/AFm8tnM.png",
                        "action": {
                            "type": "message",
                            "label": "使用說明(公會)",
                            "text": "使用說明(公會)"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/cXz3gXf.png",
                        "action": {
                            "type": "message",
                            "label": "關於我們",
                            "text": "關於我們"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/HAmKKIX.png",
                        "action": {
                            "type": "message",
                            "label": "商品列表",
                            "text": "商品列表"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/oLNSiqb.png",
                        "action": {
                            "type": "message",
                            "label": "尋找店家",
                            "text": "尋找店家"
                        }
                    },
                    {
                        "type": "action",
                        "action": {
                            "type": "location",
                            "label": "傳送我的位置訊息"
                        }
                    }
                ]
            }
        }
        container_obj = TextSendMessage.new_from_json_dict(quick_list)

        # line_bot_api.push_message
        line_bot_api.reply_message(event.reply_token, messages=container_obj)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


def moreInfo(event):
    try:
        quick_list = {
            "type": "text",
            "text": "請選擇",
            "quickReply": {
                "items": [
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/JXBiw7w.png",
                        "action": {
                            "type": "message",
                            "label": "電腦版選單",
                            "text": "電腦版選單"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/qh9QJX2.png",
                        "action": {
                            "type": "message",
                            "label": "使用說明",
                            "text": "使用說明"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/CQWuOeq.png",
                        "action": {
                            "type": "message",
                            "label": "關於我們",
                            "text": "關於我們"
                        }
                    },
                    {
                        "type": "action",
                        "imageUrl": "https://i.imgur.com/6h0Vwzo.png",
                        "action": {
                            "type": "message",
                            "label": "回報問題",
                            "text": "填寫問卷: https://forms.gle/Sih3tJvJtHAn4S8G6"
                        }
                    }
                ]
            }
        }
        container_obj = TextSendMessage.new_from_json_dict(quick_list)

        # line_bot_api.push_message
        line_bot_api.reply_message(event.reply_token, messages=container_obj)
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))


def testFlex(event):
    try:
        payload = {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "size": "giga",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/hnvJZLk.png",
                                    "align": "center",
                                    "size": "xxl",
                                    "margin": "none",
                                    "gravity": "top",
                                    "aspectMode": "fit"
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/3SRAW8i.png",
                                    "align": "center",
                                    "size": "xxl",
                                    "margin": "none",
                                    "gravity": "top"
                                }
                            ],
                            "paddingAll": "0px",
                            "margin": "none"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/nBhQuQR.png",
                                    "align": "center",
                                    "size": "xxl",
                                    "margin": "none",
                                    "gravity": "top"
                                },
                                {
                                    "type": "image",
                                    "url": "https://i.imgur.com/hS4BAXs.png",
                                    "align": "center",
                                    "size": "xxl",
                                    "margin": "none",
                                    "gravity": "top",
                                    "aspectMode": "fit"
                                }
                            ],
                            "paddingAll": "0px",
                            "margin": "none"
                        }
                    ],
                    "paddingAll": "0px",
                    "backgroundColor": "#999999",
                    "margin": "none"
                }, "styles": {
                    "body": {
                        "paddingAll": "0px",
                        "backgroundColor": "#999999",
                        "margin": "none"
                    }
                }
            }}

        tt = {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "label": "Line",
                        "uri": "https://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Brown Cafe",
                            "size": "xl",
                            "weight": "bold"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "margin": "md",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "icon",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                                    "size": "sm"
                                },
                                {
                                    "type": "text",
                                    "text": "4.0",
                                    "flex": 0,
                                    "margin": "md",
                                    "size": "sm",
                                    "color": "#999999"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "margin": "lg",
                            "color": "#AAAAAA",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Place",
                                            "flex": 1,
                                            "size": "sm",
                                            "color": "#AAAAAA"
                                        },
                                        {
                                            "type": "text",
                                            "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                                            "flex": 5,
                                            "size": "sm",
                                            "color": "#666666",
                                            "wrap": True
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "Time",
                                            "flex": 1,
                                            "size": "sm",
                                            "color": "#666666"
                                        },
                                        {
                                            "type": "text",
                                            "text": "10:00 - 23:00",
                                            "flex": 5,
                                            "size": "sm",
                                            "color": "#AAAAAA",
                                            "wrap": True
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
                    "flex": 0,
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "CALL",
                                "uri": "https://linecorp.com"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "WEBSITE",
                                "uri": "https://linecorp.com"
                            },
                            "height": "sm",
                            "style": "link"
                        },
                        {
                            "type": "spacer",
                            "size": "sm"
                        }
                    ]
                },
                "styles": {
                    "body": {
                        "backgroundColor": "#5E7EA2cc",
                    }
                }
            }}

        container_obj = FlexSendMessage.new_from_json_dict(payload)
        container_obj2 = FlexSendMessage.new_from_json_dict(tt)

        # line_bot_api.push_message
        line_bot_api.reply_message(event.reply_token, messages=[
                                   container_obj])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='非常不好意思！系統目前忙碌中，稍待幾分鐘後可以再次要求我幫你查詢'))
