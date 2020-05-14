# Generated by Django 3.0.5 on 2020-05-11 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppoInfo',
            fields=[
                ('appoid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('appocontent', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'appo_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('remainnum', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'batch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('cid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('real_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('band', models.CharField(max_length=20)),
                ('ctype', models.CharField(max_length=20)),
                ('inventory', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('describe', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'car_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarShortage',
            fields=[
                ('car_shortage_id', models.CharField(db_column='Car_shortage_id', max_length=20, primary_key=True, serialize=False)),
                ('ct_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'car_shortage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('coid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('coname', models.CharField(blank=True, max_length=30, null=True)),
                ('cotype', models.CharField(blank=True, max_length=20, null=True)),
                ('conumber', models.IntegerField(blank=True, null=True)),
                ('coprice', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
            options={
                'db_table': 'components',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusno', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('cgender', models.CharField(max_length=4)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('caddress', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FaultInfo',
            fields=[
                ('faultinfoid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('renum', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fault_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FaultList',
            fields=[
                ('faultid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('faultname', models.CharField(max_length=30)),
                ('Fa_id', models.CharField(max_length=30, null=True)),
                ('eload', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'fault_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('oid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ostate', models.CharField(blank=True, max_length=20, null=True)),
                ('sumprice', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('ostime', models.DateTimeField(blank=True, null=True)),
                ('oftime', models.DateTimeField(blank=True, null=True)),
                ('return_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pickuplist',
            fields=[
                ('pickid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('license', models.CharField(blank=True, max_length=20, null=True)),
                ('pickstate', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'pickuplist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchaseid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('purchasenum', models.IntegerField(blank=True, null=True)),
                ('purchasestate', models.CharField(blank=True, max_length=20, null=True)),
                ('warehouse_time', models.DateTimeField(blank=True, null=True)),
                ('psumprice', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('ptime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'purchase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('wid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('wname', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('postion', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'worker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkerArrange',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timeatwork', models.DateTimeField()),
                ('appostate', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'worker_arrange',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Worksheet',
            fields=[
                ('wsid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('wsstate', models.CharField(blank=True, max_length=20, null=True)),
                ('repeatnum', models.IntegerField(blank=True, null=True)),
                ('wsftime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'worksheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorksheetCompoInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'worksheet_compo_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CarPurchase',
            fields=[
                ('purchaseid', models.OneToOneField(db_column='purchaseid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Sale.Purchase')),
                ('purchasenum', models.IntegerField(blank=True, null=True)),
                ('purchasestate', models.CharField(blank=True, max_length=20, null=True)),
                ('psumprice', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('ptime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'car_purchase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompoUseInfo',
            fields=[
                ('wsid', models.OneToOneField(db_column='wsid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Sale.Worksheet')),
                ('compo_use_state', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'compo_use_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaintenanceWorker',
            fields=[
                ('wid', models.OneToOneField(db_column='wid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Sale.Worker')),
                ('wname', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('postion', models.CharField(max_length=20)),
                ('workload', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'maintenance_worker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceWorker',
            fields=[
                ('wid', models.OneToOneField(db_column='wid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Sale.Worker')),
                ('wname', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('postion', models.CharField(max_length=20)),
                ('order_finish', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service_worker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoPurchase',
            fields=[
                ('purchaseid', models.OneToOneField(db_column='purchaseid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Sale.Purchase')),
                ('purchasenum', models.IntegerField(blank=True, null=True)),
                ('purchasestate', models.CharField(blank=True, max_length=20, null=True)),
                ('warehouse_time', models.DateTimeField(blank=True, null=True)),
                ('psumprice', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('ptime', models.DateTimeField(blank=True, null=True)),
                ('coid', models.ForeignKey(blank=True, db_column='coid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Sale.Components')),
            ],
            options={
                'db_table': 'co_purchase',
                'managed': True,
            },
        ),
    ]
