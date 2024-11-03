## Inspiration
After discovering that our stomachs are often larger than our wallets, we set out to find a way to make shopping more efficient and meaningful. We wanted to prove that with proper planning you can eat well without breaking the bank. 

## What it does
Each morning our bot _manually_ goes through Food Lion's website taking note of items on sale. We store each sale item in MongoDB, along with the discount amount and original price. We then configure Spoonacular's REST API to generate recipes that optimize the number of items on sale called for in the instructions. Each recipe is stored as a MongoDB document and presented on the website. 

## How we built it
We built a Selenium agent to visit Food Lion's website and record information on sale items and discount percentages. Then, the data is sent by FastAPI to MongoDB where the ingredients and their metadata are stored as documents. We created API endpoints that are automatically triggered each morning to repeat scraping to ensure fresh data and generate recipes through the use of Spoonacular's API. Each call to Spoonacular requires a list of ingredients and returns JSON data describing possible recipes and the number of ingredients it was able to match from the input in its response. Using this ratio, we calculate the savings and send the information to our Next.js front end.

## Challenges we ran into
Food Lion, the grocery store we targeted our project at, uses a dynamically loaded website, making traditional static web scrappers useless on their own. To parse the HTML for data we had to pivot towards Selenium, building and leveraging an agent to manually interact with the page and scrape the data one page request at a time. 

## Accomplishments that we're proud of
The scope of the project is large for the amount of time we've set aside to complete it. We're proud of the level of professionalism we've been able to put into an endeavor of this size and at such speed. We're also proud of the difficulty level of the project, particularly the web scraper, and that we've been able to push our technical ability. 

## What we learned
It's very easy to be narrow-minded when coming up with your tech stack. Both of us came into this project with personal preferences and our own ways of doing things, but the challenges we faced during the time crunch helped us learn how to adapt to the situation on the fly. Albeit jumping ship from Flask to FastAPI early on in the process or discovering that **every** grocery website is dynamically loaded, we learned to pivot quickly while moving at full throttle towards the finish line. 

## What's next for Budget Bites
We believe that big brands like Walmart and Target encode store locations in the URL of their website so people can log on and see the items on sale for their given area. We plan to take Meals For Less one step further by allowing you to share your location, choose the stores near you, and get specialized results for regional sales. We also have plans to optimize the suggestion of recipes further by giving higher promotions to meals that help you save more on our website. 
