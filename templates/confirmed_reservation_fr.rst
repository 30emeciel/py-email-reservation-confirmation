{% extends "email_base.rst" %}
{% block title %}{% include 'confirmed_reservation_title_fr.txt' %}{% endblock %}

{% block content %}

:Nom:
    {{ pax.name }}
:Date d'arrivée:
    {{ request.arrival_date|dateformat }}

{% if request.kind == "COLIVING" %}
:Date de départ:
    {{ request.departure_date|dateformat }}
:Nombre de nuit(s):
    {{ request.number_of_nights }}
{% endif %}

:Type:
    {{ request.kind }}
:Date de réservation:
    {{ request.created|dateformat }}


Quelques informations pour ta venue
************************************************************************************************************************


Adresse
========================================================================================================================

| 16 rue Vandrezanne
| Tour Jade
| Utilises l'interphone de droite et tape le code "A303".
| Montes au 30ème puis dirige-toi vers la porte à gauche numéro 30.3


Rejoindre la communauté du 30ème Ciel
========================================================================================================================

Tu peux rejoindre la communauté privé du 30ème Ciel sur Discord :
https://discord.gg/eH5Xx7EPDu

ou sur le groupe privé Facebook, que tu peux le rejoindre en suivant ce lien :
https://www.facebook.com/groups/au30emeciel

Wifi
========================================================================================================================

:SID:
    303
:Mdp:
    clitoris


Changement de dernières minutes ?
========================================================================================================================
Si tu souhaites modifier ta réservation, suis ce lien `Gérer mes réservations <https://coliv.30emeciel.fr/reservations>`_.



{% endblock %}


