# Generated by Django 2.0 on 2017-12-17 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_auto_20170927_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by', to='deploy.Creeper'),
        ),
    ]
