import numpy
import qrcode
from PIL import Image
from moviepy.editor import VideoFileClip, clips_array, vfx

clip1 = VideoFileClip("test_vid_src_01.mp4").resize(width=640, height=360)
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
    frame[640-64:640,360-64:360,:] = qrimg_arr[:,:,:]
    return frame
modifiedClip = clip1.fl( scroll )
modifiedClip.preview()
#modifiedClip.write_videofile("my_stack.mp4")
