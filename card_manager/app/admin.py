from django.contrib import admin


from .models import Card, CardClassification


class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'first_name', 'last_name', 'department', 'phone_number', 'postal_code',
                    'office_address', 'building_name', 'card_img', 'created_at')
    list_display_links = ('id',)


class CardClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'classification')
    list_display_links = ('id',)


admin.site.register(Card, CardAdmin)

admin.site.register(CardClassification, CardClassificationAdmin)