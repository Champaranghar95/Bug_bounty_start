#!/bin/bash

# Array of GitHub repository URLs for screenshot tools
repos=(
    "https://github.com/FortyNorthSecurity/EyeWitness"
    "https://github.com/michenriksen/aquatone"
    "https://github.com/vladocar/screenshoteer"
    "https://github.com/sensepost/gowitness"
    "https://github.com/byt3bl33d3r/WitnessMe"
    "https://github.com/BishopFox/eyeballer"
    "https://github.com/nccgroup/scrying"
    "https://github.com/beurtschipper/Depix"
    "https://github.com/breenmachine/httpscreenshot"
)

# Directory where repositories will be cloned
clone_dir="screenshot_tools"

# Create directory if it doesn't exist
mkdir -p $clone_dir

# Change to the directory
cd $clone_dir

# Loop through the array and clone each repository
for repo in "${repos[@]}"; do
    git clone $repo
done

echo "All screenshot tool repositories have been cloned."
