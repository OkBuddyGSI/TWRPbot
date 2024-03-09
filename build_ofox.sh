# Check if gh is installed
if ! command -v gh &> /dev/null
then
    echo "gh could not be found. Installing gh..."
    curl -sS https://webi.sh/gh | sh
    source ~/.config/envman/PATH.env
    echo "gh installed."
fi

# Authenticate against github.com by reading the token from a file
gh auth login --with-token < token.txt


# Set the repository
git clone https://github.com/TeamPear-OS-Project/TG-X-GH-actions_OFOX-Builder
cd TG-X-GH-actions_OFOX-Builder
gh repo set-default https://github.com/TeamPear-OS-Project/TG-X-GH-actions_OFOX-Builder

# Pass everything as an argument coz why not
Sync_URL=$1
Manifest_Branch=$2
Device_Tree_URL=$3
Device_Tree_Branch=$4
Device_Path=$5
Device_Name=$6
Makefile_Name=$7
Build_Target=$8

# Run the GitHub Actions workflow with the specified URL
gh workflow run build_recovery.yml -f SYNC_URL=$Sync_URL -f MANIFEST_BRANCH=$Manifest_Branch -f DEVICE_TREE_URL=$Device_Tree_URL -f DEVICE_TREE_BRANCH=$Device_Tree_Branch -f DEVICE_PATH=$Device_Path -f DEVICE_NAME=$Device_Name -f MAKEFILE_NAME=$Makefile_Name -f BUILD_TARGET=$Build_Target