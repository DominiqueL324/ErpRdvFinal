# Generated by Django 4.1.1 on 2022-09-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdv', '0010_rendezvous_couleur_rendezvous_statut'),
    ]

    operations = [
        migrations.AddField(
            model_name='rendezvous',
            name='agent_constat',
            field=models.IntegerField(null=True, verbose_name='Agent constat'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='ancien_agent_trigramme',
            field=models.CharField(max_length=15, null=True, verbose_name='Ancien agent trigramme'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='ancien_client_id',
            field=models.IntegerField(null=True, verbose_name='ancien client ID'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name='Date de creation'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='last_update_by',
            field=models.IntegerField(null=True, verbose_name='Modifier par'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='numero',
            field=models.CharField(max_length=20, null=True, verbose_name='Numero'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='ref_commande',
            field=models.CharField(max_length=40, null=True, verbose_name='Reference commande'),
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date de modification'),
        ),
    ]