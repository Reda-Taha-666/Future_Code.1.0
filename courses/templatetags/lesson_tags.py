from django import template

register = template.Library()

@register.filter
def get_next(lessons, current_id):
    lesson_list = list(lessons)
    for i, lesson in enumerate(lesson_list):
        if lesson.id == current_id and i < len(lesson_list) - 1:
            return lesson_list[i+1].id
    return None

@register.filter
def get_previous(lessons, current_id):
    lesson_list = list(lessons)
    for i, lesson in enumerate(lesson_list):
        if lesson.id == current_id and i > 0:
            return lesson_list[i-1].id
    return None
