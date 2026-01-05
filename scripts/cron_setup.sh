#!/bin/bash

# Absolute paths for project and venv
PROJECT_DIR=/home/ubuntu/Projet_Linux
PYTHON_PATH=$PROJECT_DIR/venv/bin/python
SCRIPT_PATH=$PROJECT_DIR/scripts/daily_report_v2.py
LOG_PATH=$PROJECT_DIR/data/cron.log

echo "Setting up cron job for daily report..."
echo "Project directory: $PROJECT_DIR"
echo "Python path: $PYTHON_PATH"

# Cron job: run daily at 20:00 (8pm)
CRON_COMMAND="0 20 * * * cd $PROJECT_DIR && $PYTHON_PATH $SCRIPT_PATH >> $LOG_PATH 2>&1"

# Install cron job (remove old entry if exists)
(crontab -l 2>/dev/null | grep -v "daily_report.py"; echo "$CRON_COMMAND") | crontab -

echo "Cron job installed successfully!"
echo "Daily report will run at 20:00 (8pm) every day"
echo ""
echo "To verify, run: crontab -l"
echo "To remove, run: crontab -r"
