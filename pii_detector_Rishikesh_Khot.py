import csv
import json
import re
import sys

# regex patterns for common identifiers
phone_pattern = re.compile(r'^\d{10}$')
aadhar_pattern = re.compile(r'^\d{12}$')
passport_pattern = re.compile(r'^[A-Z]\d{7}$')
upi_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+$')

# sets of fields to check
standalone_keys = {"phone", "aadhar", "passport", "upi_id"}
combo_keys = {"name", "email", "address", "device_id", "ip_address"}

def is_standalone_pii(key, val):
    val = str(val).strip()
    if key == "phone" and phone_pattern.match(val):
        return True
    if key == "aadhar" and aadhar_pattern.match(val):
        return True
    if key == "passport" and passport_pattern.match(val):
        return True
    if key == "upi_id" and upi_pattern.match(val):
        return True
    return False

def has_combo_pii(data):
    found = 0
    for k in combo_keys:
        if k in data and data[k]:
            if k == "name":
                if len(data[k].split()) > 1:
                    found += 1
            elif k == "address":
                if re.search(r'\d{6}', data[k]):  # pin code like
                    found += 1
            elif k == "email":
                if "@" in data[k]:
                    found += 1
            else:
                found += 1
    return found >= 2

def redact(data):
    out = dict(data)
    for k, v in data.items():
        val = str(v)
        if is_standalone_pii(k, v):
            if k == "phone":
                out[k] = val[:2] + "XXXXXX" + val[-2:]
            elif k == "aadhar":
                out[k] = val[:2] + "XXXXXX" + val[-4:]
            elif k == "passport":
                out[k] = val[0] + "XXXXXXX"
            elif k == "upi_id":
                u, p = val.split("@")
                out[k] = u[:2] + "XXXX" + u[-2:] + "@" + p
        elif k in combo_keys:
            if k == "name":
                parts = val.split()
                out[k] = " ".join([p[0] + "XXX" for p in parts])
            elif k == "email":
                u, p = val.split("@")
                out[k] = u[:2] + "XXX@" + p
            elif k == "address":
                out[k] = "[REDACTED_ADDRESS]"
            elif k in ("device_id", "ip_address"):
                out[k] = "[REDACTED]"
    return out

def process_csv(input_file, output_file):
    with open(input_file, newline='', encoding="utf-8") as f_in, \
         open(output_file, "w", newline='', encoding="utf-8") as f_out:
        
        reader = csv.DictReader(f_in)
        writer = csv.writer(f_out)
        writer.writerow(["record_id", "redacted_data_json", "is_pii"])
        
        for row in reader:
            rid = row.get("record_id", "")
            try:
                data = json.loads(row["data_json"].replace('\\"','"'))
            except Exception:
                data = {}
            
            has_standalone = any(is_standalone_pii(k, v) for k, v in data.items())
            has_combo = has_combo_pii(data)
            pii_flag = has_standalone or has_combo

            if pii_flag:
                redacted = redact(data)
            else:
                redacted = data

            writer.writerow([rid, json.dumps(redacted), str(pii_flag)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pii_detector.py <input_csv>")
        sys.exit(1)
    inp = sys.argv[1]
    process_csv(inp, "redacted_output.csv")
    print("done, output -> redacted_output.csv")

