# Generated by Django 5.0.6 on 2024-05-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
