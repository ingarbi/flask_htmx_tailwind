from random import randint

db = {
    "posts": [
        {
            "id": "1",
            "title": "This is HTMX!",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
        },
        {
            "id": "2",
            "title": "This is HTMX post 2",
            "content": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        },
        {
            "id": "3",
            "title": "Nulla vehicula",
            "content": "Nulla dignissim, magna eget consectetur sodales, ligula tellus pharetra nisl, eu maximus turpis ipsum vitae ex. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        },
        {
            "id": "4",
            "title": "Nunc ac sodales nunc.",
            "content": "Donec at fermentum mi, varius gravida justo. Nullam lacinia pretium quam non ultrices. In rhoncus sem eget nulla viverra condimentum sit amet vitae lacus. .",
        },
    ]
}


def get_posts():
    global db
    return db["posts"]


def get_post(post_id):
    global db
    for post in db["posts"]:
        if post["id"] == post_id:
            return post
    return None


def update_post(post_id, title, content):
    global db
    for post in db["posts"]:
        if post["id"] == post_id:
            post["title"] = title
            post["content"] = content
            return post
    return None


def add_post(title, content):
    global db
    post = {
        "id": str(randint(1000, 9999)),
        "title": title,
        "content": content,
    }
    db["posts"].insert(0, post)
    return post


def set_post(id, title, content):
    global db
    for post in db["posts"]:
        if post["id"] == id:
            post["title"] = title
            post["content"] = content
            return post
    return None


def delete_post(id):
    global db
    db["posts"] = [post for post in db["posts"] if post["id"] != id]
