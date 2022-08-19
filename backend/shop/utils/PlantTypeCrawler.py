import requests
from bs4 import BeautifulSoup
# from re import findall,compile
from fake_useragent import UserAgent

from ..models import PlantType
 
class PlantTypeCrawler():

    def crawler(self):
        """
        데이터가 많아서 시간 좀 걸려요..
        한..10분..?
        """
        global page_idx
        for page_idx in range(1,420):
            user_agent = UserAgent(verify_ssl=False, use_cache_server=True)
            #  국가생물종지식정보시스템
            url = f"http://www.nature.go.kr/kbi/plant/pilbk/selectPlantPilbkGnrlList.do?mn=&orgId=&pageIndex={page_idx}&searchCnd=&searchWrd=&pageUnit=10"
            header={'User-Agent':user_agent.random}
            response = requests.get(url=url, headers=header)
            if response.status_code == 200:
                html = response.content.decode('utf-8', 'replace')
                soup = BeautifulSoup(html, 'html.parser')
                elements = soup.select("strong.gr")

                for element in elements:
                    plant_type=element.get_text().strip().replace(" ","")
                    PlantType(type=plant_type).save()
            else :
                print(response.status_code)

    def __str__(self):
        return self.plant_type
