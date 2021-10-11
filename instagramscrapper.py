from instagram_scraper import InstagramScraper
scraper = InstagramScraper(usernames = ['']) #enter Insta ID in single qoutes
scraper.authenticate_as_guest()
scraper.scrape()