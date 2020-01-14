#!/usr/bin/env bash
fab -H $1 --port 22 --user='root' -- "sed -i 's/ip = /&$2,/' /data/www/analysis_center/.env" 
fab -H $1 --port 22 --user='root' -- "sed -i 's/ip = /&$2,/' /data/www/analysis_api/.env" 
