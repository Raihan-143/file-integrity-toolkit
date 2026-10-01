# File Integrity Monitor (FIM) Toolkit

A lightweight, robust Python-based **File Integrity Monitoring (FIM)** utility designed to detect unauthorized modifications, ransomware tampering, and configuration drift in critical system files.


## Overview & Problem Statement

In enterprise security architecture, attackers and malware often tamper with critical system files (e.g., `/etc/passwd`, `hosts`, or system binaries) to establish persistence, elevate privileges, or redirect traffic. 

Traditional signature-based antivirus solutions may fail to catch zero-day manipulations. **File Integrity Monitoring (FIM)** solves this by establishing a cryptographic baseline (ground truth) of sensitive files and verifying their state continuously.


## How It Works (Technical Architecture)

1. **Chunk-Based Stream Hashing (Memory Optimization):**
   * Instead of loading entire large files into memory (which triggers `MemoryError` on multi-gigabyte files), the script reads files in **4096-byte (4KB) chunks**.
   * It feeds chunks sequentially into Python's native `hashlib.sha256` hasher.
2. **Cryptographic Avalanche Effect:**
   * SHA-256 ensures that even a **single-bit alteration** (such as adding a single space, newline, or payload line) drastically mutates the resulting 64-character hexadecimal digest.
3. **Automated Drift Detection & Alerting:**
   * Compares the computed digest against the known baseline.
   * Instantly raises a critical alert if any unauthorized alteration is detected.


## Getting Started

### Prerequisites
* Python 3.10+ (Built entirely using Python's standard library — zero external dependencies).

### Installation & Run

1. **Clone the repository:**
  git clone github.com/Raihan-143/python_security_toolkit.git
  file-integrity-toolkit.git
   cd file-integrity-toolkit

### Author   
  Md. Raihan Hasan Rana - Cybersecurity Enthusiast
 