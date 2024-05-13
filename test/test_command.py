import unittest
from cmdcompass.models.command import Command
from cmdcompass.models.tag import Tag

class TestCommand(unittest.TestCase):
    def setUp(self):
        self.tag1 = Tag("Network", "blue", uuid="tag1")
        self.tag2 = Tag("Database", "green", uuid="tag2")
        self.command = Command(
            command_str="ping {{ host  }} -c {{count}}",
            comment="Ping a host",
            tag_ids=["tag1", "tag2"],
        )

    def test_parse_command_success(self):
        replacements = {"host": "google.com", "count": "4"}
        parsed_command = self.command.parse_template(replacements)
        self.assertEqual(parsed_command, "ping google.com -c 4")

    def test_parse_command_missing_variable(self):
        replacements = {"host": "google.com"}  # Missing 'count', so fail
        with self.assertRaises(ValueError) as context:
            self.command.parse_template(replacements)
        self.assertEqual(str(context.exception), "Variable 'count' not found in replacements")

    def test_parse_command_extra_spaces(self):
        replacements = {"host": "google.com", "count": "4"}
        command_with_spaces = Command(
            command_str="ping {{  host }} -c {{ count     }}", 
            comment="Ping a host",
            tag_ids=["tag1", "tag2"]
        )
        parsed_command = command_with_spaces.parse_template(replacements)
        self.assertEqual(parsed_command, "ping google.com -c 4")

    def test_extract_options_tar(self):
        command = Command(
            command_str="tar -czvf 'filename.tar'",
            comment="Create a tar archive",
            tag_ids=["tag1", "tag2"]
        )
        self.assertEqual(command.extract_options(), {'c', 'z', 'v', 'f'})

    def test_extract_options_grep(self):
        command = Command(
            command_str="grep --color=auto --context=2 'some_pattern' 'some_file'",
            comment="Grep with color and context",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.extract_options(), {'color', 'context'})

    def test_extract_options_ls(self):
        command = Command(
            command_str="ls -la --color=auto",
            comment="List directory contents with detail",
            tag_ids=["tag2"]
        )
        self.assertEqual(command.extract_options(), {'l', 'a', 'color'})

    def test_extract_options_gcc(self):
        command = Command(
            command_str="gcc -O2 -Wall 'test.c' -o test",
            comment="Compile a C program with gcc",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.extract_options(), {'O', '2', 'W', 'a', 'l', 'o'})

    def test_extract_options_curl(self):
        command = Command(
            command_str="curl -X POST --header 'Content-Type: application/json' --data '{}' http://example.com",
            comment="Make a POST request with curl",
            tag_ids=["tag2"]
        )
        self.assertEqual(command.extract_options(), {'X', 'header', 'data'})

    def test_extract_options_mount(self):
        command = Command(
            command_str="mount -t ext4 /dev/sda1 /mnt",
            comment="Mount an ext4 filesystem",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.extract_options(), {'t'})

    def test_extract_options_git(self):
        command = Command(
            command_str="git commit -m 'Initial commit'",
            comment="Commit changes with git",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.extract_options(), {'m'})

    def test_extract_options_wget(self):
        command = Command(
            command_str="wget --mirror -p --convert-links -P './local-dir' http://site.com",
            comment="Download a website with wget",
            tag_ids=["tag2"]
        )
        self.assertEqual(command.extract_options(), {'mirror', 'p', 'convert', 'P'})

    def test_extract_options_docker(self):
        command = Command(
            command_str="docker run -d --name mycontainer ubuntu /bin/bash",
            comment="Run a Docker container",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.extract_options(), {'d', 'name'})

    def test_get_template_variables_basic(self):
        command = Command(
            command_str="echo {{name}}",
            comment="Echo a name",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.get_template_variables(), ['name'])

    def test_get_template_variables_multiple(self):
        command = Command(
            command_str="curl -d '{{data}}' http://example.com/api/{{endpoint}}",
            comment="Send data to an API endpoint",
            tag_ids=["tag1", "tag2"]
        )
        self.assertEqual(sorted(command.get_template_variables()), ['data', 'endpoint'])

    def test_get_template_variables_none(self):
        command = Command(
            command_str="ls -l",
            comment="List directory contents",
            tag_ids=["tag2"]
        )
        self.assertEqual(command.get_template_variables(), [])

    def test_get_template_variables_repeated(self):
        command = Command(
            command_str="ping {{host}} -c 4 && ping {{host}} -c 4",
            comment="Ping a host twice",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.get_template_variables(), ['host', 'host'])

    def test_get_template_variables_with_spaces(self):
        command = Command(
            command_str="scp {{ source }} {{ destination }}",
            comment="Secure copy from source to destination",
            tag_ids=["tag2"]
        )
        self.assertEqual(sorted(command.get_template_variables()), ['destination', 'source'])

    def test_get_template_variables_special_chars(self):
        command = Command(
            command_str="echo '{{greeting_message}}' > /dev/null",
            comment="Echo a greeting to null",
            tag_ids=["tag1"]
        )
        self.assertEqual(command.get_template_variables(), ['greeting_message'])

    def test_get_template_variables_nested(self):
        command = Command(
            command_str="docker run --name {{container_name}} ubuntu bash -c 'echo {{message}}'",
            comment="Run a Docker container and echo a message",
            tag_ids=["tag2"]
        )
        self.assertEqual(sorted(command.get_template_variables()), ['container_name', 'message'])

    def test_get_template_variables_case_sensitivity(self):
        command = Command(
            command_str="mv {{SourcePath}} {{destinationPath}}",
            comment="Move files from SourcePath to destinationPath",
            tag_ids=["tag1"]
        )
        self.assertEqual(sorted(command.get_template_variables()), ['SourcePath', 'destinationPath'])

    def test_get_template_variables_with_numbers(self):
        command = Command(
            command_str="ffmpeg -i input.mp4 -r {{frame_rate}} output.mp4",
            comment="Change the frame rate of a video",
            tag_ids=["tag2"]
        )
        self.assertEqual(command.get_template_variables(), ['frame_rate'])

    def test_get_template_variables_complex(self):
        command = Command(
            command_str="ssh -i {{private_key}} {{user}}@{{host}}",
            comment="SSH into a host with a private key",
            tag_ids=["tag1", "tag2"]
        )
        self.assertEqual(sorted(command.get_template_variables()), ['host', 'private_key', 'user'])

if __name__ == "__main__":
    unittest.main()