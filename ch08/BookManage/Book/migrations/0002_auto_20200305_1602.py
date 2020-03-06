# Generated by Django 3.0.4 on 2020-03-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfoManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]