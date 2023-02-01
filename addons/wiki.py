import wikipedia


def get_answer(arg):
    try:
        topic = wikipedia.page(arg)
        message = topic.content.split('\n')[0]
        link = topic.url
        return [message, link]
    except wikipedia.exceptions.DisambiguationError:
        return 'Please be more specific...'
