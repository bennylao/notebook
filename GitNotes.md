# Git

## Branch

- create new branch

```sh
git switch -c <new-branch-name>
```

```sh
git checkout -b <new-branch-name>
```

```sh
git branch <new-branch-name>
```

- switch branches

```sh
git switch <branch-name>
```

```sh
git checkout <branch-name>
```

> [!NOTE] `checkout` vs `switch`
>
> - Purpose: `checkout` is used for both switching branches and restoring file states, whereas `switch` is specifically tailored for switching branches.
> - Safety: `switch` does not allow you to accidentally overwrite changes, as it is designed to handle branch operations exclusively.
> - Clarity: `switch` makes scripts and commands clearer, as it's obvious from the command itself that you are performing a branch change.

## Commit

- undo last commit

```sh
git reset --soft HEAD^
```

## Restore

- restore a specific file

```sh
git checkout -- <file-name>
```

## Stash

- create a stash

```sh
git stash
```

```sh
git stash push -m <message>
```

- apply and remove the latest stash

```sh
git stash pop
```

- list stashes

```sh
git stash list
```

- apply a specific stash (0 for the latest stash, 1 for the second latest stash)

```sh
git stash apply
```

```sh
git stash apply stash@{<stash-index>}
```
