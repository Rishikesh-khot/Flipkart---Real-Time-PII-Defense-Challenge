# PII Detector & Redactor

This project scans CSV data, detects **PII (Personally Identifiable Information)**, and redacts it before saving to a new file.

---

## Features
- Detects PII like **phone**, **Aadhaar**, **passport**, and **UPI IDs**.  
- Detects combinations like **name + email / address / IP**.  
- Masks sensitive data (e.g., `9876543210 → 98XXXXXX10`).  
- Creates a new CSV with a `True/False` flag for PII.  

---

## How to Use
1. Make sure **Python 3** is installed.  
2. Place your input CSV (e.g., `iscp_pii_dataset_-_Sheet1.csv`) in the same folder as `pii_detector.py`.  
3. Run the script:  

   ```bash
   python3 pii_detector.py iscp_pii_dataset_-_Sheet1.csv
Output will be saved as:
  ```bash
     redacted_output.csv

Example
Input:

```bash
{"name": "Rahul Kumar", "email": "rahul123@gmail.com"}

Output:

```bash
{"name": "RXXX KXXX", "email": "raXXX@gmail.com"}

Notes
Uses regex for standalone PII (phone, Aadhaar, passport, UPI).

Detects combinational PII (e.g., name + email, name + address).

Redacts sensitive fields while keeping other data intact.

Optimized for accuracy and efficiency.

Submitted by: Rishikesh Khot
