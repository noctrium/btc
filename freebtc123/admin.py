from django.contrib import admin
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

from freebtc123.models import Wallet, UserInfo, Nav, Classify, Site, Evaluate, Like, Favorite, Visit


class WalletAdmin(admin.ModelAdmin):
    list_display = ('walletUrl',)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'wallet')


class NavAdmin(admin.ModelAdmin):
    list_display = ('navName', 'navTitle', 'navPosition')


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('csyName', 'csyDescription', 'nav', 'csyPosition')


class SiteAdmin(admin.ModelAdmin):
    list_display = ('siteName', 'siteDescription', 'siteUrl', 'siteClickNum', 'siteEvaluateNum', 'siteLikeNum', 'siteUnlikeNum', 'siteFavNum', 'siteDateTime', 'classify')


class EvaluateAdmin(admin.ModelAdmin):
    list_display = ('site', 'evaContent', 'evaDateTime')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'wallet', 'host', 'flag', 'likeTime')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'wallet', 'host', 'favoriteTime')


class VisitAdmin(admin.ModelAdmin):
    list_display = ('site', 'user', 'wallet', 'host', 'visitTime')

admin.site.register(Wallet, WalletAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Evaluate, EvaluateAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Visit, VisitAdmin)