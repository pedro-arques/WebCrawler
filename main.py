import Crawler
import Conexao

if __name__ == '__main__':
    crawler = Crawler.Application()
    connection = Conexao.Connection()

    crawler.navigation(crawler.URL)
    data = crawler.formatting(crawler.cardInfo(), crawler.scoreInfo())
    crawler.navigationClose()

    connection.conexaoDatabase()
    connection.insertData(data)
