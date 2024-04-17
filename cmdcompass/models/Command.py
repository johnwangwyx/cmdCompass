from dataclasses import dataclass
from typing import List, Dict
import re

@dataclass
class Tag:
    name: str
    color: str

@dataclass
class Command:
    command_str: str
    description: str
    tags: List[Tag]

    def parse_command(self, replacements: Dict[str, str]) -> str:
        """Parses the command string, replaces variables, and handles missing keys."""
        def replace_var(match):
            var_name = match.group(1)
            if var_name not in replacements:
                raise ValueError(f"Variable '{var_name}' not found in replacements")
            return replacements[var_name]

        # Regular expression to match variables with optional spaces inside {{}}
        pattern = r"\{\{\s*(\w+)\s*\}\}"
        return re.sub(pattern, replace_var, self.command_str)