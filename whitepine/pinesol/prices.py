#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#
#      Purpose: Oasis data prices parser
#
#----------------------------------------------------------------------------
import time
import urllib2
#----------------------------------------------------------------------------
#
#	Variables
#
#----------------------------------------------------------------------------
lstamp = time.strftime("%Y%m%d")
dstamp = time.strftime("%A, %B %d, %Y")
tstamp = time.strftime("%I:%M %p")
url = 'http://www.pjm.com/pub/account/lmpda/' + lstamp + '-da.csv'
webpage = '/var/www/html/pinesol60/r/testing/1/html/prices2.html'
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
lmpdata = response.readlines()
for line in lmpdata:
	if 'WESTERN HUB' in line:
		rlist = line.split(",")
		web.write("</table>\n<tr><td>\n<table border=1 cellpadding=4>\n<tr><td colspan=2 align=center>Western HUB</td></tr>\n<tr><td>Time</td><td>Megawatt/Hour</td></tr>\n")
		web.write("<tr><td>HE13</td><td>" + rlist[43] + "</td></tr>\n")
		web.write("<tr><td>HE14</td><td>" + rlist[46] + "</td></tr>\n")
		web.write("<tr><td>HE15</td><td>" + rlist[49] + "</td></tr>\n")
		web.write("<tr><td>HE16</td><td>" + rlist[52] + "</td></tr>\n")
		web.write("<tr><td>HE17</td><td>" + rlist[55] + "</td></tr>\n")
		web.write("<tr><td>HE18</td><td>" + rlist[58] + "</td></tr>\n")
		web.write("<tr><td>HE19</td><td>" + rlist[61] + "</td></tr>\n")
#----------------------------------------------------------------------------
#
#	Footer
#
#----------------------------------------------------------------------------
web.write("</table></td></tr>\n</table>\n</center>\n</body>\n</html>\n")
web.close



