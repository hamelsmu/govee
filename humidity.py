import datetime, requests
from lxml import html

def get_hourly_humidity(zip):
    "Get historical hourly humidity for the last 3 months for a zip code."
    url = 'http://www.wunderground.com/history/airport/{}/{}/{}/{}/DailyHistory.html'
    url = url.format(zip[0:2], zip[2:5], zip[5:], datetime.date.today().strftime('%Y/%m/%d'))
    page = requests.get(url)
    # print(page.content)
    tree = html.fromstring(page.content)
    rows = tree.xpath('//*[@id="obsTable"]/tbody/tr')
    data = []
    for row in rows:
        data.append([td.text_content() for td in row.xpath('td')])
    return data


if __name__ == '__main__':
    get_hourly_humidity('97229')