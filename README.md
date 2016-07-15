# Amnesia
<br>
John has a certain kind of amnesia. Every hour, he forgets his name. He’s tired of setting an alarm on his very old phone which doesn’t allow setting cron alarm jobs.
<br><br>
He wants to hire you to create an application which will send him an SMS every hour to remind him of his name. He also wants you to make sure that he doesn’t get alarms during the night when he is asleep.
<br><br>
Since you don’t know which part of the world John lives in, you have to use an SMS provider which can send an SMS to nearly every country. Twillio is a nice service for sending out SMSes. However, sometimes Twillio’s SMS fails, in which case you have to send it again.
<br><br><br>
##### Please do the following:
<br>
1. Create a (basic) web based application where John can set his phone number<br>
2. Send an SMS every one hour except at night<br>
3. Try resending an SMS if it fails, but retry no more than 5 times. (There is only so much you can do!)<br>
4. The web application should also log all the failed messages and tell John for how many hours the application has been running.<br>

<br><br>
## Instructions
<br>The Web App requires Redis to function, operating on the typical 6379 port.
<br>Redis 3.2.1 was used in this instance. Once redis-server is called and is active, and the Django application is also live [ using `python3 manage.py runserver 8000` ] on the local system, go to `http://127.0.0.1:8000/amnesia_app/home` from the web browser.
<br>Open 2 other terminals also in the folder where manage.py exists and run :<br>
1. celery -A amnesia worker -l info<br>
2. celery -A amnesia beat -l info<br>
<br><br>
Twilio's API was utilized to send the SMS alerts. Twilio allows free accounts so make one of those, once the login details are obtained export them into the `~./bashrc` file so that they are saved in the system environment.<br>
export TWILIO_ACCOUNT_SID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br>
export TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br>
<br>It is important to note that one must register their phone number on their free Twilio account and verify it via SMS. Non registered numbers cannot have SMSs sent from a free account.
<br>
If you want to change the hours between which the messages are sent go to `/amnesia_app/tasks.py` and modify the `ALERT_START_TIME` and `ALERT_STOP_TIME`. The Web App automatically obtains the country code from the phone number and gets the time difference from that to ensure that no matter which time zone one is in, the app is consistent.