import os
import sys
from typing import List, Callable, Dict, Any
import tiktoken
from langchain_text_splitters import RecursiveCharacterTextSplitter
from litellm import completion

class FabricTextProcessor:
    def __init__(self, model: str = "gpt-4-turbo", max_tokens_per_chunk: int = 1000):
        self.model = model
        self.max_tokens_per_chunk = max_tokens_per_chunk
        self.encoding = tiktoken.encoding_for_model(model)
        self.config = {}

    def preprocess_text(self, text: str) -> str:
        paragraphs = text.split('\n\n')
        processed_paragraphs = []
        
        for paragraph in paragraphs:
            lines = paragraph.split('\n')
            processed_lines = []
            for i, line in enumerate(lines):
                if i == 0 or not line.strip():
                    processed_lines.append(line)
                elif (len(line) > 0 and not line[0].isupper() and not line[0].isdigit() and 
                    i > 0 and len(lines[i-1].strip()) > 0 and 
                    lines[i-1].strip()[-1] not in '.!?:;'):
                    processed_lines[-1] += ' ' + line.strip()
                else:
                    processed_lines.append(line)
            processed_paragraphs.append('\n'.join(processed_lines))
        
        return '\n\n'.join(processed_paragraphs)

    def split_text(self, text: str) -> List[str]:
        preprocessed_text = self.preprocess_text(text)
        chars_per_token = len(preprocessed_text) / len(self.encoding.encode(preprocessed_text))
        max_chars = int(self.max_tokens_per_chunk * chars_per_token)
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=max_chars,
            chunk_overlap=50,
            length_function=lambda t: len(self.encoding.encode(t)),
            separators=["\n\n", "\n", "。", "！", "？", "；", "，", ".", "!", "?", ";", ",", " ", ""]
        )
        chunks = text_splitter.split_text(preprocessed_text)
        
        return [self._split_chunk(chunk) if len(self.encoding.encode(chunk)) > self.max_tokens_per_chunk else chunk for chunk in chunks]

    def _split_chunk(self, chunk: str) -> str:
        import re
        sentences = re.split(r'(?<=[。！？.!?])\s*', chunk)
        sub_chunks = []
        current_sub_chunk = []
        current_token_count = 0

        for sentence in sentences:
            sentence_token_count = len(self.encoding.encode(sentence))
            if current_token_count + sentence_token_count > self.max_tokens_per_chunk:
                if current_sub_chunk:
                    sub_chunks.append(" ".join(current_sub_chunk))
                    current_sub_chunk = []
                    current_token_count = 0
            
            current_sub_chunk.append(sentence)
            current_token_count += sentence_token_count

        if current_sub_chunk:
            sub_chunks.append(" ".join(current_sub_chunk))

        return " ".join(sub_chunks)

    def read_system_prompt(self, pattern_name: str) -> str:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        system_prompt_path = os.path.join(project_root, 'patterns', pattern_name, 'system.md')
        try:
            with open(system_prompt_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except IOError as e:
            self.log_error(f"Error reading system prompt: {e}")
            sys.exit(1)

    def query_api(self, messages: List[Dict[str, str]], model: str) -> str:
        try:
            response = completion(model=model, messages=messages)
            return response.choices[0].message.content
        except Exception as e:
            self.log_error(f"Error calling API: {e}")
            sys.exit(1)

    def process_chunk(self, chunk: str) -> str:
        raise NotImplementedError("Subclasses must implement process_chunk method")

    def process_text(self, text: str) -> List[str]:
        preprocessed_text = self.preprocess_headers(text)
        chunks = self.split_text(preprocessed_text)
        return [self.process_chunk(chunk) for chunk in chunks]

    def log_error(self, message: str):
        print(f"ERROR: {message}", file=sys.stderr)

    def set_config(self, key: str, value: Any):
        self.config[key] = value

    def get_config(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def preprocess_headers(self, text: str) -> str:
        lines = text.split('\n')
        return '\n'.join('## ' + line[2:] if line.startswith('# ') else line for line in lines)

    def process_chunks(self, chunks: List[str], pipeline: List[Callable]) -> List[str]:
        return [self.process_single_chunk(chunk, pipeline) for i, chunk in enumerate(chunks, 1)]

    def process_single_chunk(self, chunk: str, pipeline: List[Callable]) -> str:
        for step in pipeline:
            chunk = step(self, chunk)
        return chunk