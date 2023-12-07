import httpx
from parsel import Selector
import asyncio


class AsyncNewsScraper:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        # 'Referer': 'https://www.prnewswire.com/news-releases/',
        'Connection': 'keep-alive',
    }
    MAIN_URL = "https://www.ts.kg/"
    LINK_XPATH = '//div[@class="app-shows-item-full"]/a/@href'
    PLUS_URL = 'https://www.ts.kg'
    IMG_XPATH = '//div[@class="app-shows-item-full"]/a/img/@src'


    async def async_generator(self, limit):
        for page in range(1, limit + 1):
            yield page

    async def parse_pages(self):
        async with httpx.AsyncClient(headers=self.headers) as client:
            async for page in self.async_generator(limit=3):
                await self.get_url(
                    client=client,
                    url=self.MAIN_URL.format(
                        page=page
                    )
                )

    async def get_url(self, client, url):
        response = await client.get(url=url)
        print('response: ', response)
        await self.scrape_responses(response)

    async def scrape_responses(self, response):
        tree = Selector(text=response.text)
        links = tree.xpath(self.LINK_XPATH).extract()
        for link in links:
            print('PLUS_URL: ', self.PLUS_URL + link)


if __name__ == '__main__':
    scraper = AsyncNewsScraper()
    scraper.parse_pages()