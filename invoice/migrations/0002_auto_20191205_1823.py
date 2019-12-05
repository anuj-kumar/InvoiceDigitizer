# Generated by Django 2.2.8 on 2019-12-05 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.Buyer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(blank=True, choices=[('INR', 'Indian Rupee'), ('USD', 'US Dollar')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='generated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='invoice.Item'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.Vendor'),
        ),
    ]
