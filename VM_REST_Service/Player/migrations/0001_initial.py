# Generated by Django 2.2.6 on 2019-10-24 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GameMap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='User name')),
                ('playerclass', models.CharField(choices=[('Knight', 'Knight'), ('Wizard', 'Wizard'), ('Thief', 'Thief'), ('Paladin', 'Paladin')], default='Knight', max_length=15, verbose_name='Class')),
                ('email', models.CharField(blank=True, max_length=50, verbose_name='Email')),
                ('level', models.IntegerField(default=0, verbose_name='Player level')),
                ('position', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='GameMap.Location')),
            ],
        ),
    ]
