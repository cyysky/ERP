# Generated by Django 4.0.4 on 2022-07-21 11:36

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
                ('BOMID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('BOM_Level', models.CharField(default='', max_length=150)),
                ('ProductID', models.CharField(default='', max_length=150)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('MaterialID', models.CharField(default='', max_length=150)),
                ('material_name', models.CharField(default='', max_length=150)),
                ('source', models.CharField(default='', max_length=150)),
                ('UOM', models.TextField()),
                ('usage', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('remarks', models.CharField(default='', max_length=150)),
                ('amount', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'bom',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=150)),
                ('address_ship', models.TextField()),
                ('address_sold', models.TextField()),
                ('address_bill', models.TextField()),
                ('term', models.TextField()),
                ('email', models.EmailField(max_length=150)),
                ('phone1', models.IntegerField()),
                ('phone2', models.IntegerField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ea0', models.CharField(default='', max_length=150)),
                ('ea1', models.CharField(default='', max_length=150)),
                ('ea2', models.CharField(default='', max_length=150)),
                ('ea3', models.CharField(default='', max_length=150)),
                ('ea4', models.CharField(default='', max_length=150)),
                ('ea5', models.CharField(default='', max_length=150)),
                ('ea6', models.CharField(default='', max_length=150)),
                ('ea7', models.CharField(default='', max_length=150)),
                ('ea8', models.CharField(default='', max_length=150)),
                ('ea9', models.CharField(default='', max_length=150)),
                ('ea10', models.CharField(default='', max_length=150)),
                ('ea11', models.CharField(default='', max_length=150)),
                ('ea12', models.CharField(default='', max_length=150)),
            ],
            options={
                'db_table': 'history',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('MachineID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('machine_name', models.CharField(default='', max_length=150)),
                ('unit_price', models.IntegerField(verbose_name=150)),
            ],
            options={
                'db_table': 'machine',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('MaterialID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('material_name', models.CharField(default='', max_length=150)),
                ('measure_unit', models.CharField(default='', max_length=150)),
                ('tybe', models.CharField(default='', max_length=150)),
                ('Form', models.CharField(default='', max_length=150)),
                ('thickness', models.CharField(default='', max_length=150)),
                ('width', models.CharField(default='', max_length=150)),
                ('length', models.CharField(default='', max_length=150)),
                ('pltch', models.CharField(default='', max_length=150)),
                ('default_stock_locatiuon', models.CharField(default='', max_length=150)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
            ],
            options={
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='Material_Supplier',
            fields=[
                ('MaterialSupplierID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('material_name', models.CharField(default='', max_length=150)),
                ('source', models.IntegerField()),
                ('UOM', models.IntegerField()),
                ('EOQ', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('term', models.IntegerField()),
                ('remarks', models.CharField(default='', max_length=150)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
            ],
            options={
                'db_table': 'material_supplier',
            },
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('PackagingID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('packaging_name', models.CharField(default='', max_length=150)),
                ('packaging_unit', models.CharField(default='', max_length=150)),
                ('packaging_type', models.CharField(default='', max_length=150)),
                ('size', models.CharField(default='', max_length=150)),
                ('heigh', models.CharField(default='', max_length=150)),
                ('width', models.CharField(default='', max_length=150)),
                ('length', models.CharField(default='', max_length=150)),
                ('color', models.CharField(default='', max_length=150)),
                ('model', models.CharField(default='', max_length=150)),
                ('packaging_location', models.CharField(default='', max_length=150)),
                ('quantity', models.CharField(default='', max_length=150)),
                ('product_company', models.CharField(default='', max_length=150)),
                ('defaul_stock_location', models.CharField(default='', max_length=150)),
            ],
            options={
                'db_table': 'packaging',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('product_group', models.CharField(default='', max_length=150)),
                ('product_tooling', models.CharField(default='', max_length=150)),
                ('product_unit', models.CharField(default='', max_length=150)),
                ('BOM_Level', models.CharField(default='', max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(verbose_name=150)),
                ('product_type', models.CharField(default='', max_length=150)),
                ('unit_price', models.IntegerField(verbose_name=150)),
                ('start_time', models.CharField(default='', max_length=150)),
                ('finish_time', models.CharField(default='', max_length=150)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProjectID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('project_name', models.CharField(default='', max_length=150)),
                ('customerpart_id', models.CharField(default='', max_length=150)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('quantity', models.IntegerField(verbose_name=150)),
                ('unitprice', models.IntegerField(verbose_name=150)),
                ('project_date', models.IntegerField()),
                ('term', models.CharField(default='', max_length=150)),
                ('start_time', models.CharField(default='', max_length=150)),
                ('finish_time', models.CharField(default='', max_length=150)),
                ('DeliveryDatetime', models.CharField(default='', max_length=150)),
                ('CustomerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.customer')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.product')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('ResourceID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('reesource_name', models.CharField(default='', max_length=150)),
                ('remarks', models.CharField(default='', max_length=150)),
            ],
            options={
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SupplierID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(default='', max_length=150)),
                ('supplier_type', models.CharField(default='', max_length=150)),
                ('address', models.TextField()),
                ('term', models.TextField()),
                ('email', models.CharField(default='', max_length=150)),
                ('phone1', models.IntegerField(verbose_name=150)),
                ('phone2', models.IntegerField(verbose_name=150)),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('SalesID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(default='', max_length=150)),
                ('term', models.TextField()),
                ('customer_po_id', models.CharField(default='', max_length=150)),
                ('description', models.CharField(default='', max_length=150)),
                ('quantity', models.CharField(default='', max_length=150)),
                ('unit_price', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_time', models.CharField(default='', max_length=150)),
                ('finish_time', models.CharField(default='', max_length=150)),
                ('CustomerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.customer')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.product')),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='Require',
            fields=[
                ('RequireID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('material_name', models.CharField(default='', max_length=150)),
                ('project_name', models.CharField(default='', max_length=150)),
                ('material_supplier_name', models.CharField(default='', max_length=150)),
                ('quantity', models.CharField(default='', max_length=150)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
                ('MaterialSupplierID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material_supplier')),
                ('ProjectID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.project')),
            ],
            options={
                'db_table': 'require',
            },
        ),
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('ReceiveID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('grade', models.CharField(default='', max_length=150)),
                ('size', models.CharField(default='', max_length=150)),
                ('usage', models.CharField(default='', max_length=150)),
                ('quantity', models.CharField(default='', max_length=150)),
                ('remarks', models.CharField(default='', max_length=150)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
                ('SupplierID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.supplier')),
            ],
            options={
                'db_table': 'receive',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('PurchaseID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('purchase_name', models.CharField(default='', max_length=150)),
                ('deliver_date', models.CharField(default='', max_length=150)),
                ('material_name', models.CharField(default='', max_length=150)),
                ('quantity', models.CharField(default='', max_length=150)),
                ('unit_price', models.CharField(default='', max_length=150)),
                ('discount', models.CharField(default='', max_length=150)),
                ('total_MYR', models.CharField(default='', max_length=150)),
                ('remarks', models.CharField(default='', max_length=150)),
                ('MaterialSupplierID', models.CharField(default='', max_length=150)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
                ('RequireID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.require')),
            ],
            options={
                'db_table': 'purchase',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='SalesID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.sales'),
        ),
        migrations.CreateModel(
            name='Product_Reject',
            fields=[
                ('RejectbatchID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('type', models.TextField()),
                ('quantity', models.CharField(default='', max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.product')),
            ],
            options={
                'db_table': 'product_reject',
            },
        ),
        migrations.CreateModel(
            name='Product_Material',
            fields=[
                ('ProductID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('usage', models.CharField(default='', max_length=150)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
            ],
            options={
                'db_table': 'product_material',
            },
        ),
        migrations.CreateModel(
            name='Product_Good',
            fields=[
                ('GoodbatchID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('type', models.TextField()),
                ('quantity', models.CharField(default='', max_length=150)),
                ('term', models.CharField(default='', max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('CustomerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.customer')),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.product')),
            ],
            options={
                'db_table': 'product_good',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('ProcessID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('process_name', models.CharField(default='', max_length=150)),
                ('process_tooling', models.CharField(default='', max_length=150)),
                ('start_time', models.CharField(default='', max_length=150)),
                ('finish_time', models.CharField(default='', max_length=150)),
                ('duration', models.CharField(default='', max_length=150)),
                ('quanitiy', models.IntegerField(default='')),
                ('unit_price', models.IntegerField(default='')),
                ('cost', models.IntegerField(default='')),
                ('total', models.IntegerField(default='')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.product')),
                ('ProjectID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.project')),
                ('ResourceID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.resource')),
            ],
            options={
                'db_table': 'process',
            },
        ),
        migrations.AddField(
            model_name='material_supplier',
            name='SupplierID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.supplier'),
        ),
        migrations.CreateModel(
            name='Material_Stock',
            fields=[
                ('MaterialStockID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('material_name', models.CharField(default='', max_length=150)),
                ('material_location_id', models.CharField(default='', max_length=150)),
                ('shelf_id', models.CharField(default='', max_length=150)),
                ('quantity', models.IntegerField(verbose_name=150)),
                ('MaterialID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.material')),
            ],
            options={
                'db_table': 'material_stock',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('DeliveryID', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('sales_name', models.CharField(default='', max_length=150)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('quantity', models.CharField(default='', max_length=150)),
                ('unitprice', models.CharField(default='', max_length=150)),
                ('term', models.TextField()),
                ('DeliveryDatetime', models.CharField(default='', max_length=150)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('CustomerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.customer')),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.product')),
                ('SalesID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ERPSystem.sales')),
            ],
            options={
                'db_table': 'delivery',
            },
        ),
    ]
