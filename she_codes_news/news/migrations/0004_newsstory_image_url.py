# Generated by Django 4.1.3 on 2022-12-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(default='https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1296&q=60'),
            preserve_default=False,
        ),
    ]
