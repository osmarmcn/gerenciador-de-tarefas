# Generated by Django 5.0.4 on 2024-05-04 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('criar_atividade', models.DateTimeField(auto_now_add=True)),
                ('prazo_final', models.DateTimeField()),
                ('finalziar_atividade', models.DateTimeField()),
            ],
        ),
    ]
