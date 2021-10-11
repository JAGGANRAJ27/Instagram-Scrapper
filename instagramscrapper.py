from instagram_scraper import InstagramScraper
scraper = InstagramScraper(usernames = [''])
scraper.authenticate_as_guest()
scraper.scrape()