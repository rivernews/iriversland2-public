if [[ $1 == '' ]]
then
    git_commit_msg=fix
else
    git_commit_msg="$1"
fi


commit_git_submodule="git submodule foreach git add . && git commit -m '$git_commit_msg'"
commit_git="git add . && git commit -m '$git_commit_msg'"
push_git="git push --recurse-submodules=on-demand"


eval $commit_git_submodule 
eval $commit_git
eval $push_git