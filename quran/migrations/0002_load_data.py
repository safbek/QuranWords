# Generated by Django 2.1 on 2018-09-08 09:13

from os import path
from django.db import migrations
from django.core.management import call_command

fixture_dir = path.abspath(
    path.join(path.dirname(__file__), '../fixtures/'))
fixture_surahs = 'surah_list.json'
fixture_ayahs = 'ayah_list.json'


def load_surahs(apps, schema_editor):
    fixture_file = path.join(fixture_dir, fixture_surahs)
    call_command('loaddata', fixture_file)


def unload_surahs(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    Surah = apps.get_model("quran", "Surah")
    Surah.objects.all().delete()


def load_ayahs(apps, schema_editor):
    fixture_file = path.join(fixture_dir, fixture_ayahs)
    call_command('loaddata', fixture_file)


def unload_ayahs(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    Ayah = apps.get_model("quran", "Ayah")
    Ayah.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_surahs, reverse_code=unload_surahs),
        migrations.RunPython(load_ayahs, reverse_code=unload_ayahs),
    ]
