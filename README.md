# instagramDataScraper
This is the Instagram Scraping Framework which can be able to scrape publicly available data that is available on particular instagram hashtags pages.
--

Using this script following data can be scraped from the hashtag pages:

  --Username
  
  --Full Name
  
  --Followers
  
  --Following
  
  --Biography
  
  --Private(Is account is private or not)
  
  --Verified User or not
  
  --Number of Posts an user posted
  
  --Liked
  
  --Comment
  
  This script supports linux, windows OS.
  
  
  
The script description is mentioned below
--

1)Open the project and go to the InstagramHashtagDataScraper in your windows terminal or on linux operating system.

2)Install all the required python packages using below command:

       pip install -r requirements.txt

3)Now go to the project directory using command below:

       cd .\InstagramHashtagDataScraper\
       
4)After reaching InstagramHashtagDataScraper directory run below command to create the Python path over all the directories and files in the project.

    a) Command for Windows OS:

            command = $env:PYTHONPATH = "Absolute Path of Directory;$env:PYTHONPATH" # Abslolute path of this "InstagramHashtagDataScraper" directory
          
            While entering Absolute path of the directory ensure to change backword Slash (/) into forward slash(\) inside the path in case when running in windows machine.
    
    b) Command for linux OS:
    
            Command : export PYTHONPATH="Absolute Path of Directory" # Abslolute path of this "InstagramHashtagDataScraper" directory i your linux machine
          
            In this case there is no need to change backward slash.

5)To scrape data from hashtag you need a instagram login. Need to add your credentials in parameter.py file
 
    a)Instagram_username = "Enter_Instagram_Username"
 
    b)Instagram_password = "Enter_Instagram_Password"
    
    c)Instagram_Hashtag = "Enter_Hashtag" (for eg.rentinnoida) #Hashtag from which need to scrape data

6)Now Go to the scraperSkeleton(outer) directory using command in terminal mentined below
 
              Command : cd .\scraperSkeleton\

7)After reaching to the scraperSkeleton directory Run following command in terminal.

              Command : scrapy crawl InstagramCrawler --nolog

8)The outputfile of the scraped records is generated inside scraperSkeleton(outer) folder having random name which has nomenclature as given below.
      
      Output File name exaample : 20230518142546cfzl3.csv,
      
      a) Where 20230518 is the date on which file is created
      
      b) Where 142546 followed by date is the time at which the file is created.
      
      c) After time there are 5 alphanumeric characters

Notes:

1)If you got the Login Checkpoint Exception then try to login to instagram Manually in the browser and it will ask for change your password.change your password and now try 
to run the code if you got the same error again then try again using different set of credentials

2)Instagram have their robot to detect the automated script scraping data from their website after certain no of request it starts give 409 (Too Many Request)/Bad Request in that case you can change the credentials
