#######################################################################################################

WEBSCRAPING PROJECT USING SCRAPY

In this project , i use scrapy to extract all books from :  https://books.toscrape.com/

The differents informations that i extract are:   Name, Price and Book cover or image

After that I store all informations to csv file


To complile this project in your local machine,  you should have this package installed:    scrapy
  - after that you can create or not a virtual environment
  -so you are now free to compile it 

For compilation , you have two options:   
  -compile juste the spider and see the result in your terminal with this command:   scrapy crawl books
  -or compile and convert it to csv file automaticaly with this command:   scrapy crawl books -o 'name of your file'.csv
  (you should replace 'name of you file' by your preference basename that you want to provide to your csv file)

You have an example csv file named 'books.csv' in the directory of the project, so after testing it , you can compare your result with it. 

###############################################################################################################