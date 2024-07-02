from django.contrib import admin

# Register your models here.

from .models import HuggingFaceModel, ModelInfor, AmazonLabels, AmazonProductReviews

class ModelInforInline(admin.TabularInline):
    model = ModelInfor
    extra = 3

class HuggingFaceModelAdmin(admin.ModelAdmin):
    filedSets = [
        ("path", {"fields: [pub_path]"}),
        ("Date information", {"files": ["upd_date"],
                              "classes": ["collapse"]}),
    ]
    inlines = [ModelInforInline]

    list_display = ["pub_path", "upd_date"]
    list_filter = ["upd_date"]
    search_fields = ["pub_path", "upd_date"]

class AmazonProductReviewsInline(admin.TabularInline):
    model = AmazonProductReviews
    extra = 3

class AmazonLabelsAdmin(admin.ModelAdmin):
    inlines = [AmazonProductReviewsInline]
    list_display = ["label", "cat_name", "svg_str"]


admin.site.register(HuggingFaceModel, HuggingFaceModelAdmin)
admin.site.register(AmazonLabels, AmazonLabelsAdmin)
admin.site.register(AmazonProductReviews)