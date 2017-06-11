headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs

for el in headlines:
    ln_news = len(news_ticker)
    if ln_news >= 140:
        break
    elif ln_news + len(el) + 1 < 140:
        news_ticker += el + ' '
    else:
        news_ticker += el[:(140-ln_news)]
        break

print(news_ticker)
print(len(news_ticker))
