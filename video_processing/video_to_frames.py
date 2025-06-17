import moviepy.editor as mp
import os
import zipfile
import numpy as np

def video_to_frames_time_range_and_zip(video_path, output_folder, zip_filename, start_time_sec, end_time_sec, frame_rate=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        clip = mp.VideoFileClip(video_path)
        total_duration = clip.duration

        start_time_sec = max(0, start_time_sec)
        end_time_sec = min(total_duration, end_time_sec)

        if start_time_sec >= end_time_sec:
            print("Error: Invalid time range.")
            return

        frame_times = np.arange(start_time_sec, end_time_sec, 1.0 / frame_rate)
        if end_time_sec not in frame_times:
            frame_times = np.append(frame_times, end_time_sec)
            frame_times = np.unique(frame_times)

        extracted_frame_paths = []

        for i, frame_time in enumerate(frame_times):
            frame_path = os.path.join(output_folder, f"frame_{i:06d}.png")
            try:
                clip.save_frame(frame_path, t=frame_time)
                extracted_frame_paths.append(frame_path)
            except Exception as e:
                print(f"Failed to extract frame at {frame_time}s: {e}")

        if extracted_frame_paths:
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for frame_path in extracted_frame_paths:
                    zipf.write(frame_path, os.path.basename(frame_path))

    finally:
        import shutil
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)
