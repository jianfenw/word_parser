# coding: utf-8
import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")


# First task, the parser should match any photo url in the html file
# Then, it should download the photo. We can either store them or write them direclty
# to a word file

def get_inline_pic_url(line):

	
	return


# Second task, the parser should match any post paragraph in the html file
# Then, it should direclty output the paragraph to the word file




def global_main():
	#filename = raw_input("Please input the filename: ")
	filename = './nian.html'

	with open(filename, 'r') as fp:

		for line_count, line in enumerate(fp):
			#line.decode('gbk', 'utf-8')
			# <div> </div>

			match_obj = re.match( r'<div style="display:inline-block"><a href=(*) target="_blank">「 图片 」</a></div>', line, )
			if match_obj:
				print match_obj.group()


	return


if __name__ == '__main__':
	global_main()