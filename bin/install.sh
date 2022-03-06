#!/usr/bin/env bash


main() {
	local root_dir

	# shellcheck disable=SC2164,SC2128
	root_dir="$( cd "$(dirname "${BASH_SOURCE}")/.." ; pwd -P )"

  link_macros "$root_dir"
}

link_macros() {
	local root_dir="$1"
	local file_name
	local user_macro_path

	echo "linking *.py files from the repository to *.FCMacro targets in the default user macros directory"
	for file_path in "$root_dir"/macros/*.py; do
		file_name="$(basename "$file_path")"
		user_macro_path=~/Library/Preferences/FreeCAD/Macro/"${file_name%.py}.FCMacro"

		ln -s "$file_path" "$user_macro_path"
	done
}

main "$@"
