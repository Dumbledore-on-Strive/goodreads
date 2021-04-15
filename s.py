#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('pip install bs4==0.0.1')


# In[121]:


#important libraries
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests as rq


# # Web Scrapping 

# In[ ]:


#url - str done
 # title - str done
 # author - str done 
 # num_reviews - int done
  # num_ratings - int done 
  # avg_rating - float done 
  # num_pages - int done
  # original_publish_year - int done 
  # series - bool done 
  # genres - str doen 
  # awards - str done 
  # places str done 


# # 

# In[122]:



base_url = 'https://www.goodreads.com/list/show/1043.Books_That_Should_Be_Made_Into_Movies'

def get_books_url_per_page(base_url, tag, tag_class):

    book_url_list = []
    base_page = rq.get(base_url)
    base_content = BeautifulSoup(base_page.content, 'html.parser')

    for a in base_content.find_all(tag, class_= tag_class):
        book_url_list.append('https://www.goodreads.com/' + a['href'])
    
    return book_url_list


def get_base_page_list(base_url, n):
    base_page_list = []
    for i in range(n):
        base_page_list.append(base_url + str(i + 1))
    
    return base_page_list

whole_book_url_list = []

for link in get_base_page_list('https://www.goodreads.com/list/show/1043.Books_That_Should_Be_Made_Into_Movies?page=', 3):
    whole_book_url_list.append(get_books_url_per_page(link, 'a', 'bookTitle'))

whole_book_url_list = [link for subs in whole_book_url_list for link in subs]


# In[123]:


whole_book_url_list


# In[124]:


def get_data_frame(links):
    data_frame=[]
    for url  in  links:
        page_html = rq.get(url)
        page_soup = BeautifulSoup(page_html.content, 'html.parser')
        title=get_title(page_soup)
      
        author=get_author(page_soup)
      
        num_rating=get_num_rating(page_soup)
       
        num_reviews=get_num_reviews(page_soup)
       
        avg_rating=get_avg_rating(page_soup)
        
        num_pages=get_num_pages(page_soup)
      
        original_publish_year=get_original_publish_year(page_soup)
        
        series=get_series(page_soup)
       
        genres=get_genres(page_soup)
       
        award=get_award(page_soup)
       
        place=get_place(page_soup)
        dictionary={
            "title": title,
            "author": author,
            "num_rating": num_rating,
            "num_reviews": num_reviews,
            "avg_rating": avg_rating,
            "num_pages": num_pages,
            "original_publish_year": original_publish_year,
            "series": series,
            "genres": genres,
            "award": award,
            "place": place,
            "url": url
        }
        data_frame.append(dictionary)
    return data_frame


# In[ ]:


data=get_data_frame(whole_book_url_list)


# In[ ]:


df = pd.DataFrame(data)
  
# saving the dataframe
df.to_csv('df.csv')


# for Test  

# In[127]:


# page_html = rq.get("https://www.goodreads.com//book/show/1582996.City_of_Ashes")
# i = BeautifulSoup(page_html.content, 'html.parser')
# print(i)
i="https://www.goodreads.com//book/show/618177.Legend"


# In[67]:


def getlink(i):
    
    data_frame=[]
    page_html = rq.get(i)
    page_soup = BeautifulSoup(page_html.content, 'html.parser')
    title=get_title(page_soup)
      
    author=get_author(page_soup)
      
    num_rating=get_num_rating(page_soup)
       
    num_reviews=get_num_reviews(page_soup)
       
    avg_rating=get_avg_rating(page_soup)
        
    num_pages=get_num_pages(page_soup)
      
    original_publish_year=get_original_publish_year(page_soup)
        
    series=get_series(page_soup)
       
    genres=get_genres(page_soup)
       
    award=get_award(page_soup)
       
    place=get_place(page_soup)
    dictionary={
            "title": title,
            "author": author,
            "num_rating": num_rating,
            "num_reviews": num_reviews,
            "avg_rating": avg_rating,
            "num_pages": num_pages,
            "original_publish_year": original_publish_year,
            "series": series,
            "genres": genres,
            "award": award,
            "place": place,
            "url": i
    }
    data_frame.append(dictionary)
    return data_frame


# In[68]:


getlink(i)


# In[ ]:





# #                                                      To define all functions

# In[115]:



def get_title(page_soup):
    try :
        title = page_soup.find('h1', {"id":"bookTitle"}).text.strip()
        return title
    except:
        return np.nan


# In[116]:


def get_author(page_soup):
    try :
        author = page_soup.find("a", {"class":"authorName"}).text.strip()
        return author
    except:
        return np.nan


# In[117]:


def get_num_rating(page_soup):
    try :
        num_rating=page_soup.find(itemprop="ratingCount").text.strip().replace("ratings", "").replace(",", "")
        return int(num_rating)
    except:
        return np.nan


# In[118]:


def get_num_reviews(page_soup):
    try :
        num_review=page_soup.find(itemprop="reviewCount").text.replace("reviews", "").replace(",", "").strip()
        return int(num_review)
    except:
        return np.nan


# In[119]:


def get_avg_rating(page_soup):
    try :
        avg_rating=page_soup.find("span", itemprop="ratingValue").text.strip()
        return float(avg_rating)
    except:
        return np.nan


# In[120]:


def get_num_pages(page_soup):
    try :
        num_pages=int(page_soup.find(itemprop="numberOfPages").text.strip().replace("pages", ""))
        return num_pages
    except:
        return np.nan



# In[108]:


i="https://www.goodreads.com//book/show/618177.Legend"
page_html = rq.get(i)
page_soup = BeautifulSoup(page_html.content, 'html.parser')


