from models import TodoModel

class TodoService:
    def __init__(self):
        self.model = TodoModel()

    def create(self, params):
        return self.model.create(params["Title"],params["Description"])

    def get_all(self):
        return  self.model.get_all()