# Generated by Django 5.0.7 on 2024-08-05 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal_app', '0002_comuna_inmueble_region_tipoinmuble_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoInmueble',
            fields=[
                ('id_tipo_inmueble', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_inmueble', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo_inmuebles',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TipoInmuble',
        ),
    ]
