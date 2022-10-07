# Git Workflow

## git initialize a local repo

```bash
git init
git add . # adds all the branches
#make any changes if required
git commit # commit
```

## Add local repo to github

```bash
# establish the connection using 'ssh-keygen -t rsa -....'
git remote add <repo_name> <ssh link>
git push -u <repo_name> <branch_name>
```

### To remove a remote

```bash
git remote -v
git remote remove <repo name>
```

## Clone remote repo local

```bash
# establish the connection using 'ssh-keygen -t rsa -....'
git clone <ssh link>
```

## To pull and push changes to local and remote respectively

```bash
git pull <remote_name> <branch_name>
git push <remote_name> <branch_name>
```

## To make/ remove / merge / move a new branch

```bash
git branch # see all the branches
git branch <branch_name> #create a new branch
git checkout -b <branch_name> # create a new branch and move to the branch
git merge <branch_name> # merge the branch to the current branch
git branch --delete <branch_name> # delete the branch.
```