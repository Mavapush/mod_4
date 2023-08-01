from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display=['id','title','description',
                  'price','auction','created_date','updated_at']
    list_filter =['auction','created_at']
    actions = ['make_auction_as_false','make_auction_as_true']

    fieldsets =(
        (
            'общее',
            (
                {
                    'fields':('title','description')
                }
            )
        ),
        (
            "финансы",
            (
                {
                    'fields':('auction','price'),
                    'classes':['collapse']
                }
            )
        )
    )

    @admin.action(description="убрать возможность торга")
    def make_auction_as_false(self,request,queryset):
        queryset.update(auction=False)

    @admin.action(description="добавить возможность торга")
    def make_auction_as_true(self,request,queryset):
        queryset.update(auction=True)



admin.site.register(Advertisement,AdvertisementAdmin)