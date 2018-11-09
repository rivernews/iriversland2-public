port_num=

if [[ $1 == '' ]]
then
    return
else
    port_num="$1"
fi

sudo lsof -t -i tcp:$port_num | xargs kill -9