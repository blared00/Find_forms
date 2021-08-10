#!/bin/bash


exec gunicorn web_setting.wsgi:application -b 0.0.0.0:8080 --reload


