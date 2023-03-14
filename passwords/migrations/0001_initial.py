# Generated by Django 4.1 on 2023-03-14 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Password URL',
                'verbose_name_plural': 'Password URLs',
            },
        ),
        migrations.CreateModel(
            name='PasswordEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid_for_password', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('note', models.TextField(blank=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='passwords.passwordurl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Password Entry',
                'verbose_name_plural': 'Password Entries',
            },
        ),
    ]