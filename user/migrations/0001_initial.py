# Generated by Django 3.0.6 on 2020-05-22 03:50

import datetime
from django.db import migrations, models
import django.db.models.deletion

import datetime

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='오늘부터 1일', max_length=45)),
                ('energy', models.IntegerField(default=2000)),
                ('valid_date', models.DateTimeField(default=datetime.datetime(2020, 6, 21, 3, 50, 42, 207599))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'energies',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=1, max_digits=5)),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'interests',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_methods',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, null=True, unique=True)),
                ('nickname', models.CharField(max_length=200, null=True)),
                ('kakao_id', models.IntegerField(null=True, unique=True)),
                ('kakao_name', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=400, null=True)),
                ('phone_number', models.CharField(max_length=100, null=True, unique=True)),
                ('auth_number', models.IntegerField(blank=True, null=True)),
                ('coupon', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Account')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserInterestDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Interest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'users_interest_details',
            },
        ),
        migrations.CreateModel(
            name='UserHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Host')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'users_hosts',
            },
        ),
        migrations.CreateModel(
            name='UserFrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Frip')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'users_frips',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('child_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.ChildOption')),
                ('frip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Frip')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Grade')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Host')),
                ('itinerary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Itinerary')),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Option')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('child_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.ChildOption')),
                ('frip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Frip')),
                ('itinerary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Itinerary')),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frip.Option')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.PaymentMethod')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Review')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Status')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'purchases',
            },
        ),
        migrations.CreateModel(
            name='InterestDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('interest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Interest')),
            ],
            options={
                'db_table': 'interest_details',
            },
        ),
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='오늘부터 1일', max_length=45)),
                ('energy', models.IntegerField(default=2000)),
                ('valid_date', models.DateTimeField(default=datetime.datetime(2020, 6, 21, 2, 52, 31, 435316))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User')),
            ],
            options={
                'db_table': 'energies',
            },
        ),
    ]
