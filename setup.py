from distutils.core import setup

setup(
    name='django-call-after-commit',
    version='1.0.1',
    packages=(
        'django_call_after_commit',
    ),
    url='https://chris-lamb.co.uk/projects/django-call-after-commit',
    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    description="Django utility to easily queue methods to be called after current transaction has been committed",
    install_requires=['django>=1.0'],
)
