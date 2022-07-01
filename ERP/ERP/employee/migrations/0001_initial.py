# Generated by Django 4.0.4 on 2022-06-30 02:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bom_id', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('material_id', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bom',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone1', models.IntegerField(verbose_name=100000)),
                ('phone2', models.IntegerField(verbose_name=100000)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_id', models.CharField(max_length=100)),
                ('sales_name', models.CharField(max_length=100)),
                ('custiomer_id', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('unitprice', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'delivery',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ea0', models.CharField(max_length=100)),
                ('ea1', models.CharField(max_length=100)),
                ('ea2', models.CharField(max_length=100)),
                ('ea3', models.CharField(max_length=100)),
                ('ea4', models.CharField(max_length=100)),
                ('ea5', models.CharField(max_length=100)),
                ('ea6', models.CharField(max_length=100)),
                ('ea7', models.CharField(max_length=100)),
                ('ea8', models.CharField(max_length=100)),
                ('ea9', models.CharField(max_length=100)),
                ('ea10', models.CharField(max_length=100)),
                ('ea11', models.CharField(max_length=100)),
                ('ea12', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'history',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machine_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=100)),
                ('unit_price', models.IntegerField(verbose_name=100000)),
            ],
            options={
                'db_table': 'machine',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('material_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_supplier', models.CharField(max_length=100)),
                ('measure_unit', models.CharField(max_length=100)),
                ('tybe', models.CharField(max_length=100)),
                ('Form', models.CharField(max_length=100)),
                ('thickness', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=100)),
                ('pltch', models.CharField(max_length=100)),
                ('default_stock_locatiuon', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('nit_price', models.IntegerField(verbose_name=1000)),
            ],
            options={
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packaging_id', models.CharField(max_length=100)),
                ('packaging_name', models.CharField(max_length=100)),
                ('packaging_unit', models.CharField(max_length=100)),
                ('packaging_type', models.CharField(max_length=100)),
                ('packaging_size', models.CharField(max_length=100)),
                ('packaging_heigh', models.CharField(max_length=100)),
                ('packaging_width', models.CharField(max_length=100)),
                ('packaging_length', models.CharField(max_length=100)),
                ('packaging_color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('packaging_location', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('product_company', models.CharField(max_length=100)),
                ('defaul_stock_location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'packaging',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('process_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=100)),
                ('resource_id', models.CharField(max_length=100)),
                ('project_id', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'process',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_group', models.CharField(max_length=100)),
                ('product_tooling', models.CharField(max_length=100)),
                ('product_unit', models.CharField(max_length=100)),
                ('materil_id', models.CharField(max_length=100)),
                ('material_usage', models.CharField(max_length=100)),
                ('process_id', models.CharField(max_length=100)),
                ('bom_id', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(verbose_name=100000)),
                ('product_type', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('finish_time', models.CharField(max_length=100)),
                ('unit_price', models.IntegerField(verbose_name=100000)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Product_Good',
            fields=[
                ('goodbatch_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name=100000)),
                ('product_name', models.CharField(max_length=100)),
                ('customer_id', models.IntegerField(verbose_name=100000)),
                ('type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(verbose_name=100000)),
                ('term', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('material_id', models.IntegerField(verbose_name=100000)),
            ],
            options={
                'db_table': 'product_good',
            },
        ),
        migrations.CreateModel(
            name='Product_Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name=100000)),
                ('material_id', models.IntegerField(verbose_name=100000)),
                ('usage', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product_material',
            },
        ),
        migrations.CreateModel(
            name='Product_Reject',
            fields=[
                ('rejectbatch_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(verbose_name=100000)),
                ('product_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(verbose_name=100000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('material_id', models.IntegerField(verbose_name=100000)),
            ],
            options={
                'db_table': 'product_reject',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('sales_id', models.CharField(max_length=100)),
                ('customer_id', models.CharField(max_length=100)),
                ('customerpart_id', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(verbose_name=100000)),
                ('unitprice', models.IntegerField(verbose_name=100000)),
                ('term', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('finish_time', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone1', models.IntegerField(verbose_name=100000)),
                ('phone2', models.IntegerField(verbose_name=100000)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sales_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('term', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.CharField(max_length=100)),
                ('finish_time', models.CharField(max_length=100)),
                ('customer_po_id', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('unit_price', models.IntegerField(verbose_name=100000)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.product')),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='Material_Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(max_length=100)),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.supplier')),
            ],
            options={
                'db_table': 'material_supplier',
            },
        ),
        migrations.CreateModel(
            name='Material_Location',
            fields=[
                ('material_location_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_id', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(verbose_name=100000)),
                ('material_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.material')),
            ],
            options={
                'db_table': 'material_location',
            },
        ),
    ]