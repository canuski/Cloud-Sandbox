import asyncio
import subprocess
import os
from telegram_sender import send_telegram_msg

async def scan_file(file_name):
    try:
        result = subprocess.run(['clamscan', '--no-summary', '--verbose', file_name], capture_output=True, text=True)
        output = result.stdout + result.stderr
        print(output)  # Print output to terminal
        await send_telegram_msg(output)
    except FileNotFoundError:
        print('ClamAV is not installed or not in the PATH.')

async def scan_directory(directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Scanning file: {file_path}")
                await scan_file(file_path)  # Await scan_file
    except Exception as e:
        print(f"Error scanning directory: {e}")

async def main():
    directory = "../test_files/"
    await scan_directory(directory)

if __name__ == "__main__":
    asyncio.run(main())
