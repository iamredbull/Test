import requests

TIME_ETHERSCAN = 0
HEXCONVER_ETHERSCAN = 0
TIME_BLOCKCYPHER = 0
KEY_BLOCKCYPHER = 0


def api_etherscan():
    global TIME_ETHERSCAN
    global HEXCONVER_ETHERSCAN
    url = "https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken"
    ans = requests.get(url=url)
    answer_js = ans.json()
    TIME_ETHERSCAN = ans.elapsed.total_seconds()
    HEXCONVER_ETHERSCAN = (int(answer_js.get('result'),0))
    print(f"Время ответа составило:Etherscan {TIME_ETHERSCAN}, ключ result = {answer_js.get('result')} или {HEXCONVER_ETHERSCAN}")


def api_blockcypher():
    global TIME_BLOCKCYPHER
    global KEY_BLOCKCYPHER
    url = "https://api.blockcypher.com/v1/eth/main"
    ans = requests.get(url=url)
    answer_js = ans.json()
    TIME_BLOCKCYPHER = ans.elapsed.total_seconds()
    KEY_BLOCKCYPHER = answer_js.get('height')
    print(f"Время ответа составило:Blockcypher {TIME_BLOCKCYPHER}, ключ height = {KEY_BLOCKCYPHER}")


def main():
    api_etherscan()
    api_blockcypher()

    if TIME_ETHERSCAN  > TIME_BLOCKCYPHER:
        print(f"Blockcypher быстрее: {TIME_ETHERSCAN } > {TIME_BLOCKCYPHER}")
    else:
        print(f"Etherscan быстрее: {TIME_BLOCKCYPHER} > {TIME_ETHERSCAN }")
    if HEXCONVER_ETHERSCAN == KEY_BLOCKCYPHER:
        print(f"Key value: {HEXCONVER_ETHERSCAN} = {KEY_BLOCKCYPHER}")
    elif  HEXCONVER_ETHERSCAN > KEY_BLOCKCYPHER:
        print(f"Key value: {HEXCONVER_ETHERSCAN} > {KEY_BLOCKCYPHER}")
    elif HEXCONVER_ETHERSCAN < KEY_BLOCKCYPHER:
        print(f"Key value: {HEXCONVER_ETHERSCAN} < {KEY_BLOCKCYPHER}")


if __name__ == '__main__':
    main()
