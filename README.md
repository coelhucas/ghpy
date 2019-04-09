# ghpy
Control github from your terminal.
GHPY - Github Python
`ghpy` is a terminal utility based on the original one [gh](https://github.com/victorgama/gh) made in GoLang that allow you to use Github directly from your terminal. I'm creating this Python implementation as a challenge to myself.

# TODO List

- [X] [*Priority*] Project Architecture
  - [X] Use commands as a separated module
  - [X] Wrap authentication into an utils module
  - [X] Define the best way to rework the current content to join all the commands to the same parser. (Click)
  
- [x] Command `new`
  - [x] Create repositories
  - [x] Define either as `--public` or `--private` during creation
  - [x] Define initial license by `--license` followed by the license name
  - [x] Optionally create with a `.gitignore` using `--gitignore` + language
 
- [ ] Command Collab
  - [x] Collab add
  - [ ] Collab rm
 
 - [ ] Command `rm`
   - [x] Remove user repositories
   - [ ] Remove team repositories

- [ ] Team commands - ref from original https://github.com/victorgama/gh#team-management
  - [ ] `teams list`
  - [ ] `teams members`
  - [ ] `teams add`
  - [ ] `teams rm`
  
 - [ ] CI?/CD
   - [ ] Implement travis CI
   - [ ] Implement Tests
