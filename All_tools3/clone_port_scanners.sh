#!/bin/bash

# Array of GitHub repository URLs for port scanners
repos=(
    "https://github.com/robertdavidgraham/masscan"
    "https://github.com/RustScan/RustScan"
    "https://github.com/projectdiscovery/naabu"
    "https://github.com/nmap/nmap"
    "https://github.com/trimstray/sandmap"
    "https://github.com/johnnyxmas/ScanCannon"
)

# Directory where repositories will be cloned
clone_dir="port_scanners"

# Create directory if it doesn't exist
mkdir -p $clone_dir

# Change to the directory
cd $clone_dir

# Loop through the array and clone each repository
for repo in "${repos[@]}"; do
    git clone $repo
done

echo "All port scanning repositories have been cloned."
