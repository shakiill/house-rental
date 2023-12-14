from django import template
import calendar

register = template.Library()


# @register.filter
# def sort_by_sequence(queryset):
#     return queryset.order_by('sequence')
#
#
# @register.filter
# def month_name(month_number):
#     a = int(month_number)
#     return calendar.month_name[a]
#
#
# @register.filter
# def test_tag(a, b):
#     a = int(a) + int(b)
#     return a
