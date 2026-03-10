from faker import Faker
from json import dump
from pathlib import Path
from typing import List, Callable

FAKE = Faker()
OUTPUT_PATH = Path("blog/fixtures/initial_data.json")
IMAGE_EXTENSIONS = ["jpg", "png", "tiff", "webp"]


def generate_data(model: str, n: int, fields_func) -> List[dict]:
    """
    Generate initial data for DB.
    Return list of dicts.
    """
    data = []
    for i in range(1, n + 1):
        data.append({"model": model, "pk": i, "fields": fields_func()})
    return data


def user_fields() -> dict:
    """
    Generate initial fields about User for DB using faker.
    """
    return {
        "first_name": FAKE.first_name(),
        "last_name": FAKE.last_name(),
        "birth_date": str(FAKE.date_of_birth()),
        "email": FAKE.email(),
        "country": FAKE.country_code(),
    }


def posts_fields(num_of_users: int) -> Callable:
    """
    Generate initial data related to Post for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "title": FAKE.catch_phrase(),
            "text": FAKE.text(max_nb_chars=20),
            "user": FAKE.random_int(min=1, max=num_of_users),
        }

    return fields


def categories_fields(num_of_posts) -> Callable:
    """
    Generate initial data related to post category for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "name": FAKE.word(),
            "post": FAKE.random_int(min=1, max=num_of_posts),
        }

    return fields


def tags_fields() -> dict:
    """
    Generate initial Tags for DB using faker.
    """
    return {"name": FAKE.word()}


def images_fields(num_of_posts: int) -> Callable:
    """
    Generate initial images (image paths) for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""

        return {
            "image_file": FAKE.file_path(
                depth=2,
                extension=FAKE.random_element(IMAGE_EXTENSIONS),
            ),
            "post": FAKE.random_int(min=1, max=num_of_posts),
            "alter_text": FAKE.sentence(nb_words=5),
        }

    return fields


def comments_fields(num_of_posts: int, num_of_users: int) -> Callable:
    """
    Generate initial comments for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "text": FAKE.text(max_nb_chars=50),
            "post": FAKE.random_int(min=1, max=num_of_posts),
            "user": FAKE.random_int(min=1, max=num_of_users),
        }

    return fields


def likes_fields(num_of_users: int, num_of_posts: int) -> Callable:
    """
    Generate likes for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "user": FAKE.random_int(min=1, max=num_of_users),
            "post": FAKE.random_int(min=1, max=num_of_posts),
        }

    return fields


def follows_fields(num_of_users: int) -> Callable:
    """
    Generate followers and followings for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "follower": FAKE.random_int(min=1, max=num_of_users),
            "following": FAKE.random_int(min=1, max=num_of_users),
        }

    return fields


def notifications_fields(num_of_users: int, num_of_posts: int) -> Callable:
    """
    Generate notifications for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "user": FAKE.random_int(min=1, max=num_of_users),
            "notification_type": FAKE.catch_phrase(),
            "post": FAKE.random_int(min=1, max=num_of_posts),
        }

    return fields


def post_tags_fields(num_of_posts: int, num_of_tags: int) -> Callable:
    """
    Generate post tags for linking post and tag tables for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "post": FAKE.random_int(min=1, max=num_of_posts),
            "tag": FAKE.random_int(min=1, max=num_of_tags),
        }

    return fields


def user_tags_fields(num_of_users: int, num_of_tags: int) -> Callable:
    """
    Generate post tags for linking post and tag tables for DB using faker.
    """

    def fields():
        """Closure func for "memorazing" params from post_fields."""
        return {
            "user": FAKE.random_int(min=1, max=num_of_users),
            "tag": FAKE.random_int(min=1, max=num_of_tags),
        }

    return fields


def save_to_json(path: Path, data: List[dict]) -> None:
    """Save generated fixtures to json file."""
    with open(path, "w") as file:
        dump(data, file, indent=2)


def main():
    """Proccess everything."""
    NUM_OF_USERS = 10
    NUM_OF_POSTS = 20
    NUM_OF_TAGS = 15
    NUM_OF_CATEGORIES = 5
    NUM_OF_IMAGES = 10
    NUM_OF_COMMENTS = 5
    NUM_OF_LIKES = 5
    NUM_OF_FOLLOWS = 10
    NUM_OF_NOTIFICATIONS = 15
    NUM_OF_POST_TAG = 4
    NUM_OF_USER_TAG = 7

    all_data = []
    all_data += generate_data("blog.user", NUM_OF_USERS, user_fields)
    all_data += generate_data(
        "blog.post", NUM_OF_POSTS, posts_fields(NUM_OF_USERS)
    )
    all_data += generate_data(
        "blog.category", NUM_OF_CATEGORIES, categories_fields(NUM_OF_POSTS)
    )
    all_data += generate_data("blog.tag", NUM_OF_TAGS, tags_fields)
    all_data += generate_data(
        "blog.image", NUM_OF_IMAGES, images_fields(NUM_OF_POSTS)
    )
    all_data += generate_data(
        "blog.comment",
        NUM_OF_COMMENTS,
        comments_fields(NUM_OF_POSTS, NUM_OF_USERS),
    )
    all_data += generate_data(
        "blog.like", NUM_OF_LIKES, likes_fields(NUM_OF_USERS, NUM_OF_POSTS)
    )
    all_data += generate_data(
        "blog.follow", NUM_OF_FOLLOWS, follows_fields(NUM_OF_USERS)
    )
    all_data += generate_data(
        "blog.notification",
        NUM_OF_NOTIFICATIONS,
        notifications_fields(NUM_OF_USERS, NUM_OF_POSTS),
    )
    all_data += generate_data(
        "blog.posttag",
        NUM_OF_POST_TAG,
        post_tags_fields(NUM_OF_POSTS, NUM_OF_TAGS),
    )
    all_data += generate_data(
        "blog.usertag",
        NUM_OF_USER_TAG,
        user_tags_fields(NUM_OF_USERS, NUM_OF_TAGS),
    )
    save_to_json(OUTPUT_PATH, all_data)


if __name__ == "__main__":
    main()
