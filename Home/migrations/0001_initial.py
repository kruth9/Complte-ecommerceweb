# Generated by Django 4.2.1 on 2023-06-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, null=True, upload_to='image/')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('Price', models.TextField()),
            ],
        ),
    ]
