# Django-მ ავტომატურად შექმნა (ვერსია 6.1.2), 2026-11-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.CharField(blank=True, max_length=300, verbose_name='სურათის ფაილი'),
        ),
    ]
