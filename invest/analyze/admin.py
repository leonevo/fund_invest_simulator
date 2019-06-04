from django.contrib import admin

# Register your models here.
from analyze.models import regress_invest


class analyzeadmin(admin.ModelAdmin):
    list_display = ('id', 'fund_code', 'fund_name', 'start_date', 'end_date', 'base_interest_rate', 'fund_return_rate',
                    'base_return_rate')

# Register your models here.


admin.site.register(regress_invest, analyzeadmin)
