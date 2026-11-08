# Django-მ ავტომატურად შექმნა (ვერსია 6.1.2), 2026-10-26 16:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='დასახელება')),
            ],
            options={
                'verbose_name': 'კატეგორია',
                'verbose_name_plural': 'კატეგორიები',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='დასახელება')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='ფასი')),
                ('image', models.URLField(blank=True, max_length=300, verbose_name='სურათის ბმული')),
                ('spiciness', models.PositiveSmallIntegerField(default=0, help_text='0 - არ არის ცხარე, 4 - ძალიან ცხარე', validators=[django.core.validators.MaxValueValidator(4)], verbose_name='სიცხარე')),
                ('nuts', models.BooleanField(default=False, verbose_name='ნიგვზიანი')),
                ('vegetarian', models.BooleanField(default=False, verbose_name='ვეგეტარიანული')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dishes', to='menu.category', verbose_name='კატეგორია')),
            ],
            options={
                'verbose_name': 'კერძი',
                'verbose_name_plural': 'კერძები',
                'ordering': ['category', 'id'],
            },
        ),
    ]
