# Generated by Django 2.1.3 on 2018-11-16 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FieldChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FieldImplementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('text', 'Text Field'), ('integer', 'Number Field'), ('date', 'Date Field'), ('enum', 'Enum Field')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('is_forced', models.BooleanField(default=False)),
                ('regular_expression', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='fieldimplementation',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.RiskType'),
        ),
        migrations.AddField(
            model_name='fieldchoice',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.FieldImplementation'),
        ),
    ]
