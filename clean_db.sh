#!/bin/bash

echo "Clean the database.."
rm db.sqlite3

echo "Remove all migrations.."
rm -rf migrations/*

echo "Make migrations from scratch.."
python3 manage.py makemigrations levelupapi

echo "Migrating.."
python3 manage.py migrate

echo "Loading data.."
python3 manage.py loaddata users tokens gamers game_types games events gamerEvents
