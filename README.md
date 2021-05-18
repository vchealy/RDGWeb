Setup your virtual environment  
Install the requirements

There are three main python files to this script.

main.py
choice_functions.py
request_functions.py

main.py
Is the initisation file. Run this to start the code

choice_functions.py
This module contains all of the working code.
Deciding which request to action and gathering up the custom requirements for the function.

request_function.py
This file holds the bulk of the requests, header, custom parameters
Defaults have been put in place from the initial function testing. This may have to be altered
for the calling of the function as I found the surname default would not action when
the surname was left blank by the user.

Currently the replies are only going to console log.
There is a little error control added in to console log the reply status code with a pass/fai; message. This will be left in for the time being.

Some of the information, by default, gives 404 Errors and this is most likely the request
content rathan that the construction of the request.
