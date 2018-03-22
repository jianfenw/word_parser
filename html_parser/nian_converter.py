# coding: utf-8
import sys
import os
import re
import html_parser as my_html
import img_download as my_img
reload(sys)
sys.setdefaultencoding("utf-8")


class my_post(object):
	def __init__(self):
		self.post_time = None
		self.post_content = None
		self.post_pic_time = None
		self.post_pic_url = None

	def get_my_post_time(self):
		return


# First task, the parser should match any photo url in the html file
# Then, it should download the photo. We can either store them or write them direclty
# to a word file

def get_inline_pic_url(line):

	#if "<div>" in line and "</div>" in line:
	#	print line
	url_pattern = "<div style=\"display:inline-block\"><a href=\"(.*)\" target=\"_blank\">(.*)</div>"
	div_pattern = "<div>(.*)</div>"
	res = re.match( r"(.*)<div>(.*)</div>(.*)", line, re.M|re.I)
	return res


# Second task, the parser should match any post paragraph in the html file
# Then, it should direclty output the paragraph to the word file

def global_main():
	file_dir = raw_input("Please input the file directory: ")
	#file_dir = './simple_example.html'
	file_name = None
	if "./" in file_dir:
		file_name = re.match(r"./(.*).html", file_dir, re.M|re.I).group(1)
	else:
		file_name = re.match(r"(.*).html", file_dir, re.M|re.I).group(1)
	#print file_name
	#return # for file_name parser test

	image_repo = "./resources/%s/" %(file_name)
	image_repo_exist = os.path.exists(image_repo)
	if not image_repo_exist:
		os.makedirs(image_repo)

	output_filename = "./local_%s.html" %(file_name)
	output_fp = open(output_filename, 'w')
	#output_fp.close()
	#return
	img_count = 0
	with open(file_dir, 'r') as fp:
		for line_count, line in enumerate(fp):
			if my_html.pic_match(line):
				img_count += 1
				curr_pic_url = my_html.div_pic_match(line)
				local_pic_url = image_repo+"%d.jpg" %(img_count)
				next_pic_url = image_repo+"%d.jpg" %(img_count+1)
				next_pic_img_exist = os.path.exists(next_pic_url)
				if next_pic_img_exist:
					print("Image %d exists...\n" %(img_count))
				else:
					print("Downloading a image...\n%s\nThe local file is %s\n" %(curr_pic_url, local_pic_url))
					my_img.download_image( curr_pic_url, image_repo, "%d.jpg" %(img_count) )
				
				line = line.replace( curr_pic_url, local_pic_url)
				output_fp.write(line)
				show_image_html = my_html.get_show_img_html(local_pic_url)
				output_fp.write(show_image_html)
			else:
				output_fp.write(line)

	output_fp.close()
	print("HTML Converter Ends!")
	return


if __name__ == '__main__':
	global_main()
