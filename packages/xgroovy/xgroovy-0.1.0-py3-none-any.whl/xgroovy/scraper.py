import asyncio
from pyppeteer import launch
import json

async def scrape_videos(query):
    # Launch a headless browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Navigate to the target webpage with the query parameter
    await page.goto(f"https://xgroovy.com/search/{query}")

    # Wait for the page to load (you might need to add explicit wait strategies here if content loads dynamically)
    await page.waitForSelector('.list-videos .item', {'timeout': 5000})

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

    # Convert to JSON format
    json_data = json.dumps(videos_data, indent=2)

    # Release the resources and close the browser
    await browser.close()
    # print(json_data)
    return json_data


# # # Running the scrape_videos function
# query = 'cosplay'
# asyncio.get_event_loop().run_until_complete(scrape_videos(query))
