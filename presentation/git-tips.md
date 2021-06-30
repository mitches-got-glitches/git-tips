---
theme : "blood"
transition: "slide"
highlightTheme: "gruvbox-dark"
logoImg: false
slideNumber: false
customTheme: "css/tweaks"
title: "Tips for a better Git workflow"
---

### Tips for a better Git Workflow

---

### Writing good commit messages

---

#### The 7 rules of a great commit message

1. Separate subject from the body with a blank line {.fragment}
1. Limit the subject line to 50 characters {.fragment}
1. Capitalise the subject line {.fragment}
1. Do not end the subject line with a period {.fragment}
1. Use the imperative mood in the subject line {.fragment}
1. Wrap the body at 72 characters {.fragment}
1. Use the body to explain what and why vs. how {.fragment}

From here: [How to write a commit message](https://chris.beams.io/posts/git-commit/#wrap-72)

<aside class="notes">
I think the limit is set at 65 chars on the cprices project.
Enforced by a pre-commit helper.
We have the branch name in there too.
Changes colour when you're over 50 chars
not a hard limit, just a rule of thumb
Git will truncate any subject line longer than 72 characters with an ellipsis
Consider 72 the hard limit
</aside>

--

#### Limit subject line to 50 characters

> Tip: If you’re having a hard time summarizing, you might be committing too many changes at once. Strive for [atomic commits](https://www.freshconsulting.com/atomic-commits/) (a topic for a separate post).

Shoot for 50 chars, consider 72 the hard limit.

--

#### Wrap the body at 72 characters

Add this to your .vimrc:

```vim
" Automatically wrap git commit message body to 72 chars
au FileType gitcommit setlocal tw=72
```

--

#### Write in imperative mood

If applied, this commit will:

- Refactor subsystem X for readability
- Update getting started documentation
- Remove deprecated methods
- Release version 1.0.0

<aside class="notes">
We’re more used to speaking in the indicative mood, which is all about reporting facts.
What I still do!
</aside>

---

#### A good commit message should (my thoughts)

1. Add context to the changes you made
1. Communicate your thought processes as you develop
1. Provide narrative for reviewers / maintainers (where possible)

---

### Atomic commits

- An “atomic” change revolves around one task or one fix.
- i.e. commit the bug fix as one change, and the layout changes as a separate one

--

### The atomic approach

- Commit each fix or task as a separate change
- Only commit when a block of work is complete
- Commit each layout change separately
- Joint commit for layout file, code behind file, and additional resources

--

### Benefits

- Easy to roll back without affecting other changes
- Easy to make other changes on the fly
- Easy to merge features to other branches

---

## Some tips!

--

Add additional changes to a commit by staging them then:

 `git commit --amend`

Or to fix a typo in the commit message.

Without editing the commit msg:

`git commit --amend --no-edit`


```bash
alias gca='git commit --amend'
alias gcaf='git commit --amend --no-edit'
```

--

Sometimes you'll want to stage only your modified files, not the untracked ones. You can't use:

`git add -A` or `git add .`

To do this, use:

`git add -u`

Or with `alias ga='git add'`:

`ga -u`

--

Rather than using the full filepath for adding files that are nested in several layers, use pattern matching instead.

So say for:
cprices/alternative_sources/index_methods/geary_khamis_working.ipynb

`git add *geary*`

The above is particularly useful when staging changes to source code and the test script at the same time.

Add all changes in one sub-package:

`git add cprices/alternative_sources/*`

--


Stage/unstage changes in a file change-by-change using the GitLens extension to VS Code

--

- Use `git rebase -i` "interactive rebase" to squash/reorder commits to be more atomic.
- Learning some vim commands is helpful for this.
- Don't push commits that often, once a commit is pushed you shouldn't really be editing the history.

--

If you have Git commit hooks installed they can mess with the rebase. Better to uninstall then reinstall.

```bash
alias install_hooks='pre-commit install; pre-commit install --hook-type prepare-commit-msg --hook-type commit-msg'
alias remove_hooks='pre-commit uninstall; pre-commit uninstall --hook-type prepare-commit-msg --hook-type commit-msg'

grb() {
  remove_hooks
  git rebase -i HEAD~"$1"
  install_hooks
}
```

Then use `grb 5` to rebase last 5 commits.

--

Checkout the previous branch using:

`git checkout -`

Or with `alias gco='git checkout'`:

`gco -`

Or back two with:

`git checkout @{-2}`


---

### Some other useful aliases


