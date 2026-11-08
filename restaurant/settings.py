"""
პროექტის პარამეტრები (settings).

ეს ფაილი Django-მ თავად შექმნა `startproject` ბრძანებით.
ჩვენ შევცვალეთ მხოლოდ ის, რაც ქვემოთ „ჩვენი ცვლილება“-თაა მონიშნული.
"""

from pathlib import Path

# პროექტის მთავარი საქაღალდე
BASE_DIR = Path(__file__).resolve().parent.parent

# საიდუმლო გასაღები: Django იყენებს session-ებისა და ფორმების დასაცავად
SECRET_KEY = 'django-insecure-l09xb=%hu%r=xu@1%k%i9l(0+mzv740cv-eso4gf#s5n966g4o'

# DEBUG = True: შეცდომისას დეტალური ინფორმაცია ჩანს (მხოლოდ დეველოპმენტისთვის)
DEBUG = True

ALLOWED_HOSTS = []


# აპლიკაციები, რომლებიც პროექტშია ჩართული
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ჩვენი ცვლილება: ჩვენი სამი აპლიკაცია
    'menu',      # კატეგორიები და კერძები
    'cart',      # კალათა
    'accounts',  # რეგისტრაცია, შესვლა, გამოსვლა
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ჩვენი ცვლილება: HTML შაბლონების საქაღალდე
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart_count',  # ჩვენი ცვლილება: კალათის მრიცხველი ყველა გვერდზე
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurant.wsgi.application'


# მონაცემთა ბაზა: SQLite, ერთი ფაილი db.sqlite3 პროექტის საქაღალდეში
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ჩვენი ცვლილება: Django-ს პაროლის შემოწმებები გამორთულია, რადგან მათი შეცდომები ინგლისურადაა.
# პაროლის სიგრძეს (მინიმუმ 8) ჩვენ თვითონ ვამოწმებთ ქართული ტექსტით: accounts/forms.py
AUTH_PASSWORD_VALIDATORS = []


# ჩვენი ცვლილება: ავტორიზაციის მისამართები
LOGIN_URL = 'login'                     # სადაც გადაჰყავს შეუსვლელი მომხმარებელი (მაგ. კალათის გახსნისას)
LOGIN_REDIRECT_URL = 'menu:dish_list'   # სადაც გადაჰყავს შესვლის შემდეგ
LOGOUT_REDIRECT_URL = 'menu:dish_list'  # სადაც გადაჰყავს გამოსვლის შემდეგ


# ჩვენი ცვლილება: ენა ქართული (Django-ს საკუთარი ტექსტებიც, მაგ. ადმინ პანელი), დრო თბილისის
LANGUAGE_CODE = 'ka'
TIME_ZONE = 'Asia/Tbilisi'
USE_I18N = True
USE_TZ = True


# სტატიკური ფაილები (CSS, სურათები)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # ჩვენი ცვლილება: ჩვენი CSS აქ დევს
