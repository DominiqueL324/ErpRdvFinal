# Generated by Django 4.0.1 on 2022-12-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0018_rename_audit_planneir_rendezvous_audit_planneur'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='dte_sortie_ancien_loc',
            field=models.DateTimeField(null=True, verbose_name='Date sortie Ancien locataire'),
        ),
    ]
