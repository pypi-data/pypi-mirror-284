#!/usr/bin/env python

schema = {
    "type": "object",
    "required": ["issue", "status"],
    "properties": {"issue": {"type": "string"}, "status": {"type": "string"}},
    "additionalProperties": False,
}
