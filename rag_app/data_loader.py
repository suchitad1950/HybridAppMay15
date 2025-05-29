import wikipedia


def get_wikipedia_data(query: str, lang: str = "en") -> str:
    wikipedia.set_lang(lang)
    return wikipedia.page(query).content