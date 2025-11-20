# Generated manually on 2025-11-20 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20251120_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model_name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='backend.cardetails'),
        ),
    ]

