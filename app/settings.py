import os
from dotenv import load_dotenv


class Base:
    # Environmentally global configs
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(BASE_DIR, ".env"))
    ENVIRONMENT = os.environ["ENV"]

    ALLOWED_HOSTS = []
    ALLOW_ORIGINS = []


class Dev(Base):
    pass


class Test(Base):
    pass


class Staging(Base):
    pass


class Prod(Base):
    pass


def get_config() -> Base:
    environment = os.environ["ENV"]

    if environment == "DEV":
        return Dev()

    elif environment == "PROD":
        return Prod()

    elif environment == "TEST":
        return Test()

    elif environment == "STAGING":
        return Staging()
