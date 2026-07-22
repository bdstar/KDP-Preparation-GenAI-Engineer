def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression."""
    return str(eval(expression, {"__builtins__": {}}))   # sandboxed for the demo
 
def word_count(text: str) -> str:
    """Count the words in a piece of text."""
    return str(len(text.split()))
 
TOOLS = {"calculator": calculator, "word_count": word_count}
TOOL_SCHEMAS = [
    {"name": "calculator", "description": "Evaluate arithmetic.",
     "parameters": {"type": "object", "properties": {"expression": {"type": "string"}},
                    "required": ["expression"]}},
    {"name": "word_count", "description": "Count words in text.",
     "parameters": {"type": "object", "properties": {"text": {"type": "string"}},
                    "required": ["text"]}},
]
