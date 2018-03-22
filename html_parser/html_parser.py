# coding: utf-8
import sys
import re
#import PIL
#from PIL import Image
reload(sys)
sys.setdefaultencoding("utf-8")

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

def get_show_img_html(img_url):
	res_code = ""
	#img = Image.open(img_url)
	#print(img.size)
	res_code += "\t<br>\n\t<div><img src=\"%s\" width=\"230\" height=\"400\"/></div>\n" %(img_url)

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
