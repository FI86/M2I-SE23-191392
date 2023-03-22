# Import module
import cgitb

# Activation
cgitb.enable()

# Affichage d'une page web basique
name = "Xavier"
# Content-type: text/html  (à mettre si besoin au debut du code html)
print(f"""
<html>
<head> <title> Titre de la page
</title> </head>
<style>
</style>
<body>
<h3> Mon nom est {name} </h3>
</body>
</html>
""")