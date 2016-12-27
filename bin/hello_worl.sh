# !/usr/bin/env bash
# This loads fixtures automatically after deployment of review apps to Heroku

# Load Fixtures
if [ $HOLA == True ]; then
  echo "=> Hello World..."
else
  echo "=> Hey whats up!"
fi