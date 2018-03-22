# HTML FILE Parser
The repo contains the html file parser.<br>
Recently, the developer for an iOS app 'Nian' has claimed that he is going to stop the Nian's service. If you were an user, you may want to download all your past post. Otherwise, when the app service stops, your data will get lost.<br>
'Nian' provides you a download link to download your post book. However, for these post books, your cannot see your uploaded photos. These photos are just some URLs linked to the images, which are still stored in their servers.<br>
This tool is used to automate the process to download the images in a html file, store them locally, and modify the html file to make these images visible.<br>

# How to use it
(1) install git in your computer :-)<br>
(2) clone this repo :-)<br>
Open your terminal and type:<br>
- $git clone https://github.com/jwangee/word_parser.git<br>
(plz fork it if you like this tool :-) )<br>
(3) visit the html_parser repo, and place your html file into that directory<br>
If you are cool people, you should always use command line to do things, even when you COPY and PASTE<br>
(4) run my pipeline<br>
Let's assume that you are in the html_parser directory (inside your terminal). The target html file is called 'simple\_example.html'.<br>
You can run this tool by typing the following into your terminal:<br>
- $python nian\_converter.py<br>
Then, the tool will ask you to pass the file name.<br>
- simple\_example.html<br>
After that, you go and grap a cup of coffer. When you come back, your output file is ready. The output file is named as 'local_simple\_example.html'.<br>

# Where are my photos
All your photos are stored in the 'resources' directory. Each repo is named the same as its html file's name.<br>
Hope you like it!