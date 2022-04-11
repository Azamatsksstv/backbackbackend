# Generated by Django 4.0.2 on 2022-04-04 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductParametrName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_names', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductParametrValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parameter_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_value', to='store.productparametrname')),
            ],
        ),
    ]
