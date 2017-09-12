import xadmin
from .models import LegalSecurity, MentalHealthSecurity, TrafficSecurity
from .models import ActivityStudySecurity, FoodSecurity,  NationalSecurity
from .models import FireSecurity, PersonalSecurity, NetworkSecurity


class LegalSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(LegalSecurityAdmin, self).post(request, args,
                                                    kwargs)


class MentalHealthSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(MentalHealthSecurityAdmin, self).post(request,
                                                           args, kwargs)


class NationalSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(NationalSecurityAdmin, self).post(request, args, kwargs)


class NetworkSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(NetworkSecurityAdmin, self).post(request, args, kwargs)


class FoodSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(FoodSecurityAdmin, self).post(request, args, kwargs)


class ActivityStudySecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(ActivityStudySecurityAdmin, self).post(request,
                                                            args, kwargs)


class PersonalSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(PersonalSecurityAdmin, self).post(request, args, kwargs)


class FireSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(FireSecurityAdmin, self).post(request, args, kwargs)


class TrafficSecurityAdmin(object):
    list_display = ['questionType', 'questionNumber',
                    'questionScore', 'addTime']
    search_fields = ['questionType', 'questionNumber',
                     'questionScore', 'addTime']
    list_filter = ['questionType', 'questionNumber',
                   'questionScore', 'addTime']
    list_editable = ['questionScore']
    import_excel = True

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(TrafficSecurityAdmin, self).post(request, args, kwargs)


xadmin.site.register(LegalSecurity, LegalSecurityAdmin)
xadmin.site.register(TrafficSecurity, TrafficSecurityAdmin)
xadmin.site.register(FireSecurity, FireSecurityAdmin)
xadmin.site.register(PersonalSecurity, PersonalSecurityAdmin)
xadmin.site.register(MentalHealthSecurity, MentalHealthSecurityAdmin)
xadmin.site.register(ActivityStudySecurity, ActivityStudySecurityAdmin)
xadmin.site.register(FoodSecurity, FoodSecurityAdmin)
xadmin.site.register(NationalSecurity, NationalSecurityAdmin)
xadmin.site.register(NetworkSecurity, NetworkSecurityAdmin)
