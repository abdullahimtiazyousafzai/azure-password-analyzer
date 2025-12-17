# Password Strength Analyzer & Breach Checker

## Project Overview

This project is a **cloud-based password analysis tool** deployed on **Microsoft Azure** using **App Service** and **Azure Database for MySQL**. It provides two main functionalities:

1. **Password Strength Analysis** – Evaluates user passwords based on length, character variety, and common patterns.
2. **Password Breach Check** – Checks whether a password has been exposed in known data breaches using an offline database or API integration.

This project demonstrates **cloud-native architecture**, **PaaS usage**, and **secure application development**, making it suitable for real-world cybersecurity scenarios.

---

## Architecture

**User / Client**  
↓  
**Azure App Service** – Flask Web API (PaaS)  
↓  
**Azure Database for MySQL** – Stores analysis logs and results (PaaS)  

**Cloud Models Used:**

| Component           | Cloud Model |
|--------------------|------------|
| Azure App Service    | PaaS       |
| Azure MySQL Database | PaaS       |
| GitHub CI/CD         | SaaS       |

**Features:**
- Secure connection using environment variables  
- Scalable via Azure App Service auto-scaling  
- Fault-tolerant database with managed backups  

---

## Features

### 1. Password Strength Analysis
- Checks for:
  - Minimum length  
  - Use of uppercase, lowercase, digits, and symbols  
  - Avoids common passwords  
- Returns a **score** and **recommendations** for improvement  

### 2. Password Breach Checker
- Checks if a password exists in a **known breach database**  
- Provides a warning if compromised  
- Stores query logs in the database for analytics  

### 3. Secure Cloud Deployment
- Application credentials stored in **environment variables**  
- Flask app deployed via **Azure App Service**  
- Database hosted on **Azure MySQL**  

---
