import requests


class NewsRelated:
    def __init__(self, company_name, day2, day1):
        self.news_api_url = "https://newsapi.org/v2/everything"
        self.news_api_key = "aa1576800d72490292afe75ae8e76eeb"
        self.news_params = {
            "apiKey": self.news_api_key,
            "qInTitle": company_name,
            "from": day2,
            "to": day1,
            "sortBy": "relevancy",
        }
        self.final_data = self.news()

    def news(self):
        final_data = []
        with requests.get(self.news_api_url, params=self.news_params) as response_news:
            response_news.raise_for_status()
            data = response_news.json()
            three_news = data["articles"][:3]
        for news in three_news:
            final_data.append({
                "title": news['title'],
                "description": news['description'],
                "url": news['url']
            })
        return final_data
