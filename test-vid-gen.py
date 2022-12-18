import numpy
import qrcode
from PIL import Image
from moviepy.editor import VideoFileClip, clips_array, vfx

out_width = 640
out_height = 360

clip1 = VideoFileClip("test_vid_src_01.mp4").resize(width=out_width, height=out_height)
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
    frame[out_height-64-32:out_height-32,out_width-64-32:out_width-32,:] = qrimg_arr[:,:,:]
    return frame
modifiedClip = clip1.fl( scroll )
modifiedClip.preview()
#modifiedClip.write_videofile("my_stack.mp4")
