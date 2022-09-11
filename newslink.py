import feedparser
import sqlite3 as sql
import urllib.request as urllib2
from bs4 import BeautifulSoup as bs

link_scrap = []
keywords = []
scrapper_link = []
description = ''

class Scrapper():
# Creates Database Connection
    def create_connection(self):
        database = 'C:\\Users\\aditi\\OOAD\\db.sqlite3'
        return sql.connect(database)


# Go to the topic page of the timesofIndia and filter out all the topics and their respective RSS links
    def scrap_rss_page(self):
        page = 'https://timesofindia.indiatimes.com/rss.cms'
        page_content = urllib2.urlopen(page)
        soup = bs(page_content)
        div_content = soup.find_all("div", id='main-copy')
        count = 0
        for tag in div_content:
            tdtags = tag.find_all("td")
            # count = count+1
            for tag in tdtags:
                # print tag,' ',count
                for link in tag.select('.rssurl'):
                    scrapper_link.append(link['href'])
                # print link['href']
                if tag.text != '' and tag.text != 'More':
                    keywords.append(tag.text)
                    # print ''.join(map(str,div_content.contents))
                    # print keywords

                    print (scrapper_link,keywords)
                    for i in range(62):
                        if 'Most' in keywords[i]:
                            pass
                        else:
                            self.parse_rss(scrapper_link[i], keywords[i])


# print len(keywords)
# print scrapper_link
# print len(scrapper_link)


# parse rss_link of each page and save the required xml tags in the list news details
    def parse_rss(self,link, tag):
        # if(tag != 'Most Read' or tag != 'Most Shared' or tag !='Most Commented'):1
        d = feedparser.parse(link)
        news_details = []
        # count=count_rows_indb().fetchone()[0];

        for post in d['entries']:
            # print count
            # try:
            description = self.beautiful_soup(post.link)
            print('Printing', description)
            news_details.append([post.title, description, post.link, post.published, tag, 0])
        # post.title + " :: " + post.published + " :: " + post.description.replace("'","''") + " :: "+post.link
        # count=count+1
        # print news_details
        # except Exception as e:
        #	print tag

        self.store(news_details);


# from the news_details list store the required topics from xml in the db
    def store(self,news_details):
        con = self.create_connection();
        c = con.cursor()
        c.executemany('INSERT INTO newsapp_topstories (title,desc,link,published,tag,status) VALUES (?,?,?,?,?,?);',
                      news_details)

        con.commit()
        con.close()


# Find each link from the databases for a particular page
# def find_link():
#	con=create_connection()
#	c=con.cursor()
#	for row in c.execute('SELECT * FROM newsapp_topstories'):
#		link_scrap.append(row[3])
#	#return link_scrap
#	scrapper();

# scrap data from each link of the page
# def scrapper():
# count =0;
#	for each_link in link_scrap:
# print each_link
#		beautiful_soup(each_link)
# count=count+1;

    def beautiful_soup(each_link):
        page = each_link
        try:
            page_content = urllib2.urlopen(page)
        except Exception as e:
            print(page, "Something Bad Happened !")
        else:
            soup = bs(page_content)
            content = ""
            div_content = soup.find_all('div', {'class': "article_content clearfix"})
            for wrapper in div_content:
                content = wrapper.text

                # image = soup.find('img')['src']
                # print image
                # image_section = soup.find_all('section',{'class' : "highlight clearfix"})
                # image="https://timesofindia.indiatimes.com"
                # for image_src in image_section:
                # image+=image_src.find('img')['src']
        return content


# print description
# save_image_link(content,each_link,image)

# Save the scraped image and content of news paper in the database
# def save_image_link(content,each_link,image):
#	con=create_connection()
#	c=con.cursor()
# print 'Printing Content:',content
#	project = (content,each_link,image)
#	c.execute('INSERT INTO newsapp_content_image(desc,link,image_link) VALUES (?,?,?);',project)
# c.executemany('INSERT INTO newsapp_topstories (title,desc,link,published,tag,status) VALUES (?,?,?,?,?,?);',news_details)
#	con.commit()
#	con.close()

    def main(self):
        self.scrap_rss_page()


# parse_rss();

# find_link();


if __name__ == '__main__':
    webscrapper = Scrapper();
    webscrapper.main()
