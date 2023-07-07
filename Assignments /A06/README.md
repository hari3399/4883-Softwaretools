
# Vim (Vi IMproved)

## What is Vim?

Vim, short for Vi IMproved, is a highly configurable text editor built upon the original vi editor found on Unix systems. It provides a wide range of powerful features and is designed to be efficient, customizable, and extensible.

## How to Use Vim?

To use Vim, follow these steps:

1. Launch your terminal.
2. Type `vim` followed by the name of the file you want to edit, e.g., `vim myfile.txt`.
3. Press **Enter** to open the file in Vim.
4. You will be in the "normal" mode by default. Use the following commands to navigate and edit the file:
   # Vim Insert Mode

In Vim, there are several ways to enter insert mode, which allows you to insert and edit text. Here are the most common ways to enter insert mode:

1. **i**: Enter insert mode to start editing the file.
2. **a**: Enter append mode to insert text after the cursor.
3. **I**: Enter insert mode at the beginning of the line.
4. **A**: Enter insert mode at the end of the line.
5. **o**: Open a new line below the current line and enter    insert mode.
6. **O**: Open a new line above the current line and enter insert mode.
7. **s**: Substitute the character under the cursor and enter insert mode.
8. **S**: Substitute the entire line and enter insert mode.
9. **c** followed by a motion or text object: Delete and enter insert mode. For example, `cw` changes the word under the cursor and enters insert mode.
10. **C**: Delete from the cursor position to the end of the line and enter insert mode.


   - **Esc**: Exit insert mode and return to normal mode.
   - **:w**: Save the changes.
   - **:q**: Quit Vim.
   - **:wq**: Save the changes and quit Vim.
   - **:q!**: Quit Vim without saving changes.

## Most Useful Vim Commands

Here are some commonly used commands in Vim:

### Navigation

- **h**: Move the cursor one character to the left.
- **j**: Move the cursor one line down.
- **k**: Move the cursor one line up.
- **l**: Move the cursor one character to the right.
- **{number}h**: Move the cursor {number} characters to the left.
- **{number}j**: Move the cursor {number} lines down.
- **{number}k**: Move the cursor {number} lines up.
- **{number}l**: Move the cursor {number} characters to the right.
- **0**: Move to the beginning of the line.
- **$**: Move to the end of the line.
- **gg**: Go to the top of the file.
- **G**: Go to the bottom of the file.
- **Ctrl+f**: Scroll forward one screen.
- **Ctrl+b**: Scroll backward one screen.
- **Ctrl+d**: Scroll down half a screen.
- **Ctrl+u**: Scroll up half a screen.

### Editing

- **x**: Delete the character under the cursor.
- **dw**: Delete from the cursor to the end of the word.
- **dd**: Delete the current line.
- **yy**: Copy the current line.
- **p**: Paste the copied or deleted content below the cursor.
- **P**: Paste the copied or deleted content above the cursor.
- **u**: Undo the last action.
- **Ctrl+r**: Redo the last undone action.
- **:s/old/new**: Substitute "old" with "new" in the current line.
- **:%s/old/new/g**: Substitute "old" with "new" in the entire file.

### Searching

- **/pattern**: Search forward for "pattern".
- **?pattern**: Search backward for "pattern".
- **n**: Go to the next occurrence of the search pattern.
- **N**: Go to the previous occurrence of the search pattern.

# Vim usful  Functionalities

1. **Autocompletion with Control + P**: In Vim, when you're in insert mode, pressing Control + P triggers autocompletion. Vim will try to suggest and complete words or phrases based on the existing content in the buffer or previously typed text.

2. **Buffer Commands**:
   - `:bnext`: Switch to the next buffer in the buffer list.
   - `:bprevious`: Switch to the previous buffer in the buffer list.
   - `:enew`: Create a new empty buffer.

3. **Recording Commands**:
   - `qa`: Start recording a macro into the register "a".
   - `q`: Stop recording the macro.
   - `@a`: Execute the macro stored in register "a".
   - `10@a`: Execute the macro stored in register "a" ten times.
   - `@@`: Replay the previous macro.

4. **External Command Execution**:
   - `!command`: Execute an external command from within Vim.
   - `!sort`: Execute the `sort` command, which is a Unix utility to sort lines of text.

5. **Opening Files or Links**:
   - `gx`: Open the file or link under the cursor in the appropriate program or viewer.
   - `gf`: Open the file whose filename is currently under the cursor.

6. **File Encryption with :X**: In Vim, the `:X` command is used to encrypt or decrypt a file. When you execute `:X`, Vim prompts you for a key to encrypt or decrypt the file.

These are some useful commands and functionalities available in Vim. Each command serves a specific purpose.


### Key Bindings

Vim allows you to define custom key bindings to streamline your workflow. You can add key bindings in your `.vimrc` file. Here's an example of a key binding to save and quit:


## Useful Plugins

Vim supports a vast ecosystem of plugins that enhance its functionality. Here are some popular plugins:

### Plugin Managers

- [Vundle](https://github.com/VundleVim/Vundle.vim): Vim plugin manager with a simple configuration.
- [packer](https://github.com/wbthomason/packer.nvim): A simple plugin manager for Vim.
- [vim-plug](https://github.com/junegunn/vim-plug): Minimalist Vim plugin manager with parallel installation support.

### Productivity Plugins

- [NERDTree](https://github.com/preservim/nerdtree): A file system explorer for Vim.
- [Nvim-tree](https://github.com/nvim-tree/nvim-tree.lua.git)
  simple file explorer for neo vim
- [Comment.Nvim](https://github.com/numToStr/Comment.nvim): provides simple ways to comment and uncomment  lines of code and suppport all the popular laguages. 
- [Lualine](https://github.com/nvim-lualine/lualine.nvim):provides simple status line in neovim.
- [vim-surround](https://github.com/tpope/vim-surround): Quoting/parenthesizing made simple.
- [telescope](https://github.com/nvim-telescope/telescope.nvim):This plugin is a fuzzy finder that helps with searching and navigating files, buffers, and more. 

### Syntax Highlighting and Language Support

- [vim-polyglot](https://github.com/sheerun/vim-polyglot): A collection of language packs for Vim.
- [vim-go](https://github.com/fatih/vim-go): Go programming language support for Vim.
- [vim-python-pep8-indent](https://github.com/Vimjas/vim-python-pep8-indent): PEP8 indentation support for Python.

### Themes and UI Enhancements

- [vim-airline](https://github.com/vim-airline/vim-airline): A sleek status bar for Vim.
- [gruvbox](https://github.com/morhetz/gruvbox): Retro groove color scheme for Vim.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons): Adds file type icons to Vim.
- 
## Acknowledgements

https://www.youtube.com/watch?v=vdn_pKJUda8

https://github.com/josean-dev/dev-environment-files

https://www.barbarianmeetscoding.com/notes/neovim-plugins/











