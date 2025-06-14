#!bin/bash

echo "=============="

git config --global user.name "${GITHUB_ACTOR}"
git config --global user.email "${INPUT_EMAIL}"
git congig --global --add safe.directory /github/workspace

python /usr/bin/feed.py

git add .
git commit -m "Update feed"
git push --set-upstream origin main


echo "=============="