from src.errors import NotFoundError


def error_handler(ns):
    @ns.errorhandler(Exception)
    def handle(error):
        if isinstance(error, NotFoundError):
            return {'message': error.message}, 404
        else:
            return {'message': 'Internal server error'}, 500
