#!/bin/zsh

echo "metti il numero: "
read num

if [[ -z $num || $num == *[!0-9]* ]]; then
    echo "Non è numerico"
    exit
fi

somma=0
for (( i=0; i<${#num}; i++ )); do
    if (( $i % 2 == 0 )); then
        mol=$(( 1 * ${num:$i:1} ))
    else
        mol=$(( 3 * ${num:$i:1} ))
    fi
    somma=$(( somma + mol ))
done

decina=$(( (somma + 9) / 10 * 10 ))
echo "$(( decina - somma ))"
