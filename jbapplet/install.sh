#!/bin/bash

#Install Script for this plasma applet

zip -r ../jbapplet.zip .

sudo plasmapkg -i jbapplet.zip

plasmoidviewer jbapplet

