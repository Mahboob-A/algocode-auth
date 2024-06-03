#!/usr/bin/env bash 

# prints new line 
message_newline(){
    echo
}

# prints the value in the @ with DEBUG prefix 
message_debug(){
    echo -e "DEBUG: ${@}"
}

# prints with bold text 
message_welcome(){
    echo -e "\e[1mWELCOME - ${@}\e[0m"
}

# print text WARNIGN in yellow color 
message_warning(){
    echo -e "\e[33mWARNING\e[0m: ${@}"
}

# prints text error in red color 
message_error(){
    echo -e "\e[31mERROR\e[0m: ${@}"
}


# prints text info in light gray color 
message_info(){
    echo -e "\e[37mINFO\e[0m: ${@}"
}

# prints text suggestion in yellow color 
message_suggestion(){
    echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}


# prints text success in green color 
message_success(){
    echo -e "\e[32mSUCCESS\e[0m: ${@}"
}