# password_checker

A program which can be used to check if an existing password has already been breached, or to check a new password if it doesn't have been breached yet.
This program uses the Have I Been Pwnd A.P.I to gather information, and any number of inputs from the uer to generate the required services of breached password informations.

This API uses K-Anonymity function to send only a specific number of the hashed password's digits to the database to compare the password to get the breached amount information. This function ensures that the passwords provided to the program will be safe and secure.

Usage
-----
> python checkmypass.py [password-argument]
