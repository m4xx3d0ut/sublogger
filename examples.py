#!/usr/bin/env python3

import sublogger

cmd = "ls -lha"

# This will log the output to the default output.log
log = sublogger.sublogger()
log.cmd_out(cmd)

# This will log the output to the specifed script.log
log = sublogger.sublogger('script.log')
log.cmd_out(cmd)


# This will only output in your terminal and will not write to a log
log = sublogger.sublogger(log_on='n')
log.cmd_out(cmd)