"""
* IMG_DOWNLOAD.PY
* This file is used to provide function to download images.
* (Let's assume you can access the image through Internet)
* For my personal interests, I include most of the methods to download images
* when you have the image url. 
*
* Author: Jianfeng Wang
* Email: jianfenw@usc.edu
* Organization: USC
*
"""

# coding: utf-8
import sys
import re
import urllib
reload(sys)
sys.setdefaultencoding("utf-8")

def download_image( img_url, local_save_repo, local_filename ):
	urllib.urlretrieve( img_url, local_save_repo+local_filename)
	return

def tester_main():
	"""
	The main tester function:
	It is used to download a test image from the following URL.
	I store this image locally in the following directory, i.e. "./1.jpg".
	For any user, you should remember to decide your own image repo.
	Also, you should handle your image naming very well to avoid conflicts.
	"""
	img_url = "https://urldefense.proofpoint.com/v2/url?u=http-3A__img.nian.so_step_50121-5F1412258647.jpg&d=DwMGaQ&c=clK7kQUTWtAVEOVIgvi0NU5BOUHhpN0H8p7CSfnc_gI&r=XybUqauKSbpZL9Xe2uI0yA&m=8y67cIW4UZQHrFvXSG8cTQPeiuVOIpsKesC8sBoobkE&s=CbVPBX7uoUEzt5qpZ8FWal9CsmF_uzgWZ244mLjdy4c&e="
	download_image(img_url, "./num/", "1.jpg")
	return


if __name__ == '__main__':
	tester_main()
