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
                print(body)  # ?????????
                mtext = event.message.text
                if mtext == "????????????":
                    func.sendUse(event)

                # if mtext == "????????????(??????)":
                #     func.sendUseP(event)

                elif mtext == "????????????":
                    func.guild(event, user_id)

                # elif mtext == "@????????????":
                #     func.sendBooking(event, user_id)

                # elif mtext == "@????????????":
                #     func.sendCancel(event, user_id)

                elif mtext == "????????????":
                    func.sendAbout(event)

                # elif mtext == "@????????????":
                #     func.sendPosition(event)

                # elif mtext == "@????????????":
                #     func.sendContact(event)

                elif mtext[:3] == "###" and len(mtext) > 3:  # ??????LIFF?????????FORM??????
                    func.manageForm(event, mtext, user_id)

                elif mtext[:10] == "" and len(mtext) > 10:  # ?????????????????????
                    func.pushMessage(event, mtext)

                elif "testflex" in mtext:
                    func.testFlex(event)

                # elif mtext == "????????????":
                #     onSale.onSale(event)

                elif "????????????" in mtext:  # ????????????
                    productlist.productlist(event)

                elif "????????????" in mtext:
                    look4store.look4store(event)

                # elif "????????????" in mtext:
                #     myorder.myorder(event)

                elif mtext[:4] == "????????????" and len(mtext) > 4:
                    mtext = mtext.strip()
                    trail.trail_search(event, mtext)

                elif "????????????" in mtext:
                    trail.trail(event)

                elif "????????????" in mtext:
                    func.moreInfo(event)

                elif "???????????????" in mtext:
                    func.menu(event)

            if isinstance(event, PostbackEvent):  # PostbackTemplateAction???????????????
                backdata = dict(parse_qsl(event.postback.data))  # ??????Postback??????
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
            print(body)  # ?????????
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
