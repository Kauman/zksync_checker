import csv


def read_wallets(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def read_csv(file_path):
    wallet_dict = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            wallet, reward = row[0], row[1]
            wallet_dict[wallet] = reward
    return wallet_dict


def compare_wallets(wallets, wallet_dict):
    for wallet in wallets:
        wallet = wallet.lower()
        if wallet in wallet_dict:
            print(f"Кошелек: {wallet}, Награда: {wallet_dict[wallet]}")


wallets_file_path = 'wallets.txt'
csv_file_path = 'eligibility_list.csv'
wallets = read_wallets(wallets_file_path)
wallet_dict = read_csv(csv_file_path)
compare_wallets(wallets, wallet_dict)
