#  TrollSquadAI

## Présentation du projet

La TrollSquad vous présente leur nouvelle API permettant d'automatiser la création de vos fantaisies les plus folles ! Grâce à l'utilisation des intelligences artificielles, vous pouvez à la fois créer un scénario à votre histoire grâce à llama, et même l'illustrer grâce à stable diffusion !

Vous retrouverez les tutoriels nécessaires au fonctionnement de notre application dans la suite de ce document.

## Membres

- Darren STEPHAN
- Maxime BECK
- Mathieu CHAMPAGNE
- Tanaël CLAUDE
- Rayane SCHAHL

## Installation
En premier lieu, il vous faut d'abord avoir installé les trois IAs dont notre application fait l'utilisation. 
Vous trouverez ci-dessous les tutoriels à suivre afin de vous simplifier la tâche.

---
### Prérequis

 - [PIP](https://pip.pypa.io/en/stable/installation/)
 - [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) (minimum)
 - Replicate token api (llama)
---

### Llama
#### Windows, Linux & MacOS
```
pip install replicate python-dotenv
```

### Stable diffusion

#### Windows
1. Télecharger le [dépôt de stable diffusion webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running)
```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git.
```
2. Modifier le fichier ```webui-user.bat ``` pour y ajouter l'attribut ```--api``` à la variable ```COMMANDLINE_ARGS``` comme ci-dessous:
``` 
set COMMANDLINE_ARGS=--api
```
3. Exécuter le fichier `webui-user.bat`


#### Linux

1. Télécharger le script d'installation de stable diffusion webui
```
wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh
```
2. Modifier le fichier ```webui-user.sh ``` pour y ajouter l'attribut ```--api``` à la variable `COMMANDLINE_ARGS` comme ci-dessous:
``` 
set COMMANDLINE_ARGS=--api
```
3. Exécuter le fichier ```webui.sh```

#### MacOS

1. Installer Homebrew via https://brew.sh.
2. Ouvrir un terminal, exécuter :
```
brew install cmake protobuf rust python@3.10 git wget
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
cd stable-diffusion-webui && ./webui.sh
```
3. Placer les modèles dans stable-diffusion-webui/models/Stable-diffusion.
4. Exécuter le fichier ```webui.sh```

Pour plus d'informations : [Installation de Stable diffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui#installation-and-running)

### Helsinki
#### Windows, Linux & MacOS
Helsinki est une IA de traduction de texte. Pour l'utiliser il faut installer transformers avec pip.
``` 
pip install transformers
```

---
## API

Notre application propose une API locale qui permet de faire des requêtes.
Pour lancer cette API il suffit d'aller dans le dossier `/src` et lancer le fichier `api.py` avec la commande : 
### Windows
```
py api.py
```
### Linux & MacOS
```
python3 api.py
```

---

## Contribution

N'importe qui peut participer à l'amélioration de ce projet, proposer l'ajout d'une nouvelle feature, ou signaler un bug.

Les étapes pour contribuer à notre projet sont disponible dans le fichier [CONTRIBUTING.md]("https://github.com/La-trollsquad/llm/blob/main/CONTRIBUTING.md")

## Licence

[MIT](https://github.com/La-trollsquad/llm/blob/main/LICENSE)