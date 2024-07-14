import asyncio
from pyppeteer import launch
from loguru import logger
import json

async def download_video(url):
    # Launch a headless browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    try:
        logger.info(f"Opening URL: {url}")
        # Open the URL
        await page.goto(url)
        
        # Get the title of the page
        title = await page.title()
        logger.info(f"Page title: {title}")
        
        # Wait for the video element to be available
        await page.waitForSelector('video', {'timeout': 5000})
        
        # Get the video source URL
        video_source_url = await page.evaluate('''() => {
            const videoElement = document.querySelector('video');
            return videoElement ? videoElement.src : null;
        }''')

        if video_source_url:
            logger.info(f"Found video source URL: {video_source_url}")
            # Navigate to the video source URL
            await page.goto(video_source_url)
            
            # Wait for some time (adjust as necessary)
            await asyncio.sleep(5)  # Wait for 5 seconds (adjust this if needed)
            
            # Get the current URL (which should be the direct video URL)
            current_url = page.url
            logger.info(f"Current video URL: {current_url}")
            
            # Return JSON with title and url
            result = json.dumps({"title": title, "url": current_url})
            print(result)
            return result
        else:
            logger.warning("No video element found on the page")
            return None

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        await browser.close()
        logger.info("Browser closed")

# # Example usage
# url = 'https://xgroovy.com/shemale/videos/360473/petite-slim-busty-asian-tranny-in-a-cosplay-costume-enjoys-her-bf-s-ass-after-sucking-his-cock'
# asyncio.run(download_video(url))
