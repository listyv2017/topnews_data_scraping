import openai
import os
from newspaper import Article

# API key
openai.api_key = os.environ["OPENAI_API_KEY"]

#retrieve news content
URL = "https://www.cnn.com/2023/01/17/health/procrastination-types-how-to-stop-wellness/index.html"
article = Article(URL)
article.download()
article.parse()
title = article.title

#text
text = article.text

#Generate summaries using gpt3
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=(f"Please summarize the following text:\n{text}\n\nSummary:"),
    temperature=0.5,
    max_tokens=1024,
    n = 1,
    stop="\"\"\""
)

print(response.choices[0].text.strip())

