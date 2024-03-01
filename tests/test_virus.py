import clamd
import os

# Initialize Clamd scanner
clamd_host = "127.0.0.1"  # Clamd server host (adjust as needed)
clamd_port = 3310  # Clamd server port (adjust as needed)
clamd_conn = clamd.ClamdNetworkSocket(clamd_host, clamd_port)

def test_virus_scan():
    # Define a list of test files with different file types
    test_files = [
        "test_files/test.txt",
        "test_files/test.pdf",
        "test_files/test.docx",
        # Add more file types as needed
    ]

    for file_path in test_files:
        # Ensure the file exists
        assert os.path.exists(file_path), f"File '{file_path}' does not exist."

        # Open the file and read its contents
        with open(file_path, "rb") as file:
            file_content = file.read()

        # Scan the file contents for viruses
        result = clamd_conn.instream(file_content)

        # Check if the scan result indicates the presence of a virus
        if "FOUND" in result[0]:
            # If a virus is found, mark the test as failed
            assert False, f"Virus detected in file '{file_path}': {result[1]}"

        # Print scan result (for debugging purposes)
        print(f"Scan result for '{file_path}': {result[1]}")

# Run the test
test_virus_scan()
