import urllib.request
import json

# Replace with your actual Etherscan API key
API_KEY = "YourEtherscanAPIKeyHere"

def get_eth_balance(address):
    url = (
        f"https://api.etherscan.io/api"
        f"?module=account&action=balance&address={address}"
        f"&tag=latest&apikey={API_KEY}"
    )
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data["status"] != "1":
                print("❌ Error from Etherscan:", data["message"])
                return None
            balance_wei = int(data["result"])
            balance_eth = balance_wei / 10**18
            return balance_eth
    except Exception as e:
        print("⚠️  Failed to fetch balance:", e)
        return None

def main():
    print("=== Ethereum Balance Checker ===")
    address = input("Enter Ethereum address: ").strip()
    if not address.startswith("0x") or len(address) != 42:
        print("❌ Invalid Ethereum address format.")
        return
    balance = get_eth_balance(address)
    if balance is not None:
        print(f"✅ Balance of {address}: {balance:.6f} ETH")

if __name__ == "__main__":
    main()
