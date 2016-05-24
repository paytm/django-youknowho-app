from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Rule

class RulesList(ListView):

    '''
        returns a list of rules, like

        [{
          "id": 1,
          "name": "Natural Number ",
          "external_reference": "",
          "conditionsOperator": "&&",
          "priority": 170001,
          "tags": [
            "natural",
          ],
          "conditions": [{
            "id": 1,
            "key": "integer",
            "operation": ">",
            "value": "0"
          }],
          "actions": [{
            "id": 2,
            "action": "SET_VARIABLE",
            "key": "is_natural",
            "value": 1
          }]
        }]
    '''

    def get(self, request, *args, **kwargs):
        output_json = {}
        rules = Rule.objects.all().order_by('-id')
        rules_arr = []
        for each_rule in rules:
            temp_rule = {}
            temp_rule['id'] = each_rule.id
            temp_rule['name'] = each_rule.name.strip()
            temp_rule['externalReference'] = each_rule.external_reference.strip()
            temp_rule['priority'] = each_rule.priority
            temp_rule['conditionsOperator'] = each_rule.conditions_operator.strip()
            rule_tags = list(each_rule.tags.all().values_list('tag_name', flat=True)) or []
            temp_rule['tags'] = rule_tags

            # rule actions
            rule_actions = each_rule.ruleaction_set.select_related('key').all() or []
            actions_arr = []
            for each_action in rule_actions:
                temp_action = {}
                temp_action['id'] = each_action.id
                temp_action['action'] = each_action.action.strip()
                temp_action['key'] = each_action.key.name.strip()
                temp_action['value'] = each_action.value.strip()

                if temp_action['id']:
                    actions_arr.append(temp_action)
            temp_rule['actions'] = actions_arr

            # rule conditions
            rule_conditions = each_rule.rulecondition_set.select_related('key').all() or []
            conditions_arr = []
            for each_condition in rule_conditions:
                temp_condition = {}
                temp_condition['id'] = each_condition.id
                temp_condition['operation'] = each_condition.operation.strip()
                temp_condition['key'] = each_condition.key.name.strip()
                temp_condition['value'] = each_condition.value.strip()

                if temp_condition['id']:
                    conditions_arr.append(temp_condition)
            temp_rule['conditions'] = conditions_arr

            if temp_rule.get('id'):
                rules_arr.append(temp_rule)

        output_json['rules'] = rules_arr
        return JsonResponse(output_json)
