#!/usr/bin/env python3
"""
Setup Verification Script for Emotion Detector Project

This script verifies that all files are in place and the project structure is correct.
"""

import os
import sys


def check_file_exists(filepath, description):
    """Check if a file exists and print status."""
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description}: {filepath} - MISSING")
        return False


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("Emotion Detector Project - Setup Verification")
    print("=" * 60)
    print()

    base_dir = "/Users/mohamedkhalif/MK-Dev/Emotion Detector Project"
    os.chdir(base_dir)

    checks = []

    # Check Core Application Files
    print("1. Core Application Files")
    print("-" * 60)
    checks.append(check_file_exists(
        "EmotionDetection/emotion_detection.py",
        "Emotion Detection Module"
    ))
    checks.append(check_file_exists(
        "EmotionDetection/__init__.py",
        "Package Initialization"
    ))
    checks.append(check_file_exists(
        "server.py",
        "Flask Server"
    ))
    print()

    # Check Web Interface Files
    print("2. Web Interface Files")
    print("-" * 60)
    checks.append(check_file_exists(
        "templates/index.html",
        "HTML Template"
    ))
    checks.append(check_file_exists(
        "static/css/style.css",
        "CSS Stylesheet"
    ))
    print()

    # Check Testing Files
    print("3. Testing Files")
    print("-" * 60)
    checks.append(check_file_exists(
        "tests/test_emotion_detection.py",
        "Unit Tests"
    ))
    checks.append(check_file_exists(
        "tests/__init__.py",
        "Test Package Init"
    ))
    print()

    # Check Configuration Files
    print("4. Configuration Files")
    print("-" * 60)
    checks.append(check_file_exists(
        "requirements.txt",
        "Dependencies"
    ))
    checks.append(check_file_exists(
        "README.md",
        "Documentation"
    ))
    checks.append(check_file_exists(
        ".gitignore",
        "Git Ignore"
    ))
    checks.append(check_file_exists(
        ".pylintrc",
        "Pylint Config"
    ))
    print()

    # Check Documentation Files
    print("5. Documentation Files")
    print("-" * 60)
    checks.append(check_file_exists(
        "PROJECT_SUMMARY.md",
        "Project Summary"
    ))
    checks.append(check_file_exists(
        "COMMANDS.md",
        "Command Reference"
    ))
    checks.append(check_file_exists(
        "setup.sh",
        "Setup Script"
    ))
    print()

    # Summary
    print("=" * 60)
    total_checks = len(checks)
    passed_checks = sum(checks)
    failed_checks = total_checks - passed_checks

    print(f"Verification Summary: {passed_checks}/{total_checks} checks passed")

    if failed_checks == 0:
        print("✓ All files are in place!")
        print()
        print("Next Steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Configure IBM Watson credentials in emotion_detection.py")
        print("3. Run tests: pytest tests/test_emotion_detection.py -v")
        print("4. Run pylint: pylint server.py")
        print("5. Start server: python server.py")
        return 0
    else:
        print(f"✗ {failed_checks} file(s) missing!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
