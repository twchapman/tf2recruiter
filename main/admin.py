from django.contrib import admin
from main.models import *
    
# class ClassAdmin(admin.ModelAdmin):
#     list_display = ('cancelled_reverse', 'last_name', 'first_name', 'name_tag', 'globalid', 'campusID', 'gender', 'shirt_size', 'signedup', 'requested_date', 'assigned_date', 'paid','payment_type', 'quikpay_id', 'has_involvements' ,'has_needs', 'share_info', 'willbe18')
#     list_display_links = ('first_name', 'last_name', 'name_tag', 'campusID')
#     fieldsets = [
#             ('Personal Information', {'fields': ('first_name', 'last_name', 'globalid', 'nametag', 'campusID', 'email', 'gender', 'willbe18', 'highschool_other', 'highschool_city', 'share_info')}),
#             ('Contact Information', {'fields': ('addr_street', 'addr_city', 'addr_state', 'addr_zip', 'phone')}),
#             ('Dates', {'fields': ('requested_date_key','assigned_date_key', 'signedup')}),
#             ('Payment', {'fields': ('paid', 'payment_reminder_sent', 'payment_type', 'paid_date', 'quikpay_id')}),
#             ('Other', {'fields': ('involvements','special_needs', 'comments', 'staff_comments', 'cancelled')})
#     ]
#     date_hierarchy = 'signedup'
#     actions = [assign_selected, mark_selected_as_paid, mark_selected_as_cancelled, export_to_csv, export_emails_to_csv]
#     readonly_fields = ['share_info', 'first_name', 'last_name', 'signedup', 'quikpay_id', 'willbe18']
#     list_filter = ('cancelled', 'gender', 'paid', 'signedup', 'requested_date_text', 'assigned_date_text', 'shirt_size', 'payment_type','share_info', 'willbe18')
#     ordering = ('signedup',)
#     filter_horizontal = ('involvements','special_needs')
#     save_on_top = True
#    
admin.site.register(Player)
admin.site.register(Class)