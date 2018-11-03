from icrawler.builtin import GoogleImageCrawler

def google_image_crawl(directory='lena', keyword='lena', max_num=500):
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': directory})
    google_crawler.crawl(keyword=keyword, max_num=max_num, min_size=(200,200), max_size=None)

google_image_crawl(directory='images', keyword='blue signs', max_num=400)
