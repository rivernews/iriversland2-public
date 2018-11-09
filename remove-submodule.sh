submodule_path=

if [[ $1 == '' ]]
then
    return
else
    submodule_path="$1"
fi

git submodule deinit -f $submodule_path && \
git rm -r -f $submodule_path && \
git commit -m "Removed submodule" && \
rm -rf .git/modules/$submodule_path && \
echo SUCCESS && return

echo ERROR: see above message.