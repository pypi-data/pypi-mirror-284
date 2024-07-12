import asyncio
from pyppeteer import launch

async def download_video(url):
    # Launch a headless browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    try:
        # Open the URL
        await page.goto(url)
        
        # Wait for the video element to be available
        await page.waitForSelector('video', {'timeout': 5000})
        
        # Get the video source URL
        video_source_url = await page.evaluate('''() => {
            const videoElement = document.querySelector('video');
            return videoElement ? videoElement.src : null;
        }''')

        if video_source_url:
            # Navigate to the video source URL
            await page.goto(video_source_url)
            
            # Wait for some time (adjust as necessary)
            await asyncio.sleep(5)  # Wait for 5 seconds (adjust this if needed)
            
            # Get the current URL (which should be the direct video URL)
            current_url = page.url
            print(current_url)
            return current_url
        else:
            print("No video element found on the page")
            return None
    
    finally:
        # Close the browser
        await browser.close()

# Example usage
url = 'https://xgroovy.com/shemale/videos/360473/petite-slim-busty-asian-tranny-in-a-cosplay-costume-enjoys-her-bf-s-ass-after-sucking-his-cock'
asyncio.run(download_video(url))
