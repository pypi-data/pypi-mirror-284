from beartype.typing import Callable
from tree_sitter_bash import language as bash_language
from tree_sitter_c import language as c_language
from tree_sitter_c_sharp import language as c_sharp_language
from tree_sitter_commonlisp import language as commonlisp_language
from tree_sitter_cpp import language as cpp_language
from tree_sitter_css import language as css_language
from tree_sitter_cuda import language as cuda_language
from tree_sitter_embedded_template import (
    language as embedded_template_language,
)
from tree_sitter_glsl import language as glsl_language
from tree_sitter_go import language as go_language
from tree_sitter_gstlaunch import language as gstlaunch_language
from tree_sitter_html import language as html_language
from tree_sitter_java import language as java_language
from tree_sitter_javascript import language as javascript_language

# from tree_sitter_arduino import language as arduino_language (issue opened https://github.com/tree-sitter-grammars/tree-sitter-arduino/issues/30)
from tree_sitter_jsdoc import language as jsdoc_language
from tree_sitter_json import language as json_language
from tree_sitter_odin import language as odin_language
from tree_sitter_php import language_php as php_language
from tree_sitter_pymanifest import language as pymanifest_language
from tree_sitter_python import language as python_language
from tree_sitter_ruby import language as ruby_language
from tree_sitter_rust import language as rust_language
from tree_sitter_scss import language as scss_language
from tree_sitter_slang import language as slang_language
from tree_sitter_starlark import language as starlark_language
from tree_sitter_toml import language as toml_language
from tree_sitter_typescript import language_typescript as typescript_language
from tree_sitter_wgsl_bevy import language as wgsl_bevy_language
from tree_sitter_yaml import language as yaml_language

conversion_dict: dict[str, Callable] = {
    "starlark": starlark_language,
    "commonlisp": commonlisp_language,
    "odin": odin_language,
    "glsl": glsl_language,
    "javascript": javascript_language,
    "python": python_language,
    "toml": toml_language,
    "bash": bash_language,
    "c_sharp": c_sharp_language,
    "c": c_language,
    "php": php_language,
    "cuda": cuda_language,
    "pymanifest": pymanifest_language,
    # "arduino": arduino_language,
    "css": css_language,
    "embedded_template": embedded_template_language,
    "jsdoc": jsdoc_language,
    "wgsl_bevy": wgsl_bevy_language,
    "html": html_language,
    "yaml": yaml_language,
    "cpp": cpp_language,
    "slang": slang_language,
    "ruby": ruby_language,
    "java": java_language,
    "scss": scss_language,
    "go": go_language,
    "json": json_language,
    "rust": rust_language,
    "typescript": typescript_language,
    "gstlaunch": gstlaunch_language,
}

__all__ = ["conversion_dict"]
