from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip("test_vid_src_01.mp4").margin(10).resize(width=640, height=360) # add 10px contour
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip1.resize(0.60) # downsize 60%
final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])
final_clip.write_videofile("my_stack.mp4")
