import json
import os

import requests
from dotenv import load_dotenv


class Settings:
    notion_key: str = "<your-notion-api-key-should-be-set-in-.env>"
    notion_list_page_id: str = "<shopping-list-page-id-should-be-set-in-.env>"

    load_dotenv()


def get_list_of_items():
    page_size = 1000
    payload = {"page_size": page_size}
    response = requests.post(
        url=f"https://api.notion.com/v1/databases/"
        f"{os.getenv('NOTION_LIST_PAGE_ID', 'notion_list_page_id')}/query",
        json=payload,
        headers={
            "Authorization": f"Bearer {os.getenv('NOTION_KEY', 'notion_key')}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        },
    )

    notion_shoppinglist_json = json.loads(response.content.decode("utf-8"))

    items = []
    for item in notion_shoppinglist_json["results"]:
        items.append(item["properties"]["Name"]["title"][0]["plain_text"])

    # TODO: could add quantities / day / recipe links here?

    return items


def login_to_online_shop():
    pass


def empty_basket():
    # empty basket if user confirms (otherwise add to existing)
    pass


def add_items_to_basket(list):
    # auto add list of items to the basket, return a list of items not found
    # for item in list:
    #     search_url =
    #     f"https://www.tesco.com/groceries/en-GB/search?query={item}"

    pass


def manually_order_other_items():
    # individually choose items not found and remember choices for next time
    pass


def confirm_and_complete():
    pass


def main():
    Settings()
    list = get_list_of_items()
    login_to_online_shop()
    empty_basket()
    add_items_to_basket(list)
    manually_order_other_items()
    confirm_and_complete()


if __name__ == "__main__":
    main()
