class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name:
            raise ValueError("Name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles() if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)  # Add the new article to the author's articles list
        return new_article

    def topic_areas(self):
        topic_areas = list(set(article.magazine.category for article in self._articles))
        return topic_areas if topic_areas else None

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in Article.all_articles if article.magazine == self))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles())
        return [author for author, count in author_counts.items() if count > 2]


class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters, inclusive")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)
        
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = value

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value
