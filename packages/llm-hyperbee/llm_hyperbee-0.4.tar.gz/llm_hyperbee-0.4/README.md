# llm-hyperbee

[![PyPI](https://img.shields.io/pypi/v/llm-fireworks.svg)](https://pypi.org/project/llm-hyperbee/)
[![Changelog](https://img.shields.io/github/v/release/HyperbeeAI/llm-hyperbee?include_prereleases&label=changelog)](https://github.com/HyperbeeAI/llm-hyperbee/releases)
[![Tests1](https://github.com/HyperbeeAI/llm-hyperbee/actions/workflows/test.yml/badge.svg)](https://github.com/HyperbeeAI/llm-hyperbee/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/HyperbeeAI/llm-hyperbee/blob/main/LICENSE)

Access [hyperbee.ai](https://www.hyperbee.ai/) models via API

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-hyperbee
```
## Usage
Obtain a [Hyperbee API key](https://www.hyperbee.ai/) and save it like this:

```bash
llm keys set hyperbee
# <Paste key here>
```

Run `llm models` to get a list of models.

Run prompts like this:
```bash
llm -m hyperbee 'five great names for a pet ocelot'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-hyperbee
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
