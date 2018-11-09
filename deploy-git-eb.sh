git_commit_msg=

if [[ $1 == '' ]]
then
    git_commit_msg=fix
else
    git_commit_msg="$1"
fi

# default to ng production
if [[ $2 == '' ]]
then
    build_angular="ng build ---prod"

# update ng w/o prod, use dev instead
elif [[ $2 == 'dev' ]] 
then
    build_angular="ng build"

# no ng update so don't build ng, can save time. Useful when ng/dj succeed but eb error.
elif [[ $2 == 'wo-ng' ]] 
then
    build_angular=
else
    echo "ERROR: arguments incorrect format"
    return
fi

cd frontend && eval $build_angular && cd .. && \
source git-push-w-sub.sh "$1" && \
cd backend && source setup-python-env.sh && \
eb deploy && echo "SUCCESS: Deployed on elastic beanstalk. Please allow 30 sec to 1 min for the server to apply the new code base." && \
cd .. && return

echo "ERROR: See message above."