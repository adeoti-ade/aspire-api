from django.contrib import admin

from movie.models import FavouriteQuote, Quote, Character, FavouriteCharacter

admin.site.register(FavouriteQuote)
admin.site.register(Quote)
admin.site.register(Character)
admin.site.register(FavouriteCharacter)