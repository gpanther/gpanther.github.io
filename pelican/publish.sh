#!/bin/bash
set -ue

echo -n "Commit message: "
read -r COMMIT_MESSAGE

pelican
TEMP_DIR=`mktemp -d`
mv output $TEMP_DIR
cd ..
git checkout master
cp -r $TEMP_DIR/output/* .
rm -r $TEMP_DIR
git add -A
git commit -m "$COMMIT_MESSAGE"
git push --all
