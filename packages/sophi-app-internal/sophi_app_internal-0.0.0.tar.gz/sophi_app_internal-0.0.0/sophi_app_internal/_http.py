import json, typing, types
import collections.abc

class BaseHeaders(collections.abc.Mapping):
    """
    A base class for handling HTTP headers in a case-insensitive manner.

    Args:
        source (typing.Optional[typing.Mapping], optional): A mapping containing initial HTTP headers. Defaults to None.
    """
    def __init__(self, source: typing.Optional[typing.Mapping] = None) -> None:
        self.__http_headers__: typing.Dict[str, str] = {}

        if source is not None:
            self.__http_headers__.update(
                {k.lower(): v for k, v in source.items()})

    def __getitem__(self, key: str) -> str:
        """
        Get the value of the specified header.

        Args:
            key (str): The header key.

        Returns:
            str: The header value.
        """
        return self.__http_headers__[key.lower()]

    def __len__(self):
        """
        Get the number of headers.

        Returns:
            int: The number of headers.
        """
        return len(self.__http_headers__)

    def __contains__(self, key: typing.Any):
        """
        Check if a header exists.

        Args:
            key (typing.Any): The header key.

        Returns:
            bool: True if the header exists, False otherwise.
        """
        return key.lower() in self.__http_headers__

    def __iter__(self):
        """
        Iterate over the headers.

        Returns:
            Iterator: An iterator over the headers.
        """
        return iter(self.__http_headers__)

class HttpRequestHeaders(BaseHeaders):
    """
    A class for handling HTTP request headers.
    """
    pass

class HttpRequest():
    """
    An HTTP request object.

    Args:
        method (str): HTTP request method name.
        url (str): HTTP URL.
        headers (typing.Optional[typing.Mapping[str, str]], optional): An optional mapping containing HTTP request headers. Defaults to None.
        params (typing.Optional[typing.Mapping[str, str]], optional): An optional mapping containing HTTP request params. Defaults to None.
        route_params (typing.Optional[typing.Mapping[str, str]], optional): An optional mapping containing HTTP request route params. Defaults to None.
        body (bytes): HTTP request body.
    """
    def __init__(self,
                 method: str,
                 url: str, *,
                 headers: typing.Optional[typing.Mapping[str, str]] = None,
                 params: typing.Optional[typing.Mapping[str, str]] = None,
                 route_params: typing.Optional[
                     typing.Mapping[str, str]] = None,
                 body: bytes) -> None:
        self.__method = method
        self.__url = url
        self.__headers = HttpRequestHeaders(headers or {})
        self.__params = types.MappingProxyType(params or {})
        self.__route_params = types.MappingProxyType(route_params or {})
        self.__body_bytes = body

    @property
    def url(self):
        """
        Get the request URL.

        Returns:
            str: The request URL.
        """
        return self.__url

    @property
    def method(self):
        """
        Get the request method.

        Returns:
            str: The request method.
        """
        return self.__method.upper()

    @property
    def headers(self):
        """
        Get the request headers.

        Returns:
            HttpRequestHeaders: The request headers.
        """
        return self.__headers

    @property
    def params(self):
        """
        Get the request parameters.

        Returns:
            typing.MappingProxyType: The request parameters.
        """
        return self.__params

    @property
    def route_params(self):
        """
        Get the route parameters.

        Returns:
            typing.MappingProxyType: The route parameters.
        """
        return self.__route_params

    def get_body(self) -> bytes:
        """
        Get the request body.

        Returns:
            bytes: The request body.
        """
        return self.__body_bytes

    def get_json(self) -> typing.Any:
        """
        Get the JSON-decoded request body.

        Returns:
            typing.Any: The JSON-decoded request body.
        """
        return json.loads(self.__body_bytes.decode('utf-8'))
