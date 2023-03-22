# Fichier d'exemples pour travailler avec les dates

from datetime import date
from datetime import datetime
from datetime import timedelta

import locale
locale.setlocale(locale.LC_ALL, "fr_FR")

def main():
    # Les heures et les dates peuvent être formatées à l'aide d'un ensemble de chaînes prédéfinies.
    # Obtenir la date et l'heure actuelles
    now = datetime.now()
    print("La date et l'heure actuelles sont ", now)

    # %y/%Y - Année, %a/%A - jour de la semaine, %b/%B - mois, %d - jour du mois
    # Année complète avec siècle
    print(now.strftime("L'année actuelle is: %Y"))

    # Jour abrégé, num, mois complet, année abrégée
    print(now.strftime(r"%a, %d %B, %y"))

    # %c - date et heure locale, %x - date locale, %X - heure locale
    print(now.strftime("Date et heure locale : %c"))
    print(now.strftime("Date locale : %x"))
    print(now.strftime("Heure locale : %X"))

    #### Formattage Heure ####
    # %I/%H - 12h/24h, %M - minute, %S - second, %p - AM/PM
    # H:M:S format 12h AM
    # Si locale en français, AM/PM n'est pas affiché
    print(now.strftime("Heure actuelle (12h) : %I:%M:%S %p"))

    # H:M:S format 24h
    print(now.strftime("Heure actuelle (24h) : %H:%M:%S"))

    ### OBJET DATE
    # Obtenir la date actuelle de la methode today de la classe Date
    today = date.today()
    print(f"La date d'aujourd'hui est : {today}")

    # Afficher individuellement les composants d'une date
    print(f"Composant d'une date : {today.day:02d} / {today.month:02d} / {today.year}")

    # Récupérer le jour de semaine d'aujourd'hui (0 = lundi, 6 = dimanche)
    print(f"Le jour de cette semaine est : {today.weekday()}")
    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    print(f"en français : {days[today.weekday()]}")

    ### OBJET DATETIME
    # Obtenir l'heure actuelle
    t = datetime.time(datetime.now())
    print(f"Le temps actuel est : {t}")
    
    ### TIMEDELTA ###
    # Construire un basic timedelta et l'afficher
    print(timedelta(days = 365, hours = 5, minutes = 1))

    # Ajouter un an à la date actuelle
    print(f"Un an à partir d'aujourd'hui sera : {now + timedelta(days = 365)}")

    # Créer un timedelta qui utilise plus d'un argument
    print(f"Dans deux semaines et 3 jours, il sera : {str(now + timedelta(weeks = 2, days = 3))}")

    # Calculer la date d'il y a une semaine, formatée comme un String
    t = datetime.now() - timedelta(weeks = 1)
    s = t.strftime(r"%A %d %B %Y")
    print(f"Il y a une semaine, c'etait le {s}")

    # Obtenir une date precise (Nouvel an)
    nouvel_an = date(today.year, 1, 1)
    print("nouvel an :", nouvel_an)

    # Opérations entre les dates
    diff = today - nouvel_an
    print(f"diff days : {diff.days}")
    # diff seconds n'affiche rien car les variable sont des dates et non des datetime
    print(f"diff sec : {diff.seconds}")

    # Obtenir la date pour le prochain nouvel an
    nouvel_an = nouvel_an.replace(year = today.year + 1)
    print(f"prochaine nouvel an : {nouvel_an}")
    
if __name__ == "__main__":
    main()