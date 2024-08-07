# Generated by Django 5.0.6 on 2024-05-27 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HuggingFaceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_path', models.CharField(max_length=200)),
                ('upd_date', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='AmazonLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.IntegerField(default=0)),
                ('cat_name', models.CharField(max_length=64)),
                ('svg_str', models.CharField(default='nothing', max_length=3000)),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AmazonProductReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewText', models.CharField(max_length=1500)),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transformer.amazonlabels')),
            ],
        ),
        migrations.CreateModel(
            name='ModelInfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_los', models.DecimalField(decimal_places=12, max_digits=15)),
                ('train_acc', models.DecimalField(decimal_places=12, max_digits=15)),
                ('val_los', models.DecimalField(decimal_places=12, max_digits=15)),
                ('val_acc', models.DecimalField(decimal_places=12, max_digits=15)),
                ('test_los', models.DecimalField(decimal_places=12, max_digits=15)),
                ('test_acc', models.DecimalField(decimal_places=12, max_digits=15)),
                ('model_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transformer.huggingfacemodel')),
            ],
        ),
    ]
