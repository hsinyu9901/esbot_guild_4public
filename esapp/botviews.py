from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, PostbackEvent
from flask import render_template

from module import func, onSale, look4store, productlist, sport, myorder, trail
from urllib.parse import parse_qsl
from esapp.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
handler = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == "POST":
        signature = request.META["HTTP_X_LINE_SIGNATURE"]
        body = request.body.decode("utf-8")
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                user_id = event.source.user_id
                profile = line_bot_api.get_profile(user_id)

                # print(profile.display_name)
                # print(profile.user_id)
                # print(profile.picture_url)
                # print(profile.status_message)
                if not (Friend.objects.filter(lineid=profile.user_id).exists()):
                    user = User.objects.create_user(
                        username=profile.user_id,
                        password="",
                    )
                    friend = Friend.objects.create(
                        # DBfield=local
                        user=user,
                        name=profile.display_name,
                        lineid=profile.user_id,
                    )
                    group = Group.objects.get(name='producer')
                    user.groups.add(group)
                    user.is_staff = True
                    user.save()
                    Producer.objects.create(
                        charge=friend,
                    )

                    # unit = Friend.objects.create(lineid=profile.user_id)
                    # unit.save()
                    ##
                print(body)  # 偵錯用
                mtext = event.message.text
                if mtext == "使用說明":
                    func.sendUse(event)

                # if mtext == "使用說明(公會)":
                #     func.sendUseP(event)

                elif mtext == "公會專屬":
                    func.guild(event, user_id)

                # elif mtext == "@房間預約":
                #     func.sendBooking(event, user_id)

                # elif mtext == "@取消訂房":
                #     func.sendCancel(event, user_id)

                elif mtext == "關於我們":
                    func.sendAbout(event)

                # elif mtext == "@位置資訊":
                #     func.sendPosition(event)

                # elif mtext == "@聯絡我們":
                #     func.sendContact(event)

                elif mtext[:3] == "###" and len(mtext) > 3:  # 處理LIFF傳回的FORM資料
                    func.manageForm(event, mtext, user_id)

                elif mtext[:10] == "" and len(mtext) > 10:  # 推播給所有顧客
                    func.pushMessage(event, mtext)

                elif "testflex" in mtext:
                    func.testFlex(event)

                # elif mtext == "特賣商品":
                #     onSale.onSale(event)

                elif "特賣商品" in mtext:  # 商品列表
                    productlist.productlist(event)

                elif "尋找店家" in mtext:
                    look4store.look4store(event)

                # elif "我的訂單" in mtext:
                #     myorder.myorder(event)

                elif mtext[:4] == "登山步道" and len(mtext) > 4:
                    mtext = mtext.strip()
                    trail.trail_search(event, mtext)

                elif "登山步道" in mtext:
                    trail.trail(event)

                elif "查看更多" in mtext:
                    func.moreInfo(event)

                elif "電腦版選單" in mtext:
                    func.menu(event)

            if isinstance(event, PostbackEvent):  # PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  # 取得Postback資料
                if backdata.get("action") == "yes":
                    func.sendYes(event, event.source.user_id)

        return HttpResponse()

    else:
        return HttpResponseBadRequest()


@csrf_exempt
def test_getprofile(request):
    guild_pass = str(request.POST.get('guild_pass'))
    if guild_pass.strip() == '':
        return redirect('login')
    return render(request, "liff.html")


@csrf_exempt
def test_getprofile1(request):
    if request.method == "POST":
        body = request.body.decode("utf-8")
        events = parser.parse(body)

        for event in events:
            print(body)  # 偵錯用
            user_id = event.source.user_id
            profile = line_bot_api.get_profile(user_id)
            guild_pass = str(request.POST.get('guild_pass'))
            if guild_pass.strip() == '':
                group = Group.objects.get(name='producer')
                user.groups.add(group)
                user.is_staff = True
                user.save()
                Producer.objects.create(
                    charge=friend,
                )
                return HttpResponseRedirect('login')
            return HttpResponse(request, "liff.html")
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
