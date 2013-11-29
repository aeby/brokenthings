# brokenthings

Scrape the internets for broken things

## Prerequisites

Installed [Python](http://python.org/) and [Virtualenv](http://pypi.python.org/pypi/virtualenv). See [this guide](http://docs.python-guide.org/en/latest/starting/install/linux/) for guidance.

## Setup

    git clone git@github.com:aeby/brokenthings.git
    cd brokenthings
    virtualenv venv --distribute --no-site-packages
    source venv/bin/activate
    pip install -r requirements.txt


## Usage

    scrapy crawl tutti
    scrapy crawl tutti -o tutti_items.json -t json

