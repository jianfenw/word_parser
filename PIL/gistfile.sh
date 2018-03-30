# First install Xcode via the Mac App Store (Might be required when you compile and install from source).

# Download and install JPEG libraries
curl -O http://www.ijg.org/files/jpegsrc.v8d.tar.gz
tar zxvf jpegsrc.v8d.tar.gz
cd jpeg-8d/
./configure
make
sudo make install

# Download and install Freetype libraries
curl -O http://ftp.igh.cnrs.fr/pub/nongnu/freetype/freetype-2.4.9.tar.gz
tar zxvf freetype-2.4.9.tar.gz
cd freetype-2.4.9
./configure
make
sudo make install

# Download and install PIL
curl -O -L http://effbot.org/downloads/Imaging-1.1.7.tar.gz
tar -xzf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
python setup.py build
sudo python setup.py install

