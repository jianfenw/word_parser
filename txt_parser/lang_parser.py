# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def main():
	filename = "./example_2.txt"
	with open(filename, 'r') as fp:

		judge_flag = False
		line_count = 0
		for line in fp:
			line_count += 1
			line.decode('gbk', 'utf-8')
			print line
			#print line_count, line

			#print line.index('\n')
			"""
			if "著作权" in line:
				#print "YES", line
				print line.count("著作权")

			if "判决如下" in line:
				judge_flag = True

			if judge_flag:
				print line
			"""

	print line_count


if __name__ == '__main__':
	main()
