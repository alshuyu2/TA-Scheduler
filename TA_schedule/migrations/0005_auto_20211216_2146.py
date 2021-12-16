# Generated by Django 3.2.8 on 2021-12-16 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TA_schedule', '0004_personalinfo_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classtolab',
            name='class_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_schedule.class'),
        ),
        migrations.AlterField(
            model_name='classtolab',
            name='lab_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_schedule.lab'),
        ),
        migrations.AlterField(
            model_name='tatoclass',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TA_schedule.class'),
        ),
        migrations.AlterField(
            model_name='tatoclass',
            name='ta_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
