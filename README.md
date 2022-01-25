## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Compte Heroku
- Compte Sentry
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- Générer une secret_key : [Djecrety](https://djecrety.ir/)
- Créer un fichier .env à la racine du projet et y mettre la clé généré dans une variable SECRET_KEY
- Créer un projet Django sur Sentry et ajouter le dsn fournie par sentry à votre .env sous le nom de SENTRY_URL
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Deploiement 

### Fonctionnement

Le déploiement ce fait sur heroku où une image docker de notre application est construite à partir du fichier Dockerfile, puis est déployé. Cela permet de simplifier la mise en production et de retrouver le même environnement que en local ainsi que notre base de données et son contenu.


### Configuration requise

- Un compte heroku et heroku CLI
- Un fichier Dockerfile (déjà présent)

### Deploiement heroku

- se connecter a heroku : `heroku container:login`
- Créer un projet heroku : `heroku create <name-of-app>`
- Aller dans les settings de votre projet précédemment généré sur votre espace du site heroku, dans config vars ajouter la variable SECRET_KEY et SENTRY_URL
- Build une image docker et la push sur heroku : `heroku container:push web`
- Release l'image : `heroku container:release web`
- L'application devrait être accessible a l'url fournie par heroku

## Sentry

Vous pouvez vous rendre sur l'url /sentry-debug/ cela vous donnera une erreur et une issue devrait se créer concernant cette erreur dans votre espace sentry.





