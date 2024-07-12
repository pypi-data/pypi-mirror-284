================
Figshare Driver
================

Driver to retrieve metrics from the Figshare portal.

Refer to https://figshare.com to get the user and password from.

For more information about the OPERAS metrics, go to
https://metrics.operas-eu.org/


Troubleshooting
===============

At the moment of development, the endpoint https://stats.figshare.com/tome/breakdown/
only takes one item_id per call, making the data fetching inefficient,
Once the api is ready for ingesting a list of ids we will be able to overcome this issue.

Release Notes:
==============

[0.0.1] - 2024-06-10
---------------------
Added
.......
    - Logic to initialise the Figshare driver
