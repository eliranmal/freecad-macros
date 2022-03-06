#!/usr/bin/env bash


main() {
  local user_macros_dir="$1"
	local root_dir

	# shellcheck disable=SC2164,SC2128
	root_dir="$( cd "$(dirname "${BASH_SOURCE}")/.." ; pwd -P )"

  link_macros "$root_dir" "$user_macros_dir"
}

link_macros() {
	local root_dir="$1"
	local user_macros_dir="$2"
	local file_name
	local user_macro_path

  echo "validating user macros directory..."
	if [ ! -d "$user_macros_dir" ]; then
    user_macros_dir=~/Library/Preferences/FreeCAD/Macro
	fi
	echo "user macros directory set to $user_macros_dir"

	echo "linking *.py files from the repository to *.FCMacro targets in the default user macros directory..."
	for file_path in "$root_dir"/macros/*.py; do
		file_name="$(basename "$file_path")"
		user_macro_path="$user_macros_dir/${file_name%.py}.FCMacro"

		ln -s "$file_path" "$user_macro_path"
	done
	echo "files linked"
}

main "$@"
