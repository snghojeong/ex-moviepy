import numpy
import qrcode
import argparse
from PIL import Image
from moviepy.editor import VideoFileClip, clips_array, vfx

parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description='Script for generating test video',
            )
parser.add_argument('width', metavar='out_width', nargs='?', type=int, default=1280,
                    help='Width of output video')
parser.add_argument('height', metavar='out_height', nargs='?', type=int, default=720,
                    help='Height of output video')

args = parser.parse_args()

qrcode_margin = 8

clip1 = VideoFileClip("test_vid_src_01.mp4").resize(width=args.width, height=args.height)
def scroll(get_frame, t):
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    QRcode.add_data(t)
    QRcode.make()
    QRcolor = 'Black'
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").resize((64, 64), Image.NEAREST).convert('RGB')
    qrimg_arr = numpy.asarray(QRimg);
    frame = get_frame(t)
    frame[args.height-64-qrcode_margin:args.height-qrcode_margin,args.width-64-32:args.width-32,:] = qrimg_arr[:,:,:]
    return frame
modifiedClip = clip1.fl( scroll )
modifiedClip.preview()
modifiedClip.write_videofile("test_qrcode_vga.mp4")
