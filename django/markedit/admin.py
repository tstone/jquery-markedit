from django.contrib import admin
from markedit.widgets import AdminMarkEdit

class MarkEditAdmin(admin.ModelAdmin):

    class MarkEdit:
        fields = ['text',]
        options = {}

    class Media:
        from markedit import settings
        css = getattr(settings, 'MARKEDIT_CSS', {})
        js = getattr(settings, 'MARKEDIT_JS', [])

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(MarkEditAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in self.MarkEdit.fields:
            formfield.widget = AdminMarkEdit(attrs = {
                'options': self.MarkEdit.options,
            })
        return formfield

