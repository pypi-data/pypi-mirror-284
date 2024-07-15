<p align="center">
  <img src="https://raw.githubusercontent.com/hypergrok/chunkit/main/chn.png" alt="chunkit" width="200"/>
</p>

<div align="center">
  <a href="https://badge.fury.io/py/chunkit"><img src="https://badge.fury.io/py/chunkit.svg" alt="PyPI version" /></a>
  <a href="https://pepy.tech/project/chunkit"><img src="https://pepy.tech/badge/chunkit" alt="Downloads" /></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0.html"><img src="https://img.shields.io/badge/License-AGPL%20v3-blue.svg" alt="License: AGPL v3" /></a>
</div>

<h3 align="center">Turn URLs into LLM-friendly markdown chunks</h3>

Install:

```bash
pip install chunkit
```

Start chunking:

```python
from chunkit import Chunker

# Initialize the Chunker
chunker = Chunker()

# Define URLs to process
urls = ["https://en.wikipedia.org/wiki/Chunking_(psychology)"]

# Process the URLs into markdown chunks
chunkified_urls = chunker.process(urls)

# Output the resulting chunks
for item in chunkified_urls:
    print(f"Chunking for url {item['url']} successful: {item['success']}")
    if item['success']:
        for chunk in item['chunks']:
            print("-"*64)
            print(chunk[:100]+'...')
```
Example results:
```markdown
### Chunking (psychology)

In cognitive psychology, **chunking** is a process by which small individual pieces of a set of information are bound together to create a meaningful whole later on in memory. The chunks, by which the information is grouped, are meant to improve short-term retention of the material, thus bypassing the limited capacity of working memory...
```
```markdown
### Modality effect

A modality effect is present in chunking. That is, the mechanism used to convey the list of items to the individual affects how much "chunking" occurs. Experimentally, it has been found that auditory presentation results in a larger amount of grouping in the responses of individuals than visual presentation does...
```
```markdown
### Memory training systems, mnemonic

Various kinds of memory training systems and mnemonics include training and drills in specially-designed recoding or chunking schemes. Such systems existed before Miller's paper, but there was no convenient term to describe the general strategy and no substantive and reliable research...
```

### Chunkit Core

Chunkit Core is free OSS and handles only HTML. For further filetypes use Chunkit Plus.

### Chunkit Plus

Chunkit Plus allows you to chunk further filetypes: PDF, CSV, JSON, YAML, MD and DOCX.

1. Go to [app.chunkit.dev](https://app.chunkit.dev) and log in.
2. Navigate to Deploy API section.
3. Generate a new API key.
4. Same usage as above, but initialize Chunker with API key:

```python
from chunkit import Chunker

# Initialize the Chunker
chunker = Chunker(api_key='your-api-key-here')
```
That's it! Enjoy chunking.
### License

This project is licensed under AGPL v3 - see the [LICENSE](LICENSE) file for details.

### Contact

For questions or support, please open an issue. 