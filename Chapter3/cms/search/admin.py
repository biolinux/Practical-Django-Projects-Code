from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from search.models import SearchKeyword


class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)



# This code defines the subclass of admin.ModelAdmin called SearchKeywordAdmin
# The pass statement means you don't want to customize anything in this class.

'''class SearchKeywordAdmin(admin.ModelAdmin):
    pass'''


# admin.site.register function will tells Django's administration interface to associate
# this ModelAdmin subclass with the SearchKeyword model.

#admin.site.register(SearchKeyword, SearchKeywordAdmin)


