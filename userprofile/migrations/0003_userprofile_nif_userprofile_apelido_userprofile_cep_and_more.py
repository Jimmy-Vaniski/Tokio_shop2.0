# Generated by Django 4.2.1 on 2023-07-02 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_is_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Nif',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='apelido',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cep',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cep_empresa',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='endereco',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='endereco_empresa',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nif_empresa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nome',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nome_empresa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telefone',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='telefone_empresa',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]