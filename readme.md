# Security Incident Report Generator

A Python-based security log analysis project that analyzes authentication and security logs, detects failed login attempts and suspicious activities, calculates a rule-based risk level, generates security findings and recommendations, and creates an automated incident report with data visualizations.

## Project Overview

The **Security Incident Report Generator** automates the analysis of security log data.

Security logs can contain a large number of events, making manual analysis time-consuming. This project uses **Python and Pandas** to process security logs, identify failed login attempts and suspicious activities, determine the overall risk level, and generate a security incident report.

**Matplotlib** is used to create charts for better visualization of login activity and detected anomalies.

## Objectives

- Read and analyze security log files.
- Identify failed and successful login attempts.
- Detect suspicious activities from security logs.
- Identify different types of anomalies.
- Calculate an overall security risk level.
- Generate security findings.
- Provide security recommendations.
- Automatically generate an incident report.
- Save the report as a TXT file.
- Create security data visualizations.

## Technologies Used

- **Python** – Core programming language
- **Pandas** – Data loading, processing, filtering, and analysis
- **Matplotlib** – Data visualization and chart generation
- **CSV** – Security log dataset format

## Project Structure

```text
Security_Incident_Report_Generator/
│
├── data/
│   └── security_logs.csv
│
├── reports/
│   └── incident_report.txt
│
├── charts/
│   ├── login_status_chart.png
│   └── anomaly_distribution_chart.png
│
├── main.py
│
└── README.md
```

## Dataset

The project uses a security log dataset containing authentication and anomaly-related information.

### Dataset Columns

```text
timestamp
source_ip
server
username
service
attempts
status
port
protocol
comment
anomaly_label
delta_t
```

### Dataset Statistics

- **Total Events:** 334,533
- **Failed Logins:** 237,939
- **Successful Logins:** 96,594
- **Suspicious Activities:** 144,411
- **Overall Risk Level:** HIGH

### Anomaly Distribution

| Anomaly Type | Number of Events |
|---|---:|
| Normal | 190,122 |
| Port Scan | 136,883 |
| Brute Force | 4,876 |
| Geo Anomaly | 2,652 |

## How the Project Works

### 1. Load Security Logs

The CSV security log file is loaded using Pandas.

```python
df = pd.read_csv("data/security_logs.csv")
```

### 2. Calculate Total Events

The total number of security events is calculated from the dataset.

### 3. Detect Failed and Successful Logins

The `status` column is analyzed to count failed and successful login events.

### 4. Detect Suspicious Activities

Suspicious events are identified using the `anomaly_label` column.

The project analyzes:

- Port Scan
- Brute Force
- Geo Anomaly

### 5. Calculate Risk Level

A rule-based threshold is used to categorize the overall security risk as:

- LOW
- MEDIUM
- HIGH

For the current dataset, the calculated risk level is:

**HIGH**

### 6. Generate Findings

The program automatically generates findings based on detected security events.

Examples:

- Multiple failed login attempts detected.
- Port scanning activity observed.
- Brute force attack attempts identified.
- Geographical access anomalies detected.

### 7. Generate Recommendations

The program generates security recommendations based on the detected activities.

Examples:

- Enable Multi-Factor Authentication (MFA).
- Investigate brute force attack sources.
- Review firewall and network security rules.
- Monitor logins from unusual locations.
- Monitor user activity regularly.
- Block suspicious IP addresses.

### 8. Generate Incident Report

A structured incident report is generated containing:

- Date
- Total events
- Failed logins
- Successful logins
- Suspicious activities
- Risk level
- Findings
- Recommendations

### 9. Save Report

The generated report is saved as:

```text
reports/incident_report.txt
```

### 10. Generate Charts

Matplotlib generates two visualizations.

**Login Status Distribution**

Compares failed and successful login events.

```text
charts/login_status_chart.png
```

**Anomaly Distribution**

Shows the number of detected port scan, brute force, and geographical anomaly events.

```text
charts/anomaly_distribution_chart.png
```

## How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Security_Incident_Report_Generator.git
```

### Step 2: Open the Project Folder

```bash
cd Security_Incident_Report_Generator
```

### Step 3: Install Required Libraries

```bash
python -m pip install pandas matplotlib
```

### Step 4: Run the Program

```bash
python main.py
```

## Sample Output

```text
============================================================
SECURITY INCIDENT REPORT
============================================================

Date: DD-MM-YYYY

Total Events: 334533
Failed Logins: 237939
Successful Logins: 96594
Suspicious Activities: 144411

Risk Level: HIGH

Findings:
- Multiple failed login attempts detected.
- Port scanning activity observed.
- Brute force attack attempts identified.
- Geographical access anomalies detected.

Recommendations:
- Enable Multi-Factor Authentication (MFA).
- Investigate brute force attack sources.
- Review firewall and network security rules.
- Monitor logins from unusual locations.
- Monitor user activity regularly.
- Block suspicious IP addresses.

============================================================
END OF REPORT
============================================================
```

## Generated Outputs

The project generates:

- `reports/incident_report.txt`
- `charts/login_status_chart.png`
- `charts/anomaly_distribution_chart.png`

## Key Features

- Security log processing
- Failed login detection
- Successful login analysis
- Suspicious activity detection
- Port scan detection
- Brute force detection
- Geographical anomaly detection
- Rule-based risk assessment
- Automated security findings
- Automated recommendations
- Incident report generation
- TXT report creation
- Login activity visualization
- Anomaly visualization
- Pandas-based data analysis

## Concepts Demonstrated

- Python Programming
- Pandas Data Analysis
- CSV File Handling
- Data Filtering
- Data Aggregation
- Security Log Analysis
- Threat Detection
- Anomaly Detection
- Rule-Based Risk Assessment
- Security Reporting
- Data Visualization

## Results

The project successfully analyzed **334,533 security events** and identified:

- **237,939** failed login events
- **96,594** successful login events
- **144,411** suspicious activity events
- **HIGH** overall risk level

The system automatically generated security findings, recommendations, a TXT incident report, and visualization charts.

## Future Enhancements

- Real-time security log monitoring
- Email alerts for high-risk incidents
- Interactive security dashboard
- Machine learning-based anomaly detection
- Automated suspicious IP blocking
- Database integration
- Geographic visualization of IP addresses
- Advanced risk scoring
- Web-based security monitoring dashboard

## Learning Outcomes

Through this project, I gained practical experience in:

- Analyzing large security datasets using Pandas.
- Working with authentication and security logs.
- Identifying failed login attempts and suspicious activities.
- Applying rule-based security risk assessment.
- Generating automated security reports.
- Creating data visualizations using Matplotlib.
- Understanding basic cybersecurity monitoring concepts.
- Combining data analysis with cybersecurity applications.

## Author

**Syed Tanzeela**

**B.Tech – Information Technology**

**NRI Institute of Technology**

## Project Category

**Data Analysis | Cybersecurity | Security Log Analysis | Threat Detection**

## Conclusion

The **Security Incident Report Generator** successfully automates the process of analyzing security logs and generating security incident reports.

The project demonstrates how Python, Pandas, and Matplotlib can be used for security log analysis, threat detection, risk assessment, automated reporting, and data visualization.

It provides practical exposure to both **Data Analysis** and **Cybersecurity Log Analysis** concepts.
