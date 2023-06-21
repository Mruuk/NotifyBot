#!/bin/bash

if [ "$1" == "-v" ]; then
  python3 -c "from notify import handle_send_notificationVerbose; print(handle_send_notificationVerbose('$2'))"
else
  python3 -c "from notify import handle_send_notification; handle_send_notification('$1')"
fi
