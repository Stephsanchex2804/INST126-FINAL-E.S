# INST126-FINAL-E.S
#README
readme_content

Mental Health Blog Webscrapping 

In this project I utilized a previous blog that I have created in the past. This is a blog that I created that speaks on mental health. 
specifically in this project I decided to webscrape my blog, performing data analysis while utilizing pandas, and in the end I tried to capture this data by utilizing GIT. 

Requirements: 
- Python 3.11.4
- Beautifulsoup4
- panda library

Usage:

1. To webscrape this program you begin by navigating the folder of the project. The project folder is called inst126_final_project attempt 
2. once we have navigated the folder and created we have to make sure that we are creating a path for this folder utilizing os
3. After navigating the the folder you would have to install the required dependencies which in order to run this program correctly 
These dependencies include: 
- requests (pip install requests) which you would install in your terminal
- beautifulsoup4 (pip install beautifulsoup4)which would also be installed in terminal 
- pandas (pip install pandas)
-  matplotlib. (pip install matplotlib) all installed in terminal.
3.These downloads install all required packages needed to create the code and run it clearly. 
4. After doing that we begin the webscraping portion but capturing data analysis, this includes the headline, the title, a graph etc.
5. we start by gathering the headline by using soup.find
6. we then continue by trying to get the title of the blog and we use soup.title to capture the title
7. Additionally, we try to gather the links of the blog and we do this by using link.get and soup.find_all
8. After capturing the data of the blog we create a datframe for this information using pandas (pd)

9 . After completing this we would make sure we create a remote repository to run the program and view the results



