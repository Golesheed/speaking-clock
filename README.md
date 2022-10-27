# Floor & Golshid's DreamClock
## Description
This is a speaking clock which was made as an assignment for our Introduction to Voice Technology course from MSc Voice Technology at Rijksuniversiteit Groningen/Campus Fryslân.
## Requirements
Make sure you have Python 3.10 installed (download from here: https://www.python.org/downloads/) , also check the requirements file.
## How to run the code?
Download files by clicking the green "code" button and the downloading the zip, make sure that the path is correct in the code and then simply run. :)
## Languages supported
- Dutch
- Farsi

## Time Telling logic
### Dutch
Saying time in Dutch depends on where the hands of the clock are pointing and this is how it goes:
- for when " 0 minutes" we use the following sentence:
> "It is” + current hour + “hour”
- when we are in the first quarter:
> “It is” + minute + “past” + current hour
- for saying "15 minutes past":
> “It is” + “quarter past” + current hour
- when we are in the second quarter:
> “It is” + minute + “to” + “half” + next hour
- for saying "30 minutes past":
> “It is” + “half” + next hour
- when we are in the third quarter:
> “It is” + minute + “past” + “half” + next hour
- for saying "15 minutes to":
> “It is” + “quarter to” + next hour
- when we are in the fourth quarter:
> “It is” + minute + “to” + next hour

Where the minute is the amount of minutes to/past the corresponding quarter. The words in quotation marks are the equivalent translation of the words inside of quotation marks in Dutch.
### Farsi
Saying time in Farsi is generally like:
> "hour" + hour + "and" + minute + "minute" + "it is"

But there are also some exceptions that can be said in different ways which we used them in our clock. for example:
- for when " 0 minutes" we use the following sentence:
> “hour” + hour + “it is”
- for saying "15 minutes past":
> “hour” + hour + “and” + “quarter past” + “it is”
- for saying "30 minutes past":
> “hour” + hour + “and” + “half past” + “it is”
- for saying "15 minutes to":
> “hour” + “quarter to” + next hour + “it is”

Where the hour is the current time and minute is the current minute. The words in quotation marks are the equivalent translation of the words inside of quotation marks in Farsi.
## GDPR 
The recordings are from the two creators and we have signed a consent form and consent for their voices to be on this repository.

