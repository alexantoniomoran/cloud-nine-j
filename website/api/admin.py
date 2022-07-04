from django.contrib import admin

from website.api.models import Detector, Photo


@admin.register(Detector)
class DetectorAdmin(admin.ModelAdmin):
    fields = ("name", "cloud_nine")
    list_display = ("name", "cloud_nine")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ("photo", "title", "description")
    list_display = ("thumbnail_image", "title", "description")
    readonly_fields = ("thumbnail_image",)
