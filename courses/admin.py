from django.contrib import admin
from .models import Course , Lesson

admin.site.register(Course)
admin.site.register(Lesson)





# from django.contrib import admin
# from django.utils.html import format_html
# from .models import Course #, Lesson, Review
# from .models import Course


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug')
    





# # 🔹 Admin للكورس
# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'level', 'language', 'created_at')
#     list_filter = ('level', 'language', 'created_at')
#     prepopulated_fields = {"slug": ("title",)}
#     # search_fields = ('title', 'instructor__username', 'description')
#     ordering = ('-created_at',)
#     # inlines = [LessonInline, ReviewInline]

#     # عرض صورة الكورس (تصغيرها في الادمين)
#     def cover_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="80" style="border-radius:8px"/>', obj.image.url)
#         return "No Image"
#     cover_preview.short_description = "Cover"

    # # عرض اسم المدرب
    # def instructor_name(self, obj):
    #     return obj.instructor.username
    # instructor_name.short_description = "Instructor"




# # 🔹 Inline لعرض الدروس داخل الكورس
# class LessonInline(admin.TabularInline):
#     model = Lesson
#     extra = 1
#     fields = ('title', 'duration', 'is_preview', 'video_url')
#     show_change_link = True


# # 🔹 Inline لعرض المراجعات داخل الكورس
# class ReviewInline(admin.TabularInline):
#     model = Review
#     extra = 1
#     fields = ('user', 'rating', 'comment')
#     show_change_link = True
#     readonly_fields = ('user', 'created_at')  # منع تعديل بعض الحقول



# # 🔹 Admin للدروس (مستقل لو حابب تديرها برة الكورس)
# @admin.register(Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     list_display = ('title', 'course', 'duration', 'is_preview')
#     list_filter = ('is_preview', 'course')
#     search_fields = ('title', 'course__title')
#     ordering = ('course',)


# # 🔹 Admin للمراجعات
# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('course', 'user', 'rating', 'created_at')
#     list_filter = ('rating', 'created_at')
#     search_fields = ('course__title', 'user__username')
#     ordering = ('-created_at',)
