from pathlib import Path
import unittest

from mix_background_music import build_command


class MixBackgroundMusicTests(unittest.TestCase):
    def command(self, gain=0.25):
        return build_command(
            Path("approved-master.mp4"), Path("cue.m4a"), Path("candidate.mp4"),
            18.4, gain, 1.2, 1.5, 0.012, 6.0,
        )

    def test_preserves_video_and_encodes_new_audio(self):
        command = self.command()
        self.assertEqual(command[command.index("-c:v") + 1], "copy")
        self.assertEqual(command[command.index("-c:a") + 1], "aac")
        self.assertEqual(command[-1], "candidate.mp4")

    def test_builds_ducking_fades_limiter_and_requested_gain(self):
        command = self.command(0.375)
        graph = command[command.index("-filter_complex") + 1]
        self.assertIn("afade=t=in:st=0:d=1.2", graph)
        self.assertIn("afade=t=out:st=16.9:d=1.5", graph)
        self.assertIn("volume=0.375", graph)
        self.assertIn("sidechaincompress", graph)
        self.assertIn("alimiter=limit=0.95", graph)

    def test_rejects_source_overwrite(self):
        with self.assertRaises(ValueError):
            build_command(
                Path("master.mp4"), Path("cue.m4a"), Path("master.mp4"),
                10, 0.2, 1, 1, 0.012, 6,
            )

    def test_rejects_invalid_gain_and_duration(self):
        with self.assertRaises(ValueError):
            build_command(
                Path("master.mp4"), Path("cue.m4a"), Path("out.mp4"),
                0, 0.2, 1, 1, 0.012, 6,
            )
        with self.assertRaises(ValueError):
            build_command(
                Path("master.mp4"), Path("cue.m4a"), Path("out.mp4"),
                10, 5, 1, 1, 0.012, 6,
            )


if __name__ == "__main__":
    unittest.main()
