from django.contrib import admin

from .models import *

# Register your models here.


#   資料庫表單管理頁面
#    id 為資料庫自動產生之欄位，遞增1，PK

#     # 定義顯示欄位
#         list_display = ('id', 'LineId', 'name', 'email',
#                         'password', 'date_created', 'member')

#         # 欄位過濾資料
#         list_filter = ('member',)

#         # 搜尋
#         search_fields = ('LineId', 'name',)

#         # 排序
#         ordering = ('id',)

#     變更後必須執行以下兩行指令，以同步資料庫
#       python .\manage.py makemigrations
#        python .\manage.py migrate

# 用戶列表==========================================================


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lineid', 'name', 'email',
                    'phone', 'date_created', 'profile_pic')
    search_fields = ('lineid', 'name',)
    ordering = ('id',)


admin.site.register(Friend, FriendAdmin)
# 用戶列表(End)

# 廠商列表==========================================================


class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'charge', 'producer_name',
                    'producer_ctiy', 'producer_address', 'producer_time', 'producer_email', 'producer_phone',  'producer_info')
    search_fields = ('name', 'charge',)


admin.site.register(Producer, ProducerAdmin)
# 廠商列表(End)

# 屬性標籤列表==========================================================


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Tag, TagAdmin)

# 尺寸列表==========================================================


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Size, SizeAdmin)

# 顏色列表==========================================================


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Color, ColorAdmin)

# 商品列表==========================================================


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'producer', 'name', 'price', 'info', 'category',
                    'get_tags', 'note', 'date_created', 'image')
    list_filter = ('category', 'producer',)
    filter_horizontal = ('tag',)
    search_fields = ('name', 'price',)


admin.site.register(Product, ProductAdmin)
# 商品顏色尺寸組合==================================================


class ProductSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size')


admin.site.register(ProductSet, ProductSetAdmin)
# 庫存列表==========================================================


class TrailAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'gmap', 'length',
                    'once_time', 'pic_ref1', 'pic_ref2', 'info', 'source')
    search_fields = ('name', )


admin.site.register(Trail, TrailAdmin)
