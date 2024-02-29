import clamd
import os

# Initialize Clamd scanner
# Adjust the socket path as per your system configuration
clamd_socket = "/var/run/clamav/clamd.sock"
clamd_conn = clamd.ClamdUnixSocket(clamd_socket)


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

        # Scan the file for viruses
        result = clamd_conn.scan_file(file_path)

        # Check if the scan result indicates the presence of a virus
        if "FOUND" in result[file_path]:
            # If a virus is found, mark the test as failed
            assert False, f"Virus detected in file '{file_path}': {result[file_path]}"

        # Print scan result (for debugging purposes)
        print(f"Scan result for '{file_path}': {result[file_path]}")


# Run the test
test_virus_scan()
