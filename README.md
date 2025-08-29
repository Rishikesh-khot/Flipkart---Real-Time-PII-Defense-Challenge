# PII Detector & Redactor

This project scans CSV data, detects **PII (Personally Identifiable Information)**, and redacts it before saving to a new file.

---

## Features
- Detects PII like phone, Aadhaar, passport, and UPI IDs.  
- Detects combinations like name + email / address / IP.  
- Masks sensitive data (e.g., `9876543210 → 98XXXXXX10`).  
- Creates a new CSV with a `True/False` flag for PII.  

---

## How to Use
1. Make sure Python 3 is installed.  
2. Place your input CSV (e.g., `iscp_pii_dataset_-_Sheet1.csv`) in the same folder as `pii_detector.py`.  
3. Run the script:  
   ```bash
   python3 pii_detector.py iscp_pii_dataset_-_Sheet1.csv
````

4. Output will be saved as:

   ```
   redacted_output.csv
   ```

---

## Example

**Input:**

```json
{"name": "Rahul Kumar", "email": "rahul123@gmail.com"}
```

**Output:**

```json
{"name": "RXXX KXXX", "email": "raXXX@gmail.com"}
```

---

## Notes

* Uses regex for standalone PII (phone, Aadhaar, passport, UPI).
* Detects combinational PII (e.g., name + email, name + address).
* Redacts sensitive fields while keeping other data intact.
* Optimized for accuracy and efficiency.

---

**Submitted by:** \[Your Full Name or Username]

```

---

✅ Now it’s **GitHub-ready**. Just paste this as your `README.md` file, and it’ll render perfectly on GitHub with headings, code blocks, and examples.  

Do you want me to also prepare the `deployment_strategy.md` in the **same copy-paste GitHub format** so both files look uniform?
```
