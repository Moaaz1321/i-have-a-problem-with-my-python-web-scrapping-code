import requests

from  bs4 import BeautifulSoup
date =input("enter the date")

page=requests.get(f"https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa?date={date}#matchesclipPrev")

def main(page): 
    
    src=page.content
    print(src)
main(page)