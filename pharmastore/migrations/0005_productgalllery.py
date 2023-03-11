# Generated by Django 4.1.1 on 2023-02-04 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmastore', '0004_reviewrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGalllery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=255, upload_to='store/products/<django.db.models.fields.related.ForeignKey>')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pharmastore.product')),
            ],
        ),
    ]