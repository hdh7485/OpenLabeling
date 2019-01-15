from icrawler.builtin import GoogleImageCrawler

def google_image_crawl(directory='lena', keyword='lena', max_num=500):
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': directory})
    google_crawler.crawl(keyword=keyword, max_num=max_num, min_size=(200,200), max_size=None, file_idx_offset='auto')

for keyword in ['red signs', 'blue signs']:
    google_image_crawl(directory='images', keyword=keyword, max_num=1000)
