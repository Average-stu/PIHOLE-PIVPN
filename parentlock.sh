#!/bin/bash

pihole --regex '(^|\.)\.com$' '(^|\.)Netflix\.com$' '(^|\.)hotstar\.com$' '(^|\.)primevideo\.com$' '(^|\.)Youtube\.com$'
