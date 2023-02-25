from main import Parser

def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.get_html()
    pars.run()



if __name__ == '__main__':
    main()