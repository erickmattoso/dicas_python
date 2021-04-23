from newspaper import Article

url = "https://fivethirtyeight.com/features/what-were-watching-in-the-nhls-playoff-races/"
article = Article(url)

# Download html
article.download()

# Get information 
article.parse()
article.nlp()

print("title",article.title, "\n")
print("publish_date",article.publish_date, "\n")
print("top_image",article.top_image, "\n")
print("summary",article.summary, "\n")
print("keywords",article.keywords, "\n")

# >>> import numpy as np
# >>> arr = np.array([[1, 4, 10, 15], [2, 3, 8, 9]]) 
# # Mulply values that are less than 5 by 2 
# >>> np.where(arr<5, arr*2, arr) 
