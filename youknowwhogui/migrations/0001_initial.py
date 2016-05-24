# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, help_text='For personal reference. Not used anywhere in logic', blank=True)),
                ('external_reference', models.CharField(blank=True, max_length=255)),
                ('status', models.IntegerField(default=1, choices=[(1, 'Enabled'), (0, 'Disabled')])),
                ('priority', models.IntegerField(null=True, help_text='Priority 1 is highest. Lower the number higher the priority.', blank=True)),
                ('conditions_operator', models.CharField(default='&&', choices=[('&&', 'AND ( && )'), ('||', 'OR ( || )')], help_text='Please select if rule conditions should be ANDed or ORed.. By default AND is selected', blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'permissions': (('CAN_ENABLE_RULE', 'Can Enable rule'), ('CAN_DISABLE_RULE', 'Can Disable rule')),
                'managed': True,
                'db_table': 'rule',
            },
        ),
        migrations.CreateModel(
            name='RuleAction',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(null=True, help_text='For personal reference. Not used anywhere in logic', blank=True)),
                ('action', models.CharField(choices=[('SET_VARIABLE', 'Set Variable'), ('DANGEROUS_EVAL', 'Evaluate')], max_length=255)),
                ('value', models.TextField(null=True, help_text='Can have STRING ( TEMPLATED or NORMAL), BOOLEAN                             E.g.  true, false are boolean values .                             Almost all message properties can be used as variables                             like <%= userdata.amount %> <%= userdata.recharge_number %>', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'rule_action',
            },
        ),
        migrations.CreateModel(
            name='RuleActionKeys',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, max_length=255)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Rule Action Keys',
                'db_table': 'rule_action_keys',
            },
        ),
        migrations.CreateModel(
            name='RuleCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(db_column='description', null=True, help_text='For personal reference. Not used anywhere in logic', blank=True)),
                ('condition', models.CharField(default='checkvariable', choices=[('checkvariable', 'Check Variable')], max_length=255)),
                ('operation', models.CharField(choices=[('=', 'Equals ( = )'), ('!=', 'Not Equals ( != )'), ('>', 'Great than Integer ( > )'), ('>=', 'Great than Equals Integer( >= )'), ('<', 'Less than Integer( < )'), ('<=', 'Less than Equals Integer( <= )'), ('range', 'In Numerical Range ( range )'), ('!range', 'Not In Numerical Range ( !range )'), ('datetimerange', 'In DateTime Range ( datetimerange )'), ('!datetimerange', 'Not In DateTime Range ( !datetimerange )'), ('timerange', 'In Time Range ( timerange )'), ('!timerange', 'Not In Time Range ( !timerange )'), ('regex', 'In Regex ( regex )'), ('!regex', 'Not In Regex ( !regex )'), ('stringrange', 'In String Array ( stringrange )'), ('!stringrange', 'Not In String Array ( !stringrange )'), ('set', 'Is In Set(set)'), ('!set', 'Is Not In Set(!set)')], max_length=255)),
                ('value', models.TextField(help_text='Different values for different operations.                             Such as range can have numerical ranges like 1,2,4~5, 6~10,11,12~ .                             datetimerange can have range like 2015-06-11 ~ 2015-07-12 .')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'rule_condition',
            },
        ),
        migrations.CreateModel(
            name='RuleConditionKeys',
            fields=[
                ('name', models.CharField(primary_key=True, serialize=False, max_length=255)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Rule Condition Keys',
                'db_table': 'rule_condition_keys',
            },
        ),
        migrations.CreateModel(
            name='RuleTag',
            fields=[
                ('tag_name', models.CharField(primary_key=True, serialize=False, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'rule_tag',
            },
        ),
        migrations.AddField(
            model_name='rulecondition',
            name='key',
            field=models.ForeignKey(blank=True, db_column='key', null=True, to='ruleengine.RuleConditionKeys'),
        ),
        migrations.AddField(
            model_name='rulecondition',
            name='rule',
            field=models.ForeignKey(to='ruleengine.Rule'),
        ),
        migrations.AddField(
            model_name='ruleaction',
            name='key',
            field=models.ForeignKey(blank=True, db_column='key', null=True, to='ruleengine.RuleActionKeys'),
        ),
        migrations.AddField(
            model_name='ruleaction',
            name='rule',
            field=models.ForeignKey(to='ruleengine.Rule'),
        ),
        migrations.AddField(
            model_name='rule',
            name='tags',
            field=models.ManyToManyField(db_table='rule_ruletag', to='ruleengine.RuleTag', blank=True),
        ),
    ]
