# coding: utf-8
import sys
import re
#import PIL
from PIL import Image
reload(sys)
sys.setdefaultencoding("utf-8")

global height_list

def init_global_list():
	global height_list
	height_list = []
	return

def show_global_list():
	global height_list
	print height_list
	return

def div_match(line):
	"""
	Input: line(str) - a line of html code
	Output: res(str) - the content inside the <div>...</div> tag
	"""
	res = re.match(r"(.*)<div>(.*)</div>(.*)", line, re.M|re.I)
	
	if res != None:
		return res.group(2)
	else:
		return None

def div_pic_match(line):
	res = re.match(r"(.*)<div style=\"display:inline-block\"><a href=\"(.*)\" target=\"_blank\">(.*)", line, re.M|re.I)
	if res != None:
		return res.group(2)
	else:
		return None

def pic_match(line):
	if "图片" not in line:
		return False
	else:
		return True

def get_altered_img_height(org_height):
	#res_height = 400
	if org_height > 1000:
		res_height = 1400
	elif org_height > 500:
		res_height = 380
	else:
		res_height = 280

	return res_height


def get_show_img_html(img_url):
	global height_list

	bad_img_url = "./resources/bad_img.png"
	res_code = ""
	try:
		img = Image.open(img_url)
	except Exception as e:
		img = Image.open(bad_img_url)

	img_size = img.size
	img_ratio = (img_size[0]+0.0) / (img_size[1]+0.0)
	#print img_ratio
	org_height = img_size[1]
	height_list.append(org_height)
	height = get_altered_img_height(org_height)
	width = height * img_ratio

	while (width > 700):
		org_height /= 1.2
		height = get_altered_img_height(org_height)
		width = height * img_ratio

	res_code += "\t<br>\n\t<div><img src=\"%s\" width=\"%d\" height=\"%d\"/></div>\n" %(img_url, width, height)

	return res_code


def tester_main():
	filename = './nian.html'
	#get_inline_pic_url("")
	with open(filename, 'r') as fp:

		for line_count, line in enumerate(fp):
			#line.decode('gbk', 'utf-8')
			# <div> </div>
			curr_div = div_match(line)
			#if curr_url != None:
			#	print curr_url, "\n"
			
			if pic_match(line):
				curr_pic_url = div_pic_match(line)
				print(curr_pic_url + "\n")
			continue
	return

	return

if __name__ == '__main__':
	tester_main()
