# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           Register Tweet model to Django Admin page
#
# =================================================================================================
#    Date      Name                    Description of Change
# 05-Sep-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================

from django.contrib import admin
from tweets.models import Tweet

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'created_at',
        'user',
        'content',
    )