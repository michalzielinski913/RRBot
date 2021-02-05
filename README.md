# RRBot
[![GitHub issues](https://img.shields.io/github/issues/michalzielinski913/RRBot)](https://github.com/michalzielinski913/RRBot/issues)
[![GitHub stars](https://img.shields.io/github/stars/michalzielinski913/RRBot)](https://github.com/michalzielinski913/RRBot/stargazers)
[![GitHub license](https://img.shields.io/github/license/michalzielinski913/RRBot)](https://github.com/michalzielinski913/RRBot)
## Table of contents
* [General info](#general-info)
* [Current stage](#stage)
* [Setup](#setup)
* [Coming soon](#coming-soon)
## General info
This project is unofficial API for Rival Regions game. It is in early development stage so new functionalities will appear soon.
	
## Current stage
Currently API can:
#### Accessing game
* Login using Facebook account only 

#### User
* Retrieve user ID
* Retrieve username
* Retrieve current user money balance
* Check user residency region ID
* Retrieve user party ID
* Retrieve user perks
* Move user to given region (Experimental)

#### Regions
* Check region current resource limit
* Check current region daily limit

#### Parties
* Retrieve ID list of all party members
* Retrieve party name

## Setup
This project uses python 3.7 with the following libraries:
* Numpy
* Selenium
* webdriver-manager
* requests
 
After cloning this project and installing required libraries rename login_data_example to login_data and fill your login data.
Later run test file.

## Coming soon
This project was started 27.12.2020 so It is currently in very early stage of development. With time I will add more functionalities. I plan to create free open source bot for every user and game statistics tracking tool.
