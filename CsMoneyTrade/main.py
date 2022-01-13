import requests
import json
from fake_useragent import UserAgent


ua = UserAgent()


def collect_data():
    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f"https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=40&hasTradeLock=false&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={offset}&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&type=2&withStack=true"
            response = requests.get(
                url,
                headers={"user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.2.773 Yowser/2.5 Safari/537.36"}
            )

            offset += 60

            data = response.json()
            items = data.get("items")

            for i in items:
                if i.get("overprice") is not None and i.get("overprice") < -10:
                    item_full_name = i.get("fullName")
                    item_3d = i.get("3d")
                    item_price = i.get("price")
                    item_overprice = i.get("overprice")

                    result.append(
                        {
                            "full_name": item_full_name,
                            "3d": item_3d,
                            "price": item_price,
                            "overprice": item_overprice
                        }
                    )
        count += 1
        print(f"Page #{count}")
        print(url)

        if len(items) < 60:
            break

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))


def main():
    collect_data()


if __name__ == '__main__':
    main()
