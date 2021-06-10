# Generated by Django 3.1.7 on 2021-06-03 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0005_auto_20210603_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_VideoInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='VideoInformation',
        ),
        migrations.AddField(
            model_name='dataaboutuserandvideo',
            name='time_emo',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='dataaboutuserandvideo',
            name='ID_video_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.db_videoinformation'),
        ),
    ]