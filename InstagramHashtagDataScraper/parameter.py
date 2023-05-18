import random
import string
import time
from datetime import datetime
#Instagram Credentials'
Instagram_username = "Enter Instagram Username"
Instagram_password = "Enter Instagram Password"
#Hashtag from which need to scrape data
Instagram_Hashtag = "Enter The Hashtag"

# Define the Random file name
length = 5
# Generate a random string
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Get the current timestamp
timestamp = time.strftime("%Y%m%d%H%M%S")
fileName = timestamp + random_string + '.csv' #this the generated filename
print("Your output file is: ",fileName )

