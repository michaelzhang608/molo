# -*- coding: utf-8 -*-
# flake8: noqa: E128
# Generated by Django 1.9.9 on 2016-10-23 12:29
from __future__ import unicode_literals

from django.db import migrations
from django.core.management.sql import emit_post_migrate_signal


def add_core_permissions_to_groups(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    try:
        # Django 1.9
        emit_post_migrate_signal(2, False, db_alias)
    except TypeError:
        # Django < 1.9
        try:
            # Django 1.8
            emit_post_migrate_signal(2, False, 'default', db_alias)
        except TypeError:  # Django < 1.8
            emit_post_migrate_signal([], 2, False, 'default', db_alias)

    Group = apps.get_model('auth.Group')
    Permission = apps.get_model('auth.Permission')
    GroupPagePermission = apps.get_model('wagtailcore.GroupPagePermission')
    BannerIndexPage = apps.get_model('core.BannerIndexPage')
    SectionIndexPage = apps.get_model('core.SectionIndexPage')
    FooterIndexPage = apps.get_model('core.FooterIndexPage')

    if Group.objects.all().filter(name='Writer and Content Loader'):
        Group.objects.get(name='Writer and Content Loader').delete()

    if Group.objects.all().filter(name='Publisher'):
        Group.objects.get(name='Publisher').delete()

    # Create groups
    access_admin = Permission.objects.get(codename='access_admin')

    # <- Wagtail Login Only ->
    wagtail_login_only_group, _created = Group.objects.get_or_create(
        name='Wagtail Login Only')
    wagtail_login_only_group.permissions.add(access_admin)

    # <- Editors ->
    editor_group = Group.objects.get(name='Editors')

    # Remove the existing page permissions
    editor_group.page_permissions.all().delete()

    # Add page permissions
    sections = SectionIndexPage.objects.first()
    GroupPagePermission.objects.get_or_create(
        group=editor_group,
        page=sections,
        permission_type='add',
    )
    GroupPagePermission.objects.get_or_create(
        group=editor_group,
        page=sections,
        permission_type='edit',
    )

    banners = BannerIndexPage.objects.first()
    GroupPagePermission.objects.get_or_create(
        group=editor_group,
        page=banners,
        permission_type='add',
    )
    GroupPagePermission.objects.get_or_create(
        group=editor_group,
        page=banners,
        permission_type='edit',
    )

    add_sitelanguage = Permission.objects.get(codename='add_sitelanguage')
    editor_group.permissions.add(add_sitelanguage)

    # <- Moderator ->

    moderator_group = Group.objects.get(name='Moderators')

    add_sitelanguage = Permission.objects.get(codename='add_sitelanguage')
    change_sitelanguage = Permission.objects.get(
        codename='change_sitelanguage')
    change_user = Permission.objects.get(
        codename='change_user')
    moderator_group.permissions.add(add_sitelanguage, change_sitelanguage,
        change_user)

    moderator_group.page_permissions.all().delete()
    sections = SectionIndexPage.objects.first()
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=sections,
        permission_type='add',
    )
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=sections,
        permission_type='edit',
    )
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=sections,
        permission_type='publish',
    )

    banners = BannerIndexPage.objects.first()
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=banners,
        permission_type='add',
    )
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=banners,
        permission_type='edit',
    )
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=banners,
        permission_type='publish',
    )

    footers = FooterIndexPage.objects.first()
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=footers,
        permission_type='add',
    )
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=footers,
        permission_type='edit',
    )
    GroupPagePermission.objects.get_or_create(
        group=moderator_group,
        page=footers,
        permission_type='publish',
    )


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0046_sitesettings_enable_clickable_tags'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailadmin', '0001_create_admin_access_permissions'),
        ('wagtailusers', '0005_make_related_name_wagtail_specific'),
        ('sites', '0002_alter_domain_unique'),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.RunPython(add_core_permissions_to_groups),
    ]
