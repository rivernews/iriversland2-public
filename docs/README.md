# Django + Angular + RESTful + EB

## AWS

- Force redirecting http to https, [see this post](https://stackoverflow.com/questions/14693852/how-to-force-https-on-elastic-beanstalk).

  - You can also use Django's settings, or both Django and AWS. [See Django settings](https://docs.djangoproject.com/en/2.0/topics/security/#ssl-https).

## Git Submodule Basics

[Following this article](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

- *** Clone in a git repo in an existing repo as submodule

Go to the folder within your repo, where you want to put the submodule

```shell

cd to/a/good/path
git submodule add -b stable https://github.com/rivernews/ckeditor5-build-balloon

``` 

will setup config files for submodule, and pull down the submodule the very first time.

`git push origin master` for the very first time.

- Pulling updates of submodules from fork repo

`git submodule update --remote --merge`

- Auto push all submodule as well when git pushing main project. 

Set this by default `git config push.recurseSubmodules on-demand`.

One-time command: `git push --recurse-submodules=on-demand`

- *** Edit, add & commit 

manually cd to each submodule, add commit & push, or

```bash

git submodule foreach 'git add && commit'
`git push --recurse-submodules=on-demand`

```

[See also](https://stackoverflow.com/questions/5542910/how-do-i-commit-changes-in-a-git-submodule)

- (optional) Get warning message doing `git push` if submodule's commits haven't done `git push`

> want the check behavior to happen for all pushes [...](https://git-scm.com/book/en/v2/Git-Tools-Submodules):  `git config push.recurseSubmodules check`

- Cloning the whole project that contains submodule, from scratch

`git clone --recurse-submodules <git repo url>`

It will pull all the submodules as well.

- Coming soon: update from upstream of that fork