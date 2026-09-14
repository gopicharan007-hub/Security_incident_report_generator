import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/security_logs.csv")

# Total events
total_events = len(df)

# Failed logins
failed_logins = len(df[df["status"] == "Failed"])

# Successful logins
successful_logins = len(df[df["status"] == "Success"])

# Suspicious activities
port_scans = len(df[df["anomaly_label"] == "port_scan"])
brute_force = len(df[df["anomaly_label"] == "brute_force"])
geo_anomaly = len(df[df["anomaly_label"] == "geo_anomaly"])

suspicious_activities = (
    port_scans +
    brute_force +
    geo_anomaly
)

# Risk Level
if failed_logins > 100000 or suspicious_activities > 50000:
    risk_level = "HIGH"
elif failed_logins > 10000 or suspicious_activities > 10000:
    risk_level = "MEDIUM"
else:
    risk_level = "LOW"

# Findings
findings = []

if failed_logins > 0:
    findings.append("Multiple failed login attempts detected.")

if port_scans > 0:
    findings.append("Port scanning activity observed.")

if brute_force > 0:
    findings.append("Brute force attack attempts identified.")

if geo_anomaly > 0:
    findings.append("Geographical access anomalies detected.")

# Recommendations
recommendations = []

if failed_logins > 0:
    recommendations.append("Enable Multi-Factor Authentication (MFA).")

if brute_force > 0:
    recommendations.append("Investigate brute force attack sources.")

if port_scans > 0:
    recommendations.append("Review firewall and network security rules.")

if geo_anomaly > 0:
    recommendations.append("Monitor logins from unusual locations.")

recommendations.append("Monitor user activity regularly.")
recommendations.append("Block suspicious IP addresses.")

# Report Output
print("=" * 60)
print("SECURITY INCIDENT REPORT")
print("=" * 60)

print("\nDate:", datetime.now().strftime("%d-%m-%Y"))

print("\nTotal Events:", total_events)
print("Failed Logins:", failed_logins)
print("Successful Logins:", successful_logins)
print("Suspicious Activities:", suspicious_activities)

print("\nRisk Level:", risk_level)

print("\nFindings:")
for finding in findings:
    print("-", finding)

print("\nRecommendations:")
for recommendation in recommendations:
    print("-", recommendation)

print("\n" + "=" * 60)
print("END OF REPORT")
print("=" * 60)

# Create report content
report = f"""
============================================================
SECURITY INCIDENT REPORT
============================================================

Date: {datetime.now().strftime("%d-%m-%Y")}

Total Events: {total_events}
Failed Logins: {failed_logins}
Successful Logins: {successful_logins}
Suspicious Activities: {suspicious_activities}

Risk Level: {risk_level}

Findings:
"""

for finding in findings:
    report += f"\n- {finding}"

report += "\n\nRecommendations:"

for recommendation in recommendations:
    report += f"\n- {recommendation}"

report += "\n\n============================================================"
report += "\nEND OF REPORT"
report += "\n============================================================"

# Save report to file
with open("reports/incident_report.txt", "w") as file:
    file.write(report)

print("\nReport saved successfully!")
print("Location: reports/incident_report.txt")
# ============================================================
# PHASE 11 - CHARTS & VISUALIZATION
# ============================================================

# Login Status Distribution Chart
login_labels = ["Failed", "Success"]
login_values = [failed_logins, successful_logins]

plt.figure(figsize=(8, 5))
plt.bar(login_labels, login_values)
plt.title("Login Status Distribution")
plt.xlabel("Login Status")
plt.ylabel("Number of Events")
plt.tight_layout()

plt.savefig("charts/login_status_chart.png")
plt.close()

print("\nLogin Status Chart Saved!")
print("Location: charts/login_status_chart.png")


# ============================================================
# Anomaly Distribution Chart
# ============================================================

anomaly_labels = [
    "Port Scan",
    "Brute Force",
    "Geo Anomaly"
]

anomaly_values = [
    port_scans,
    brute_force,
    geo_anomaly
]

plt.figure(figsize=(8, 5))
plt.bar(anomaly_labels, anomaly_values)
plt.title("Anomaly Distribution")
plt.xlabel("Anomaly Type")
plt.ylabel("Number of Events")
plt.tight_layout()

plt.savefig("charts/anomaly_distribution_chart.png")
plt.close()

print("\nAnomaly Distribution Chart Saved!")
print("Location: charts/anomaly_distribution_chart.png")


# ============================================================
# COMPLETION MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("CHART GENERATION COMPLETED")
print("=" * 60)