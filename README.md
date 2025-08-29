# PII Detector & Redactor

This project scans CSV data, detects **PII (Personally Identifiable Information)**, and redacts it before saving to a new file.

---

## Features
- Detects standalone PII: **phone**, **Aadhaar**, **passport**, **UPI ID**.  
- Detects combinational PII: **name + email**, **name + address**, **name + IP/device**, etc.  
- Masks sensitive fields (example: `9876543210` → `98XXXXXX10`).  
- Outputs a CSV with `record_id`, `redacted_data_json`, and `is_pii` (True/False).

---

## Prerequisites
- Python 3.7 or later.

---

## How to Use
1. Put your input CSV (for example `iscp_pii_dataset_-_Sheet1.csv`) in the same folder as `pii_detector.py`.  
2. Run the script:

```bash
python3 pii_detector.py iscp_pii_dataset_-_Sheet1.csv
````

Output will be saved as:

```
redacted_output.csv
```

---

## Example

### Input (one record's `data_json`):

```json
{"name": "Rahul Kumar", "email": "rahul123@gmail.com"}
```

### Output (`redacted_data_json` in CSV):

```json
{"name": "RXXX KXXX", "email": "raXXX@gmail.com"}
```

---

## Notes

* Uses regex and simple rules (no external libraries) for speed and deterministic behavior.
* Single attributes like a lone email or first name are not flagged as PII unless paired per the combinational rules.
* Address redaction requires street/pin-like hints (to reduce false positives).
* The script writes a redacted JSON string into the CSV so downstream tools can parse it if needed.

---

## Files in this repo

* `pii_detector.py` — main script (run as shown above)
* `iscp_pii_dataset_-_Sheet1.csv` — input dataset (provided)
* `redacted_output.csv` — generated output after running the script
* `deployment_strategy.md` — short deployment notes

---

**Submitted by:** Rishikesh Khot

```

Do you also want me to shorten the section titles (like "How to Use" → "Usage") so it looks more concise, or keep them exactly as above?
```
