from api.main import hello_world

class TestHelloWorldResponse:
    def test_hello_world_responds_with_hellow_world(self):
        response = hello_world({})
        assert response == "Hello, World!"