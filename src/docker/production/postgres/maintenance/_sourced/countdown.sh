#!/usr/bin/env bash  

countdown(){

    declare desc="Countdown"

    local seconds="${1}"
    local dt=$(($(date +%s) + "${seconds}"))

    while [ "$dt" -ge `date +%s` ]; do
        echo -ne "$(date -u --date @$(($dt - `date +%s`)) +%H:%M:%S)\r";

        sleep 0.1 
    done 
}
