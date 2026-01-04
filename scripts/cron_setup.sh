#!/bin/bash

PROJECT_DIR=$(pwd)
PYTHON_PATH=$(which python3)

echo "Setting up cron job for daily report..."
echo "Project directory: $PROJECT_DIR"
echo "Python path: $PYTHON_PATH"

CRON_COMMAND="0 20 * * * cd $PROJECT_DIR && $PYTHON_PATH scripts/daily_report_v2.py >> $PROJECT_DIR/data/cron.log 2>&1"

(crontab -l 2>/dev/null | grep -v "daily_report_v2.py"; echo "$CRON_COMMAND") | crontab -

echo "Cron job installed successfully!"
echo "Daily report will run at 20:00 (8pm) every day"
echo ""
echo "To verify, run: crontab -l"
echo "To remove, run: crontab -r"