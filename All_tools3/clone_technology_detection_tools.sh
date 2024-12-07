#!/bin/bash

# Array of GitHub repository URLs for technology detection tools
repos=(
    "https://github.com/AliasIO/wappalyzer"
    "https://github.com/rverton/webanalyze"
    "https://github.com/claymation/python-builtwith"
    "https://github.com/urbanadventurer/whatweb"
    "https://github.com/RetireJS/retire.js"
    "https://github.com/projectdiscovery/httpx"
    "https://github.com/praetorian-inc/fingerprintx"
)

# Directory where repositories will be cloned
clone_dir="technology_detection_tools"

# Create directory if it doesn't exist
mkdir -p $clone_dir

# Change to the directory
cd $clone_dir

# Loop through the array and clone each repository
for repo in "${repos[@]}"; do
    git clone $repo
done

echo "All technology detection tool repositories have been cloned."
