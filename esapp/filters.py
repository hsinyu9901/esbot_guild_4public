import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter, ModelMultipleChoiceFilter, MultipleChoiceFilter

from .models import *
from .forms import *


# class Filter(django_filters.FilterSet):
#     class Meta:
#         model =
#         fields ='__all__'


# class OrderFilter(django_filters.FilterSet):
#     # start_date = DateFilter(field_name="date_created",lookup_expr='gte') # 大於某日
#     # end_date = DateFilter(field_name="date_created",lookup_expr='lte') # 小於某日
#     # note = CharFilter(field_name="date_ordered",lookup_expr='icontains')# 包含內容
#     class Meta:
#         model = Order
#         fields = '__all__'
#         exclude = ['customer']
CITY = (
    ('基隆市', '基隆市'), ('台北市', '台北市'), ('新北市', '新北市'), ('桃園縣', '桃園縣'), ('新竹市', '新竹市'),
    ('新竹縣', '新竹縣'), ('苗栗縣', '苗栗縣'), ('台中市', '台中市'), ('彰化縣', '彰化縣'), ('南投縣', '南投縣'),
    ('雲林縣', '雲林縣'), ('嘉義市', '嘉義市'), ('嘉義縣', '嘉義縣'), ('台南市', '台南市'), ('高雄市', '高雄市'),
    ('屏東縣', '屏東縣'), ('台東縣', '台東縣'), ('花蓮縣', '花蓮縣'), ('宜蘭縣', '宜蘭縣'), ('澎湖縣', '澎湖縣'),
    ('金門縣', '金門縣'), ('連江縣', '連江縣'),
)
CATEGORY = (
    ('上衣', '上衣'), ('下著', '下著'), ('內衣褲', '內衣褲'), ('外套', '外套'), ('帽子', '帽子'),
    ('襪子', '襪子'), ('鞋子', '鞋子'), ('手/袖套', '手/袖套'), ('涼感小物', '涼感小物'),
    ('泳裝', '泳裝'), ('毛巾', '毛巾'), ('護具', '護具'), ('運動器材', '運動器材'),
    ('登山用品', '登山用品'), ('機車配件', '機車配件'), ('其他', '其他'),
)


class ProducerFilter(django_filters.FilterSet):
    producer_name = CharFilter(field_name="producer_name",
                               lookup_expr='icontains', label='店名')  # 包含內容
    producer_ctiy = ChoiceFilter(
        field_name="producer_ctiy", label='城市', choices=CITY)  # 商品分類
    producer_address = CharFilter(field_name="producer_address",
                                  lookup_expr='icontains', label='地址')

    class Meta:
        model = Producer
        fields = '__all__'
        exclude = ['charge', 'producer_time', 'producer_email',
                   'producer_phone', 'producer_info', 'discount']


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name",
                      lookup_expr='icontains', label='品名')  # 包含內容
    producer = CharFilter(field_name="producer__producer_name",
                          lookup_expr='icontains', label='店家')
    category = django_filters.MultipleChoiceFilter(
        field_name="category", label='分類', choices=CATEGORY, widget=forms.CheckboxSelectMultiple)  # 商品分類

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['producer', 'price', 'info',
                   'note', 'date_created', 'tag', 'image']


class ProductSetFilter(django_filters.FilterSet):
    color = CharFilter(field_name="color__name",
                       lookup_expr='icontains', label='顏色')
    size = CharFilter(field_name="size__name",
                      lookup_expr='icontains', label='尺寸')

    class Meta:
        model = ProductSet
        fields = '__all__'
        exclude = ['product']
