import scrapy
import requests

class JobSpider(scrapy.Spider):
    name='jobs'
    start_urls=['https://www.dice.com/jobs?q=Software&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.postedDate=ONE&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&currencyCode=USD&language=en']

    def parse(self,response):
        for job in response.css('.job'):
            job_title=job.css('.company_and_position h2::text').get()
            company=job.css('.company::text').get()
            loaction=job.css('.location::text').get()
            compensation=job.css('.salary::text').get(default='Not Mentioned')
            skills=', '.join(job.css('.tags span::text').getall())
            job_details=job.css('.description::text').get()

            
            job_data={
                "job_title":job_title,
                "company":company,
                "location":loaction,
                "compensation":compensation,
                "skills":skills,
                "job_details":job_details,
                "posted_at":"2024-12-20T10:00:00Z",
                "updated_at":"2024-12-20T10:00:00Z",
                "location_type":"Remote",
                "employment_type":"Full Time"
            }

            requests.post('http://127.0.0.1:8000/api/jobs/', json=job_data)
