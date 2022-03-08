#!/usr/bin/env bash


main() {
	local root_dir

	# shellcheck disable=SC2164,SC2128
	root_dir="$( cd "$(dirname "${BASH_SOURCE}")/.." ; pwd -P )"

	prepare_env "$@"
	link_macros "$root_dir"
}

prepare_env() {
	USER_MACROS_DIR="$1"

	log
	log "validating user macros directory input..."
	if [ ! -d "$USER_MACROS_DIR" ]; then
		log "input is not a directory."
		log
		log "resolving default user macros directory..."
		USER_MACROS_DIR=$(resolve_user_macros_dir)
		if (( $? == 1 )); then
			log "resolution failed ($USER_MACROS_DIR). aborting"
			exit 1
		fi
	fi
	log "user macros directory set to $USER_MACROS_DIR"
}

link_macros() {
	local root_dir="$1"
	local file_name
	local user_macro_path

	log
	log "linking *.py files from the repository to *.FCMacro targets in the default user macros directory..."
	for file_path in "$root_dir"/macros/*.py; do
		file_name="$(basename "$file_path")"
		user_macro_path="$USER_MACROS_DIR/${file_name%.py}.FCMacro"

		ln -sv "$file_path" "$user_macro_path"
	done
	log "files linked"
}

resolve_user_macros_dir() {
	if [[ "$OSTYPE" == "linux-gnu" ]]; then
		# linux
		echo ~/.FreeCAD/Macro
	elif [[ "$OSTYPE" == "darwin"* ]]; then
		# Mac OSX
		echo ~/Library/Preferences/FreeCAD/Macro
#	elif [[ "$OSTYPE" == "cygwin" ]]; then
#		# POSIX compatibility layer and Linux environment emulation for Windows
#	elif [[ "$OSTYPE" == "msys" ]]; then
#		# Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
#	elif [[ "$OSTYPE" == "win32" ]]; then
#		# I'm not sure this can happen.
#	elif [[ "$OSTYPE" == "freebsd"* ]]; then
#		# ...
	else
		# Unknown.
		echo "error: $OSTYPE is not supported"
		return 1
	fi
}

log() {
	printf '%s\n' "$@"
}




main "$@"
