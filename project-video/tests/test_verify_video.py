"""Exercise the export checker against real media and real failure cases."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'verify_video.py'


class ExportCheckTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not all(shutil.which(tool) for tool in ['ffmpeg', 'ffprobe']):
            raise unittest.SkipTest('FFmpeg/FFprobe are required for actual-media tests')
        cls.scratch = tempfile.TemporaryDirectory(prefix='project-video-test-')
        cls.directory = Path(cls.scratch.name)
        cls.movie = cls.directory / 'example.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-f', 'lavfi',
                        '-i', 'testsrc2=size=320x180:rate=24', '-f', 'lavfi',
                        '-i', 'sine=frequency=880:sample_rate=48000', '-t', '1',
                        '-c:v', 'libx264', '-threads', '1', '-pix_fmt', 'yuv420p',
                        '-c:a', 'aac', '-y', str(cls.movie)],
                       capture_output=True, check=True, timeout=30)

    @classmethod
    def tearDownClass(cls):
        cls.scratch.cleanup()

    def invoke(self, *args, env=None):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              capture_output=True, text=True, timeout=30, env=env)

    def test_real_export_decodes_and_checker_is_read_only(self):
        before = {p.name: p.read_bytes() for p in self.directory.iterdir()}
        result = self.invoke(self.movie, '--duration', '1', '--size', '320x180',
                             '--fps', '24', '--web-compatible', '--decode')
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        report = json.loads(result.stdout)
        self.assertTrue(report['ok'])
        self.assertEqual(report['decode'], 'passed')
        self.assertEqual(report['frames'], '24')
        self.assertEqual(report['audio'][0]['codec_name'], 'aac')
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.directory.iterdir()})

    def test_wrong_expectations_fail(self):
        for expectation in [('--duration', '30'), ('--size', '180x320'), ('--fps', '30')]:
            with self.subTest(expectation=expectation):
                result = self.invoke(self.movie, *expectation)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(json.loads(result.stdout)['ok'])

    def test_invalid_media_does_not_pass(self):
        invalid = self.directory / 'not-media.txt'
        invalid.write_text('Not a media recording.\n')
        try:
            result = self.invoke(invalid)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(json.loads(result.stdout)['ok'])
        finally:
            invalid.unlink()

    def test_missing_tool_is_reported_as_a_gap(self):
        result = self.invoke(self.movie, env={**os.environ, 'PATH': ''})
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(json.loads(result.stdout)['ok'])

    def test_nonfinite_expectation_is_refused(self):
        result = self.invoke(self.movie, '--duration', 'nan')
        self.assertNotEqual(result.returncode, 0)

    def test_local_colon_filename_is_not_interpreted_as_a_protocol(self):
        selected = self.directory / 'http:example.mp4'
        shutil.copyfile(self.movie, selected)
        try:
            # Execute from that directory to exercise a relative colon name.
            result = subprocess.run([sys.executable, str(SCRIPT), selected.name,
                                     '--decode'], cwd=self.directory,
                                    capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(json.loads(result.stdout)['ok'])
        finally:
            selected.unlink()


if __name__ == '__main__':
    unittest.main()
