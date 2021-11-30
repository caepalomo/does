import scrapy
import os

class DoesSpider(scrapy.Spider):
    name = "diarios"
    direccion_base = 'descargas\\' #Direccion donde se guardaran los documentos descargados
    start_urls = [
        'https://www.diariooficial.gob.sv/diarios/'
    ]

    def save(self, path, data):
        with open(path, 'wb') as f:
            f.write(data)
            self.log(f'Diario guardado en {path}')

    def checkPath(self, mes, year):
        path = os.path.join(self.direccion_base,year)
        if (year not in os.listdir(self.direccion_base)):
            os.mkdir(path)
        if (mes not in os.listdir(path)):
            path = os.path.join(path,mes)
            os.mkdir(path)
        else:
            path = os.path.join(path,mes)
        return path




    def parse(self, response):
        if (response.url.find(".gob.sv") == -1):
            return
        diario = response.url.split("/")[-1]
        if (diario.find(".pdf") == -1):
            for link in response.css('a::attr(href)'):
                print(link)
                next_page = link.get()
                if next_page is not None:
                    next_page = response.urljoin(next_page)
                    yield scrapy.Request(next_page, callback=self.parse)
        else:
            mes = response.url.split("/")[-2]
            year = response.url.split("/")[-3]
            path = os.path.join(self.checkPath(mes,year),diario)
            self.save(path, response.body)
