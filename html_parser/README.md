# HTML FILE Parser
The repo contains the html file parser.<br>

Recently, the developer for an iOS app `Nian` has claimed that he is going to stop the `Nian`'s service. If you were an user, you must want to download all your past posts. Otherwise, when the app stops running its service, all your data will get lost.<br>

`Nian` provides you a link to download your post book. In fact, these books are just some html files. In these html files, your cannot directly see your uploaded photos. These photos are some URLs linked to the posted images, which are still stored in their servers.<br>

This tool is used to automate the process to download the images in a html file, store them locally, and modify the html file to make these images visible.<br>

# How to use it
(1) Install git in your computer :-)<br>

(2) Clone this repo :-)<br>
Open your terminal and type:<br>
```bash
$ git clone https://github.com/jwangee/word_parser.git
```
(Please `fork` it if you like this tool :-) )<br>

(3) Visit the html_parser repo, and place your html file into that directory<br>
If you are cool people, you should always use command line to do things, even when you COPY and PASTE<br>

(4) Run this tool<br>
Let's assume that you are in the html_parser directory (inside your terminal). The target html file is called 'simple\_example.html'.<br>
You can run this tool by typing the following into your terminal:<br>
```bash
$ python nian_converter.py
```
Then, the tool will ask you to pass the file name.<br>
```bash
simple_example.html
```
After that, you go and grap a cup of coffer. When you come back, your output file is ready. The output file is named as 'local_simple\_example.html'.<br>

# Where are my images stored
All your images are stored in the 'resources' directory. For a html file, the corresponding repo is named the same as the html file's name.<br>
Hope you like it!<br>