#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[50]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[9]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[10]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[11]:


slide_elem.find('div', class_='content_title')


# In[12]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[13]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[14]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[15]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[64]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[65]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# hemisphere_image_urls = [{'title': 'Cerberus Hemisphere Enhanced', 'img_url':'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},
#                         {'title': 'Schiaparelli Hemisphere Enhanced', 'img_url':'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},
#                         {'title': 'Syrtis Major Hemisphere Enhanced', 'img_url':'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},
#                         {'title': 'Valles Marineris Hemisphere Enhanced', 'img_url':'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]


html = browser.html
mars_soup = soup(html, 'html.parser')


# In[66]:


mar_div = mars_soup.find_all('div', class_='item')
# print(mar_div[0])


# In[67]:


# mar_div[0].find('a')['href']


# In[68]:


# mar_div[0].find('h3').text


# In[69]:


# url+mar_div[0].find('a')['href']


# In[70]:


# browser.visit(url+mar_div[0].find('a')['href'])
# new_h = browser.html
# mars_soup = soup(new_h, 'html.parser')


# In[71]:


# npu = mars_soup.find('div', class_='downloads')
# print(npu)
# imgn = npu.find('a')['href']
# print(imgn)


# In[72]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
for mar in mar_div:
    mar_url = mar.find('a')['href']
    print(mar_url)
    mar_title = mar.find('h3').text
    print(mar_title)
    mar_info_url = url+mar_url
    print(mar_info_url)
    browser.visit(mar_info_url)
    mar_info_html = browser.html
    mars_soup = soup(mar_info_html, 'html.parser')
    mar_img_div = mars_soup.find('div', class_='downloads')
    mar_img_url = mar_img_div.find('a')['href']
    print(mar_img_url)
    full_mar_url = url + mar_img_url
    
    mar_list = dict({'title':mar_title,
                  'img_url':full_mar_url})
    
    hemisphere_image_urls.append(mar_list)
    


# In[73]:


hemisphere_image_urls


# In[ ]:





# In[18]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[74]:


# 5. Quit the browser
browser.quit()


# In[ ]:




