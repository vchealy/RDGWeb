# Replacing Postman with a simple CLI Tool

The export from a colleagues Postman showed it would be very labour intesive to use.
I have written this small cli tool to go through the options of the various requests,selecting the correct GET request and input the value to be searched.

This work in progress starts with replies sent to console, moving onto write to file, then write ujique file names.


### Things to do:  
Setup your virtual environment  
Install the requirements - pip install -r requirements.txt

### There are three main python files to this script.  
main.py   
choice_functions.py  
request_functions.py  

**main.py**  
Is the initisation file. Run this to start the code

**choice_functions.py**  
This module contains all of the working code. Deciding which request to action and gathering up the custom requirements for the function.

**request_function.py**  
This file holds the bulk of the requests, header, custom parameters Defaults have been put in place from the initial function testing. This may have to be altered for the calling of the function as I found the surname default would not action when the surname was left blank by the user.

Initially the replies only go to console log.  
There is a little error control added in to console log, the reply status code with a pass/fai; message.  
This will be left in for the time being.

Note:  
Some of the information, by default, gives 404 Errors and this is most likely the request content rather than the construction of the request.

**res.py**  
This module now handles the server reply.  
The reply arrives as a xml object that is then converted into a json obj that is formatted for readability.  
This object was then written to a file in the path ith a generic file name.  
Now that is working, I switched the file name to a unique name. This was to prevent filie overwrite if the code was reused. There was nothing special to this other than adding the date and time to a string object that would be used in the file write.  

### Future features:    
Loop the code for the user to attempt more requests.( Exit has already been added into the options and in the background to mitigate some errors)  
Add in fuctionality for the user to input a list of requests rather than individually requests. This should help automate the process a little bit.

![gplv3-or-later-sm](https://user-images.githubusercontent.com/9987554/118978744-93f8da00-b96f-11eb-8cdc-4dca580bb3d9.png)
