import asyncio
from pyppeteer import launch
from loguru import logger
import json

async def scrape_videos(query):
    logger.info(f"Launching browser for query: {query}")
    # Launch a headless browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    try:
        # Navigate to the target webpage with the query parameter
        url = f"https://xgroovy.com/search/{query}"
        logger.info(f"Opening URL: {url}")
        await page.goto(url)

        # Wait for the page to load
        await page.waitForSelector('.list-videos .item', {'timeout': 5000})
        logger.info("Page loaded and video items found")

        # Evaluate the JavaScript to scrape the video elements
        videos_data = await page.evaluate('''() => {
            const video_elements = document.querySelectorAll('.list-videos .item');
            const videos = [];

            video_elements.forEach(video => {
                const thumbnail_url = video.querySelector('img.thumb').src;
                const preview_url = video.querySelector('img.thumb').getAttribute('data-preview');
                const video_url = video.querySelector('.popito').href;
                const title = video.querySelector('.title').textContent;

                videos.push({
                    thumbnail_url: thumbnail_url,
                    preview_url: preview_url,
                    video_url: video_url,
                    title: title
                });
            });

            return videos;
        }''')

        logger.info(f"Scraped {len(videos_data)} videos")

        # Convert to JSON format
        json_data = json.dumps(videos_data, indent=2)
        logger.info("Converted scraped data to JSON format")

        return json_data

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    
    finally:
        # Release the resources and close the browser
        await browser.close()
        logger.info("Browser closed")

# Running the scrape_videos function
# query = 'cosplay'
# result = asyncio.get_event_loop().run_until_complete(scrape_videos(query))
# print(result)
