#!/usr/bin/env python3
"""Verify encoded media expectations with installed FFmpeg tools; no writes."""
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--duration', type=float)
    parser.add_argument('--size', help='Expected encoded WIDTHxHEIGHT')
    parser.add_argument('--fps', type=float)
    parser.add_argument('--tolerance', type=float, default=0.1)
    parser.add_argument('--web-compatible', action='store_true')
    parser.add_argument('--decode', action='store_true')
    parser.add_argument('--timeout', type=float, default=300)
    args = parser.parse_args()
    if not all(math.isfinite(v) for v in [args.timeout, args.tolerance] + [v for v in [args.duration, args.fps] if v is not None]):
        parser.error('numeric expectations must be finite')
    if args.timeout <= 0 or args.tolerance < 0:
        parser.error('timeout must be positive and tolerance nonnegative')
    if any(v is not None and v <= 0 for v in [args.duration, args.fps]):
        parser.error('expected duration and frame rate must be positive')
    expected_size = None
    if args.size:
        try:
            expected_size = tuple(map(int, args.size.lower().split('x')))
            assert len(expected_size) == 2 and min(expected_size) > 0
        except (ValueError, AssertionError):
            parser.error('size must contain positive WIDTHxHEIGHT integers')
    report = {'file': args.video.name, 'ok': False, 'errors': []}
    try:
        if not args.video.is_file():
            raise ValueError('Selected video is not a regular file')
        # Resolve local names before passing them to FFmpeg's protocol parser.
        media_path = args.video.resolve(strict=True)
        for tool in ['ffprobe'] + (['ffmpeg'] if args.decode else []):
            if shutil.which(tool) is None:
                raise ValueError(f'Required installed tool unavailable: {tool}')
        result = subprocess.run(['ffprobe', '-v', 'error', '-protocol_whitelist',
                                 'file,pipe', '-show_format', '-show_streams',
                                 '-of', 'json', str(media_path)],
                                capture_output=True, text=True, timeout=args.timeout)
        if result.returncode:
            raise ValueError('ffprobe could not read the selected media')
        probe = json.loads(result.stdout)
        videos = [s for s in probe['streams'] if s['codec_type'] == 'video']
        if not videos:
            raise ValueError('No video stream')
        video = videos[0]
        audio = [s for s in probe['streams'] if s['codec_type'] == 'audio']
        duration = float(probe['format']['duration'])
        fps = float(Fraction(video.get('avg_frame_rate', '0/1')))
        size = (video['width'], video['height'])
        rotations = [int(float(video.get('tags', {}).get('rotate', '0')))]
        rotations += [int(float(s['rotation'])) for s in video.get('side_data_list', []) if 'rotation' in s]
        report.update(duration_seconds=duration, size=list(size), fps=fps,
                      codec=video['codec_name'], pixel_format=video.get('pix_fmt'),
                      sample_aspect_ratio=video.get('sample_aspect_ratio'),
                      frames=video.get('nb_frames'), rotation_degrees=rotations,
                      audio=[{k: s.get(k) for k in ['codec_name', 'sample_rate', 'channels']} for s in audio])
        if duration <= 0 or min(size) <= 0 or fps <= 0:
            report['errors'].append('Nonpositive duration, dimensions or frame rate')
        if args.duration is not None and abs(duration - args.duration) > args.tolerance:
            report['errors'].append('Duration differs from the selected expectation')
        if expected_size and expected_size != size:
            report['errors'].append('Encoded dimensions differ from the selected expectation')
        if args.fps is not None and abs(fps - args.fps) > 0.01:
            report['errors'].append('Frame rate differs from the selected expectation')
        if args.web_compatible:
            if video['codec_name'] != 'h264' or video.get('pix_fmt') != 'yuv420p':
                report['errors'].append('Selected web profile requires H264/yuv420p')
            if any(s['codec_name'] != 'aac' for s in audio):
                report['errors'].append('Selected web profile requires AAC when audio is present')
            if video.get('sample_aspect_ratio') not in [None, '1:1', 'N/A'] or any(r % 360 for r in rotations):
                report['errors'].append('Non-square pixels or rotation require explicit framing review')
        if args.decode:
            decoded = subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-xerror',
                                      '-protocol_whitelist', 'file,pipe',
                                      '-i', str(media_path), '-map', '0:v:0',
                                      '-map', '0:a?', '-f', 'null', '-'],
                                     capture_output=True, text=True, timeout=args.timeout)
            report['decode'] = 'passed' if decoded.returncode == 0 and not decoded.stderr.strip() else 'failed'
            if report['decode'] == 'failed':
                report['errors'].append('Full decode failed or reported errors')
        report['ok'] = not report['errors']
    except (ValueError, KeyError, OSError, ZeroDivisionError, subprocess.TimeoutExpired) as error:
        report['errors'].append(str(error))
    print(json.dumps(report, indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
