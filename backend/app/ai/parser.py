import re

def extract_book_details(text: str):

    # Remove empty lines
    lines = []

    for line in text.split("\n"):
        line = line.strip()

        if line:
            lines.append(line)

    # Dictionary to store extracted details
    details = {
        "title": "",
        "author": "",
        "edition": "",
        "publisher": "",
        "subject": ""
    }

    # -------- Find Edition --------
    for line in lines:
        if "edition" in line.lower():
            details["edition"] = line

    # -------- Find Publisher --------
    publishers = [
        "S.Chand",
        "Wiley",
        "Pearson",
        "McGraw",
        "Oxford",
        "Cambridge"
    ]

    for line in lines:
        for publisher in publishers:
            if publisher.lower() in line.lower():
                details["publisher"] = publisher

    # -------- Find Subject --------
    subjects = [
        "Chemistry",
        "Physics",
        "Mathematics",
        "Operating Systems",
        "Database",
        "DSP",
        "Networks"
    ]

    for line in lines:
        for subject in subjects:
            if subject.lower() in line.lower():
                details["subject"] = subject

    # -------- Find Title --------
    if len(lines) >= 2:
        details["title"] = lines[0] + " " + lines[1]
    elif len(lines) == 1:
        details["title"] = lines[0]

    # -------- Find Author --------
    if len(lines) >= 5:
        details["author"] = lines[4]

    return details