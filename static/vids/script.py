from moviepy.editor import VideoFileClip
import argparse
import os

def gif_to_mp4(gif_path, output_path, fps):
    clip = VideoFileClip(gif_path)
    clip.write_videofile(output_path, fps=fps)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a GIF to MP4.')
    parser.add_argument('gif_path', type=str, help='The path to the GIF file.')
    parser.add_argument('--output_path', type=str, help='The path where the MP4 will be saved.')
    parser.add_argument('--fps', type=int, default=10, help='The desired frames per second for the MP4.')
    
    args = parser.parse_args()

    # 如果 output_path 参数未指定，则默认将输出 MP4 与输入 GIF 同名（但扩展名不同）
    if args.output_path is None:
        base_name = os.path.basename(args.gif_path)
        name_without_ext = os.path.splitext(base_name)[0]
        args.output_path = f"{name_without_ext}.mp4"
    
    gif_to_mp4(args.gif_path, args.output_path, args.fps)
