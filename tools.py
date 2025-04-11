from crewai_tools import ScrapeWebsiteTool


def get_scraper_tool():
    return ScrapeWebsiteTool(
        website_url="https://techcrunch.com/category/artificial-intelligence/",
        extract="text",
        browser="chromium"
    )