from parser import Parser
from config import PATH, get_api_key


def main():
    parser = Parser(get_api_key(str(PATH / '.env')))
    parser.get_categories()

    print(parser.category)
    category = input('Category: ')
    print(parser.get_products(category))


if __name__ == "__main__":
    main()
