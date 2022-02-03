menu = [
    {'title': "Main page", 'url_name': "home"},
    {'title': "Contacts", 'url_name': "contacts"},
    {'title': "Queued", 'url_name': "queued"},
    {'title': "Reception", 'url_name': "new_order"},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
