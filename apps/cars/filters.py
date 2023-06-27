from django.db.models import QuerySet
from django.http import QueryDict
from .models import CarModel
from rest_framework.serializers import ValidationError

# Розібрати все що було на лекції
#
# Додати функціонал по видаленню та оновленню автопарків
#
# До Апки карів додати:
# філтри до кожного поля:
# - для числових (більше менше білше-рівне менше-рівне)
# -для текстових (починається з, закінчується на, та містить в собі)
# пошук карів по id автопарку через query_params
# а також додати сортування для будь якого поля як ASC так і DESC
def car_filtered_queryset(query:QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_lt':
                qs = qs.filter(price__lt= v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)
            case 'auto_park_id':
                qs = qs.filter(auto_park_id = v)
            case 'brand_start_with':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_end_with':
                qs = qs.filter(brand__iendswith=v)
            case 'order':
                qs = qs.order_by(v)
            case 'brand_contains':
                qs = qs.filter(brand__icontains=v)
            case _:
                raise ValidationError({'details':f'"{k}" not allowed here'})
    return qs
