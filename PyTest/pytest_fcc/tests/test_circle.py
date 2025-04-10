import PyTest.pytest_fcc.source.shapes as shapes

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_one(self):
        assert True

    def test_two(self):
        assert True