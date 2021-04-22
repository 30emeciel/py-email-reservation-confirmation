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
| Montes au 30ème puis dirige-toi vers la porte à gauche numéro 3.03


Wifi
========================================================================================================================

:SID:
    30ème Ciel
:Mdp:
    clitoris

Rejoindre la communauté des colivers du 30ème Ciel
========================================================================================================================

Tu peux rejoindre le groupe Whatsapp privé des Colivers du 30ème Ciel :
https://chat.whatsapp.com/IQaf7xSSEQAIIwrBX9j8sK
Tu ne peux rejoindre dans cette conversion que pendant ta présence au 30ème Ciel et jusqu'à deux semaines après ton dernier jour.

Le reste du temps, tu peux communiquer sur le groupe privé Facebook, que tu peux le rejoindre en suivant ce lien :
https://www.facebook.com/groups/au30emeciel

Contribuer
========================================================================================================================

Tu vas recevoir à la fin de ton passage un e-mail t'invitant si tu souhaites contribuer au projet.


Changement de dernières minutes ?
========================================================================================================================
Si tu souhaites modifier ta réservation, suis ce lien `Gérer mes réservations <https://coliv.30emeciel.fr/my-reservations>`_.




{% endblock %}


