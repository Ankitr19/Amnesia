# Amnesia
<br>
John has a certain kind of amnesia. Every hour, he forgets his name. He’s tired of setting an alarm on his very old phone which doesn’t allow setting cron alarm jobs.
<br><br>
He wants to hire you to create an application which will send him an SMS every hour to remind him of his name. He also wants you to make sure that he doesn’t get alarms during the night when he is asleep.
<br><br>
Since you don’t know which part of the world John lives in, you have to use an SMS provider which can send an SMS to nearly every country. Twillio is a nice service for sending out SMSes. However, sometimes Twillio’s SMS fails, in which case you have to send it again.
<br><br><br>
Please do the following:
<br><br>
1. Create a (basic) web based application where John can set his phone number<br>
2. Send an SMS every one hour except at night<br>
3. Try resending an SMS if it fails, but retry no more than 5 times. (There is only so much you can do!)<br>
4. The web application should also log all the failed messages and tell John for how many hours the application has been running.<br>
