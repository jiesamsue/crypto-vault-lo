import os
import time
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv("INFURA_URL")
TOKEN_CONTRACT = Web3.to_checksum_address(os.getenv("TOKEN_CONTRACT"))
MIN_THRESHOLD = int(os.getenv("MIN_THRESHOLD", "100000"))
DECIMALS = int(os.getenv("DECIMALS", "18"))

ABI = '[{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'

w3 = Web3(Web3.HTTPProvider(INFURA_URL))
contract = w3.eth.contract(address=TOKEN_CONTRACT, abi=ABI)
latest_block = w3.eth.block_number

def monitor_whale_transfers():
    global latest_block
    print(f"🐋 Monitoring whale transfers for token {TOKEN_CONTRACT}...")
    while True:
        try:
            current_block = w3.eth.block_number
            if current_block > latest_block:
                events = contract.events.Transfer().get_logs(fromBlock=latest_block + 1, toBlock=current_block)
                for e in events:
                    value = e['args']['value'] / (10 ** DECIMALS)
                    if value >= MIN_THRESHOLD:
                        print(f"🚨 Whale Transfer Detected!")
                        print(f"From: {e['args']['from']} → To: {e['args']['to']}")
                        print(f"Amount: {value:,.2f} tokens
")
                latest_block = current_block
            time.sleep(10)
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    monitor_whale_transfers()
