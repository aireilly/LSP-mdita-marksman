# LSP-mdita-marksman

![LICENSE](https://img.shields.io/badge/LICENSE-MIT-green?style=for-the-badge) ![Sublime Text](https://img.shields.io/badge/ST-Build%204126+-orange?style=for-the-badge&logo=sublime-text)

`LSP-mdita-marksman` is a LSP helper package for the [MDITA Marksman](https://github.com/aireilly/mdita-marksman) language server. It acts as a glue between the [LSP](https://packagecontrol.io/packages/LSP) package and the MDITA Marksman language server, configuring and managing the server for you.

Unlike npm-based LSP helpers, this package expects the `mdita-marksman` binary to be pre-installed on your system.

## Features

Everything that the [MDITA Marksman](https://github.com/aireilly/mdita-marksman) language server supports, which includes:

- Document and workspace symbols from headings.
- Completion for inline links, reference links, and wiki links.
- MDITA YAML front matter completion with all standard fields.
- Hover preview for links.
- `Go to Definition` and `Find References` for headings and links.
- Diagnostics for broken links, missing YAML front matter, missing short descriptions, and heading hierarchy violations.
- Code Lens with reference counts on headings.
- Rename refactoring across files.
- Code action to generate a Table of Contents.
- MDITA map file (`.mditamap`) support.
- DITA fragment identifier support (`topicID/sectionID`).

## Installation

### Prerequisites

1. Install the [LSP](https://packagecontrol.io/packages/LSP) package from Package Control.
2. Build and install the `mdita-marksman` binary:

```bash
git clone https://github.com/aireilly/mdita-marksman
cd mdita-marksman
make install
```

The binary is installed to `~/.local/bin/mdita-marksman`. Ensure `~/.local/bin` is on your `PATH`.

### Package Control

1. Open `Package Control: Install Package` from the command palette.
2. Search for `LSP-mdita-marksman` and press <kbd>Enter</kbd>.

### Manual installation

1. Open `Package Control: Add Repository` from the command palette.
2. Enter `https://github.com/aireilly/LSP-mdita-marksman` into the input panel.
3. Open `Package Control: Install Package` and search for `LSP-mdita-marksman`.

## Configuration

Open the settings via the command palette:

```
Preferences: LSP-mdita-marksman Settings
```

Or navigate to: **Preferences > Package Settings > LSP > Servers > LSP-mdita-marksman**.

### Custom binary path

If `mdita-marksman` is not on your `PATH`, specify the full path in your user settings:

```json
{
    "command": ["/path/to/mdita-marksman", "server"],
}
```

### MDITA mode

To enable MDITA-specific diagnostics (missing YAML front matter, short description validation, heading hierarchy checks), create a `.mdita-marksman.toml` file in your project root with:

```toml
[core.mdita]
enable = true
```

## Keyboard Shortcuts

All keybindings are scoped to Markdown files (`text.html.markdown`) and require the corresponding LSP server capability.

| Shortcut | Command | Description |
|---|---|---|
| <kbd>F12</kbd> | Go to Definition | Jump to the definition of a heading or link target |
| <kbd>Shift+F12</kbd> | Find References | Find all references to a heading or link |
| <kbd>F2</kbd> | Rename Symbol | Rename a heading or link across files |
| <kbd>Ctrl+Shift+O</kbd> | Document Symbols | Navigate headings in the current file |
| <kbd>Ctrl+Shift+R</kbd> | Workspace Symbols | Search symbols across all project files |
| <kbd>Ctrl+Shift+A</kbd> | Code Actions | Trigger code actions (e.g. Generate Table of Contents) |
| <kbd>Ctrl+Shift+H</kbd> | Hover | Show hover information for links and headings |
| <kbd>Ctrl+Space</kbd> | Auto Complete | Trigger completions for links, front matter fields |

## Snippets

Tab-trigger snippets are available in Markdown files for common MDITA constructs:

| Tab Trigger | Description | Output |
|---|---|---|
| `mdita-topic` | Full MDITA topic template | YAML front matter + heading + body |
| `frontmatter` | YAML front matter block | `---` block with `id`, `shortdesc`, `author` |
| `xref` | Cross-reference link | `[link text](filename.md)` |
| `fragref` | DITA fragment ID link | `[link text](filename.md#topicID/sectionID)` |
| `mapentry` | MDITA map entry | `- [Topic Title](path/to/topic.md)` |
| `wiki` | Wiki-style link | `[[target-topic]]` |

## Completions

YAML front matter field completions are provided when editing Markdown files. Type the field name and press <kbd>Tab</kbd> to expand:

`id`, `shortdesc`, `author`, `source`, `publisher`, `permissions`, `audience`, `category`, `keyword`, `resourceid`

## Reporting issues

If you encounter problems, first check whether the same issue occurs with `mdita-marksman` directly. If it does, file an issue with the [language server](https://github.com/aireilly/mdita-marksman/issues). For issues specific to the Sublime Text integration, file them at:

https://github.com/aireilly/LSP-mdita-marksman/issues

## Acknowledgements

This package relies on [LSP](https://packagecontrol.io/packages/LSP) for LSP capabilities in Sublime Text and [MDITA Marksman](https://github.com/aireilly/mdita-marksman) for the language server implementation.

## License

The MIT License (MIT). See [LICENSE.md](LICENSE.md) for details.
