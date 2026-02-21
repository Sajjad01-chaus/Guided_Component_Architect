import json

def build_generation_prompt(user_prompt, design_system, previous_component=None):
    context_block = ""
    if previous_component:
        context_block = f"""
You are modifying an existing Angular component.
Existing Component:
{json.dumps(previous_component, indent=2)}
"""

    return f"""
You are a senior Angular UI architect.

STRICT REQUIREMENTS:
- Output ONLY valid JSON.
- No markdown.
- No explanation.

JSON schema:
{{
  "typescript": "...",
  "html": "...",
  "css": "..."
}}

DESIGN SYSTEM (DO NOT DEVIATE):
{json.dumps(design_system, indent=2)}

Rules:
- Use ONLY provided colors.
- Use borderRadius exactly.
- Use fontFamily exactly.
- Angular Material + Tailwind allowed.
- TypeScript must be valid.

{context_block}

User Request:
{user_prompt}
"""