# In[126]:


def get_original_publish_year(page_soup):
    
        original_publish_year=page_soup.find_all("div", class_="row")[1].text.split()
        for i in original_publish_year[:4]:
            if i.isnumeric()==True:
                return  int(i)
            
            
    



# In[110]:


get_original_publish_year(page_soup)


# In[111]:


def get_series(page_soup):
    
        
        series = page_soup.find(id="bookSeries").text.strip() 
        if len(series)!= 0:
            return True
        else: 
            return False
    
  


# In[112]:


def get_genres(page_soup):
    try:
        g_list=[]
        genres = page_soup.find('div',class_="rightContainer").find_all(class_="left")
        for row in genres:
            row=row.text.replace(">","").strip().split()
            row=" ".join(row)
            g_list.append(row)
        return g_list
    except:
        return np.nan    
   
    


# In[113]:


def get_award(page_soup):
    try:
        count=0
        awards = page_soup.find("div", {"itemprop": "awards"}).find_all('a')
        for award in awards:
            if award!=None:
                count+=1
        return int(count)
    except:
        return np.nan


# In[114]:


def get_place(page_soup):
    try:
        place = page_soup.find("div", {'id':"bookDataBox"}).find('span',class_="darkGreyText").text.replace("(","").replace(")","").strip()
        return str(place)
    except:
        return np.nan


# # End of Functions

# #Data frame creation

# In[ ]:


df = pd.DataFrame({'url': whole_book_url_list, ''})
print(df)
#df.to_csv('goodread.csv', index=False)


# <a style='text-decoration:none;line-height:16px;display:flex;color:#5B5B62;padding:10px;justify-content:end;' href='https://deepnote.com?utm_source=created-in-deepnote-cell&projectId=8aa7b630-9ed2-4356-9070-0a10a3a5f060' target="_blank">
# <img alt='Created in deepnote.com' style='display:inline;max-height:16px;margin:0px;margin-right:7.5px;' src='data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iODBweCIgaGVpZ2h0PSI4MHB4IiB2aWV3Qm94PSIwIDAgODAgODAiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayI+CiAgICA8IS0tIEdlbmVyYXRvcjogU2tldGNoIDU0LjEgKDc2NDkwKSAtIGh0dHBzOi8vc2tldGNoYXBwLmNvbSAtLT4KICAgIDx0aXRsZT5Hcm91cCAzPC90aXRsZT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9IkxhbmRpbmciIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJBcnRib2FyZCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEyMzUuMDAwMDAwLCAtNzkuMDAwMDAwKSI+CiAgICAgICAgICAgIDxnIGlkPSJHcm91cC0zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjM1LjAwMDAwMCwgNzkuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8cG9seWdvbiBpZD0iUGF0aC0yMCIgZmlsbD0iIzAyNjVCNCIgcG9pbnRzPSIyLjM3NjIzNzYyIDgwIDM4LjA0NzY2NjcgODAgNTcuODIxNzgyMiA3My44MDU3NTkyIDU3LjgyMTc4MjIgMzIuNzU5MjczOSAzOS4xNDAyMjc4IDMxLjY4MzE2ODMiPjwvcG9seWdvbj4KICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0zNS4wMDc3MTgsODAgQzQyLjkwNjIwMDcsNzYuNDU0OTM1OCA0Ny41NjQ5MTY3LDcxLjU0MjI2NzEgNDguOTgzODY2LDY1LjI2MTk5MzkgQzUxLjExMjI4OTksNTUuODQxNTg0MiA0MS42NzcxNzk1LDQ5LjIxMjIyODQgMjUuNjIzOTg0Niw0OS4yMTIyMjg0IEMyNS40ODQ5Mjg5LDQ5LjEyNjg0NDggMjkuODI2MTI5Niw0My4yODM4MjQ4IDM4LjY0NzU4NjksMzEuNjgzMTY4MyBMNzIuODcxMjg3MSwzMi41NTQ0MjUgTDY1LjI4MDk3Myw2Ny42NzYzNDIxIEw1MS4xMTIyODk5LDc3LjM3NjE0NCBMMzUuMDA3NzE4LDgwIFoiIGlkPSJQYXRoLTIyIiBmaWxsPSIjMDAyODY4Ij48L3BhdGg+CiAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMCwzNy43MzA0NDA1IEwyNy4xMTQ1MzcsMC4yNTcxMTE0MzYgQzYyLjM3MTUxMjMsLTEuOTkwNzE3MDEgODAsMTAuNTAwMzkyNyA4MCwzNy43MzA0NDA1IEM4MCw2NC45NjA0ODgyIDY0Ljc3NjUwMzgsNzkuMDUwMzQxNCAzNC4zMjk1MTEzLDgwIEM0Ny4wNTUzNDg5LDc3LjU2NzA4MDggNTMuNDE4MjY3Nyw3MC4zMTM2MTAzIDUzLjQxODI2NzcsNTguMjM5NTg4NSBDNTMuNDE4MjY3Nyw0MC4xMjg1NTU3IDM2LjMwMzk1NDQsMzcuNzMwNDQwNSAyNS4yMjc0MTcsMzcuNzMwNDQwNSBDMTcuODQzMDU4NiwzNy43MzA0NDA1IDkuNDMzOTE5NjYsMzcuNzMwNDQwNSAwLDM3LjczMDQ0MDUgWiIgaWQ9IlBhdGgtMTkiIGZpbGw9IiMzNzkzRUYiPjwvcGF0aD4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+' > </img>
# Created in <span style='font-weight:600;margin-left:4px;'>Deepnote</span></a>
