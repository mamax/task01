from tests.test_mazurpythonlambda import MazurpythonlambdaLambdaTestCase


class TestSuccess(MazurpythonlambdaLambdaTestCase):

    def test_success(self):
        self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)

