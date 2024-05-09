from dataclasses import dataclass, field
from typing import List, Dict
import re
import uuid

@dataclass
class Command:
    command_str: str
    comment: str
    tag_ids: List[str]
    uuid: str = field(default_factory=lambda: str(uuid.uuid4()))

    def get_template_variables(self) -> List[str]:
        """Extracts variables enclosed in {{}} from the command string."""
        pattern = r"\{\{\s*(\w+)\s*\}\}"
        matches = re.findall(pattern, self.command_str)
        return matches

    def parse_template(self, replacements: Dict[str, str]) -> str:
        """Parses the command string, replaces variables, and handles missing keys."""
        def replace_var(match):
            var_name = match.group(1)
            if var_name not in replacements:
                raise ValueError(f"Variable '{var_name}' not found in replacements")
            return replacements[var_name]

        # Regular expression to match variables with optional spaces inside {{}}
        pattern = r"\{\{\s*(\w+)\s*\}\}"
        return re.sub(pattern, replace_var, self.command_str)