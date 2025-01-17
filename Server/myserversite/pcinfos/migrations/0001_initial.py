# Generated by Django 4.1.3 on 2023-01-25 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=200)),
                ('node', models.CharField(max_length=200)),
                ('relase', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('machine', models.CharField(max_length=200)),
                ('processor', models.CharField(max_length=200)),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('mac_address', models.CharField(max_length=200)),
                ('boot_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('physical_cores', models.PositiveIntegerField(null=True)),
                ('total_cores', models.PositiveIntegerField(null=True)),
                ('max_frequency', models.FloatField(null=True)),
                ('min_frequency', models.FloatField(null=True)),
                ('current_frequency', models.FloatField(null=True)),
                ('core_usage', models.CharField(max_length=500)),
                ('total_cpu_usage', models.FloatField(null=True)),
                ('memory_total', models.CharField(max_length=100)),
                ('memory_available', models.CharField(max_length=100)),
                ('memory_used', models.CharField(max_length=100)),
                ('memory_percentage', models.FloatField(null=True)),
                ('swap_total', models.CharField(max_length=100)),
                ('swap_free', models.CharField(max_length=100)),
                ('swap_used', models.CharField(max_length=100)),
                ('swap_percentage', models.FloatField(null=True)),
                ('disk_read', models.CharField(max_length=100)),
                ('disk_write', models.CharField(max_length=100)),
                ('network_sent', models.CharField(max_length=100)),
                ('network_received', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_id', models.IntegerField(null=True)),
                ('process_name', models.CharField(max_length=300)),
                ('process_start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('process_cpu_usage', models.FloatField(null=True)),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcinfos.info')),
            ],
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=100)),
                ('mountpoint', models.CharField(max_length=100)),
                ('fstype', models.CharField(max_length=100)),
                ('total_size', models.CharField(max_length=100)),
                ('used', models.CharField(max_length=100)),
                ('free', models.CharField(max_length=100)),
                ('percentage', models.FloatField(null=True)),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcinfos.info')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu_Cores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('usage', models.FloatField(null=True)),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcinfos.info')),
            ],
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=500)),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pcinfos.info')),
            ],
        ),
    ]
