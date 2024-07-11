import pprint
import re
from types import FrameType
from typing import Optional

from anthropic.types import ContentBlock

from ai_pdb.strings import (
    ERROR_INFO,
    CONTEXT,
    DEBUG_PROMPT,
    QUERY_PROMPT,
    DOCS_PROMPT,
    RESPONSE,
    SYSTEM_PROMPT,
)
from ai_pdb.types import Command

command_map: dict[Command, str] = {
    "debug": DEBUG_PROMPT,
    "query": QUERY_PROMPT,
    "docs": DOCS_PROMPT,
}


class PromptFormatter:
    system: str = SYSTEM_PROMPT

    def format(
        self,
        command: Command,
        query: Optional[str],
        frame: Optional[FrameType],
        source_context: str,
        last_exception: Optional[dict],
    ) -> str:
        debugger_context = self._format_debugger_context(
            frame,
            source_context,
            last_exception,
        )

        prompt = command_map.get(command, DEBUG_PROMPT)

        return prompt.format(debugger_context=debugger_context, query=query)

    def _format_debugger_context(
        self,
        frame: Optional[FrameType],
        code_context: str,
        last_exception: Optional[dict],
    ) -> str:
        if not frame:
            return "No active frame available for debugging."

        context = CONTEXT.format(
            filename=frame.f_code.co_filename,
            current_line=frame.f_lineno,
            function_name=frame.f_code.co_name,
            code_context=code_context,
            local_vars=pprint.pformat(frame.f_locals, indent=2),
            last_exception=self._format_exception(last_exception),
        )

        return self._strip(context)

    def _format_exception(self, last_exception: Optional[dict]) -> str:
        if not last_exception:
            return "No error captured in the current debugging session."

        return ERROR_INFO.format(
            error_type=last_exception["type"],
            error_message=last_exception["value"],
            traceback=last_exception["traceback"],
        )

    def _strip(self, context: str) -> str:
        context = re.sub(r"[^\S\n]+", " ", context)
        context = re.sub(r"^ +", "", context, flags=re.MULTILINE)
        context = re.sub(r" +$", "", context, flags=re.MULTILINE)
        context = re.sub(r"\n\s*\n", "\n", context)

        return context.strip()


class ResponseFormatter:
    def format(self, response: list[ContentBlock]) -> str:
        width = 80
        separator = "*" * width

        formatted_response = RESPONSE.format(separator=separator)
        for message in response:
            if message.type == "tool_use":
                continue

            formatted_response += message.text + "\n\n"

        formatted_response += f"{separator}\n"

        return formatted_response
