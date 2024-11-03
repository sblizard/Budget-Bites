## Inspiration
After discovering that our stomachs are often larger than our wallets, we set out to find a way to make shopping more efficient and meaningful. We wanted to prove that with proper planning you can eat well without breaking the bank. 

## What it does
Each morning our bot _manually_ goes through Food Lion's website taking note of items on sale. We store each sale item in MongoDB, along with the discount amount and original price. We then configure Spoonacular's REST API to generate recipes that optimize the number of items on sale called for in the instructions. Each recipe is stored as a MongoDB document and presented on the website. 

## How we built it
We built a Selenium agent to visit Food Lion's website and record information on sale items and discount percentages. Then, the data is sent by FastAPI to MongoDB where the ingredients and their metadata are stored as documents. We created API endpoints that are automatically triggered each morning to repeat scraping to ensure fresh data and generate recipes through the use of Spoonacular's API. Each call to Spoonacular requires a list of ingredients and returns JSON data describing possible recipes and the number of ingredients it was able to match from the input in its response. Using this ratio, we calculate the savings and send the information to our Next.js front end.
