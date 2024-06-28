# Generated by Django 4.2 on 2024-06-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id_equip', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nom_Equip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lliga',
            fields=[
                ('id_lliga', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nom_lliga', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Partit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalls', models.TextField(blank=True, null=True)),
                ('inici', models.DateTimeField(blank=True, null=True)),
                ('lliga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lliga.lliga')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits_local', to='lliga.equip')),
                ('visitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partits_visitant', to='lliga.equip')),
            ],
            options={
                'unique_together': {('local', 'visitant', 'lliga')},
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveSmallIntegerField()),
                ('nom', models.CharField(max_length=30)),
                ('cognom', models.CharField(max_length=30)),
                ('equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lliga.equip')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps', models.TimeField()),
                ('tipus', models.CharField(choices=[('GOL', 'Gol'), ('AUTOGOL', 'Autogol'), ('FALTA', 'Falta'), ('PENALTY', 'Penalty'), ('MANS', 'Mans'), ('CESSIO', 'Cessio'), ('FORA_DE_JOC', 'Fora De Joc'), ('ASSISTENCIA', 'Assistencia'), ('TARGETA_GROGA', 'Targeta Groga'), ('TARGETA_VERMELLA', 'Targeta Vermella')], max_length=30)),
                ('detalls', models.TextField(blank=True, null=True)),
                ('equip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lliga.equip')),
                ('jugador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_fets', to='lliga.jugador')),
                ('jugador2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_rebuts', to='lliga.jugador')),
                ('partit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lliga.partit')),
            ],
        ),
        migrations.AddField(
            model_name='equip',
            name='id_lliga',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lliga.lliga'),
        ),
    ]
