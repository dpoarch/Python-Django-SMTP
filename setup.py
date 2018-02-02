from setuptools import setup

setup(
    name = "django-smtp",
    version = __import__("googlemail_backend").__version__,
    author = "Glenn Washburn",
    author_email = "davidpoarchtest@gmil.com",
    description = "Django email backend for sending via gmail SMTP.",
    url = "https://github.com/dpoarch/Python-Django-SMTP",
    license = "MIT",
    packages = [
        "mailer",
    ]
)
