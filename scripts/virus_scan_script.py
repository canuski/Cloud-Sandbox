import asyncio
import subprocess
import os
from telegram_sender import send_telegram_msg

scanned_files = set()  # Keep track of scanned files

async def scan_file(file_name):
    if file_name in scanned_files:
        return  # Skip scanning if file has already been scanned
    try:
        result = subprocess.run(['clamscan', '--no-summary', '--verbose', file_name], capture_output=True, text=True)
        output = result.stdout + result.stderr
        await send_telegram_msg(output)
        scanned_files.add(file_name)  # Add file to set of scanned files
    except FileNotFoundError:
        print('ClamAV is not installed or not in the PATH.')

async def scan_directory(directory):
    try:
        while True:  # Continuous loop
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    await scan_file(file_path)  # Await scan_file
            await asyncio.sleep(10)  # Wait for 10 seconds before scanning again
    except Exception as e:
        print(f"Error scanning directory: {e}")

async def main():
    directory = "../test_files/"
    await scan_directory(directory)

if __name__ == "__main__":
    asyncio.run(main())
