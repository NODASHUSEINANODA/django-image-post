# Generated by Django 2.2.20 on 2022-10-15 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_followerships', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee_followerships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('follower', 'followee')},
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(related_name='_customuser_followers_+', through='accounts.Followership', to=settings.AUTH_USER_MODEL, verbose_name='フォロワー'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='follows',
            field=models.ManyToManyField(related_name='_customuser_follows_+', through='accounts.Followership', to=settings.AUTH_USER_MODEL, verbose_name='フォロー'),
        ),
    ]
