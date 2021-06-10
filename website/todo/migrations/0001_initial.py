# Generated by Django 3.2.3 on 2021-06-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='할일제목')),
                ('description', models.TextField(max_length=200, verbose_name='할일세부사항')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='생성날짜')),
                ('date_deadline', models.DateField(verbose_name='데드라인')),
            ],
        ),
    ]