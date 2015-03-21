from django.contrib import admin
from dictionary.models import Examples,Meanings,Wordsense,Hypernym,Synonym,Relate,Wordtypes

# Register your models here.
class WordtypesInline(admin.StackedInline):
    model=Wordtypes
    extra=1

    
class MeaningsInline(admin.StackedInline):
    model = Meanings
    extra = 3

class ExamplesInline(admin.StackedInline):
    model = Examples
    extra = 3
class RelateInline(admin.StackedInline):
    model = Relate
    extra = 1

class SynonymInline(admin.StackedInline):
    model = Synonym
    extra = 1

    
class HypernymInline(admin.StackedInline):
    model = Hypernym
    extra = 1


    
class WordsenseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('word', {'fields': ['word_id','word']}),
    ]

admin.site.register(Wordsense,WordsenseAdmin)
admin.site.register(Meanings)
admin.site.register(Relate)
admin.site.register(Synonym)
admin.site.register(Hypernym)
admin.site.register(Wordtypes)
admin.site.register(Examples)
