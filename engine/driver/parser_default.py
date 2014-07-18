# coding=utf-8

from werkzeug.wrappers import Request as wRequest, Response as wResponse
from werkzeug.urls import url_decode
from werkzeug.datastructures import EnvironHeaders
from engine.interface import BaseRequest, BaseResponse
from engine.util import CachedProperty


class Request(wRequest, BaseRequest):
    """
    """
    def __init__(self, environ):
        self.environ = environ
        BaseRequest.__init__(self, environ)
        wRequest.__init__(self, environ)

    @CachedProperty
    def headers(self):
        """ The parsed headers
        """
        return EnvironHeaders(self.environ)

    @CachedProperty
    def body(self):
        """ The parsed body
        """
        return self.get_data(parse_form_data=True)

    @CachedProperty
    def content_type(self):
        return self.environ.get('CONTENT_TYPE', '')

    @CachedProperty
    def url_args(self):
        """ The parsed URL parameters.
            return dictionary
        """
        return url_decode((self.environ.get('QUERY_STRING', '').encode("latin1")))


class Response(wResponse, BaseResponse):
    pass

