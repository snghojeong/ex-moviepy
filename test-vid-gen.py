from moviepy.editor import VideoFileClip, clips_array, vfx

clip1 = VideoFileClip("test_vid_src_01.mp4").resize(width=320, height=180)
def scroll(get_frame, t):
    frame = get_frame(t)
    frame_region = frame[:,:,[0,2,1]]
    return frame_region
modifiedClip = clip1.fl( scroll )
modifiedClip.preview()
#modifiedClip.write_videofile("my_stack.mp4")
