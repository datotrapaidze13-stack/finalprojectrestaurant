# Django-მ ავტომატურად შექმნა (ვერსია 6.1.2), 2026-11-01 09:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='რაოდენობა')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.dish', verbose_name='კერძი')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='მომხმარებელი')),
            ],
            options={
                'verbose_name': 'კალათის ჩანაწერი',
                'verbose_name_plural': 'კალათის ჩანაწერები',
                'ordering': ['id'],
            },
        ),
    ]
