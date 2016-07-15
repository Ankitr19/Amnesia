from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException
from twilio.rest import TwilioRestClient
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def is_valid_number(number):
    client = TwilioLookupsClient()
    try:
        response = client.phone_numbers.get(number)
        response.phone_number  # If invalid, throws an exception.
        return True
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e

@task(name="send_sms_task")
def send_sms_task(number, message):
    client = TwilioRestClient()
    attempts = 0
    while attempts < 5:
        try:
            client.messages.create(
                to      = number,
                from_   = "+12015915580",
                body    = message,
                )
            break
        except TwilioRestException as e:
            logger.message(e)
            attempts = attempts + 1



def celery_init(name, number):
    print("working")