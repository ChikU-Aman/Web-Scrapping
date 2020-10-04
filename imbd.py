import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
def exactmovie(url):
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page = soup(page_html,"html.parser")
	rating = page.find("div",{"class":"ratingValue"})
	return (rating.strong.span.text) 
def urls(queries):
	queries=queries.replace(" ","+")
	url = 'https://www.imdb.com/find?q='+queries+'&ref_=nv_sr_sm'
	return url
def movie(url):
	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()
	page = soup(page_html,"html.parser")
	exact_url = 'https://www.imdb.com/'
	container = page.find("td",{"class":"result_text"})
	exact_url = exact_url + container.a['href'][1:]
	return exact_url
if __name__ == '__main__':
	queries=input()
	url  = urls(queries)
	exact_url = movie(url)
	rating = exactmovie(exact_url)
	print("Rating of the {} : {}".format(queries,rating))