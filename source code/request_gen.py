class GenerateRequestCommand:
    def __init__(self, app):
        self.app = app

    def execute(self):
        self.app.generate_request()