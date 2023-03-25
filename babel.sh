#!/bin/bash

pybabel update -i translations/messages.pot -d translations
pybabel compile -d translations