def parse_input_data(data: str):
    result = {}
    if data:
        params = data.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
    return result


def parse_wsgi_input_data(data: bytes):
    result = {}
    if data:
        data_str = data.decode(encoding='utf-8')
        result = parse_input_data(data_str)
    return result


def get_wsgi_input_data(environ):
    content_length_data = environ.get('CONTENT_LENGTH')
    content_length = int(content_length_data) if content_length_data else 0
    data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


class CoreApp:
    def __init__(self, urls, front_controllers):
        self.urls = urls
        self.front = front_controllers

    def __call__(self, environ, start_response):
        print('=================WORK=================')
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        method = environ['REQUEST_METHOD']
        data = get_wsgi_input_data(environ)
        data = parse_wsgi_input_data(data)

        query_string = environ['QUERY_STRING']
        request_params = parse_input_data(query_string)

        if path in self.urls:
            view = self.urls[path]
            request = {}

            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params

            for controller in self.front:
                controller(request)
            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]


class DebugApp(CoreApp):
    def __init__(self, urls, front_controllers):
        self.application = CoreApp(urls, front_controllers)
        super().__init__(urls, front_controllers)

    def __call__(self, environ, start_response):
        print('=================DEBUG MODE=================')
        print(environ)
        return self.application(environ, start_response)


class MockApp(CoreApp):

    def __init__(self, urls, front_controllers):
        self.application = CoreApp(urls, front_controllers)
        super().__init__(urls, front_controllers)

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'From Mock with Love']
