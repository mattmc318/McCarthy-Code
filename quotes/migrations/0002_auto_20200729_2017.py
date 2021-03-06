# Generated by Django 3.0.8 on 2020-07-30 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.PositiveSmallIntegerField(choices=[(0, 'Mx.'), (1, 'Ms.'), (2, 'Mrs.'), (3, 'Mr.'), (4, 'Dr.')])),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=70)),
                ('family_first', models.BooleanField()),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='quoterequest',
            name='email',
        ),
        migrations.RemoveField(
            model_name='quoterequest',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='quoterequest',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='quoterequest',
            name='phone',
        ),
        migrations.AlterField(
            model_name='quoterequest',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AddField(
            model_name='quoterequest',
            name='contact',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.Contact'),
            preserve_default=False,
        ),
    ]
