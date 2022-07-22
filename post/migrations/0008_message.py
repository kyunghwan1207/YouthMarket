# Generated by Django 3.2.13 on 2022-07-22 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('idx', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='idx')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_message', to='post.user', verbose_name='저자')),
                ('chatroomIdx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatroom_message', to='post.chatroom', verbose_name='채팅방idx')),
            ],
        ),
    ]
