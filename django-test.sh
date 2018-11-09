ng_flag=
ng_build=
dj_static=

if [[ $1 == 'a' ]]
then
    ng_build="ng build"
    dj_static="source recollect_static.sh"

elif [[ $2 == 'wo-ng' ]] 
then
    ng_build=
fi

if [[ $2 == 'p' ]]
then
    ng_flag="--prod --source-map"
fi

cd frontend && eval $ng_build $ng_flag && cd ../backend && source setup-python-env.sh && eval $dj_static && ./manage.py runserver 8001 && return
echo "ERROR: See above message."