#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#
#      Purpose: Oasis data parser (peak values)
#
#----------------------------------------------------------------------------
import time
import urllib2
url = 'http://oasis.pjm.com/doc/projload.txt'
#----------------------------------------------------------------------------
#
#	Variables
#
#----------------------------------------------------------------------------
bge = 0
com = 0
dpl = 0
duq = 0
pec = 0
pep = 0
ppl = 0
psg = 0
rto = 0
webpage = '/var/www/html/pinesol60/r/testing/1/html/peak2.html'
#----------------------------------------------------------------------------
#
#	Header
#
#----------------------------------------------------------------------------
web = open(webpage, 'w')
web.write("<html>\n<head>\n<title>Seven-Day Peak Load Forecast</title>\n</head>\n<body>\n<center>\n<h2>Sever-Day Peak Load Forecast</h2>\n");
#----------------------------------------------------------------------------
#
#	Get max value
#
#----------------------------------------------------------------------------
def get_peak(rlist):
	peak = 0
	if rlist[1] > peak:
		peak = rlist[1]
	if rlist[2] > peak:
		peak = rlist[2]
	if rlist[3] > peak:
		peak = rlist[3]
	if rlist[4] > peak:
		peak = rlist[4]
	if rlist[5] > peak:
		peak = rlist[5]
	if rlist[6] > peak:
		peak = rlist[6]
	if rlist[7] > peak:
		peak = rlist[7]
	return peak
#----------------------------------------------------------------------------
#
#	Get data
#
#----------------------------------------------------------------------------
response = urllib2.urlopen(url)
projload = response.readlines()
for line in projload:
	line = " ".join(line.split())
	if 'BG&E' in line:
		bge = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>BGE</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'COMED HOUR' in line:
		com = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>COM</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'DP&L' in line:
		dpl = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>DPL</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'DUQUESNE' in line:
		duq = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>DUQ</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'PECO' in line:
		pec = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PEC</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'PEPCO' in line:
		pep = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PEP</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'PPL' in line:
		ppl = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PPL</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'PSE&G' in line:
		psg = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PSG</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
	if 'RTO COMBINED' in line:
		rto = 1
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>RTO</td></tr>\n<tr><td>Date</td><td>Peak MW</td></tr>\n")
#----------------------------------------------------------------------------
#
#	Date
#
#----------------------------------------------------------------------------
	if 'am ' in line:
		rlist = line.split(" ")
		oday = rlist[0]
#----------------------------------------------------------------------------
#
#	BGE
#
#----------------------------------------------------------------------------
	if 'pm' in line and bge > 0 and bge < 8:
		bge = bge + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	COM
#
#----------------------------------------------------------------------------
	if 'pm' in line and com > 0 and com < 8:
		com = com + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	DPL
#
#----------------------------------------------------------------------------
	if 'pm' in line and dpl > 0 and dpl < 8:
		dpl = dpl + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	DUQ
#
#----------------------------------------------------------------------------
	if 'pm' in line and duq > 0 and duq < 8:
		duq = duq + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PEC
#
#----------------------------------------------------------------------------
	if 'pm' in line and pec > 0 and pec < 8:
		pec = pec + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PEP
#
#----------------------------------------------------------------------------
	if 'pm' in line and pep > 0 and pep < 8:
		pep = pep + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PPL
#
#----------------------------------------------------------------------------
	if 'pm' in line and ppl > 0 and ppl < 8:
		ppl = ppl + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PSG
#
#----------------------------------------------------------------------------
	if 'pm' in line and psg > 0 and psg < 8:
		psg = psg + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	RTO
#
#----------------------------------------------------------------------------
	if 'pm' in line and rto > 0 and rto < 8:
		rto = rto + 1
		rlist = line.split(" ")
		peak = get_peak(rlist)
		web.write("<tr><td>" + oday + "</td><td>" + peak + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	Footer
#
#----------------------------------------------------------------------------
web.write("</table>\n<br><br><br>\n</center>\n</body>\n</html>\n")
web.close



