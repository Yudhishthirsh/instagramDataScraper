
#Instagram Credentials'
#Instagram_username = "Enter_Instagram_Username"
Instagram_username = "yudhishthirsharma11"
#Instagram_password = "Enter_Instagram_Password"
Instagram_password = "Qazxsw@321"
#Hashtag from which need to scrape data
Instagram_Hashtag = "rentinnoida"

# Define the Random file name
length = 5
# Generate a random string
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Get the current timestamp
timestamp = time.strftime("%Y%m%d%H%M%S")
fileName = timestamp + random_string + '.csv' #this the generated filename
print("Your output file is: ",fileName )

