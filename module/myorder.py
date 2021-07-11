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


def myorder(event):
    try:
        container_obj = FlexSendMessage.new_from_json_dict(_list)

        # line_bot_api.push_message
        line_bot_api.reply_message(event.reply_token, messages=[
                                   container_obj, container_obj])
    except:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text="發生錯誤！"))


item = {
    "type": "bubble",
    "size": "mega",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "FROM",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "廠商名稱",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                ]
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "TO",
                        "color": "#ffffff66",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "客戶名稱",
                        "color": "#ffffff",
                        "size": "xl",
                        "flex": 4,
                        "weight": "bold"
                    }
                ]
            }
        ],
        "paddingAll": "20px",
        "backgroundColor": "#0367D3",
        "spacing": "md",
        "height": "154px",
        "paddingTop": "22px"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "訂單序號",
                "color": "#b7b7b7",
                "size": "xs"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": " ",
                        "size": "sm",
                        "gravity": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "cornerRadius": "30px",
                                "height": "12px",
                                "width": "12px",
                                "borderColor": "#EF454D",
                                "borderWidth": "2px"
                            },
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "待出貨",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                ],
                "spacing": "lg",
                "cornerRadius": "30px",
                "margin": "xl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "width": "2px",
                                        "backgroundColor": "#B7B7B7"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "flex": 1
                            }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": " ",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                ],
                "spacing": "lg",
                "height": "64px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": " ",
                                "gravity": "center",
                                "size": "sm"
                            }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "cornerRadius": "30px",
                                "width": "12px",
                                "height": "12px",
                                "borderWidth": "2px",
                                "borderColor": "#6486E3"
                            },
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "已出貨",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                ],
                "spacing": "lg",
                "cornerRadius": "30px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 1
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "width": "2px",
                                        "backgroundColor": "#6486E3"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "flex": 1
                            }
                        ],
                        "width": "12px"
                    },
                    {
                        "type": "text",
                        "text": " ",
                        "gravity": "center",
                        "flex": 4,
                        "size": "xs",
                        "color": "#8c8c8c"
                    }
                ],
                "spacing": "lg",
                "height": "64px"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": " ",
                        "gravity": "center",
                        "size": "sm"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "cornerRadius": "30px",
                                "width": "12px",
                                "height": "12px",
                                "borderColor": "#6486E3",
                                "borderWidth": "2px"
                            },
                            {
                                "type": "filler"
                            }
                        ],
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "待簽收",
                        "gravity": "center",
                        "flex": 4,
                        "size": "sm"
                    }
                ],
                "spacing": "lg",
                "cornerRadius": "30px"
            }
        ]
    }
}

item_end = {
    "type": "bubble",
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "RECEIPT",
                "weight": "bold",
                "color": "#1DB446",
                "size": "sm"
            },
            {
                "type": "text",
                "text": "Brown Store",
                "weight": "bold",
                "size": "xxl",
                "margin": "md"
            },
            {
                "type": "text",
                "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
                "size": "xs",
                "color": "#aaaaaa",
                "wrap": True
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Energy Drink",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$2.99",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Chewing Gum",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$0.99",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Bottled Water",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "$3.33",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "xxl",
                        "contents": [
                            {
                                "type": "text",
                                "text": "ITEMS",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "3",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "TOTAL",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$7.31",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "CASH",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$8.0",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "CHANGE",
                                "size": "sm",
                                "color": "#555555"
                            },
                            {
                                "type": "text",
                                "text": "$0.69",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "separator",
                "margin": "xxl"
            },
            {
                "type": "box",
                "layout": "horizontal",
                "margin": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": "PAYMENT ID",
                        "size": "xs",
                        "color": "#aaaaaa",
                        "flex": 0
                    },
                    {
                        "type": "text",
                        "text": "#743289384279",
                        "color": "#aaaaaa",
                        "size": "xs",
                        "align": "end"
                    }
                ]
            }
        ]
    },
    "styles": {
        "footer": {
            "separator": True
        }
    }
}
_list = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "carousel",
        "contents": [item, item_end]
    }
}
