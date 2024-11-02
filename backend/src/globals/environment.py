# builtin

# external
from pydantic_settings import BaseSettings

class Environment(BaseSettings):
    MONGODB_URL: str  =  "mongodb+srv://seanblizard:phDD0Hb0O7s12q3f@mealsforless.yky0i.mongodb.net/?retryWrites=true&w=majority&appName=MealsForLess&ssl_cert_reqs=CERT_NONE"# Define the expected environment variable

    class Config:
        env_file = ".env"