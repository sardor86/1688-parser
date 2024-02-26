from environs import Env
from pathlib import Path

PATH = Path(__file__).parent


def get_api_key(path: str):
    env = Env()
    env.read_env(path)

    return env.str('TM_API_KEY')
