from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('Mazurpythonlambda-handler')


class Mazurpythonlambda(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        return 200
    

HANDLER = Mazurpythonlambda()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
