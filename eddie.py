
from pydub import AudioSegment
from os.path import exists
from argparse import ArgumentParser


def extract(inf, outf):
    ff = inf[-3:]
    if ff not in ['mp4', 'flv']:
       return inf + ": Invalid file format"

    seg = AudioSegment.from_file(inf, ff)
    seg.export(outf, format='mp3')


def speedup(inf, factor):
    if inf[-3:] != 'mp3':
        return inf + ": Invalid file format"

    seg = AudioSegment.from_mp3(inf)
    seg = seg.speedup(factor)
    seg.export(inf, format='mp3')

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('mode', help="Possible modes: extract, speedup")
    parser.add_argument('input', help="input file or .txt containing a list of input files for batch processing")
    parser.add_argument('--factor', default=1.2, help="Optional speedup factor, default value = 1.2x", type=float)
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.input.endswith('.txt'):
        if not exists(args.input):
            print args.input + " doesn't exist..."
            return
        with open(args.input) as rf:
           inputs = [l.strip() for l in rf.readlines()]
    else:
        inputs = [args.input]

    for inf in inputs:
        if not exists(inf):
            ret = inf + " doesn't exist..."
        elif args.mode == 'extract':
            ret = extract(inf, inf[:-4] + '.mp3')
        elif args.mode == 'speedup':
            ret = speedup(inf, args.factor)
        if ret:
            print ret


if __name__ == '__main__':
    main()
