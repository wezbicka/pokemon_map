# Generated by Django 3.1.14 on 2023-01-06 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_pokemon_previous_evolution'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewPokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('title_en', models.CharField(blank=True, max_length=200, verbose_name='Английское название')),
                ('title_jp', models.CharField(blank=True, max_length=200, verbose_name='Японское название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolution', to='pokemon_entities.pokemon', verbose_name='Предыдущая эволюция')),
            ],
        ),
    ]
