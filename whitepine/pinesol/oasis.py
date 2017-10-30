#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#
#      Purpose: Oasis data parser
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
dstamp = time.strftime("%A, %B %d, %Y")
tstamp = time.strftime("%I:%M %p")
webpage = '/var/www/html/pinesol60/r/testing/1/html/afternoon2.html'
#----------------------------------------------------------------------------
#
#	Header
#
#----------------------------------------------------------------------------
web = open(webpage, 'w')
web.write("<html>\n<head>\n</head>\n<body>\n<center>\n<table border=0 cellpadding=4>\n<tr><td width=165 align=center><img width=50% height=50% src=images/white.jpg></td><td>\n<table border=0 cellpadding=4><tr><td colspan=3><font size=+3>" + dstamp + "</font></td></tr>\n<tr><td>Forecast Time: " + tstamp + "</td><td><br></td><td align=right>ISO:PJM</td></tr>\n</table>\n<td width=165 align=center><img width=50% height=50% src=images/peak.jpg></td></tr></table>\n")
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
	if 'COMED HOUR' in line:
		com = 1
	if 'DP&L' in line:
		dpl = 1
	if 'DUQUESNE' in line:
		duq = 1
	if 'PECO' in line:
		pec = 1
	if 'PEPCO' in line:
		pep = 1
	if 'PPL' in line:
		ppl = 1
	if 'PSE&G' in line:
		psg = 1
	if 'RTO COMBINED' in line:
		rto = 1
#----------------------------------------------------------------------------
#
#	BGE
#
#----------------------------------------------------------------------------
	if 'pm' in line and bge:
		bge = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>BGE</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	COM	
#
#----------------------------------------------------------------------------
	if 'pm' in line and com:
		com = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>COM</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	DPL
#
#----------------------------------------------------------------------------
	if 'pm' in line and dpl:
		dpl = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>DPL</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	DUQ
#
#----------------------------------------------------------------------------
	if 'pm' in line and duq:
		duq = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>DUQ</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PEC
#
#----------------------------------------------------------------------------
	if 'pm' in line and pec:
		pec = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PEC</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PEP
#
#----------------------------------------------------------------------------
	if 'pm' in line and pep:
		pep = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PEP</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PPL
#
#----------------------------------------------------------------------------
	if 'pm' in line and ppl:
		ppl = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PPL</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	PSG
#
#----------------------------------------------------------------------------
	if 'pm' in line and psg:
		psg = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>PSG</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	RTO
#
#----------------------------------------------------------------------------
	if 'pm' in line and rto:
		rto = 0
		rlist = line.split(" ")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>RTO</td></tr>\n<tr><td>Time</td><td>Megawatts</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[1] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[2] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[3] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[4] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[5] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[6] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[7] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	Footer
#
#----------------------------------------------------------------------------
web.write("</table></td></tr>\n</table>\n</center>\n</body>\n</html>\n")
web.close



