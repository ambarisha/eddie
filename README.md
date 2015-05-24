# Eddie

Nifty tool to convert video courses into audiobooks.

Tribute to Eddie Vedder:

[Without You](https://www.youtube.com/watch?v=r_AHWi7HR5g)
[Society](https://www.youtube.com/watch?v=lm8oxC24QZc)


#### Usage:

eddie extract <input>
eddie speedup <input> --factor f=1.2


'extract' extracts audio from video inputt
'speedup' speeds up the input by factor


#### Installation:

git clone https://github.com/ambarisha/eddie.git
cd eddie
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt


Mac OS X:

brew install libav --with-libvorbis --with-sdl --with-theora
brew install ffmpeg --with-libvorbis --with-ffplay --with-theora

Debian / Ubuntu:

apt-get install libav-tools libavcodec-extra-53
apt-get install ffmpeg libavcodec-extra-53

