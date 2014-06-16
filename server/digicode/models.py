# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

import random
import string
import datetime
# Create your models here.

def _generate_secret():
    """Génère un mot de passe aléatoire"""
    random.seed(datetime.datetime.now().microsecond)
    chars = string.letters + string.digits + '/=+*.,$'
    length = 255
    return u''.join([random.choice(chars) for _ in xrange(length)])

CODE_LENGTH=6

def _generate_code():
    """Génère un mot de passe aléatoire,
    TODO: en prendre un qui n'existe pas déjà"""
    random.seed(datetime.datetime.now().microsecond)
    chars = string.digits
    return u''.join([random.choice(chars) for _ in xrange(CODE_LENGTH)])

class Local(models.Model):
    """Un local (et sa badgeuse/digicode)"""

    class Meta:
        verbose_name_plural = "locaux"

    nom = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    hostname = models.TextField(
        help_text=u"Nom de domaine ou IP de la badgeuse/digicode",
    )

    shared_secret = models.CharField(max_length=255,
        default=_generate_secret,
        help_text=u"Secret partagé stocké dans le digicode",
    )

    def __unicode__(self):
        return self.nom

    def try_code(self, code):
        """Essaie un code. Et le consomme si nécessaire (TODO)"""
        possible = Code.objects.filter(touches=code).filter(locaux=self)
        return bool(possible)

class Acces(models.Model):
    """Un accès à un local donné"""
    
    local = models.ForeignKey(Local)
    
    user = models.ForeignKey(User)
    
    responsable = models.BooleanField(
        help_text=u"Est-ce le responsable de ce local (droits étendus)",
    )
    
    # Toute autre restriction d'accès envisageables (créneaux horaires etc)
    # Idem, mais avec des groupes (TODO  ?)


class Code(models.Model):
    """Un code à quelqu'un.
    Tout utilisateur a le droit de créer un code, pour les locaux auxquels
    il a accès. Il peut ainsi définir si son code ne devra être utilisé qu'une
    fois, tout le temps, ou si il ne doit être valable que pour certains locaux.
    """
    
    touches = models.CharField(max_length=CODE_LENGTH,
        help_text=u"Une chaîne de caractère ne contenant que des chiffres",
        default=_generate_code,
    )

    proprietaire = models.ForeignKey(User)
    
    locaux = models.ManyToManyField(Local,
        help_text=u"Locaux pouvant être ouverts par ce code",
    )

#    otp = models.BooleanField(default=False,
#        help_text=u"One-Time-Password : le code doit-il s'autodétruire après usage ?",
#    )
#
#    expire_time = models.DateTimeField(null=True, blank=True,
#        help_text=u"Date d'expiration",
#    )
