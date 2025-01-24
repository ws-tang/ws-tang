# File: .bashrc
#
# Use: This is a .bashrc file template for a Git environment with TortoiseGit
#      Git Bash shell to set Git command aliases for convenience.
#
# Author: Wenshiuan Tang
# Created: 2025-03-13
#
# Lincese: MIT
#

# Replace _REMOTE_GIT_REPO_NAME_ with the applicable remote Git repo name
alias gitpush='git push _REMOTE_GIT_REPO_NAME_ '

# Get the latest N Git log with the format: [hash comment]
# Use: gitlog -5 => Get the latest 5 Git logs with hash and comment.
alias gitlog='git log --oneline --date=short --pretty=format:"%h%x09%s"'

# Get the latest N Git log with the format: [hash date comment]
# Use: gitlog -5 => Get the latest 5 Git logs with hash, date, and comment.
alias gitlog2='git log --oneline --date=short --pretty=format:"%h%x09%ad%x09%s"'

# Get the latest N Git log with the format: [hash date author comment]
# Use: gitlog -5 => Get the latest 5 Git logs with hash, date, author, and comment.
alias gitlog3='git log --oneline --date=short --pretty=format:"%h%x09%ad%x09%an%x09%s"'
