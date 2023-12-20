#inst126 final project attempt 2

import requests 
from bs4 import BeautifulSoup 
import re 
import pandas as pd 
import os 
import matplotlib.pyplot as plt 
import subprocess 

#I will specficy my project folder  
project_folder = 'inst126_final_project_attempt 2'

#now I will try to create the project folder as if it doesn't exists 
if not os.path.exists(project_folder):
    os.makedirs(project_folder)
#now I will move into the project folder 
os.chdir(project_folder)

#README
readme_content= """""
Mental Health Blog Webscrapping 

In this project I utilized a previous blog that I have created in the past. This is a blog that I created that speaks on mental health. 
specifically in this project I decided to webscrape my blog, performing data analysis while utilizing pandas, and in the end I tried to capture this data by utilizing GIT. 

Usage:
To webscrape this program you begin by navigating the folder of the project. The project folder is called inst126_final_project attempt 2.
After navigating the the folder you would have to install the required dependencies which in order to run this program correctly 
These dependencies include: 
- requests (pip install requests) which you would install in your terminal
- beautifulsoup4 (pip install beautifulsoup4)which would also be installed in terminal 
- pandas (pip install pandas)
-  matplotlib. (pip install matplotlib) all installed in terminal.
These downloads install all required packages needed to create the code and run it clearly. 
After doing that we begin the webscraping portion but capturing data analysis, this includes the headline, the title, a graph etc. 
After completing this we would make sure we create a remote repository to run the program and view the results
In the end we would capture the data using Git

"""""
#save README content to README.md file
with open ('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

#create License content 
license_text= """""
#   MIT License 
# Copyright (c) [2023] [Estephany Sanchez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""""
#save license text to License File
with open('License','w') as license_file:
    license_file.write(license_text)

def scrape_blog(url):
 source = requests.get(url).text
 soup = BeautifulSoup(source, 'lxml')

#getting headline
 headline = soup.find('article').h3.a.text if soup.find('article')else 'N/A'
 print("Headline:", headline)

#getting title 
 title = soup.title.text if soup.title else 'N/A'
 print("Title:", title)

#getting text 
 text = soup.find('article').get_text() if soup.find('article') else 'N/A'
 print("Text:", text)

#getting links 
 all_links = [link.get("href") for link in soup.find_all("a")]
 print("Links:", all_links)

#creating a dataframe
 df = pd.DataFrame({'Headline' : [headline], 'Title' : [title], 'Text' : [text], 'Links' : [all_links]})
 print("\nDataFrame:")
 print(df)
 return df 

#function to creat a .gitgnore file 
def create_gitignore():
    try: 
        gitignore_content = ""
        with open ('.gitignore', 'w') as gitignore_file:
            gitignore_file.write(gitignore_content)
        print(".gitignore file created.")
    except Exception as e:
        print(f"Error creating .gitignore file: {e}")

   
#function to initialize a Git repository:
def initialize_git_repository():
    try: 
#run git init command
        subprocess.run(['git', 'init'])
        print("Git repository intialized")
    except Exception as e:
        print(f"Error initialzing Git repository: {e}")

#function to push remote repository
def push_to_remote_repository():
    try:
       subprocess.run(['git', 'push', '-u','origin', 'master'])
       print("Code pushed to remote repository")
    except Exception as e:
       print(f"Error pushing code to remote repository")

#function to add and comit changes 
def add_and_commit(commit_message):
    try:
         subprocess.run(['git','add','.'])
         subprocess.run(['git','commit','-m', commit_message])
         print("Code added and committed to Git repository.")
    except Exception as e:
         print(f"Error adding and committing changes: {e}")
#function to initialize a Git repository
def create_remote_repository():
    try:
        github_username='Stephsanchex2804'
        repo_name='https://github.com/Stephsanchex2804/instproject.git'
        personal_access_token= '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'
        headers = {'Authorization': f'token {personal_access_token}'}
        data = {'name': repo_name, 'auto_init': True}

        response = requests.post(f'https://api.github.com/user/repos', headers=headers,json=data)

        if response.status_code == 201:
           print(f"Remote repository'(rep_name)' created on GitHub.")
        else: 
           print(f"Failed ot create remote repository. Satus code: {response.status_code}")
    except Exception as e:
       print(f"Error pushing code to remote repository: {e}")
#url to scrape 
url_to_scrape= ['https://mentalhealthsteph.blogspot.com/']

create_gitignore()
initialize_git_repository()

#creating an empty dataframe 
master_df = pd.DataFrame(columns=['Headline', 'Title', 'Links'])

#loop through URLs and DataFrame
for url in url_to_scrape: 
    blog_df = scrape_blog(url)

    if blog_df is not None:
      master_df = pd.concat([master_df, blog_df], ignore_index = True)
      
#display final DataFrame
print("\nFinal DataFrame:")
print(master_df)

if not master_df.empty: 
#save dataframe to a CSV file 
   master_df.to_csv('blog_data.csv', index=False)

#Data Analysis 
   print("\nColumn Names:")
   print(master_df.columns)

#calculate the length of each blog post 
if 'Text' in master_df.columns:
    master_df['Text length'] = master_df['Text'].apply(len)


  #display basic statistics 
    print("\nText Length Statistics:")
    print(master_df['Text length'].describe())


#data visualization
    plt.figure(figsize=(10, 6))
    plt.hist(master_df['Text length'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Text Length')
    plt.xlabel('Text Length')
    plt.ylabel('Frequency')
    plt.show()

    add_and_commit("Perform data analysis")
    create_remote_repository()
    push_to_remote_repository()

else:
 print("Column 'Text' not found in the DataFrame")
