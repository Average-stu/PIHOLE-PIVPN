#!/bin/bash

pihole -b -d  --regex '(^|\.)\.com$' '(^|\.)Netflix\.com$' '(^|\.)hotstar\.com$' '(^|\.)primevideo\.com$' '(^|\.)Youtube\.com$'

