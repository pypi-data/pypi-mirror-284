# Wedge Library

## Démarrage rapide

```bash
$ pip install wedge-lib
```

### Mode maintenance

#### Middleware

```python
MIDDLEWARE=[
    "w.drf.middlewares.maintenance_mode_middleware.MaintenanceModeMiddleware",
],
```


#### Command

Ajouter la commande maintenance_mode :

```python
from w.django.commands.abstract_maintenance_mode_command import (
    AbstractMaintenanceModeCommand,
)


class Command(AbstractMaintenanceModeCommand):
    pass
```

Utilisation :

```bash
$ python manage.py maintenance_mode <on/off>
```

### Configuration pour certains services

#### MailService
TBD
#### GoogleMapService
TBD
#### YousignService
TBD

## Development

### Installation

```bash
$ pipenv sync --dev
```

### Update dependencies

```bash
$ pipenv update --dev
```

### Run test

```bash
$ pytest
```

### En cas d'ajout d'une librairie
Afin qu'elle soit également installée sur cs_back, il faut ajouter une ligne dans setup.cfg, sous la partie "install_requires ="

Des variables d'environnement doivent être configurées sur Pycharm:
- Cliquez sur Edit configurations en haut à droite de votre éditeur
- Edit configurations templates...
- Python tests - pytest
- Cliquez sur environnement variables et ajouter les api key correspondant à :
  - GOOGLE_MAP_SECRET
  - GOOGLE_MAP_API_KEY
- Les valeurs de ces variables peuvent être trouvées sur les secrets du repo ou à Eloïse

### Before commit

Pour éviter de faire échouer le CI, lancer la commande:

```bash
$ ./before_commit.zsh
```

### Publier manuellement sur PyPI

Après avoir committer et pousser:
 
1. tagguer une version dans GitHub.
2. mettre à jour la version dans le fichier `setup.cfg` avec le tag créé.
3. créer le package
    ```bash
    $ rm -rf build dist wedge_lib.egg-info
    $ WEDGELIB_VERSION=<version> python setup.py sdist bdist_wheel
    ```
4. mettre à jour sur TestPypi
    ```bash
    $ twine upload --repository testpypi dist/*
    ```
5. Si tout est ok, mettre à jour sur Pypi
    ```bash
    $ twine upload dist/*
    ```
   
### Utiliser W en mode dev depuis un autre projet (ex: csback)

Supprimer w du projet, ensuite l'installer à partir du chemin local du projet w:
```bash
pipenv uninstall wedge-lib && pipenv install <Absolute path du projet w local>
```

Après une nouvelle release de w, utiliser la version officielle :
```bash
pipenv uninstall wedge-lib && pipenv install wedge-lib
```




