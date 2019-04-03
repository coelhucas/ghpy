# ghpy
Control github from your terminal.
GHPY - Github Python
`ghpy` is a terminal utility based on the original one [gh](https://github.com/victorgama/gh) made in GoLang that allow you to use Github directly from your terminal. I'm creating this Python implementation as a challenge to myself.

# TODO List
- [ ] Command `new`
  - [ X ] Create repositories
  - [ X ] Define either as `--public` or `--private` during creation
  - [ ] Define initial license by `--license` followed by the license name
  - [ ] Optionally create with a `.gitignore` using `--gitignore` + language
  
 - [ ] Command `rm`
  - [ X ] Remove user repositories
  - [ ] Remove team repositories

- [ ] Team commands - ref from original https://github.com/victorgama/gh#team-management
  - [ ] `teams list`
  - [ ] `teams members`
  - [ ] `teams add`
  - [ ] `teams rm`
  
 - [ ] Add unit tests
