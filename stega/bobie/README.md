```bash
$ sudo mount -t msdos img folder
$ cd folder
$ find . -type t
password.txt
password.zip
$ md5sum password.txt
$ vim script.bash
#!/bin/bash
target_hash="f252376e1fa34da712056d40c401317b"
search_dir="/home/kali/Downloads/usb/laby"
find "$search_dir" -type f -exec bash -c '
    for file do
        current_hash=$(md5sum "$file" | awk "{print \$1}")
        if [ "$current_hash" != "'"$target_hash"'" ]; then
            echo "File $file has a different hash."
        fi
    done
' _ {} +


```