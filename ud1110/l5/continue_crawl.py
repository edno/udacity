def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print('Page found')
        return False
    elif len(search_history) > max_steps:
        print('Search is taking too much time')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('Search falls into a cycle')
    else:
        return True
