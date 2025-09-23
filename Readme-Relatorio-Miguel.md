Primeira coisa a se fazer é baixar o Django usando -> pip install "Django>=5.1,<6.0" python-dotenv OU pip install -r requirements.txt

Criei as Bases usando esses comandos no CMD:


# criar o projeto (Folder Config)

python -m django startproject config .

# criar o app principal (Folder WebButler)

python manage.py startapp webbutler


Após isso eu criei as pastas restantes, Templates (é onde vai ficar o css e o html) e suas pastas internas, isso pra terminar a estruturação das pastas

Tudo isso seguido da criação das pastas do javascript (é bem opcional nem ach q vcs vão usar) do Css e do Html base, q vai servir mais ou como um template para as outras paginas pra fazer o head delas, como assim vc me pergunta, bem o html é feito como um corpo, tem a parte da  `<head> <body> <scripts>`

ai entra o seguinte, por mts veses vcs ficar repetindo a HEAD q normalmente é a mesma para todas as paginas vcs faz uma Base q so vai conter a head, e nas outras paginas vc importa essa head e so controi o corpo dela e o scripts se necessario, a base serve apenas pra se conectar com o css e deixar tudo igual nisso ai

mas a vdd é q vcs podem fazer do jeito que acharem melhor, ces podem cagar ai pra base e usar ela como uma home ou algo do tipo tbm, mas eu faria desas forma, outra coisa, se o projeto visa ter uma navbar é bom fazer um arquivo navbar.html e construir o BODY da navbar la e dps tu importa tudo pra as outras paginas, sim vc pode fazer isso com o body tbm, so lembrando que primeiro se importa a HEAD e depois o BODY certo

depois disso eu fui configurar a settings.py la na pasta config, primeira alteração adicionei o app webbutler la nos apps:


INSTALLED_APPS=[

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    "webbutler",

]

pq eu fiz isso, pq se ele n tiver la ele n roda ponto, ent TODO app que vcs criarem TEM QUE SER ADICIONADO AQUI, pois se n ele n roda

depois ajustei o PATH ou DIR dos templates para esse aqui:
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates" / "html"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

por que é necessario declarar la na setting aonde o django deve procurar os Htmls, normalmente se coloca no app central, mas da pra conctar a outros apps usando o urls.py la da config tbm, mas como a base do projeto vai ser voltado a 1 app eu decidi colocar o templates fora e dai ajustar o PATH la


lembrando que, como eu mudei o path eu tbm tenho que mudar o static la no settings

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "templates" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"   # opcional (usado em collectstatic)

ai eu declaro so uns path tbm, é mais burocracia do que eficiencia mas tem que ser feito

# COMO RODAR O DJANGO

primeiro passo, caso teu models tenha sofrido quaisquer alterações é obrigatorio rodar python manage.py makemigrations

caso n teve alterações no models, tu roda python manage.py migrate e depois roda python manage.py runserver ISSO TUDO DEVE SER FEITO EM UM TERMINAL
qnd tu rodar o runserver ele vai mandar uma mensagem e nela vai estar o link do django, tu segura ctrl e clica no link e ele vai te levar para sua home, lembrando que o link n muda, é estatico ent tu pode copiar ele para usar nos testes, mas ele so funciona se a aplicação estiver rodando, como fazer pra aplicação parar de rodar, no terminal que vc fez o runserver tu vai clicar ctrl + c, isso vai terminar a aplicação


/
