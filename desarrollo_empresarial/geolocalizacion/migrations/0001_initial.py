# Generated by Django 4.1.6 on 2023-02-02 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=60)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='municipios', to='geolocalizacion.departamento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DivisionTerritorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=60)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='divisiones_territoriales', to='geolocalizacion.municipio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departamentos', to='geolocalizacion.pais'),
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=60)),
                ('division_territorial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='barrios', to='geolocalizacion.divisionterritorial', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]