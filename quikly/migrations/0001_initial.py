# Generated by Django 2.0.3 on 2018-03-10 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_model', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(decimal_places=5, default=0, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=5, default=0, max_digits=9)),
                ('status', models.CharField(choices=[('Not_Available', 'Not_Available'), ('Available', 'Available')], default='Not_Available', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='QuiklyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('LogIn', 'LogIn'), ('LogOut', 'LogOut')], default='LogOut', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cycles',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_cycle', to='quikly.QuiklyUser'),
        ),
    ]
