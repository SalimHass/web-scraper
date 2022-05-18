# Web Scraping

in this lab we want to get the Citations needed from each pargraph and print that paragrph

## method

1. we created a new project 
2. we used poetry add requests
3. we used poetry add bs4
4. in the code file we imported requests 
5. from bs4 import BeatufulSoup
6. added the url we wanted to work with
7. we used requests.get(url) to get object from the url
8. we used BeautifulSoup(page.content, "html.parser") to get the content of the page and to be able to work with it as html
9. we used findAll("a", title="Wikipedia:Citation needed"), which will collect all the "a" tags that has a title = "Wikipedia:Citation needed" int then and return them as a list 
10. by printing the length of the lest above we get the number of paragaraphes that has citation needed in them
11. we def new function for the citation report
12. we used the same as before but we used findAll('p') to get all the p tags .
13. we declared result=""-> empty string
14. if the 'p' tag has an 'a' tag with the citation needed we added the text of that 'p' to the result 
15. we returned the result 
----
## Pull request
https://github.com/SalimHass/web-scraper/pull/1
