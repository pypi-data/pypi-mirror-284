import os
import pickle
import dotenv
from typing import Any


def get_cache_folderpath() -> str:
    if os.path.isfile('.env'):
        dotenv.load_dotenv()
        cache_folderpath = os.environ['cache_folderpath']
    else:
        cache_folderpath = 'cache'

    return cache_folderpath


def get_cache_filepath(filename: str) -> str:

    return os.path.join(get_cache_folderpath(), filename)


def write_to_cache(obj: Any, filename: str) -> None:
    cache_folderpath = get_cache_folderpath()
    if not os.path.isdir(cache_folderpath):
        os.mkdir(cache_folderpath)

    with open(get_cache_filepath(filename), 'wb') as file:
        pickle.dump(obj, file)


def read_from_cache(filename: str) -> Any:
    with open(get_cache_filepath(filename), 'rb') as file:
        obj = pickle.load(file)

    return obj


def file_in_cache(filename: str) -> bool:
    return os.path.isfile(get_cache_filepath(filename))


def remove_from_cache(filename: str) -> None:
    os.remove(get_cache_filepath(filename))
