# password_checker

A program which can be used to check if an existing password has already been breached, or to check a new password if it doesn't have been breached yet.
This program uses the Have I Been Pwnd A.P.I to gather information, and any number of inputs from the uer to generate the required service.

This API uses K-Anonymity function to send only a specific amount of the hashed password to the database to compare the password to get the breached amount information. This helps to have the password be more sucured.

Usage
-----
> python checkmypass.py [password-argument]
