from flask_restx import Resource, Namespace, fields
from src.repositories import TodoRepository
from src.handlers import error_handler

ns = Namespace('todos', description='TODO operations')
error_handler(ns)

todo = ns.model(
    'Todo',
    {
        'id': fields.Integer(readonly=True, description='The task unique identifier'),
        'task': fields.String(required=True, description='The task details'),
    },
)

TODO_REPO = TodoRepository()
TODO_REPO.create({'task': 'Build an API'})
TODO_REPO.create({'task': '?????'})
TODO_REPO.create({'task': 'profit!'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''

    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return TODO_REPO.todos

    @ns.doc('create_todo')
    @ns.expect(todo)
    @ns.marshal_with(todo, code=201)
    def post(self):
        '''Create a new task'''
        return TODO_REPO.create(ns.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''

    @ns.doc('get_todo')
    @ns.marshal_with(todo)
    def get(self, id):
        '''Fetch a given resource'''
        return TODO_REPO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        TODO_REPO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return TODO_REPO.update(id, ns.payload)
