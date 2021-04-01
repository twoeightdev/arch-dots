" Autoinstall
if ! filereadable(system('echo -n "$XDG_CONFIG_HOME/nvim/autoload/plug.vim"'))
  echo "Downloading junegunn/vim-plug to manage plugins..."
  silent !mkdir -p $XDG_CONFIG_HOME/nvim/autoload/
  silent !curl "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim" > $XDG_CONFIG_HOME/nvim/autoload/plug.vim
  autocmd VimEnter * PlugInstall
endif

" General settings
let mapleader=' '              " Map <space> as leader key
set clipboard+=unnamedplus     " Enable pasting
set mouse=a                    " Enable mouse scrolling
set hidden                     " This is recommended by coc
set nobackup                   " This is recommended by coc
set nowritebackup              " This is recommended by coc
set shortmess+=icw             " Avoid message and prompts
set noswapfile                 " Disable swaps
set bg=light                   " Set background
set nohlsearch                 " Highlighted search
set noshowmode                 " Disable INSERT mode showing up
set noruler
"set cursorline                 " Highlight current line
"set cursorcolumn               " Horizontal cursor line
set laststatus=2
set noshowcmd                  " Disable line or column number
set nowrap                     " Display long lines as just one line
set tabstop=2                  " Insert 4 spaces for tab
set shiftwidth=2               " Change number of space characters inserted for indention
set expandtab                  " Convert tabs to spaces
set splitbelow                 " Horizontal splits will automatically set below
set splitright                 " Vertical splits will automaticall set to the right
filetype plugin on
syntax on
set encoding=utf-8
set number relativenumber      " Show line numbers
set wildmenu                   " Enable wildmenu
set wildmode=longest:list,full " Wildmenu style

" Show invisibles
set list
set listchars=
set listchars+=tab:.\
set listchars+=trail:.
set listchars+=extends:»
set listchars+=precedes:«
set listchars+=nbsp:░

" Load plugins
call plug#begin('~/.config/nvim/plugged')

Plug 'liuchengxu/vim-which-key'                                         " Shows keybindings in popup
Plug 'tpope/vim-fugitive'                                               " Git integration
Plug 'lukelbd/vim-tabline'                                              " Simple buffer tabline
Plug 'Yggdroot/indentLine'                                              " Indent guidelines

call plug#end()

" Reload programs when configuration is updated
  autocmd BufWritePost *Xresources !xrdb %
  autocmd BufWritePost dunstrc !pkill dunst; dunst &
  autocmd BufWritePost *sxhkdrc !pkill -USR1 sxhkd
  autocmd BufWritePost init.vim,statusline.vim source $MYVIMRC

" Disables automatic commenting on newline:
  autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Source and load plugins configurations
source $HOME/.config/nvim/pconf/keymaps.vim
source $HOME/.config/nvim/pconf/whichkey.vim
source $HOME/.config/nvim/pconf/indentline.vim
source $HOME/.config/nvim/pconf/statusline.vim
