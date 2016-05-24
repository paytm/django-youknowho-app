from django.contrib import admin

from .forms import *
from .models import *


class RuleConditionsInLine(admin.TabularInline):
    model                   = RuleCondition
    extra                   = False
    form                    = RuleConditionForm


class RuleActionsInLine(admin.TabularInline):
    model                   = RuleAction
    form                    = RuleActionForm
    extra                   = False


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):

    list_per_page           = 100
    actions_on_top          = True
    preserve_filters        = True
    save_on_top             = True
    list_select_related     = True
    save_as                 = True

    list_display            = ('id', 'name', 'status', 'priority', 'external_reference', 'created_at', )
    list_filter             = ('updated_at', 'status', 'tags', 'status',)
    exclude                 = ('updated_at' , 'external_reference', 'created_at', )
    list_display_links      = ['id', 'name', ]
    search_fields           = ['name', ]
    list_editable           = ['status', 'priority', ]
    filter_horizontal       = ('tags',)

    inlines                 =  [ RuleConditionsInLine, RuleActionsInLine ]


    def enable_rule(modeladmin, request, queryset):
        if queryset.count() == 0:
            return messages.error(request, 'Select atleast one entry')

        if request.user.is_superuser or request.user.has_perms(['ruleengine.CAN_ENABLE_RULE']):
            queryset.update(status=1)
        else:
            return messages.error(request, 'You are not authorised to perform such action')
    enable_rule.short_description = "Enable rule"

    def disable_rule(modeladmin, request, queryset):

        if queryset.count() == 0:
            return messages.error(request, 'Select atleast one entry')

        if request.user.is_superuser or request.user.has_perms(['ruleengine.CAN_DISABLE_RULE']):
          queryset.update(status=0)
        else:
          return messages.error(request, 'You are not authorised to perform such action')
    disable_rule.short_description = "Disable rule"

    actions = [enable_rule, disable_rule]

    def get_actions(self,request):
        # fetch the esisting actions
        actions = super(RuleAdmin,self).get_actions(request)
        # check if the user is authorized to view the action or not
        if not request.user.has_perms(['ruleengine.CAN_ENABLE_RULE']):
            if 'enable_rule' in actions:
                del actions['enable_rule']
            if 'disable_rule' in actions:
                del actions['disable_rule']
        return actions


@admin.register(RuleTag)
class RuleTagAdmin(admin.ModelAdmin):

    list_per_page           = 100
    actions_on_top          = True
    preserve_filters        = True
    save_on_top             = True
    list_select_related     = True
    save_as                 = True
    list_display            = ('tag_name',)
    search_fields           = ('tag_name',)
    exclude                 = ('created_at', 'updated_at', )


@admin.register(RuleActionKeys)
class RuleActionKeysAdmin(admin.ModelAdmin):

    list_display = ('name', )


@admin.register(RuleConditionKeys)
class RuleConditionKeysAdmin(admin.ModelAdmin):

    list_display = ('name', )