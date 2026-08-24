from pathlib import Path
import unittest

from finish_video import Caption, build_command, escape_drawtext, parse_caption


class FinishVideoTests(unittest.TestCase):
    def test_parse_caption_preserves_commas(self):
        self.assertEqual(parse_caption("1.5,3.25,Hello, world"), Caption(1.5, 3.25, "Hello, world"))

    def test_parse_caption_rejects_invalid_window(self):
        with self.assertRaises(Exception):
            parse_caption("4,2,Backwards")

    def test_escape_drawtext(self):
        self.assertEqual(escape_drawtext("It's 50%: ready"), r"It\'s 50\%\: ready")

    def test_build_command_contains_exact_text_and_copy_audio(self):
        command = build_command(
            Path("input.mp4"),
            Path("output.mp4"),
            [Caption(0, 2, "Find what matters")],
            "Example.ai",
            3.5,
            40,
        )
        filters = command[command.index("-vf") + 1]
        self.assertIn("Find what matters", filters)
        self.assertIn("Example.ai", filters)
        self.assertIn("gte(t,3.5)", filters)
        self.assertEqual(command[command.index("-c:a") + 1], "copy")

    def test_requires_some_finishing_work(self):
        with self.assertRaises(ValueError):
            build_command(Path("in.mp4"), Path("out.mp4"), [], None, None, 42)


if __name__ == "__main__":
    unittest.main()
