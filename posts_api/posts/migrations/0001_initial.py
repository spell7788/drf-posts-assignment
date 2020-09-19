# Generated by Django 3.1.1 on 2020-09-19 13:49

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='author name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('title', models.CharField(help_text='Post title.', max_length=100, verbose_name='title')),
                ('link', models.URLField(help_text='Post link.', verbose_name='link')),
                ('upvotes_number', models.PositiveSmallIntegerField(help_text='The number of post upvotes.', verbose_name='upvotes number')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='author name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('content', models.CharField(help_text='Comment content.', max_length=250, verbose_name='content')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='Parent comment.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='posts.comment', verbose_name="comment's parent")),
                ('post', models.ForeignKey(help_text='Related post.', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post', verbose_name="comment's post")),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]