# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examples',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('example', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hypernym',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('hyper', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meanings',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('meaning', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('derived', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('synon', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wordsense',
            fields=[
                ('word', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('word_id', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wordtypes',
            fields=[
                ('types', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='synonym',
            name='word_id3',
            field=models.ForeignKey(to='dictionary.Wordsense', default='abc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relate',
            name='word_id2',
            field=models.ForeignKey(to='dictionary.Wordsense', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meanings',
            name='word_id1',
            field=models.ForeignKey(to='dictionary.Wordsense'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meanings',
            name='wortype',
            field=models.ForeignKey(to='dictionary.Wordtypes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hypernym',
            name='word_id4',
            field=models.ForeignKey(to='dictionary.Wordsense', default='xyz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='examples',
            name='wordsense',
            field=models.ForeignKey(to='dictionary.Wordsense'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='examples',
            name='wordtype',
            field=models.ForeignKey(to='dictionary.Wordtypes'),
            preserve_default=True,
        ),
    ]
