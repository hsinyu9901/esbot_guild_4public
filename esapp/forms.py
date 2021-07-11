from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


"""
2020/07/25

"""


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Customer
class FriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'
        exclude = ['user', 'lineid', 'member']
        labels = {
            'name': _('我的暱稱'),
            'email': _('個人信箱'),
            'phone': _('個人電話'),
            'charge': _('廠商負責人'),
            'profile_pic': _('形象照片')
        }
        help_texts = {
            'email': _('請填寫正確，這將是你變更密碼的信箱'),
            'phone': _('請填寫正確，這將是你的新帳號，建議使用與LINE帳號相同之號碼，10碼電話，如: 0987654321或 0287654321'),
            'profile_pic': _('請點選按鈕，推薦您上傳 [品牌LOGO] 或 [店面照片] 這將會呈現給其他使用者'),
        }


class ProducerForm(ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'
        labels = {
            'producer_name': _('廠商名稱'),
            'producer_ctiy': _('廠商城市'),
            'producer_address': _('廠商地址'),
            'producer_email': _('廠商信箱'),
            'producer_phone': _('廠商電話'),
            'charge': _('廠商負責人'),
            'producer_info': _('廠商簡介'),
            'producer_time': _('營業時間'),
        }

        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

        help_texts = {
        }


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {
            'name': _('標籤名稱'),
        }


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        labels = {
            'name': _('尺寸名稱'),
        }


class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        labels = {
            'name': _('顏色名稱'),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'producer': _('廠商名稱'),
            'name': _('商品名稱'),
            'price': _('價格'),
            'info': _('商品簡介'),
            'category': _('分類'),
            'note': _('備註'),
            'date_created': _('新增日期時間'),
            'tag': _('屬性標籤'),
            'image': _('圖片'),
        }
        help_texts = {
            'tag': _('若無合適標籤可至"規格定義 > 產品標籤"新增'),
            'discount': _('0.1~1.0之間，不打折為1.0，打八五折為0.85，以此類推'),
            'note': _('優惠條件或可用折價券...等，例如:三倍券'),
        }


class ProductSetForm(ModelForm):
    class Meta:
        model = ProductSet
        fields = '__all__'
        labels = {
            'product': _('品名'),
            'color': _('顏色'),
            'size': _('尺寸'),
        }
        help_texts = {
            'color': _('若無合適顏色可至"規格定義 > 顏色型錄"新增'),
            'size': _('若無合適尺寸可至"規格定義 > 尺寸型錄"新增'),
        }
