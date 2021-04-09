check=$(ps | grep python3)

if [[ $check == '' ]]
then
    python3 ./app.py &
else
    echo "sudah jalan"
fi
