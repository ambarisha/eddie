# Eddie

Nifty tool to convert video courses into audiobooks.

Tribute to Eddie Vedder: 
[Without You](https://www.youtube.com/watch?v=r_AHWi7HR5g),
[Society](https://www.youtube.com/watch?v=lm8oxC24QZc)


#### Usage:

`python eddie.py extract <input>`

`python eddie.py speedup <input> --factor f=1.2`


'extract' extracts audio from video input

'speedup' speeds up the input by factor

'input' input file or a .txt containing paths to input files for batch processing


#### Installation:

`git clone https://github.com/ambarisha/eddie.git`

`cd eddie`

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`


Mac OS X:

`brew install libav --with-libvorbis --with-sdl --with-theora`

`brew install ffmpeg --with-libvorbis --with-ffplay --with-theora`

Debian / Ubuntu:

`apt-get install libav-tools libavcodec-extra-53`

`apt-get install ffmpeg libavcodec-extra-53`

