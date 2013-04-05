# Copyright (c) 2012-2013 SHIFT.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import thunderdome

from werkzeug.routing import BaseConverter


class UUIDConverter(BaseConverter):
    """
    Performs URL parameter validation against a UUID.

    Example:

    @app.route('/<uuid:uid>')

    """
    def __init__(self, url_map, *items):
        super(UUIDConverter, self).__init__(url_map)
        self.regex = r'[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}'

    def to_python(self, value):
        return value.lower()

    def to_url(self, value):
        return value.lower()


        
class VertexConverter(UUIDConverter):
    """
    Used to convert URL parameters into instances of thunderdome vertices.
    """
    
    def __init__(self, url_map, klass):
        """
        Initialize this vertex converter

        :param url_map: The url map to be matched against
        :type url_map: mixed
        :param klass: The thunderdome.Vertex instance to instantiate with
        :type klass: thunderdome.Vertex
        
        """
        super(VertexConverter, self).__init__(url_map)
        self.klass = klass

    def to_python(self, value):
        """
        Assuming that value is a valid UUID this will return an instance of the
        class used to initialize this vertex converter.

        :param value: The UUID value to be converted
        :type value: str

        :rtype: thunderdome.Vertex
        
        """
        return self.klass.get(value)


def converter_wrapper(klass):
    """
    Returns a closure which will create new converter for the given class
    when called like a normal constructor.

    :param klass: The vertex class to be used
    :type klass: thunderdome.Vertex
    
    """
    def wrapper_result(url_map):
        return VertexConverter(url_map, klass)
    return wrapper_result
