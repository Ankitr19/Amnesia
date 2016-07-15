from twilio.rest.lookups import TwilioLookupsClient
from twilio.rest.exceptions import TwilioRestException
from twilio.rest import TwilioRestClient


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

def send_sms(number, name):
    client = TwilioRestClient()
    client.messages.create(
        to      = number,
        from_   = "+12015915580",
        body    = name,
        )

def cron_worker(number):
    print("working")