import abc
import httpx
import logging
import datetime
import functools

from httpx._exceptions import ConnectTimeout, ReadTimeout

logging.basicConfig(level=logging.INFO)


class IFetchUrl(abc.ABC):
    """Abstract base class. You can't instantiate this independently."""

    @abc.abstractmethod
    def get_data(self, url: str) -> dict:
        pass

    @abc.abstractmethod
    def get_headers(self, data: dict) -> dict:
        pass

    @abc.abstractmethod
    def get_args(self, data: dict) -> dict:
        pass

class FetchUrl(IFetchUrl):
    """Concrete class that doesn't handle exceptions and loggings."""

    def get_data(self, url: str) -> dict:
        with httpx.Client() as client:
            response = client.get(url)
            data = response.json()
            return data

    def get_headers(self, data: dict) -> dict:
        return data["headers"]

    def get_args(self, data: dict) -> dict:
        return data["args"]

class ExcFetchUrl(IFetchUrl):
    """This class can be swapped out with the FetchUrl class.
    It provides additional exception handling and logging."""

    def __init__(self) -> None:
        self._fetch_url = FetchUrl()

    def get_data(self, url: str) -> dict:
        try:
            data = self._fetch_url.get_data(url)
            return data

        except ConnectTimeout:
            logging.error("Connection time out. Try again later.")

        except ReadTimeout:
            logging.error("Read timed out. Try again later.")

    def get_headers(self, data: dict) -> dict:
        headers = self._fetch_url.get_headers(data)
        logging.info(f"Getting the headers at {datetime.datetime.now()}")
        return headers

    def get_args(self, data: dict) -> dict:
        args = self._fetch_url.get_args(data)
        logging.info(f"Getting the args at {datetime.datetime.now()}")
        return args

class CacheFetchUrl(IFetchUrl):
    def __init__(self) -> None:
        self._fetch_url = ExcFetchUrl()

    @functools.lru_cache(maxsize=32)
    def get_data(self, url: str) -> dict:
        data = self._fetch_url.get_data(url)
        return data

    def get_headers(self, data: dict) -> dict:
        headers = self._fetch_url.get_headers(data)
        return headers

    def get_args(self, data: dict) -> dict:
        args = self._fetch_url.get_args(data)
        return args


if __name__ == "__main__":
    fetch = CacheFetchUrl()

    for arg1, arg2 in zip([1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]):
        url = f"https://postman-echo.com/get?foo1=bar_{arg1}&foo2=bar_{arg2}"
        print(f"\n {'-'*75}\n")
        data = fetch.get_data(url)
        print(f"Cache Info: {fetch.get_data.cache_info()}")
        print(fetch.get_headers(data))
        print(fetch.get_args(data))
