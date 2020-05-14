# Generated by Django 3.0.5 on 2020-05-11 07:05

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
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
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('has_confirmed', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('customer', '顾客'), ('finance', '财务'), ('HR', '人事'), ('purchase', '采购'), ('repair', '维修'), ('sale', '销售'), ('storage', '仓库')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-c_time'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Touch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('status', models.CharField(blank=True, choices=[('done', '已联系'), ('undo', '未联系')], max_length=5, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceWorker',
            fields=[
                ('wid', models.OneToOneField(db_column='wid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='welcome.Worker')),
                ('wname', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('postion', models.CharField(max_length=20)),
                ('workload', models.DecimalField(blank=True, decimal_places=1, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'maintenance_worker',
            },
        ),
        migrations.CreateModel(
            name='ServiceWorker',
            fields=[
                ('wid', models.OneToOneField(db_column='wid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='welcome.Worker')),
                ('wname', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('postion', models.CharField(max_length=20)),
                ('order_finish', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service_worker',
            },
        ),
        migrations.CreateModel(
            name='WorkerArrange',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timeatwork', models.DateTimeField()),
                ('appostate', models.CharField(blank=True, max_length=20, null=True)),
                ('wid', models.ForeignKey(blank=True, db_column='wid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='welcome.Worker')),
            ],
            options={
                'db_table': 'worker_arrange',
                'unique_together': {('wid', 'timeatwork')},
            },
        ),
        migrations.CreateModel(
            name='PsdConfirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('cgender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], max_length=10, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('caddress', models.CharField(blank=True, max_length=60, null=True)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(max_length=20)),
                ('ctype', models.CharField(max_length=20)),
                ('inventory', models.IntegerField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('describe', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='carimage/', verbose_name='配图')),
            ],
            options={
                'db_table': 'car_info',
                'unique_together': {('band', 'ctype')},
            },
        ),
        migrations.CreateModel(
            name='AppoInfo',
            fields=[
                ('appoid', models.AutoField(primary_key=True, serialize=False)),
                ('appocontent', models.CharField(blank=True, max_length=20, null=True)),
                ('cusno', models.ForeignKey(blank=True, db_column='cusno', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='welcome.Customer')),
                ('id', models.ForeignKey(blank=True, db_column='id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='App_id', to='welcome.WorkerArrange')),
            ],
            options={
                'db_table': 'appo_info',
            },
        ),
    ]
