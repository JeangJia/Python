from platform import release

from lxml import html
import requests
import csv

MOVIE_LIST_FILE = '20 movie.csv'
URL = 'https://www.themoviedb.org/movie/top-rated'  # 第一页(前20)
URL_2 = 'https://www.themoviedb.org/discover/movie/items'  # 第二页(后80)
ind = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


# 获得各个电影信息
def get_movie_info(url):
    global ind
    print(f"{ind}. 发送请求：{url},请求数据中...")
    ind += 1
    ret = requests.get(url, headers=headers, timeout=60)
    doc = html.fromstring(ret.text)
    name = doc.xpath('/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/a/text()')  # 电影名称
    year = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/h2/span/text()')  # 上映年份
    date = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[@class="release"]/text()')  # 上映时间
    tag = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[@class="genres"]/a/text()')  # 电影标签
    time = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[1]/div/span[@class="runtime"]/text()')  # 电影时长
    scores = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[2]/div/div/div[1]/div/div[1]/div/div/@data-percent')  # 评分
    language = doc.xpath(
        '/html/body/div[1]/main/section/div[3]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')  # 语言
    authors = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()')  # 作者
    protagonist = doc.xpath(
        '/html/body/div[1]/main/section/div[3]/div/div/div[1]/div/section[2]/div/ol/li[1]/p[1]/a/text()')  # 主演
    slogans = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/h3[1]/text()')  # 标语
    description = doc.xpath(
        '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[3]/div/p/text()')  # 描述
    # print(name, year, date, tag, time, scores, language, authors, protagonist, slogans, description)
    movie_info = {
        '电影名': name[0].strip() if name else '',
        '上映年份': year[0].strip() if year else '',
        '上映时间': date[0].strip() if date else '',
        '标签': ','.join(tag) if tag else '',
        '时长': time[0].strip() if time else '',
        '评分': scores[0].strip() if scores else '',
        '语言': language[0].strip() if language else '',
        '作者': ','.join(authors) if authors else '',
        '主演': ','.join(protagonist) if protagonist else '',
        '标语': slogans[0].strip() if slogans else '',
        '描述': description[0].strip() if description else ''
    }
    return movie_info


# 保存电影信息
def save_movie_info(all_movies):
    print('正在保存数据...')
    with open(MOVIE_LIST_FILE, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f,
                                fieldnames=['电影名', '上映年份', '上映时间', '标签', '时长', '评分', '语言', '作者',
                                            '主演', '标语', '描述'])
        writer.writeheader()  # 写入表头
        writer.writerows(all_movies)  # 写入数据


def main():
    all_movies = []
    for page_num in range(1, 6):
        if page_num == 1:
            ret = requests.get(URL, headers=headers, timeout=60)
        else:
            ret = requests.post(URL_2,
                                data=f"air_date.gte=&air_date.lte=&certification=&certification_country=US&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={page_num}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2026-12-20&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=US&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                headers=headers, timeout=60)
        doc = html.fromstring(ret.text)
        # 获得电影链接
        movie_url_list = doc.xpath(
            f"//*[@id='page_{page_num}']//div[contains(@class, 'poster-card')]//div[contains(@class,'relative')]/a/@href")
        movie_url_list = [f'https://www.themoviedb.org{href}' for href in movie_url_list]
        for url in movie_url_list:
            movie_info = get_movie_info(url)
            all_movies.append(movie_info)
    save_movie_info(all_movies)
    print('保存成功！')


if __name__ == '__main__':
    main()
