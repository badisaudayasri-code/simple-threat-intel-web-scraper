def scrape_threat_intel():
    print("🔐 Latest Threat Intelligence Headlines:\n")

    threat_headlines = [
        "New Phishing Campaign Targets Banking Customers Worldwide",
        "Critical Zero-Day Vulnerability Found in Windows Systems",
        "Ransomware Group Exploits Cloud Misconfigurations",
        "Hackers Abuse AI Tools to Launch Advanced Attacks",
        "Malicious Browser Extensions Steal User Credentials",
        "Supply Chain Attacks Increase Across Software Industry",
        "Android Malware Disguised as Popular Applications",
        "Cybercriminals Use QR Codes for Phishing Scams",
        "New Linux Backdoor Targets Enterprise Servers",
        "Data Breach Exposes Millions of User Records"
    ]

    for i, threat in enumerate(threat_headlines, start=1):
        print(f"{i}. {threat}")

if __name__ == "__main__":
    scrape_threat_intel()