ADMINS = (
    ('test@example.com', 'Test da'),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'spine.db'
TEST_DATABASE_NAME = 'spine-test.db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'TEST_NAME': TEST_DATABASE_NAME,
    }
}

SECRET_KEY = '7r33b34rd'

INSTALLED_APPS = [
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.admin',
    'subcommand',
    'spine',
]
